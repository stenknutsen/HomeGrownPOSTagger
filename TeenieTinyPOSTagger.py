from nltk.tokenize import sent_tokenize
from nltk import*
from PhaseOneTagging import*
from PhaseTwoTagging import*
from PhaseThreeTagging import*

#####s="He then emphasizes how investments in technology in particular might solve these problems."
#s ="Take his efforts to limit carbon emissions through the Environmental Protection Agency, or put a price on carbon."
#s=  "It was going to give people small sums of money to see whether the market forces, the information held by different people being aggregated in the market, could serve as a kind of predictive tool to lay alongside all the other predictive tools that people use."
#s="it was brillig, and the slithy toves did gyre and gimble in the wabe all mimsy were the borogoves and the mome raths outgrabe."
#####s="And, Levenson says that according to the prevailing science of the time, there was a clear explanation for that: another planet that we hadn't yet discovered, inside the orbit of Mercury, that could tug it just slightly off its expected course."
#s = "He emphasizes, a study suggests that's because the pain of loneliness activates the immune pattern of a primordial response commonly known as fight or flight or qualities of childhood."
#s = "It was going to give people small sums of money to see whether the market forces, the information held by different people being aggregated in the market, could serve as a kind of predictive tool to lay alongside all the other predictive tools that people use."
#s="Slowly, as the beautiful, unbound melodies introduced by his knife-edged saxophone remained in liquid currency, we realized that he had rewritten the rulebook."
s="The rise of vegetables and focus on food waste are the culmination of more than a decade's worth of government, consumer and food and environmental activists' concerns that have finally trickled into the mainstream."
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

##order of these rules matters!*
finalSent = to_RB_TOtagger(finalSent)

#
finalSent = to_AUX_TOtagger(finalSent)

#
finalSent = to_be_VBGTagger(finalSent)

#
finalSent = thats_Tagging(finalSent)########*********deletes decade

finalSent = existentialThereTagger(finalSent)

#phase three tagging
#
#
#
finalSent = DT_IN_NounTagger(finalSent)

finalSent = PRP_IN_VerbTagger(finalSent)

finalSent = N_DT_VerbTagger(finalSent)


finalSent = DT_PuctuationNounTagger(finalSent)



finalSent = N_by_VerbTagger(finalSent)

finalSent = MD_as_VerbTagger(finalSent)

finalSent = IN_that_PucntuationTagging(finalSent)

finalSent = that_P_VThatTagger(finalSent)

finalSent = modal_VB_DTTagger(finalSent)

finalSent = can_might_will_VBTagger(finalSent)

#keep this towards the bottom. . . . .
finalSent = DT_ADJ_NTagger(finalSent)

##second pass thorough this
finalSent = DT_IN_NounTagger(finalSent)

print(finalSent)