#uses two points of context (left or right) to tag (provisionally, in cases of N and V)

#tags anything between a DT and IN as NN. Note *****(add plural filter later)*******
def DT_IN_NounTagger(sent):
    sentToReturn = []
    skip = False
    for i in range(len(sent)-2):

        if skip == True:
            skip = False
            continue

        leftContext = sent[i]
        target = sent[i+1]
        rightContext = sent[i+2]

        if (leftContext[1] == "DT")&(rightContext[1] == "IN")&(target[1]=="UNK"):

            sentToReturn += [leftContext]
            newTup = (target[0], "N")
            sentToReturn += [newTup]

            skip = True
        else:

          sentToReturn += [leftContext]

    sentToReturn += [sent[len(sent)-2]]
    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn


#verbs tagged between PRPs & INs
def PRP_IN_VerbTagger(sent):
    sentToReturn = []
    skip = False
    for i in range(len(sent)-2):

        if skip == True:
            skip = False
            continue

        leftContext = sent[i]
        target = sent[i+1]
        rightContext = sent[i+2]

        if (leftContext[1] == "PRP")&(rightContext[1] == "IN")&(target[1]=="UNK"):

            sentToReturn += [leftContext]
            newTup = (target[0], "V")
            sentToReturn += [newTup]

            skip = True
        else:

          sentToReturn += [leftContext]

    sentToReturn += [sent[len(sent)-2]]
    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn


#verbs tagged between N & DT
def N_DT_VerbTagger(sent):
    sentToReturn = []
    skip = False
    for i in range(len(sent)-2):

        if skip == True:
            skip = False
            continue

        leftContext = sent[i]
        target = sent[i+1]
        rightContext = sent[i+2]

        if (leftContext[1].startswith("N"))&(rightContext[1] == "DT")&(target[1]=="UNK"):

            sentToReturn += [leftContext]
            newTup = (target[0], "V")
            sentToReturn += [newTup]

            skip = True
        else:

          sentToReturn += [leftContext]

    sentToReturn += [sent[len(sent)-2]]
    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn

#nouns tagged between DT & [punctuation]####NOTE: DUPLICATES NOUN AT END OF SENTENCE****************
def DT_PuctuationNounTagger(sent):
    sentToReturn = []
    skip = False
    for i in range(len(sent)-2):

        if skip == True:
            skip = False
            continue

        leftContext = sent[i]
        target = sent[i+1]
        rightContext = sent[i+2]

        if (leftContext[1]=="DT")&(target[1]=="UNK")&((rightContext[1] == ".")|(rightContext[1] == ",")|(rightContext[1] == "!")|
                                   (rightContext[1] == "?")|(rightContext[1] == ":")|(rightContext[1] == "?")):

            sentToReturn += [leftContext]
            newTup = (target[0], "N")
            sentToReturn += [newTup]

            skip = True
        else:

          sentToReturn += [leftContext]

    sentToReturn += [sent[len(sent)-2]]
    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn

#verbs between N and "by" tagged
def N_by_VerbTagger(sent):
    sentToReturn = []
    skip = False
    for i in range(len(sent)-2):

        if skip == True:
            skip = False
            continue

        leftContext = sent[i]
        target = sent[i+1]
        rightContext = sent[i+2]

        if (leftContext[1].startswith("N"))&(target[1]=="UNK")&(rightContext[0].lower() == "by"):

            sentToReturn += [leftContext]
            newTup = (target[0], "V")
            sentToReturn += [newTup]

            skip = True
        else:

          sentToReturn += [leftContext]

    sentToReturn += [sent[len(sent)-2]]
    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn

#verbs tagged between MD and as
def MD_as_VerbTagger(sent):
    sentToReturn = []
    skip = False
    for i in range(len(sent)-2):

        if skip == True:
            skip = False
            continue

        leftContext = sent[i]
        target = sent[i+1]
        rightContext = sent[i+2]

        if (leftContext[1]=="MD")&(target[1]=="UNK")&(rightContext[0].lower() == "as")&(target[0].lower()!="just"):

            sentToReturn += [leftContext]
            newTup = (target[0], "V")
            sentToReturn += [newTup]

            skip = True
        else:

          sentToReturn += [leftContext]

    sentToReturn += [sent[len(sent)-2]]
    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn


#nouns tagged at end of IN "that" [punctuation mark] sequence
def IN_that_PucntuationTagging(sent):
    sentToReturn = []
    skip = False
    for i in range(len(sent)-2):

        if skip == True:
            skip = False
            continue

        leftContext = sent[i]
        target = sent[i+1]
        rightContext = sent[i+2]

        if (leftContext[1]=="IN")&(target[0].lower()=="that")&(target[1]=="UNK")&(
            (rightContext[0] == ".")|(rightContext[0] == ",")|(rightContext[0] == "!")|
            (rightContext[0] == "?")|(rightContext[0] == ":")|(rightContext[0] == "?")):

            sentToReturn += [leftContext]
            newTup = (target[0], "DT")
            sentToReturn += [newTup]

            skip = True
        else:

          sentToReturn += [leftContext]

    sentToReturn += [sent[len(sent)-2]]
    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn



#"that" P V sequence, "that" tagged as WDT
def that_P_VThatTagger(sent):
    sentToReturn = []
    skip = False
    for i in range(len(sent)-2):

        if skip == True:
            skip = False
            continue

        leftContext = sent[i]
        target = sent[i+1]
        rightContext = sent[i+2]

        if (leftContext[0].lower()=="that")&(leftContext[1] == "UNK")&(target[1].startswith("P"))&\
                (rightContext[1].startswith("V")):


            newTup = (leftContext[0], "WDT")
            sentToReturn += [newTup]
            sentToReturn += [target]

            skip = True
        else:

          sentToReturn += [leftContext]

    sentToReturn += [sent[len(sent)-2]]
    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn