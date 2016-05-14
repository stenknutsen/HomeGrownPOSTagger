from nltk.tokenize import sent_tokenize
from nltk import*
from mini_lexicon import common_dict
from PhaseOneTagging import new_NNPTagger
from PhaseOneTagging import lexicon_tagger
from PhaseOneTagging import tinyDictionaryTagger

s="For hours each night, Obama worked in a shadows laboratory lit by a single lamp, passing bottles of urine through a hand-size hole in the wall, to be ready for testing the next day, he said."
s="Donald Trump and women: The words evoke a familiar cascade of casual insults, hurled from the safe distance of a Twitter account, a radio show or a campaign podium."
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