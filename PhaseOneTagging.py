import headers

#In this phase of tagging, there will be no consideration of context.
#Unambigous, closed-class(and nearly closed-class) morphemes will be tagged.
#Morphemes are also tagged by unique orthographic features.

#dictionary of exceptions to ending clusters
endingClusterExceptions = {"witness":"UNK","witnesses":"UNK", "priest":"NN","earliest":"UNK","ration":"UNK",
                           "station":"UNK","vacation":"UNK","rations":"UNK","stations":"UNK","vacations":"UNK",
                           "questions":"UNK","question":"UNK","mention":"UNK","mentions":"UNK","function":"UNK",
                           "functions":"UNK","sanction":"UNK","sanctions":"UNK","auction":"UNK","auctions":"UNK",
                           "caution":"UNK","cautions":"UNK","motion":"UNK","motions":"UNK","option":"UNK",
                           "options":"UNK","apportion":'UNK',"portion":"UNK","apportions":'UNK',"portions":"UNK",
                           "licence":"UNK","reference":"UNK","silence":"UNK","sentence":"UNK","fence":"UNK","evidence":"UNK",
                           "licences":"UNK","references":"UNK","silences":"UNK","sentences":"UNK","fences":"UNK",
                           "evidences":"UNK","rally":"UNK","tally":"UNK","sizes":"UNK","prizes":"UNK","prize":"UNK",
                           "size":"UNK","maize":"NN","random":"UNK","seldom":"RB","ship":"UNK","worship":"UNK",
                           "ships":"UNK","worships":"UNK","pity":"UNK","fruity":"UNK","quality":"UNK","uppity":"UNK",
                           "pities":"VBZ","static":"UNK"}

#list of ending clusters
#NOTE: added "ize" as VB. Will later disambiguate base and present tense form.
endingClusterList = [("ness","NN"),("nesses","NNS"),("iest","JJS"),("ation","NN"),("ations","NNS"),("stion","NN"),
                     ("stions","NNS"),("ntion","NN"),("ntions","NNS"),("ction","NN"),("ctions","NNS"),("dence","NN"),
                     ("dences","NNS"),("ency","NN"),("encies","NNS"),("ously","RB"),("city","NN"),("cities","NNS"),
                     ("sity","NN"),("sities","NNS"),("ution","NN"),("utions","NNS"),("otion","NN"),("otions","NNS"),
                     ("ption","NN"),("ptions","NNS"),("rtion","NN"),("rtions","NNS"),("nment","NN"),("tment","NN"),
                     ("pment","NN"),("sment","NN"),("dment","NN"),("hment","NN"),("yment","NN"),("nments","NNS"),
                     ("tments","NNS"),("pments","NNS"),("sments","NNS"),("dments","NNS"),("hments","NNS"),("yments","NNS"),
                     ("cence","NN"),("rence","NN"),("lence","NN"),("sence","NN"),("tence","NN"),("dence","NN"),("fence","NN"),
                     ("cences","NNS"),("rences","NNS"),("lences","NNS"),("sences","NNS"),("tences","NNS"),
                     ("dences","NNS"),("fences","NNS"),("nence","NN"),("nences","NNS"),("matic","JJ"),("cally","RB"),
                     ("eally","RB"),("vally","RB"),("ially","RB"),("rally","RB"),("mally","RB"),("nally","RB"),
                     ("tally","RB"),("ette","NN"),("ettes","NNS"),("ably","RB"),("izes","VBZ"),("ize","VB"),("hood","NN"),
                     ("hoods","NNS"),("dom","NN"),("doms","NNS"),("geous","JJ"),("geously","RB"),("ship","NN"),
                     ("ships","NNS"),("ity","NN"),("ities","NNS"),("ology","NN"),("ologies","NNS"),("ental","J"),
                     ("ers","NNS"),("osis","NN"),("ents","NNS"),("ors","NNS"),("aire","NN"),("aires","NNS"),("ful","J"),
                     ("atic","J"),("ives","NNS"),("ables","NNS"), ("ians","NNS"),("ions","NNS")]

tinyDictionary = {",":",",".":".",";":";","?":"?","!":"!",":":":",#punctuation
    "a":"DT","an":"DT","any":"DT","the":"DT","this":"DT","these":"DT","those":"DT", "another":"DT", #determiners
    "my":"PRP$", "your":"PRP$","its":"PRP$","our":"PRP$", "their":"PRP$","his":"PRP$",#posessive pronouns
    "and":"CC","or":"CC", "but":"CC","&":"CC", "nor":"CC","yet":"CC",#coordingating conjuctions
    "in":"IN","by":"IN", "of":"IN","for":"IN","with":"IN","on":"IN","at":"IN","from":"IN","into":"IN","because":"IN",
    "through":"IN", "after":"IN", "over":"IN","between":"IN","before":"IN","during":"IN","under":"IN",
    "whether":"IN", "while":"IN", #prepositions
    "me":"PRP","him":"PRP","us":"PRP","them":"PRP","i":"PRP","she":"PRP","he":"PRP","we":"PRP","they":"PRP",
    "it":"PRP",#personal pronouns
    "cannot":"MD","could":"MD","may":"MD", "must":"MD", "ought":"MD", "shall":"MD", "should":"MD", "would":"MD",#modals
    "have":"V","having":"VBG","has":"VBZ","be":"VB","was":"VBD","were":"VBD","been":"VBN","am":"VPB","are":"VBP",
    "is":"VBZ", "do":"VBP","did":"VBD", "doing":"VBG", "done":"VBN", "does":"VBZ", "'ve":"VBP", "'d":"MD",
    "'m":"VBP", "'re":"VBP", "'ll":"MD", "had":"VBD", #aux verbs
    "something":"NN", "nothing":"NN", "anything":"NN", "everything":"NN", "someone":"NN", "everyone":"NN",
    "anyone":"NN", "everybody":"NN", "somebody":"NN",#indefinite pronouns
    "now":"RB", "then":"RB", "always":"RB","today":"RB","yesterday":"RB", "not":"RB","n't":"RB","also":"RB",
    "never":"RB", "here":"RB", #adverbs
    "how":"WRB", "why":"WRB","when":"WRB","where":"WRB","what":"WP","who":"WP"
    }

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


#tags everything in tinyDictionary
def tinyDictionaryTagger(sent):
    sentToReturn = []
    for word in sent:
        if word[0].lower() in tinyDictionary:
            newTup = (word[0], tinyDictionary[word[0].lower()])
            sentToReturn += [newTup]
        else:
            sentToReturn += [word]
    return sentToReturn


#tagger for all endings, minus their exceptions
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

