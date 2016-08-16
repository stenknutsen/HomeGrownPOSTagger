from nltk.tokenize import sent_tokenize
from nltk import*
from mini_lexicon import common_dict
from PhaseOneTagging import new_NNPTagger
from PhaseOneTagging import lexicon_tagger
from PhaseOneTagging import tinyDictionaryTagger

s="But Mr. Maduro, who succeeded Hugo Chavez, went on television and rejected the effort, describing the move as a bid to undermine him and privatize the hospital system."

s="He drank, smoked marijuana, and got hooked on prescription painkillers and later heroin."
s="She also invested in real estate just in case her career with the Atlanta Symphony Orchestra didn't last."
s="He thought, too, that some younger men, if confronted with cancer as he had been, would probably rather risk their lives with lesser, ineffective treatments than allow their penises to be amputated. "
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