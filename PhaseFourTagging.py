# 4-grams

#tags words between "DT" and "IN" as J and N
def DT_UNK_UNK_IN_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+3)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        rightTarget = sent[i+2]
        rightContext = sent[i+3]


        if ((leftContext[1]=="DT"))&(leftTarget[1]=="UNK")&(rightTarget[1]=="UNK")&((rightContext[1]=="IN")|(rightContext[0].lower()=="to")):

            sentToReturn += [leftContext]

            newTup = (leftTarget[0], "J")
            sentToReturn += [newTup]

            newTup = (rightTarget[0], "N")
            sentToReturn += [newTup]

            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags words between "DT" and "." as J and N
def DT_UNK_UNK_PUNC_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+3)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        rightTarget = sent[i+2]
        rightContext = sent[i+3]


        if ((leftContext[1]=="DT"))&(leftTarget[1]=="UNK")&(rightTarget[1]=="UNK")&(rightContext[1]=="."):

            sentToReturn += [leftContext]

            newTup = (leftTarget[0], "J")
            sentToReturn += [newTup]

            newTup = (rightTarget[0], "N")
            sentToReturn += [newTup]

            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags words between "IN" and "." as J and N
def IN_UNK_UNK_PUNC_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+3)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        rightTarget = sent[i+2]
        rightContext = sent[i+3]


        if ((leftContext[1]=="IN"))&(leftTarget[1]=="UNK")&(rightTarget[1]=="UNK")&(rightContext[1]=="."):

            sentToReturn += [leftContext]

            newTup = (leftTarget[0], "J")
            sentToReturn += [newTup]

            newTup = (rightTarget[0], "N")
            sentToReturn += [newTup]

            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn


#tags word between IN/PRP$, N and "." as N
def IN_N_UNK_PUNC_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+3)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        rightTarget = sent[i+2]
        rightContext = sent[i+3]


        if ((leftContext[1]=="IN")|(leftContext[1]=="PRP$"))&(leftTarget[1].startswith("N"))&(rightTarget[1]=="UNK")&(rightContext[1]=="."):

            sentToReturn += [leftContext]


            sentToReturn += [leftTarget]

            newTup = (rightTarget[0], "N")
            sentToReturn += [newTup]

            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags word between IN/PRP$, N and "." as J
def IN_UNK_N_PUNC_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+3)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        rightTarget = sent[i+2]
        rightContext = sent[i+3]


        if ((leftContext[1]=="IN")|(leftContext[1]=="PRP$"))&(leftTarget[1]=="UNK")&(rightTarget[1].startswith("N"))&(rightContext[1]=="."):

            sentToReturn += [leftContext]


            sentToReturn += [(leftTarget[0], "J")]


            sentToReturn += [rightTarget]

            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags words between "ing" and "." as J and N
def ing_what_UNK_to_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+3)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        rightTarget = sent[i+2]
        rightContext = sent[i+3]


        if ((leftContext[1]=="UNK")&(leftContext[0].lower().endswith("ing")))&(leftTarget[0].lower()=="what")&\
                (rightTarget[1]=="UNK")&(rightContext[0].lower()=="to"):

            sentToReturn += [(leftContext[0], "VBG")]


            sentToReturn += [leftTarget]

            newTup = (rightTarget[0], "V")
            sentToReturn += [newTup]

            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn


#tags words between IN and DT as J and N
def IN_UNK_UNK_DT_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+3)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        rightTarget = sent[i+2]
        rightContext = sent[i+3]


        if ((leftContext[1]=="IN"))&(leftTarget[1]=="UNK")&(rightTarget[1]=="UNK")&(rightContext[1]=="DT"):

            sentToReturn += [leftContext]

            newTup = (leftTarget[0], "J")
            sentToReturn += [newTup]

            newTup = (rightTarget[0], "N")
            sentToReturn += [newTup]

            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags words between IN and "," ending in "ble" and UNK, as J and N
def IN_able_UNK_PUNC_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+3)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        rightTarget = sent[i+2]
        rightContext = sent[i+3]


        if ((leftContext[1]=="IN"))&(leftTarget[1]=="UNK")&(leftTarget[0].endswith("ble"))&(rightTarget[1]=="UNK")&(rightContext[1]==","):

            sentToReturn += [leftContext]

            newTup = (leftTarget[0], "J")
            sentToReturn += [newTup]

            newTup = (rightTarget[0], "N")
            sentToReturn += [newTup]

            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags words between N and "that" DT as V and IN
def N_UNK_that_DT_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+3)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        rightTarget = sent[i+2]
        rightContext = sent[i+3]


        if (leftContext[1].startswith("N"))&(leftTarget[1]=="UNK")&(rightTarget[1]=="UNK")&(rightTarget[0].lower()=="that")&(rightContext[1]=="DT"):

            sentToReturn += [leftContext]

            newTup = (leftTarget[0], "V")
            sentToReturn += [newTup]

            newTup = (rightTarget[0], "IN")
            sentToReturn += [newTup]

            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn