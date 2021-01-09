import os
db = {}

with open('all.csv', 'r',  encoding='gbk')as f:
    rdl = f.readlines()
    for line in rdl:
        if not line.startswith('序号'):
            data = line.split(',')
            db[str(data[0])] = {}
            db[str(data[0])]['qus'] = data[1].strip()
            db[str(data[0])]['ans'] = data[2].strip()
            db[str(data[0])]['r_ans'] = data[3].strip()

if __name__ == '__main__':
    while True:
        query_result = ""
        query = input('输入关键词：')
        if not query.strip() == '':
            query = query.split()
            print('\n===========================')
            for n in db:
                count = 0
                for key in query:
                    if key in db[n]['qus']:
                        count += 1
                if len(query) == count:
                    query_result += db[n]['qus'] + '\n'
                    query_result += db[n]['ans']
                    query_result += '\n'
                    query_result += db[n]['r_ans']
                    query_result += '\n===========================\n'
        print(query_result)
