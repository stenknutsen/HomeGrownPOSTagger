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


        if ((leftContext[1]=="DT"))&(leftTarget[1]=="UNK")&(rightTarget[1]=="UNK")&((rightContext[1]==".")|(rightContext[1]==";")):

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


        if ((leftContext[1]=="IN"))&(leftTarget[1]=="UNK")&(rightTarget[1]=="UNK")&((rightContext[1]==".")|(rightContext[1]==";")):

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


        if ((leftContext[1]=="IN")|(leftContext[1]=="PRP$"))&(leftTarget[1].startswith("N"))&(rightTarget[1]=="UNK")&((rightContext[1]==".")|(rightContext[1]==";")):

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


        if ((leftContext[1]=="IN")|(leftContext[1]=="PRP$"))&(rightTarget[1]=="UNK")&((rightContext[1]==".")|(rightContext[1]==";")):

            sentToReturn += [leftContext]


            sentToReturn += [(leftTarget[0], "J")]


            sentToReturn += [(rightTarget[0],"N")]

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


#tags words between DT and "," N as N
def DT_UNK_PUNC_N_Tagger(sent):
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


        if (leftContext[1]=="DT")&(leftTarget[1]=="UNK")&(rightTarget[1]==",")&(rightContext[1].startswith("N")):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "N")]
            sentToReturn += [rightTarget]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn


#tags words between PRP "to" and N as V
def PRP_to_UNK_N_Tagger(sent):
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


        if (leftContext[1]=="PRP")&(leftTarget[0].lower()=="to")&(rightTarget[1]=="UNK")&(rightContext[1].startswith("N")):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "TO")]
            sentToReturn += [(rightTarget[0],"V")]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn


#tags words between DT and "to V" as N TO
def DT_UNK_to_V_Tagger(sent):
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


        if (leftContext[1]=="DT")&(leftTarget[1]=="UNK")&(rightTarget[0].lower()=="to")&(rightContext[1].startswith("V")):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "N")]
            sentToReturn += [(rightTarget[0],"TO")]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn





#tags words between DT and V as J N
def DT_UNK_UNK_V_Tagger(sent):
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


        if (leftContext[1]=="DT")&(leftTarget[1]=="UNK")&(rightTarget[1]=="UNK")&(rightContext[1].startswith("V")):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "J")]
            sentToReturn += [(rightTarget[0],"N")]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn


#tags words between "be so" and "that" as J
def be_so_UNK_that_Tagger(sent):
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


        if ((leftContext[0].lower()=="are")|(leftContext[0].lower()=="is")|(leftContext[0].lower()=="was")|(leftContext[0].lower()=="were"))&\
                (leftTarget[0].lower()=="so")&(rightTarget[1]=="UNK")&(rightContext[0]=="that"):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "RB")]
            sentToReturn += [(rightTarget[0],"J")]
            sentToReturn += [(rightContext[0],"IN")]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags words between IN and N "that" as J
def IN_UNK_N_that_Tagger(sent):
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


        if (leftContext[1]=="IN")&(leftTarget[1]=="UNK")&(rightTarget[1].startswith("N"))&(rightContext[0].lower()=="that"):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "J")]
            sentToReturn += [rightTarget]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags words between "who" and "ly" IN as V, RB
def who_UNK_ly_IN_Tagger(sent):
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


        if (leftContext[0].lower()=="who")&(leftTarget[1]=="UNK")&(rightTarget[0].endswith("ly"))&(rightContext[1]=="IN"):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "V")]
            sentToReturn += [(rightTarget[0],"RB")]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags words between J "to" and "there as TO V
def J_to_UNK_there_Tagger(sent):
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


        if (leftContext[1].startswith("J"))&(leftTarget[0].lower()=="to")&(rightTarget[1]=="UNK")&(rightContext[0].lower()=="there"):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "TO")]
            sentToReturn += [(rightTarget[0],"V")]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags words between IN NN and as J when ending in comma or period
def IN_UNK_NN_PUNC_Tagger(sent):
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


        if (leftContext[1]=="IN")&(leftTarget[1]=="UNK")&(rightTarget[1].startswith("N"))&((rightContext[0]==",")|(rightContext[0]==".")):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "J")]
            sentToReturn += [rightTarget]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn


#tags words between that and PRP as V
def that_UNK_PRP_to_Tagger(sent):
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


        if (leftContext[0].lower()=="that")&(leftTarget[1]=="UNK")&(rightTarget[1]=="PRP")&(rightContext[0].lower()=="to"):

            sentToReturn += [(leftContext[0],"WDT")]
            sentToReturn += [(leftTarget[0], "V")]
            sentToReturn += [rightTarget]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn


#tags words between CD and "'" as NNS POS and N
def CD_UNK_PUNC_UNK_Tagger(sent):
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


        if (leftContext[1]=="CD")&(leftTarget[1]=="UNK")&(rightTarget[0]=="'")&(rightContext[1]=="UNK"):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "NNS")]
            sentToReturn += [(rightTarget[0],"POS")]
            sentToReturn += [(rightContext[0],"N")]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags words between CD and "ing" as NNS VBG
def CD_UNK_ing_on_Tagger(sent):
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


        if (leftContext[1]=="CD")&(leftTarget[1]=="UNK")&(rightTarget[0].lower().endswith("ing"))&(rightContext[0].lower()=="on"):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "NNS")]
            sentToReturn += [(rightTarget[0],"VBG")]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags words between CD and "there" as NNS
def CD_UNK_there_PUNC_Tagger(sent):
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


        if (leftContext[1]=="CD")&(leftTarget[1]=="UNK")&(rightTarget[0].lower()=="there")&((rightContext[0]==",")|(rightContext[0]==".")):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "NNS")]
            sentToReturn += [(rightTarget[0],"RB")]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn



#tags words after "a" and before "," as J N
def a_UNK_UNK_PUNC_Tagger(sent):
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


        if (leftContext[0].lower()=="a")&(leftTarget[1]=="UNK")&(rightTarget[1]=="UNK")&(rightContext[0]==","):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "J")]
            sentToReturn += [(rightTarget[0],"N")]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#
def to_UNK_N_that_Tagger(sent):
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


        if (leftContext[0].lower()=="to")&(leftTarget[1]=="UNK")&(rightTarget[1].startswith("N"))&(rightContext[0].lower()=="that"):

            sentToReturn += [(leftContext[0],"TO")]
            sentToReturn += [(leftTarget[0], "N")]
            sentToReturn += [rightTarget]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#
def IN_UNK_PUNC_so_Tagger(sent):
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


        if (leftContext[1]=="IN")&(leftTarget[1]=="UNK")&(rightTarget[0]==",")&(rightContext[0].lower()=="so"):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "N")]
            sentToReturn += [rightTarget]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn


#
def MD_UNK_better_IN_Tagger(sent):
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


        if ((leftContext[1]=="MD")|((leftContext[1]=="UNK")&((leftContext[0].lower()=="will")|(leftContext[0].lower()=="must"))))&\
                (leftTarget[1]=="UNK")&(rightTarget[0].lower()=="better")&(rightContext[1]=="IN"):

            sentToReturn += [(leftContext[0],"MD")]
            sentToReturn += [(leftTarget[0], "V")]
            sentToReturn += [(rightTarget[0],"RB")]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#
def whether_to_UNK_to_Tagger(sent):
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


        if (leftContext[0].lower()=="whether")&(leftTarget[0].lower()=="to")&(rightTarget[1]=="UNK")&(rightContext[0].lower()=="to"):

            sentToReturn += [leftContext]
            sentToReturn += [(leftTarget[0], "TO")]
            sentToReturn += [(rightTarget[0],"VB")]
            sentToReturn += [rightContext]
            skip = 3

        else:
            sentToReturn += [leftContext]

    return sentToReturn