from nltk.tokenize import sent_tokenize
from nltk import*
from PhaseOneTagging import*
from PhaseTwoTagging import*
from PhaseThreeTagging import*
#s="He's a nice guy."
##s="He then emphasizes how investments in technology in particular might solve these problems."
#s ="Take his efforts to limit carbon emissions through the Environmental Protection Agency, or put a price on carbon."
#s=  "It was going to give people small sums of money to see whether the market forces, the information held by different people being aggregated in the market, could serve as a kind of predictive tool to lay alongside all the other predictive tools that people use."
#s="it was brillig, and the slithy toves did gyre and gimble in the wabe all mimsy were the borogoves and the mome raths outgrabe."
#s="And, Levenson says that according to the prevailing science of the time, there was a clear explanation for that: another planet that we hadn't yet discovered, inside the orbit of Mercury, that could tug it just slightly off its expected course."
#s = "He emphasizes, a study suggests that's because the pain of loneliness activates the immune pattern of a primordial response commonly known as fight or flight or qualities of childhood."
#s = "It was going to give people small sums of money to see whether the market forces, the information held by different people being aggregated in the market, could serve as a kind of predictive tool to lay alongside all the other predictive tools that people use."
#####s="Slowly, as the beautiful, unbound melodies introduced by his knife-edged saxophone remained in liquid currency, we realized that he had rewritten the rulebook."
##s="The rise of vegetables and focus on food waste are the culmination of more than a decade's worth of government, consumer and food and environmental activists' concerns that have finally trickled into the mainstream."
######s = "But the current process of diagnosis amounts to giving a questionnaire to parents and doctors."

#s="Iliff studied the glymphatic system in living mice by looking through a window created in the skull."

#s="The Justice Department has gained a reputation in recent years for forcing companies to pay big fines, while sparing the executives involved. "

##s="With North Korea announcing it conducted a nuclear test of a hydrogen bomb, China, India, Russia and other nations are condemning the move."

#s="The intentions of all of our policy statements are the same: to translate the best available data on child health and development into recommendations that help parents, health care providers and policymakers work together to foster children's optimal well-being."


#s="Being a Star Wars fan, I approached the movie theater with trepidation, worried that the new episode would flop. "

#s="If The Force represents some kind of cosmic consciousness, an abstract representation of a deity, the movie tells us that, even in the divine, good and evil must coexist. "

#s="His mother tries to tell him about the town where she grew up and, maddeningly, the boy doesn't really care, so ignores her and her voice fades into the background."

s="North Korea was celebratory in its claims that it detonated its first hydrogen bomb on Wednesday."

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

finalSent = ed_IN_VBNTagger(finalSent)
##order of these rules matters!*
finalSent = to_RB_TOtagger(finalSent)

#
finalSent = to_AUX_TOtagger(finalSent)

#
finalSent = to_be_VBGTagger(finalSent)


finalSent = PRP_isVBZTagger(finalSent)

finalSent = existentialThereTagger(finalSent)

finalSent = her_DT_PRPTagger(finalSent)

#phase three tagging
#
#
#

finalSent = to_DT_VerbTagger(finalSent)

finalSent = DT_noun_POSTagger(finalSent)

finalSent = DT_IN_NounTagger(finalSent)

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

finalSent = PRP_IN_VerbTagger(finalSent)

finalSent = have_DT_VBNTagger(finalSent)

finalSent = IN_DT_VBGTagger(finalSent)

finalSent = PRP_DT_VerbTagger(finalSent)

finalSent = N_ing_PRP_VerbTagger(finalSent)

print(finalSent)