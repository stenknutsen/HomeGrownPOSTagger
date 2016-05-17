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
s="We all don't like things. People develop individual tastes for all sorts of things, and we don't seem to single out any other category of behavior or preference in the same way we single out food."
s="For people who are picky eaters, they can feel very strongly under assault by being around other people who are kind of pushing on them, telling them, 'Oh, you should eat this, it's healthy, it tastes good,' when they feel that's clearly something wrong."
s="We have a slight preference for slightly salty things, but not much of a preference, and a slight preference for moderate to low sour things."
s="Tim was 21 and a college student at the University of Michigan. He was majoring in English and biology and active in the Lutheran church."
s="The soldiers had come to the military hospital weak and with a tingling sensation up their arms and legs."
s="That is not good, because like the insulation around an electrical wire, if the nerve coating gets damaged, the messages traveling from the central nervous system to the rest of the body can get lost."
s="Researchers have studied how people think about humans in relation to the natural world, and how the way we reason about humans and other animals changes over the course of development and as a function of education and culture."
s="These findings suggest that children are sensitive to all sorts of information from their environments, and also point to a great deal of conceptual flexibility. "
s="The Law School Admissions Council, the group that oversees the administration of the LSAT, recently considered whether the University of Arizona could lose its membership for violating council bylaws."
s="Dell Inc. is moving closer to completing one of the largest bond deals ever, luring investors with hefty yields that reflect the troubles of the computer-hardware industry and a recent flood of corporate-bond issuance."
s="The spokesman refused to answer questions on who Cameron would like to see win in November but said there was no telephone call or meeting planned with Trump, adding: 'If one is proposed we will consider it.'"
s="There were no humans in the Americas until people crossed the land bridge that once connected Siberia to Alaska during the Ice Age but the timing of that event remains mysterious."

s="The real cost of the project, which could have a major impact on Guinea's flagging economy, has yet to be revealed but it is tipped to reach $20 billion."
s="If the House and Senate approve competing versions they would have to reconcile their differences and pass one uniform bill before sending it to Obama for signing into law."


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