import headers

#In this phase of tagging, there will be no consideration of context.
#Unambigous, closed-class(and nearly closed-class) morphemes will be tagged.
#Morphemes are also tagged by unique orthographic features.

#dictionary of exceptions to ending clusters
endingClusterExceptions = {"witness":"UNK","witnesses":"UNK", "priest":"NN","earliest":"UNK","ration":"UNK",
                           "station":"UNK","vacation":"UNK","rations":"UNK","stations":"UNK","vacations":"UNK",
                           "questions":"UNK","question":"UNK","mention":"UNK","mentions":"UNK"}

#list of ending clusters
endingClusterList = [("ness","NN"),("nesses","NNS"),("iest","JJS"),("ation","NN"),("ations","NNS"),("stion","NN"),
                     ("stions","NNS"),("ntion","NN"),("ntions","NNS")]

tinyDictionary = {",":",",".":".",";":";","?":"?","!":"!",#punctuation
    "a":"DT","an":"DT","any":"DT","the":"DT","this":"DT","these":"DT","those":"DT",#determiners
    "my":"PRP$", "your":"PRP$","its":"PRP$","our":"PRP$", "their":"PRP$","his":"PRP$",#posessive pronouns
    "and":"CC","or":"CC", "but":"CC","&":"CC", "nor":"CC",#coordingating conjuctions
    "in":"IN","by":"IN", "of":"IN","for":"IN","with":"IN","on":"IN","at":"IN","from":"IN","into":"IN",
    "through":"IN", "after":"IN", "over":"IN","between":"IN","before":"IN","during":"IN","under":"IN",#prepositions
    "me":"PRP","him":"PRP","us":"PRP","them":"PRP","i":"PRP","she":"PRP","he":"PRP","we":"PRP","they":"PRP",
    "it":"PRP",#personal pronouns
    "cannot":"MD","could":"MD","may":"MD", "must":"MD", "ought":"MD", "shall":"MD", "should":"MD", "would":"MD",#modals
    "having":"VBG","has":"VBZ","be":"VB","was":"VBD","were":"VBD","been":"VBN","am":"VPB","are":"VBP",
    "is":"VBP", "did":"VBD", "doing":"VBG", "done":"VBN", "does":"VBZ", "'ve":"VBP", "'d":"MD",
    "'m":"VBP", "'re":"VBP",#aux verbs
    "something":"NN", "nothing":"NN", "anything":"NN", "everything":"NN", "someone":"NN", "everyone":"NN",
    "anyone":"NN", "everybody":"NN", "somebody":"NN",#indefinite pronouns
    "now":"RB", "then":"RB", "always":"RB","today":"RB","yesterday":"RB"#adverbs
    }
#tags anything ending in -ntion(s) as NN(S)
def NN_ntionTagger(sent):
    sentToReturn = []
    for word in sent:
        if (word[0].lower()=="mention")|(word[0].lower()=="mentions"):
            sentToReturn += [(word[0], 'UNK')]
            continue
        if word[0].lower().endswith("ntion"):
            newTup = (word[0], "NN")
            sentToReturn += [newTup]
        elif word[0].lower().endswith("ntions"):
            newTup = (word[0], "NNS")
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn

#tags anything ending in -ction(s) as NN(S)
def NN_ctionTagger(sent):
    sentToReturn = []
    for word in sent:
        if (word[0].lower()=="function")|(word[0].lower()=="functions"):
            sentToReturn += [(word[0], 'UNK')]
            continue
        if (word[0].lower()=="sanction")|(word[0].lower()=="sanctions"):
            sentToReturn += [(word[0], 'UNK')]
            continue
        if (word[0].lower()=="auction")|(word[0].lower()=="auctions"):
            sentToReturn += [(word[0], 'UNK')]
            continue
        if word[0].lower().endswith("ction"):
            newTup = (word[0], 'NN')
            sentToReturn += [newTup]
        elif word[0].lower().endswith("ctions"):
            newTup = (word[0], 'NNS')
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn


#tags anything ending in -dence(s) as NN(S)
def NN_denceTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower().endswith("dence"):
            newTup = (word[0], 'NN')
            sentToReturn += [newTup]
        elif word[0].lower().endswith("dences"):
            newTup = (word[0], 'NNS')
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn

#tags anything ending in -enc/y(ies) as NN(S)
def NN_encyTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower().endswith("ency"):
            newTup = (word[0], 'NN')
            sentToReturn += [newTup]
        elif word[0].lower().endswith("encies"):
            newTup = (word[0], 'NNS')
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn


#tags anything ending in -ness(es) as NN(S)
def NN_nessTagger(sent):
    sentToReturn = []
    for word in sent:
        if (word[0].lower()=="witness")|(word[0].lower()=="witnesses"):
            sentToReturn += [(word[0], 'UNK')]
            continue
        if word[0].lower().endswith("ness"):
            newTup = (word[0], 'NN')
            sentToReturn += [newTup]
        elif word[0].lower().endswith("nesses"):
            newTup = (word[0], 'NNS')
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn


#tags anything ending in -ously as RB
def RB_ouslyTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower().endswith("ously"):
            newTup = (word[0], 'RB')
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn


#Tags anything starting with a captial letter as NNP (excluding first word in sentence)
def NNPTagger(sent):
    iterSent = iter(sent)
    sentToReturn = []
    sentToReturn += [next(iterSent)]
    for word in iterSent:
        token = word[0]
        if token[0].isupper():
            tup = (word[0], 'NNP')
        else:
            tup = (word[0], word[1])
        sentToReturn += [tup]
    return sentToReturn


#tags everything in dictionary
def tinyDictionaryTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower() in tinyDictionary:
            newTup = (word[0], tinyDictionary[word[0].lower()])
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn


#tagger for all endings and their exceptions
def endingClusterTagger(sent):
    sentToReturn = []
    newTuple = ()
    for word_POS_tuple in sent:
        #set to existing tuple by defaut
        newTuple = word_POS_tuple
        #if the word is one of the exceptions, add to sentToReturn and keep going
        if word_POS_tuple[0].lower() in endingClusterExceptions:
            newTuple = (word_POS_tuple[0],endingClusterExceptions[word_POS_tuple[0].lower()])
            sentToReturn += [newTuple]
            continue
        #see if word ends in targeted ending. If so, put in newTuple
        for endingCluster in endingClusterList:
            if word_POS_tuple[0].lower().endswith(endingCluster[0]):
                newTuple = (word_POS_tuple[0],endingCluster[1])
        #add new tuple to sentToReturn
        sentToReturn += [newTuple]

    return sentToReturn

