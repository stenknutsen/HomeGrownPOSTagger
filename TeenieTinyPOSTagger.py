from nltk.tokenize import sent_tokenize
from nltk import *
from PhaseOneTagging import*
from PhaseTwoTagging import*


#s = "The race to the bottom is a socio-economic phrase which is used to describe government deregulation of the business environment or taxes in order to attract or retain economic activity in their jurisdictions. "
s ="I'd go to the convention for inventions now, but I'm not sure how to get there."
#takes sentence, tokenizes and renders default POS tag form
def conditionSentence(sent):
    str = word_tokenize(sent)
    conditionedString = []
    for word in str:
        conditionedString += [(word, 'UNK')]
    return conditionedString


finalSent = conditionSentence(s)
finalSent = NNPTagger(finalSent)

finalSent = tinyDictionaryTagger(finalSent)

#finalSent = JJSTagger(finalSent)



#finalSent = NN_stionTagger(finalSent)

#finalSent = NN_ationTagger(finalSent)

#finalSent = NN_ntionTagger(finalSent)

#finalSent = NN_ctionTagger(finalSent)

#finalSent = NN_denceTagger(finalSent)

#finalSent = NN_encyTagger(finalSent)

#finalSent = NN_nessTagger(finalSent)

finalSent = to_INtagger(finalSent)

#finalSent = RB_ouslyTagger(finalSent)

finalSent = endingClusterTagger(finalSent)

print(finalSent)