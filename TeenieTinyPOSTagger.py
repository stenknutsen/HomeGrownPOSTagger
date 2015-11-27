from nltk.tokenize import sent_tokenize
from nltk import *
from PhaseOneTagging import*


s = "I've been waiting for the day they'd address this issue."

#takes sentence, tokenizes and renders default POS tag form
def conditionSentence(sent):
    str = word_tokenize(sent)
    conditionedString = []
    for word in str:
        conditionedString += [(word, "UNK")]
    return conditionedString


finalSent = conditionSentence(s)

finalSent = tinyDictionaryTagger(finalSent)

finalSent = JJSTagger(finalSent)

finalSent = NNPTagger(finalSent)

finalSent = NN_stionTagger(finalSent)

finalSent = NN_ationTagger(finalSent)

finalSent = NN_ntionTagger(finalSent)

finalSent = NN_ctionTagger(finalSent)

finalSent = NN_denceTagger(finalSent)

finalSent = NN_encyTagger(finalSent)

print(finalSent)