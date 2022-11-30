import operator

words = ["привет"]
in_chat = False
users = {}
name = ""
from_id = ''
with open('result.json', encoding='utf-8') as f:
    for line in f:
        line = line.strip().replace('\"', '').replace(',', '').split(':')
        if line[0] == 'from_id':
            from_id = line[1]
        elif line[0] == 'from':
            name = line[1]
        elif line[0] == 'text':
            text = line[1].split(' ')
            for word in text:
                if word.lower() in words:
                    if from_id not in users:
                        users[from_id] = [1, name]
                    else:
                        users[from_id][0] += 1
sorted_result = reversed(sorted(users.items(), key=operator.itemgetter(1)))
for x in sorted_result:
    print(x[1])