# CCC '97 S1 - Sentences

n = int(input())

for i in range(n):
    subs = int(input())
    objs = int(input())
    verbs = int(input())
    sub = []
    for j in range(subs):
        word = input()
        sub.append(word)
    obj = []
    for k in range(objs):
        word = input()
        obj.append(word)
    verb = []
    for l in range(verbs):
        word = input()
        verb.append(word)

    sentences = []
    for subject in sub:
        for ob in obj:
            for ver in verb:
                sentence = subject + " " + ob + " " + ver + "."
                sentences.append(sentence)
    sentences = sorted(sentences)
    for sentence in sentences:
        print(sentence)
