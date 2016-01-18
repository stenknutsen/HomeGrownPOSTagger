#5-grams

#
def IN_N_and_UNK_PUNC_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+4)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        centerTarget = sent[i+2]
        rightTarget = sent[i+3]
        rightContext = sent[i+4]


        if (leftContext[1]=="IN")&(leftTarget[1].startswith("N"))&(centerTarget[0].lower()=="and")&\
                (rightTarget[1]=="UNK")&(rightTarget[0].endswith("ing"))&(rightContext[1]==","):

            sentToReturn += [leftContext]
            sentToReturn += [leftTarget]
            sentToReturn += [centerTarget]
            sentToReturn += [(rightTarget[0],"N")]
            sentToReturn += [rightContext]
            skip = 4

        else:
            sentToReturn += [leftContext]

    return sentToReturn


#
def DT_UNK_UNK_PUNC_N_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+4)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        centerTarget = sent[i+2]
        rightTarget = sent[i+3]
        rightContext = sent[i+4]


        if (leftContext[1]=="DT")&(leftTarget[1]=="UNK")&(centerTarget[1]=="UNK")&\
                (rightTarget[1]==",")&(rightContext[1].startswith("N")):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0],"J")]
            sentToReturn += [(centerTarget[0],"N")]
            sentToReturn += [rightTarget]
            sentToReturn += [rightContext]
            skip = 4

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#
def PRPS_UNK_s_UNK_PUNC_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+4)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        centerTarget = sent[i+2]
        rightTarget = sent[i+3]
        rightContext = sent[i+4]


        if (leftContext[1]=="PRP$")&(leftTarget[1]=="UNK")&(centerTarget[0]=="'s")&(rightTarget[1]=="UNK")&\
                ((rightContext[0]==",")|(rightContext[0]==".")):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0],"N")]
            sentToReturn += [(centerTarget[0],"POS")]
            sentToReturn += [(rightTarget[0],"N")]
            sentToReturn += [rightContext]
            skip = 4

        else:
            sentToReturn += [leftContext]

    return sentToReturn


#
def to_UNK_how_to_UNK_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+4)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        centerTarget = sent[i+2]
        rightTarget = sent[i+3]
        rightContext = sent[i+4]


        if (leftContext[0].lower()=="to")&(leftTarget[1]=="UNK")&(centerTarget[0].lower()=="how")&(rightTarget[0].lower()=="to")&\
                (rightContext[1]=="UNK"):

            sentToReturn += [(leftContext[0],"TO")]
            sentToReturn += [(leftTarget[0],"V")]
            sentToReturn += [centerTarget]
            sentToReturn += [(rightTarget[0],"TO")]
            sentToReturn += [(rightContext[0],"V")]
            skip = 4

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#
def when_PRPS_N_UNK_RB_Tagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue


        if (i)<0 | (i+4)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        leftTarget = sent[i+1]
        centerTarget = sent[i+2]
        rightTarget = sent[i+3]
        rightContext = sent[i+4]


        if (leftContext[0].lower()=="when")&(leftTarget[1]=="PRP$")&(centerTarget[1].startswith("N"))&(rightTarget[1]=="UNK")&\
                (rightContext[1]=="RB"):

            sentToReturn += [leftContext]
            sentToReturn += [leftTarget]
            sentToReturn += [centerTarget]
            sentToReturn += [(rightTarget[0],"VBD")]
            sentToReturn += [rightContext]
            skip = 4

        else:
            sentToReturn += [leftContext]

    return sentToReturn