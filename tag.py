from nltk.tokenize import sent_tokenize
from nltk import*
from mini_lexicon import common_dict
from PhaseOneTagging import new_NNPTagger
from PhaseOneTagging import lexicon_tagger
from PhaseOneTagging import tinyDictionaryTagger

s="But Mr. Maduro, who succeeded Hugo Chavez, went on television and rejected the effort, describing the move as a bid to undermine him and privatize the hospital system."
s="To reclaim their stories from erasure is to confront the unnoticed heartbreak inherent in a great metropolis, in the striving and missed chances of so many lives gone by."
s="But women were checked when they entered their dorms, and my hall mates constantly ratted out my friends and me just for smoking cigarettes."
s="Though his wife and two children felt fine, others in the wedding party were feeling the effects of the elevation. "
s="In the morning, when he pulled himself out of bed, the sheets were soaked with sweat."

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