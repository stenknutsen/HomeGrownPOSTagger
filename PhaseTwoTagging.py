#uses immediate context (left or right) to tag POS


#tags anything 'to' before DT or PRP$ or NNP or CD as 'IN'(preposition)
def to_INtagger(sent):
    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[0].lower()=="to")&((context[1]=='DT')|(context[1]=='PRP$')|(context[1]=='NNP')|(context[1]=="CD")):
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
            (target[0].lower() == "been"))&(context[0].lower().endswith("ing")&(context[1]=="UNK")):
            newTup = (target[0],target[1])
            sentToReturn += [newTup]
            newTup = (context[0], "VBG")
            sentToReturn += [newTup]
            skip = True
        else:

          sentToReturn += [target]

    sentToReturn += [sent[len(sent)-1]]

    return sentToReturn


#tags existential "there" and "'s" as VBZ
def existentialThereTagger(sent):
    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[0].lower()=="there")&((context[0]=='is')|(context[0]=="'s")|(context[0]=='was')|(context[0]=='were')|
                                             (context[0]=='are')):
            newTup = (target[0], 'EX')
            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    #now tag "'s" as VBZ
    sentToReturn2 = []
    for i in range(len(sentToReturn)-1):
        target = sentToReturn[i]
        context = sentToReturn[i-1]

        if (context[0].lower()=="there")&(target[0].lower()=="'s"):

            newTup = (target[0], 'VBZ')
            sentToReturn2 += [newTup]
        else:
            sentToReturn2 += [target]
    sentToReturn2 += [sent[len(sent)-1]]

    return sentToReturn2


#tags "can" "might" "will" after modal_VB tagger
def can_might_will_VBTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if ((target[0].lower()=="can")|(target[0].lower()=="might")|(target[0].lower()=="will"))&(context[1]=='VB'):
            newTup = (target[0], 'MD')
            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn


#tags "'s" after PRP as VBZ
def PRP_isVBZTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i-1]

        if ((target[0].lower()=="'s")&(target[1]=="UNK"))&(context[1]=='PRP'):
            newTup = (target[0], 'VBZ')
            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn

#tags "her" as prp when follwed by a DT
def her_DT_PRPTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[1]=="UNK")&(target[0].lower()=="her")&(context[1]=='DT'):
            newTup = (target[0], 'PRP')
            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn


##tags words ending in "ed" followed by IN as V
def ed_IN_VBNTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[1]=="UNK")&(target[0].endswith("ed"))&(context[1]=='IN'):
            if (target[0].lower()=="need"):
                newTup = (target[0], 'NN')
            else:
                newTup = (target[0], 'V')

            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn

#tags anything ending in "s" followed by him/me/them as VBZ
def s_him_VBZTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[1]=="UNK")&(target[0].endswith("s"))&((context[0].lower()=='him')|(context[0].lower()=='me')|(context[0].lower()=='them')):

            newTup = (target[0], 'VBZ')

            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn


#tags anything ending in "ed" followed by him/me/them as VBD
def ed_him_VBNTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[1]=="UNK")&(target[0].endswith("ed"))&((context[0].lower()=='him')|(context[0].lower()=='me')|(context[0].lower()=='them')):

            newTup = (target[0], 'VBD')

            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn

#tags anything following "have" verbs that ends in "ed" as VBN
def have_ed_VBNTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i-1]

        if (target[1]=="UNK")&(target[0].endswith("ed"))&((context[0]=='have')|(context[0]=='has')|(context[0]=='has')|
                                                          (context[0]=='having')):

            newTup = (target[0], 'VBN')

            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn


#tags anything  *ed and out as V, an out as RP
def d_out_VerbTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[0].endswith("d"))&(context[0].lower()=='out'):
            if (target[0].lower()=="need"):
                newTup = (target[0], 'NN')
            else:
                newTup = (target[0], 'V')

            sentToReturn += [newTup]
        else:
            sentToReturn += [target]

    sentToReturn += [sent[len(sent)-1]]

    sentToReturn2 =[]
    for i in range(len(sentToReturn)-1):
        target = sentToReturn[i]
        context = sentToReturn[i-1]
        if (target[1]=="UNK")&(target[0].lower()=="out")&(context[1]=="V"):
            newTup = (target[0],"RP")
            sentToReturn2 += [newTup]
        else:
            sentToReturn2+=[target]

    sentToReturn2 += [sentToReturn[len(sentToReturn)-1]]

    return sentToReturn2

##tags words ending in "ial" followed by N as JJ
def ial_N_JJTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[1]=="UNK")&(target[0].endswith("ial"))&(context[1].startswith("N")):

            newTup = (target[0], 'JJ')

            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn

##tags "can" as MD when followed by PRP
def can_PRP_MDTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[1]=="UNK")&(target[0].lower()=="can")&(context[1]=="PRP"):

            newTup = (target[0], 'MD')

            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn


##tags "ing" as VBG when followed by "for"
def ing_for_VerbTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[1]=="UNK")&(target[0].endswith("ing"))&(context[0].lower()=="for"):

            newTup = (target[0], 'VBG')

            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn

##tags "around" followed by DT or N as IN
def around_DT_PrepositionTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[0].lower()=="around")&((context[1].startswith("N"))|(context[1]=="DT")):

            newTup = (target[0], 'IN')

            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn

##tags "which" followed by PRP as WDT
def which_PRP_WDTTagger(sent):

    sentToReturn = []

    for i in range(len(sent)-1):
        target = sent[i]
        context = sent[i+1]

        if (target[0].lower()=="which")&(context[1]=="PRP"):

            newTup = (target[0], 'WDT')

            sentToReturn += [newTup]
        else:
            sentToReturn += [target]
    sentToReturn += [sent[len(sent)-1]]
    return sentToReturn



#tags words afet IN ending in "ine(s)" as N
def IN_ine_NounTagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue

        if (i)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        target = sent[i+1]


        if ((leftContext[1]=="IN")|(leftContext[1]=="DT"))&(target[1]=="UNK")&((target[0].lower().endswith("ine"))|(target[0].lower().endswith("ines"))):

            sentToReturn += [leftContext]
            sentToReturn += [(target[0], "N")]

            skip = 1

        else:
            sentToReturn += [leftContext]

    return sentToReturn





#tags words ending in "ism(s)" followed by "that" as N
def ism_that_NounTagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue

        if (i)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        target = sent[i+1]


        if (leftContext[1]=="UNK")&((leftContext[0].lower().endswith("ism"))|(leftContext[0].lower().endswith("isms")))&(target[1]=="UNK")&(target[0].lower()=="that"):

            sentToReturn += [(leftContext[0],"N")]
            sentToReturn += [(target[0], "WDT")]

            skip = 1

        else:
            sentToReturn += [leftContext]

    return sentToReturn


#tags "so that" as IN IN
def so_that_PrepositionTagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue

        if (i)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        target = sent[i+1]


        if (leftContext[1]=="UNK")&(leftContext[0].lower()=="so")&(target[1]=="UNK")&(target[0].lower()=="that"):

            sentToReturn += [(leftContext[0],"IN")]
            sentToReturn += [(target[0], "IN")]

            skip = 1

        else:
            sentToReturn += [leftContext]

    return sentToReturn



#tags "own" as JJ when precede by PRP$
def PRPS_own_AdjectiveTagger(sent):
    sentToReturn = []
    skip = 0

    for i in range(len(sent)):

        if skip>0:
            skip = skip -1
            continue

        if (i)<0 | (i+1)>=len(sent):
            sentToReturn += [sent[i]]
            continue

        leftContext = sent[i]
        target = sent[i+1]


        if (leftContext[1]=="PRP$")&(target[1]=="UNK")&(target[0].lower()=="own"):

            sentToReturn += [leftContext]
            sentToReturn += [(target[0], "JJ")]

            skip = 1

        else:
            sentToReturn += [leftContext]

    return sentToReturn

#tags anything ***at beginning of sent*** followed by "who" as NNS.
def UNK_who_NounTagger(sent):
    sentToReturn = []
    first = sent[0]
    second = sent[1]

    if (first[1]== "UNK")&(second[0]=="who"):
        newFirst = (first[0],"NNS")
        newSecond = second

    else:
        newFirst = first
        newSecond = second


    sentToReturn.append(newFirst)
    sentToReturn.append(newSecond)


    for i in range(2,len(sent)):
        sentToReturn.append(sent[i])



    return sentToReturn