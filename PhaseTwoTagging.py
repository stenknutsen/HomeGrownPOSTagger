#uses immediate context (left or right) to tag POS


VBZ_is_context_dictionary = {"it":"PRP","he":"PRP","she":"PRP","that":"WP","there":"EX","what":"WP","who":"WP",
                             "here":"RB","how":"WRB","why":"WRB","when":"WRB","where":"WRB"}

#tags anything 'to' before DT or PRP$ or NNP as 'IN'(preposition)
def to_INtagger(sent):
    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[0].lower()=="to")&((context[1]=='DT')|(context[1]=='PRP$')|(context[1]=='NNP')):
            newTup = (target[0], 'IN')
            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn


#tags anything 'to' before adverb as infinitive
def to_RB_TOtagger(sent):
    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[0].lower()=="to")&(context[1]=='RB'):
            newTup = (target[0], 'TO')
            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn


#tags anything 'to' before AUX verbs (and a few favorites) as infinitive
def to_AUX_TOtagger(sent):
    sentToReturn = []
    skip = False
    for i in range(len(sent)-1):

        if skip == True:
            skip = False
            continue

        target = sent[i]
        context = sent[i+1]

        if (target[0].lower() == "to")&((context[0].lower() == 'have')|(context[0].lower() == 'do')|
                                      (context[0].lower() == 'be')|(context[0].lower() == 'get')|
                                        (context[0].lower() == 'make')|(context[0].lower() == 'see')|
                                        (context[0].lower() == 'go')):

            newTup = (target[0], 'TO')
            sentToReturn += [newTup]
            newTup = (context[0], 'VB')
            sentToReturn += [newTup]
            skip = True
        else:
            sentToReturn += [target]

    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn

#tags anything ending in -ing directly following 'be' verb as gerund
def to_be_VBGTagger(sent):
    sentToReturn = []
    skip = False
    for i in range(len(sent)-1):

        if skip == True:
            skip = False
            continue

        target = sent[i]
        context = sent[i+1]

        if ((target[0].lower() == "be")|(target[0].lower() == "am")|(target[0].lower() == "is")|
            (target[0].lower() == "are")|(target[0].lower() == "was")|(target[0].lower() == "were")|
            (target[0].lower() == "been"))&(context[0].lower().endswith("ing")):
            newTup = (target[0],target[1])
            sentToReturn += [newTup]
            newTup = (context[0], "VBG")
            sentToReturn += [newTup]
            skip = True
        else:

          sentToReturn += [target]

    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn


def thats_Tagging(sent):#####<+++++a work in progresss.  . .  .. . . .  . . .
    sentToReturn = []
    skip = False
    for i in range(len(sent)-1):

        if skip == True:
            skip = False
            continue

        context = sent[i]
        target = sent[i+1]

        if (target[0].lower() == "is")|(target[0].lower() == "'s"):
            if context[0].lower() in VBZ_is_context_dictionary:

                newTup = (context[0], VBZ_is_context_dictionary[context[0]])
                sentToReturn += [newTup]

                newTup = (target[0],"VBZ")


                sentToReturn += [newTup]
                skip = True
        else:

          sentToReturn += [context]

    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn