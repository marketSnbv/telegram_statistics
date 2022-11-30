import operator


results = {}
prev_line = ""
with open('result.json', encoding='utf-8') as f:
    for line in f:
        line = line.strip().replace('\"', '').replace(',', '').replace(' ', ''). split(':')
        if line[0] == 'from_id':
            if line[1] not in results:
                results[line[1]] = [1, prev_line]
            else:
                results[line[1]][0] += 1
        elif line[0] == 'from':
            prev_line = line[1]
sorted_results = reversed(sorted(results.items(), key=operator.itemgetter(1)))
for x in sorted_results:
    print(x[1])
