import headers

test = ['In', 'fact', ',', 'when', 'he', 'was', 'questioned', 'by', 'ABC', 'News', 'today', 'about', 'his', 'assertion', 'that', '``', 'thousands', 'and', 'thousands', 'of', 'people', "''", 'cheered', 'the', 'collapse', 'of', 'the', 'World', 'Trade', 'Center', 'on', 'Sept.', '11', 'just', 'across', 'the', 'river', 'in', 'New', 'Jersey', ',', 'Trump', 'doubled', 'down', '.']
#test = ['Republican', 'presidential', 'candidate', 'Donald', 'Trump', 'speaks', 'during', 'a', 'campaign', 'stop', 'on', 'Saturday', 'in', 'Birmingham']
tinyDTDict = {"a":"DT","the":"DT","this":"DT","these":"DT","those":"DT","my":"DT", "your":"DT", "his":"DT", "her":"DT", "its":"DT", "our":"DT","their":"DT","some":"DT"}
tinyCCDict = {"and":"CC", "or":"CC","but":"CC","&":"CC"}
tinyINDict = {"in":"IN","by":"IN","of":"IN"}
#Tags anything starting with a captial letter (ecluding first word in sentence) as NNP. Also adds UNK.<==will probably change this
def NNPTagger(sent):
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


#Tags determiners
def DTTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower() in tinyDTDict:
            newTup = (word[0],'DT')
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn

#tags very limited coordinating conjuncts
def CCTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower() in tinyCCDict:
            newTup = (word[0],'CC')
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn

def INTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower() in tinyINDict:
            newTup = (word[0],'IN')
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn



findnnps = NNPTagger(test)

print(findnnps)
findnnps = DTTagger(findnnps)

print(findnnps)

findnnps = CCTagger(findnnps)

print(findnnps)

findnnps = INTagger(findnnps)

print(findnnps)