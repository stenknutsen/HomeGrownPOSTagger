from nltk.tokenize import sent_tokenize
from nltk import *
from PhaseOneTagging import*
from PhaseTwoTagging import*

#s="it was brillig, and the slithy toves did gyre and gimble in the wabe all mimsy were the borogoves and the mome raths outgrabe."
#s = "The automatic reticence of Americans to go to Europe, and Russians to visit Turkey, is likely to drive down holiday prices"
s = "Of admissible physicians who were aware of and received Medicare bonus payments, 37 percent said it made a small difference in their ability to serve their Medicare patients, and 5 percent said it made a big difference. "
#s ="I'd go to the convention for inventions now, but don't mention that it has an auction or any restrictions, no matter what the coincidence or imprudences."
#takes sentence, tokenizes and renders default POS tag form
def conditionSentence(sent):
    str = word_tokenize(sent)
    conditionedString = []
    for word in str:
        conditionedString += [(word, 'UNK')]
    return conditionedString

finalSent = conditionSentence(s)

#tag anything starting in caps as NNP
finalSent = NNPTagger(finalSent)

finalSent = tinyDictionaryTagger(finalSent)

#tags unique morphological/orthographical endings (minus a few exceptions)
finalSent = endingClusterTagger(finalSent)

#tags instances of 'to' that are prepositions. Uses context.
finalSent = to_INtagger(finalSent)

##order of thesr rules matters!
finalSent = to_RB_TOtagger(finalSent)

finalSent = to_AUX_TOtagger(finalSent)
print(finalSent)