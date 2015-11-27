#Uses context to tag POS

#tags anything 'to' before DT as IN (preposition)
def to_INtagger(sent):
    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[0].lower()=="to")&(context[1]=='DT'):
            newTup = (target[0], 'IN')
            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn









