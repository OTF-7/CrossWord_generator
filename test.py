from utilities.questions import words_list
l = list()
for x in words_list:
    d = dict(x)
    if len(d["word"]) < 7:
        l.append(d)

with open('t.txt', 'w') as file:
    file.write(l.__str__())

print(len(l))
print(len(words_list))
