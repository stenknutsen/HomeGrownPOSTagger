from nltk.tokenize import sent_tokenize
from nltk import*
from mini_lexicon import common_dict
from PhaseOneTagging import new_NNPTagger
from PhaseOneTagging import lexicon_tagger
from PhaseOneTagging import tinyDictionaryTagger

s="For hours each night, Obama worked in a shadows laboratory lit by a single lamp, passing bottles of urine through a hand-size hole in the wall, to be ready for testing the next day, he said."
s="Donald Trump and women: The words evoke a familiar cascade of casual insults, hurled from the safe distance of a Twitter account, a radio show or a campaign podium."
s="The obstacles to lethal injection have grown in the last five years as manufacturers, seeking to avoid association with executions, have barred the sale of their products to corrections agencies."
s="Lawyers for condemned inmates have challenged the efforts of corrections officials to conceal how the drugs are obtained, saying this makes it impossible to know if they meet quality standards or might cause undue suffering."
s="The Massachusetts State Senate passed a bill that would allow transgender people to use the bathrooms conforming to their gender identities."

s="The negative sentiment started to rise in recent months, as several news media reports detailed a rising tide of internal discord, quoting high-ranking insiders who placed the blame for the company's woes on Mr. Rusbridger's policies and what they saw as his intractability."
s="They found that stimulating the hypothalamus was in turn driving increased brain activity in the hippocampus, a key cog in the brain's memory circuitry."

s="In terms of efficacy, however, after one year there were no significant differences in cognition between the groups, as measured by two scales commonly used to measure Alzheimer's disease symptoms, the ADAS-Cog and CDR-SB. "

s="But no other country systematically deploys intelligence services and state resources on a massive scale to dope, bribe and cheat in sports."
s="If you accept that you have nothing to lose here, you could state diplomatically yet firmly that you're open to an interviewer contacting you if there is serious interest - but your time is too valuable to keep chasing someone who doesn't show up for appointments."
s="People with tremendous wealth have long converted residential areas into showcases for their trophies, whether Ming dynasty furniture or Impressionist landscapes or medieval manuscripts. But space has become an increasingly common problem as buyers like Mr. Tisch have amassed contemporary art, which can be monumental in scale: Stuff no longer fits, even on mansion-size walls."

s="Most collectors, Ms. Wright noted, want to keep their private galleries off the public radar, perhaps because of security concerns."

s="Steve Johnson, LinkedIn's vice president for user experience, said the company had worked over the last two years to make it clearer to members how the feature that imports their contacts works and to give them more control over it."



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