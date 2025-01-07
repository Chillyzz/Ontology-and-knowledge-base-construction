import json

def parse_facts(facts):
    datas = facts.split(";")
    fact = []
    declaration = []
    for data in datas:
        if ":" in data:
            declaration.append(data)
        else:
            fact.append(data)
    return declaration,fact


def process_data(file):
    f = open(file,'r',encoding='utf-8')
    datas = json.load(f)
    res = []
    i = 0
    for data in datas:
        d = dict()
        d['id'] = i
        d['text'] = data['text']
        d['new_text'] = data['new_text']
        declarations,facts = parse_facts(data['fact_expressions'])
        d['declarations'] = ";".join(declarations)
        d['facts'] = ";".join(facts)
        d['query'] = data['query_expressions']
        res.append(d)
        i += 1
    return res

def main():
    train_file = r"/home/zjy17/Conic10k/raw_data/test.json"
    res = process_data(train_file)

    f = open(r"/home/zjy17/Conic10k/conic10k/test.json",'w',encoding='utf8')
    json.dump(res,f,ensure_ascii=False,indent = 4)
    f.close()


if __name__ == '__main__':
    main()