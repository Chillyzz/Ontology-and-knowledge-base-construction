# -*- coding: utf-8 -*-
import re
import json
from argparse import ArgumentParser
from weakref import ref
from data import get_dataset
from metric.metric import Metric
from datasets import load_dataset

def get_dataset(
    path='/home/zcl/conic10k/conic10k',
    add_spaces_around_symbols=True,
    zero_shot_prompt=False,
    encoder_decoder=True
):
    datasets = load_dataset(path)
    datasets = datasets.map(convert_expr, load_from_cache_file=False)
    
    # semantic parsing部分只取数据的"text""fact_expressions"和"query_expressions"部分
    if add_spaces_around_symbols:
        datasets = datasets.map(tokenize_syms, load_from_cache_file=False)
        datasets = datasets.map(lambda x: set_math_expr(x, encoder_decoder), load_from_cache_file=False)

    return datasets

def convert_expr(example):
    # rearrange declarations to the front
    sentences = example['fact_expressions'].split(';')
    sentences = sorted([s for s in sentences if ':' in s]) + \
        sorted([s for s in sentences if ':' not in s])
    for i,sentence in enumerate(sentences):
        if ':' not in sentence and '=' not in sentence and '>' not in sentence and '<' not in sentence:
            sentences[i] = sentence + ' = True'
    exprs = ';'.join(sentences)
    example['expr'] = exprs + ';' + \
        ';'.join(
            list(map(lambda x: x + " = ?", example['query_expressions'].split(';'))))

    return example

def convert_expr_v2(example):
    # rearrange declarations to the front
    sentences = example['fact_expressions'].split(';')
    sentences = sorted([s for s in sentences if ':' in s]) + \
        sorted([s for s in sentences if ':' not in s])
    for i,sentence in enumerate(sentences):
        if ':' not in sentence and '=' not in sentence and '>' not in sentence and '<' not in sentence:
            sentences[i] = sentence + ' = True'
    exprs = ';'.join(sentences)
    example['expr'] = exprs + ';' + \
        ';'.join(
            list(map(lambda x: x, example['query_expressions'].split(';'))))

    return example


def set_math_expr(example, encoder_decoder):
    return {
        'text': example['text'],
        'labels': example['expr'].strip()
    }
    


def tokenize_syms(example):
    text = example['text']
    expr = example['expr']

    # add spaces around ( ) [ ] { } < > = + - * / ^ : ; , . ? & | \ !
    text = re.sub(
        r'([\(\)\[\]\{\}\<\>\=\+\-\*\/\^\:\;\,\.\?\&\|\\\!])', r' \1 ', text)
    expr = re.sub(
        r'([\(\)\[\]\{\}\<\>\=\+\-\*\/\^\:\;\,\.\?\&\|\\\!])', r' \1 ', expr)

    # remove duplicated spaces
    text = re.sub(r'\s+', ' ', text)
    expr = re.sub(r'\s+', ' ', expr)

    # remove space in front of numbers
    text = re.sub(r' (\d)', r'\1', text)
    expr = re.sub(r' (\d)', r'\1', expr)

    return {
        'text': text,
        'expr': expr
    }

parser = ArgumentParser()
parser.add_argument('--dataset_path', default='conic10k', type=str)
parser.add_argument('--prediction_file', type=str)
parser.add_argument('--split', default='test', type=str)
parser.add_argument('--report_file', default='', type=str)

if __name__ == '__main__':
    args = parser.parse_args()

    split = args.split
    report_file = args.report_file or 'qwen2.5_math_1.5b_200sample_80epoch.txt'

    # datas = get_dataset(args.dataset_path, encoder_decoder=True)[split]
    test_file =open(args.dataset_path,'r', encoding='utf-8')
    datas = json.load(test_file)

    refs = []
    ques = []
    for data in datas:
        result = convert_expr(data)
        res = tokenize_syms(result)
        refs.append(res['expr'])
        ques.append(data['text'])
        

    # refs = [
    #     d['labels']
    #     for d in datas
    # ]

    # ques = [
    #     d['text']
    #     for d in datas
    # ]

    # 使用示例
    f = open(args.prediction_file,'r',encoding='utf-8')
    result = json.load(f)

    preds = []
    for p in result:
        d= dict()
        d['fact_expressions'] = p['declarations'].strip() + ';' + p['facts'].strip()
        d['query_expressions'] = p['query']
        # d['text'] = p['text']
        d['text'] = ''
        result = convert_expr_v2(d)
        final_res = tokenize_syms(result)
        preds.append(final_res['expr'])

    mtc = Metric(max_workers=1)
    i = 200
    print(preds[i:i+1])
    mtc.cmps(preds=refs[290:297],golds=preds[290:297], questions=ques, verbose=True) # I made a mistake here, the order of preds and refs should be reversed, the left one should be the gold standard.

    if report_file:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(mtc.detail())

    print(f'accuracy: {mtc.accuracy}\nmi-f1: {mtc.f1}\nma-f1: {mtc.avg_f1}')
