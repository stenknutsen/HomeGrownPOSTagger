import headers

#In this phase of tagging, there will be no consideration of context.

tinyDictionary = {
    ",":",",
    ".":".",
    ";":";",
    "?":"?",
    "!":"!",
    "a":"DT",#determiners
    "an":"DT",
    "any":"DT",
    "the":"DT",
    "this":"DT",
    "these":"DT",
    "those":"DT",
    "my":"PRP$",#posessive pronouns
    "your":"PRP$",
    "its":"PRP$",
    "our":"PRP$",
    "their":"PRP$",
    "his":"PRP$",
    "and":"CC",#coordingating conjuctions
    "or":"CC",
    "but":"CC",
    "&":"CC",
    "nor":"CC",
    "in":"IN",##prepositions
    "by":"IN",
    "of":"IN",
    "for":"IN",
    "with":"IN",
    "on":"IN",
    "at":"IN",
    "from":"IN",
    "into":"IN",
    "through":"IN",
    "after":"IN",
    "over":"IN",
    "between":"IN",
    "before":"IN",
    "during":"IN",
    "under":"IN",
    "me":"PRP",#personal pronouns
    "him":"PRP",
    "us":"PRP",
    "them":"PRP",
    "I":"PRP",
    "she":"PRP",
    "he":"PRP",
    "we":"PRP",
    "they":"PRP",
    "it":"PRP",
    "cannot":"MD",#modals
    "could":"MD",
    "may":"MD",
    "must":"MD",
    "ought":"MD",
    "shall":"MD",
    "should":"MD",
    "would":"MD",
    "having":"VBG",#aux verbs
    "has":"VBZ",
    "be":"VB",
    "was":"VBD",
    "were":"VBD",
    "been":"VBN",
    "am":"VPB",
    "are":"VBP",
    "is":"VBP",
    "did":"VBD",
    "doing":"VBG",
    "done":"VBN",
    "does":"VBZ",
    "'ve":"VBP",
    "'d":"MD",
    "'m":"VBP",
    "'re":"VBP",
    "something":"NN",#indefinite pronouns
    "nothing":"NN",
    "anything":"NN",
    "everything":"NN",
    "someone":"NN",
    "everyone":"NN",
    "anyone":"NN",
    "everybody":"NN",
    "somebody":"NN",
    "now":"RB",
    "then":"RB",
    "always":"RB",
    "today":"RB",
    "yesterday":"RB"}##adverb

#tags anything ending in -iest as JJS (excluding 'priest', and 'earliest')
def JJSTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower()=="priest":
            sentToReturn += [('priest', "NN")]
            continue
        if word[0].lower()=="earliest":
            sentToReturn += [('earliest', "UNK")]
            continue
        if word[0].lower().endswith("iest"):
            newTup = (word[0], "JJS")
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn

#tags anything ending in ation as NN
def NN_ationTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower()=="ration":
            sentToReturn += [('ration', "UNK")]
            continue
        if word[0].lower()=="station":
            sentToReturn += [('station', "UNK")]
            continue
        if word[0].lower()=="vacation":
            sentToReturn += [('vacation', "UNK")]
            continue
        if word[0].lower().endswith("ation"):
            newTup = (word[0], "NN")
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn


#tags anything ending in stion as NN
def NN_stionTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower()=="question":
            sentToReturn += [('question', "UNK")]
            continue
        if word[0].lower().endswith("stion"):
            newTup = (word[0], "NN")
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn

#tags anything ending in ntion as NN
def NN_ntionTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower()=="mention":
            sentToReturn += [('mention', "UNK")]
            continue
        if word[0].lower().endswith("ntion"):
            newTup = (word[0], "NN")
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn

#tags anything ending in ction as NN
def NN_ctionTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower()=="function":
            sentToReturn += [('function', "UNK")]
            continue
        if word[0].lower()=="sanction":
            sentToReturn += [('sanction', "UNK")]
            continue
        if word[0].lower()=="auction":
            sentToReturn += [('auction', "UNK")]
            continue
        if word[0].lower().endswith("ction"):
            newTup = (word[0], "NN")
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn


#tags anything ending in dence as NN
def NN_denceTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower().endswith("dence"):
            newTup = (word[0], "NN")
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn

#tags anything ending in ency as NN
def NN_encyTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower().endswith("ency"):
            newTup = (word[0], "NN")
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


##tags everything in dictionary
def tinyDictionaryTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower() in tinyDictionary:
            newTup = (word[0], tinyDictionary[word[0].lower()])
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn