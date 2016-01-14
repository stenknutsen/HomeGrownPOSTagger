#uses two points of context (left or right) to tag (provisionally, in cases of N and V)

#tags anything between a DT and IN/PRP/PRP$/"her" as N. Note *****(add plural filter later)*******
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

        if (leftContext[1] == "DT")&((rightContext[1] == "IN")|(rightContext[1]=="PRP")|(rightContext[1]=="PRP$")|
                                         (rightContext[0].lower()=="her"))&(target[1]=="UNK"):

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

#nouns tagged between DT & [punctuation]
def DT_PuctuationNounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]

        if ((leftContext[1]=="DT")|(leftContext[1]=="PRP$"))&((rightContext[1] == ".")|(rightContext[1] == "!")|
                                   (rightContext[1] == "?")|(rightContext[1] == ":")|(rightContext[1] == ";")):


            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

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


#wh-pronouns tagged at end of IN "that" [punctuation mark] sequence
def IN_that_PucntuationTagging(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if (leftContext[1]=="IN")&(target[0].lower()=="that")&(target[1]=="UNK")&(
            (rightContext[0] == ".")|(rightContext[0] == ",")|(rightContext[0] == "!")|
            (rightContext[0] == "?")|(rightContext[0] == ":")|(rightContext[0] == "?")):

            newTup = (target[0], "DT")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#"that" P V sequence, "that" tagged as IN
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


            newTup = (leftContext[0], "IN")
            sentToReturn += [newTup]
            sentToReturn += [target]

            skip = True
        else:

          sentToReturn += [leftContext]

    sentToReturn += [sent[len(sent)-2]]
    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn

#tags words between modal and prep/"her"/DT/N as VB
def modal_VB_DTTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if((leftContext[1] == "MD")|(leftContext[0].lower() == "will")|(leftContext[0].lower() == "can")|
            (leftContext[0].lower() == "might"))&((rightContext[0].lower()=="her")|(rightContext[1]=="PRP")|
            (rightContext[1]=="DT")|(rightContext[1].startswith("N")|(rightContext[1]=="PRP$"))):

            newTup = (target[0], "VB")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#provisionally tags words between DT/POS/"her"/PRP$/WDT and N as J*******needs repair
def DT_ADJ_NTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if((leftContext[1] == "WDT")|(leftContext[0].lower() == "her")|(leftContext[1] == "PRP$")|(leftContext[1] == "IN")|
            (leftContext[1] == "POS")|(leftContext[1] == "DT"))&(rightContext[1].startswith("N"))&(target[1]=='UNK'):

            newTup = (target[0], "J")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#tags words between DT and "'s" as NN
def DT_noun_POSTagger(sent):
    sentToReturn = []
    ##first tag NN
    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if (leftContext[1] == "DT")&(rightContext[0].lower()=="'s")&(target[1]=='UNK'):

            newTup = (target[0], "NN")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]


    #then tag 's as POS
    sentToReturn2 = []
    for i in range(len(sentToReturn)):

        if (i-1)<0 | (i+1)>=len(sentToReturn):
            sentToReturn2 += [sentToReturn[i]]
            continue

        leftContext = sentToReturn[i-1]
        target = sentToReturn[i]
        rightContext = sentToReturn[i+1]


        if (leftContext[1] == "NN")&(target[0].lower()=="'s"):

            newTup = (target[0], "POS")
            sentToReturn2 += [newTup]

        else:
            sentToReturn2 += [target]
    return sentToReturn2

##tags words between "have" and DT as VBN
def have_DT_VBNTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if((leftContext[0].lower() == "having")|(leftContext[0].lower() == "has")|(leftContext[0].lower() == "have")|
               (leftContext[0].lower() == "had"))&(rightContext[1] == "DT")&(target[1]=='UNK'):

            newTup = (target[0], "VBN")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#tags words ending with "ing" between IN and DT as VBG
def IN_DT_VBGTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1] == "IN")&(rightContext[1] == "DT")&(target[1]=='UNK')&(target[0].lower().endswith("ing")):

            newTup = (target[0], "VBG")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#tags words between J and IN as N
def J_UNK_IN_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1].startswith("J"))&(rightContext[1] == "IN")&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn



#tags words between PRP and "too" as V
def PRP_UNK_to_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="PRP")&(rightContext[0].lower() == "too")&(target[1]=='UNK'):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words between JJ and PUNC as N
def JJ_UNK_PUNC_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="JJ")&((rightContext[0] == "?")|(rightContext[0] == ".")|(rightContext[0] == ",")|
                                  (rightContext[0] == ":")|(rightContext[0] == "!"))&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words between "be" verb and TO as JJ
def be_UNK_TO_AdjectiveTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if((leftContext[0].lower()=="'s")|(leftContext[0].lower()=="been")|(leftContext[0].lower()=="is")|(leftContext[0].lower()=="was")|
           (leftContext[0].lower()=="were")|(leftContext[0].lower()=="be"))&(rightContext[1] == "TO")&(target[1]=='UNK'):

            newTup = (target[0], "JJ")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words between POS/PRP$  and V as N
def POS_UNK_V_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if((leftContext[1]=="PRP$")|(leftContext[1]=="POS"))&(rightContext[1].startswith("V"))&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words between MD and "to" as V
def MD_UNK_to_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="MD")&(rightContext[0] == "to")&(target[1]=='UNK'):

            newTup = (target[0], "VB")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#tags words between "be" verbs  and PUNC at end of sentence as JJ
def be_UNK_PUNC_AdjectiveTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if((leftContext[0].lower()=="'s")|(leftContext[0].lower()=="is")|(leftContext[0].lower()=="was")|
           (leftContext[0].lower()=="were")|(leftContext[0].lower()=="be"))&((rightContext[0] == ".")|(rightContext[0] == "!")|
                                                                             (rightContext[0] == "?"))&(target[1]=='UNK'):

            newTup = (target[0], "JJ")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#tags words between a comma and DT and ending in "ing" as VBG
def COMMA_ing_DT_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[0]==",")&(rightContext[1] == "DT")&(target[1]=='UNK'):

            newTup = (target[0], "VBG")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words between J and RB as N
def J_UNK_RB_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1].startswith("J"))&(rightContext[1] == "RB")&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#tags words between RB and PRP$ as V
def RB_UNK_PRPS_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="RB")&(rightContext[1] == "PRP$")&(target[1]=='UNK'):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words between PRP$ and "to" as N
def PRPS_UNK_to_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="PRP$")&(rightContext[0].lower() == "to")&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words after V and IN ending in "ing" as VBG
def V_IN_ing_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-2)<0 | (i)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftmostContext = sent[i-2]
        leftContext = sent[i-1]
        target = sent[i]


        if(leftmostContext[1].startswith("V"))&(leftContext[1] == "IN")&(target[1]=='UNK')&((target[0].endswith("ing"))):

            newTup = (target[0], "VBG")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn



#tags words between IN and IN and ending in "ent" or "es" as N
def IN_UNK_IN_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="IN")&(rightContext[1] == "IN")&(target[1]=='UNK')&((target[0].endswith("ent"))|(target[0].endswith("es"))|
                                                                                   (target[0].endswith("ps"))):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#tags words between IN and "." as N
def IN_UNK_PUNC_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="IN")&(rightContext[0] == ".")&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#tags words between "who" and J as V
def who_UNK_J_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[0].lower()=="who")&(rightContext[1].startswith("J"))&(target[1]=='UNK'):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words between IN and PRP($) ending in "ing" as VBG
def IN_ing_PRP_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="IN")&(rightContext[1].startswith("PRP"))&(target[1]=='UNK')&(target[0].endswith("ing")):

            newTup = (target[0], "VBG")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words between PRP and PRPS  as V
def PRP_UNK_PRPS_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="PRP")&((rightContext[1]=="PRP$")|(rightContext[0].lower()=="her"))&(target[1]=='UNK'):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#provisionally tags words between PRP and DT as V
def PRP_DT_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1] == "PRP")&(rightContext[1] == "DT")&(target[1]=='UNK'):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words ending in "ing" between N and PRP as VBG
def N_ing_PRP_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1].startswith("N"))&(rightContext[1] == "PRP")&(target[1]=='UNK')&(target[0].lower().endswith("ing")):

            newTup = (target[0], "VBG")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words between "to" and DT as VB, and then tags "to" as TO
def to_DT_VerbTagger(sent):
    sentToReturn = []
    ##first tag VB
    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if (leftContext[0].lower() == "to")&(rightContext[1]=="DT")&(target[1]=='UNK'):

            newTup = (target[0], "VB")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]


    #then tag 'to' as TO
    sentToReturn2 = []
    for i in range(len(sentToReturn)):

        if (i-1)<0 | (i+1)>=len(sentToReturn):
            sentToReturn2 += [sentToReturn[i]]
            continue

        leftContext = sentToReturn[i-1]
        target = sentToReturn[i]
        rightContext = sentToReturn[i+1]


        if (rightContext[1] == "VB")&(target[0].lower()=="to"):

            newTup = (target[0], "TO")
            sentToReturn2 += [newTup]

        else:
            sentToReturn2 += [target]
    return sentToReturn2

#tags words between MD and PUNC as VB
def MD_UNK_PUNC_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="MD")&(rightContext[0] == ".")&(target[1]=='UNK'):

            newTup = (target[0], "VB")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#tags words between DT amd WRB as N
def DT_UNK_WRB_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="DT")&(rightContext[1] == "WRB")&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn

#tags anything between DT and V as N
def DT_UNK_V_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="DT")&(rightContext[1].startswith("V"))&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags "that" between V and N as IN
def V_that_N_PrepositionTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1].startswith("V"))&(rightContext[1].startswith("N"))&(target[1]=='UNK')&(target[0].lower()=="that"):

            newTup = (target[0], "IN")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags anything between "to" and PRP($) as TO and VB
def to_UNK_PRP_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[0]=="to")&(rightContext[1].startswith("PRP"))&(target[1]=='UNK'):

            newTup = (target[0], "VB")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

     #then tag 'to' as TO
    sentToReturn2 = []
    for i in range(len(sentToReturn)):

        if (i-1)<0 | (i+1)>=len(sentToReturn):
            sentToReturn2 += [sentToReturn[i]]
            continue

        leftContext = sentToReturn[i-1]
        target = sentToReturn[i]
        rightContext = sentToReturn[i+1]


        if (rightContext[1] == "VB")&(target[0].lower()=="to"):

            newTup = (target[0], "TO")
            sentToReturn2 += [newTup]

        else:
            sentToReturn2 += [target]
    return sentToReturn2


#tags anything between N or PRP and "up" as V
def N_UNK_up_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if((leftContext[1]=="PRP")|(leftContext[1].startswith("N")))&(rightContext[0]=="up")&(target[1]=='UNK'):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    #then tag 'up' as RB
    sentToReturn2 = []
    for i in range(len(sentToReturn)):

        if (i-1)<0 | (i+1)>=len(sentToReturn):
            sentToReturn2 += [sentToReturn[i]]
            continue

        leftContext = sentToReturn[i-1]
        target = sentToReturn[i]
        rightContext = sentToReturn[i+1]


        if (leftContext[1] == "V")&(target[0].lower()=="up"):

            newTup = (target[0], "RB")
            sentToReturn2 += [newTup]

        else:
            sentToReturn2 += [target]
    return sentToReturn2

#tags anything ending in "s" followed by "her" and a DT/CC/IN or PRP$ as a VBZ, and tags "her" as PRP
def s_her_DT_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if (leftContext[0].endswith("s")&(target[1]=='UNK')&(target[0].lower()=="her")&((rightContext[1]=="CC")|
                                                                                        (rightContext[1]=="DT")|
                                                                                        (rightContext[1]=="IN")|
                                                                                        (rightContext[1]=="PRP$"))):

            newTup = (target[0], "PRP")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]


    sentToReturn2 = []
    for i in range(len(sentToReturn)):

        if (i-1)<0 | (i+1)>=len(sentToReturn):
            sentToReturn2 += [sentToReturn[i]]
            continue

        leftContext = sentToReturn[i-1]
        target = sentToReturn[i]
        rightContext = sentToReturn[i+1]


        if (rightContext[1] == "PRP")&(rightContext[0].lower() == "her")&(target[0].endswith("s")):

            newTup = (target[0], "VBZ")
            sentToReturn2 += [newTup]

        else:
            sentToReturn2 += [target]
    return sentToReturn2




#tags anything ending in "ed" followed by "her" and a DT/CC/IN or PRP$ as a VBD, and tags "her" as PRP
def ed_her_DT_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if (leftContext[0].endswith("ed")&(target[1]=='UNK')&(target[0].lower()=="her")&((rightContext[1]=="CC")|
                                                                                        (rightContext[1]=="DT")|
                                                                                        (rightContext[1]=="IN")|
                                                                                        (rightContext[1]=="PRP$"))):

            newTup = (target[0], "PRP")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]


    sentToReturn2 = []
    for i in range(len(sentToReturn)):

        if (i-1)<0 | (i+1)>=len(sentToReturn):
            sentToReturn2 += [sentToReturn[i]]
            continue

        leftContext = sentToReturn[i-1]
        target = sentToReturn[i]
        rightContext = sentToReturn[i+1]


        if (rightContext[1] == "PRP")&(rightContext[0].lower() == "her")&(target[0].endswith("ed")):

            newTup = (target[0], "VBD")
            sentToReturn2 += [newTup]

        else:
            sentToReturn2 += [target]
    return sentToReturn2


#tags words between to/IN/PRP$ as N, and then tags "to" as IN
def IN_UNK_CC_NounTagger(sent):
    sentToReturn = []
    ##first tag N
    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if ((leftContext[1]=="IN")|(leftContext[1]=="PRP$"))&(rightContext[1]=="CC")&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]


    #then tag 'to' as IN
    sentToReturn2 = []
    for i in range(len(sentToReturn)):

        if (i-1)<0 | (i+1)>=len(sentToReturn):
            sentToReturn2 += [sentToReturn[i]]
            continue

        leftContext = sentToReturn[i-1]
        target = sentToReturn[i]
        rightContext = sentToReturn[i+1]


        if (rightContext[1] == "N")&(target[0].lower()=="to")&(target[1]=="UNK"):

            newTup = (target[0], "IN")
            sentToReturn2 += [newTup]

        else:
            sentToReturn2 += [target]
    return sentToReturn2

#tags words between "to" and "IN" as V, and then tags "to" as TO
def to_UNK_IN_VerbTagger(sent):
    sentToReturn = []
    ##first tag v
    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if ((leftContext[0].lower()=="to"))&((rightContext[1]=="IN"))&(target[1]=='UNK'):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]
    #then tag 'to' as TO
    sentToReturn2 = []
    for i in range(len(sentToReturn)):

        if (i-1)<0 | (i+1)>=len(sentToReturn):
            sentToReturn2 += [sentToReturn[i]]
            continue

        leftContext = sentToReturn[i-1]
        target = sentToReturn[i]
        rightContext = sentToReturn[i+1]


        if (rightContext[1] == "V")&(target[0].lower()=="to")&(target[1]=="UNK"):

            newTup = (target[0], "TO")
            sentToReturn2 += [newTup]

        else:
            sentToReturn2 += [target]
    return sentToReturn2


#tags words between "can" and IN as V, and then tags "can" as MD
def can_UNK_IN_VerbTagger(sent):
    sentToReturn = []
    ##first tag v
    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if ((leftContext[0].lower()=="can"))&(rightContext[1]=="IN")&(target[1]=='UNK'):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]
    #then tag 'can' as MD
    sentToReturn2 = []
    for i in range(len(sentToReturn)):

        if (i-1)<0 | (i+1)>=len(sentToReturn):
            sentToReturn2 += [sentToReturn[i]]
            continue

        leftContext = sentToReturn[i-1]
        target = sentToReturn[i]
        rightContext = sentToReturn[i+1]


        if (rightContext[1] == "V")&(target[0].lower()=="can")&(target[1]=="UNK"):

            newTup = (target[0], "MD")
            sentToReturn2 += [newTup]

        else:
            sentToReturn2 += [target]
    return sentToReturn2



#tags anything between "who" and "to" as V
def who_UNK_to_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[0].lower()=="who")&(rightContext[0].lower()=="to")&(target[1]=='UNK'):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags anything between CD and IN as N
def CD_UNK_IN_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="CD")&(rightContext[1]=="IN")&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags anything between CD and PUNC as N
def CD_UNK_PUNC_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="CD")&(rightContext[0]==".")&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn



#tags anything between PRP$ and IN as N
def PRPS_UNK_IN_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="PRP$")&(rightContext[1]=="IN")&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags anything between PRP and "to"  that ends in "s" or "ed" as V
def PRP_s_toVerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="PRP")&(rightContext[0].lower()=="to")&(target[1]=='UNK')&((target[0].lower().endswith("s"))|
                                                                                          (target[0].lower().endswith("ed"))):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags anything between who and N  that ends in "s" or "ed" as V
def who_s_N_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[0].lower()=="who")&(rightContext[1].startswith("N"))&(target[1]=='UNK')&((target[0].lower().endswith("s"))|
                                                                                          (target[0].lower().endswith("ed"))):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags anything between RB and DT  that ends in "ed" as V
def RB_ed_DT_VerbTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="RB")&(rightContext[1]=="DT")&(target[1]=='UNK')&(target[0].lower().endswith("ed")):

            newTup = (target[0], "V")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn



#tags anything between DT and PUNC  that ends in "s" as NNS
def DT_s_PUNC_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="DT")&((rightContext[0].lower()==",")|(rightContext[0].lower()==".")|(rightContext[0].lower()==":")|
                                  (rightContext[0].lower()=="?")|(rightContext[0].lower()=="!")
                                  )&(target[1]=='UNK')&(target[0].lower().endswith("s")):

            newTup = (target[0], "NNS")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags words ending inbetween CD and V as N
def CD_UNK_V_NounTagger(sent):
    sentToReturn = []

    for i in range(len(sent)):

        if (i-1)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i-1]
        target = sent[i]
        rightContext = sent[i+1]


        if(leftContext[1]=="CD")&(rightContext[1].startswith("V"))&(target[1]=='UNK'):

            newTup = (target[0], "N")
            sentToReturn += [newTup]

        else:
            sentToReturn += [target]

    return sentToReturn


#tags anything ***at beginning of sent*** between DT and "that" as N. Tags "that" as WDT
def DT_UNK_that_NounTagger(sent):
    sentToReturn = []
    first = sent[0]
    second = sent[1]
    third = sent[2]
    if (first[1]== "DT")&(second[1]== "UNK")&(third[0].lower()== "that"):
        newFirst = first
        newSecond = (second[0],"N")
        newThird = (third[0],"WDT")
    else:
        newFirst = first
        newSecond = second
        newThird = third

    sentToReturn.append(newFirst)
    sentToReturn.append(newSecond)
    sentToReturn.append(newThird)

    for i in range(3,len(sent)):
        sentToReturn.append(sent[i])



    return sentToReturn