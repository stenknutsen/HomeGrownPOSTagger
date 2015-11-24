import headers

test = ['In', 'fact', ',', 'when', 'he', 'was', 'questioned', 'by', 'ABC', 'News', 'today', 'about', 'his', 'assertion', 'that', '``', 'thousands', 'and', 'thousands', 'of', 'people', "''", 'cheered', 'the', 'collapse', 'of', 'the', 'World', 'Trade', 'Center', 'on', 'Sept.', '11', 'just', 'across', 'the', 'river', 'in', 'New', 'Jersey', ',', 'Trump', 'doubled', 'down', '.']
#test = ['Republican', 'presidential', 'candidate', 'Donald', 'Trump', 'speaks', 'during', 'a', 'campaign', 'stop', 'on', 'Saturday', 'in', 'Birmingham']
tinyDTDict = {"a":"DT","the":"DT","this":"DT","these":"DT","those":"DT","my":"DT", "your":"DT", "his":"DT", "her":"DT", "its":"DT", "our":"DT","their":"DT","some":"DT"}

def NNPFinder(sent):
    iterSent = iter(sent)

    sentToReturn = []
    tup = (next(iterSent), 'UNK')
    sentToReturn += [tup]

    for word in iterSent:

        if word[0].isupper():
            tup = (word, 'NNP')
        else:
            tup = (word, 'UNK')
        sentToReturn += [tup]

    return sentToReturn



def DTFinder(sent):
    sentToReturn = []
    for word in sent:
        if word[0] in  tinyDTDict:
            newTup = (word[0],'DT')
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]



    return sentToReturn

findnnps = NNPFinder(test)

print(findnnps)
findnnps = DTFinder(findnnps)

print(findnnps)