from nltk.tokenize import sent_tokenize
from nltk import*
from mini_lexicon import common_dict
from PhaseOneTagging import new_NNPTagger
from PhaseOneTagging import lexicon_tagger
from PhaseOneTagging import tinyDictionaryTagger

s="But Mr. Maduro, who succeeded Hugo Chavez, went on television and rejected the effort, describing the move as a bid to undermine him and privatize the hospital system."

s="Though their support for Mr. Trump is often qualified, this change of heart is one of the more remarkable turns in an erratic and precedent-defying Republican campaign. "

s="Some Amazon fulfillment center workers see unions as a way to gain more influence on pay, how job assignments are doled out and the handling of workplace complaints."

s="But it was a large enough diversion of television dollars to digital media to be of real symbolic importance."
s="If we cut that off, we push television executives into new levels of subliminal trickery."


#takes sentence, tokenizes and renders default POS tag form
def conditionSentence(sent):
    str = word_tokenize(sent)
    conditionedString = []
    for word in str:
        conditionedString += [(word, 'UNK')]
    return conditionedString

finalSent = conditionSentence(s)
finalSent = new_NNPTagger(finalSent)
finalSent = tinyDictionaryTagger(finalSent)
finalSent = lexicon_tagger(finalSent)

print(finalSent)