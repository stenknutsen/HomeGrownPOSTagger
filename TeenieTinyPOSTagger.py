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

#s="North Korea was celebratory in its claims that it detonated its first hydrogen bomb on Wednesday."

#s="Chipotle Mexican Grill is struggling to convince its customers it's a safe place to eat, after several outbreaks of foodborne illnesses have sickened hundreds of its customers. "

#s="American forces are increasingly being drawn back into the fight, even though President Obama declared an end to the combat mission last fall. "


#s="The bluntness of this statement is remarkable, in part, because the Dietary Guidelines released Thursday are, in other ways, anything but direct."

#s="The cart banged her the minute she left."

#s="These changes in the county have led to debates over government overreach, income inequality and immigration."

#s="The question at the heart of the conversation is whether the influx of refugees and migrants is changing Germany in unacceptable ways."

#s="The president is proposing requiring many more people who sell guns to get federal licenses and conduct background checks."

#s="Disappointed applicants complain that when it comes to discerning between hundreds of students who seem to have the grades, teacher recommendations and test scores, the process comes down to luck."

#s="Legendary rock musician David Bowie, who influenced generations of musicians and fans, died on Sunday, two days after his 69th birthday."

s="But even far from his home in Virginia and past his personal prime, the first president seemed quite at home creating a tradition."


s="In the past century, an earlier version of this fungus wiped out commercial plantings of a banana variety called Gros Michel that once dominated the global banana trade."

#takes sentence, tokenizes and renders default POS tag form
def conditionSentence(sent):
    str = word_tokenize(sent)
    conditionedString = []
    for word in str:
        conditionedString += [(word, 'UNK')]
    return conditionedString

finalSent = conditionSentence(s)

######################################
#
#
#PHASE ONE TAGGING
#
#
#tag anything starting in caps as NNP
finalSent = NNPTagger(finalSent)

#Tags anything starting with an int as CD  ****NEW****
finalSent =  int_Tagger(finalSent)

finalSent = tinyDictionaryTagger(finalSent)

#tags unique morphological/orthographical endings (minus a few exceptions)
finalSent = endingClusterTagger(finalSent)
#
#
#END PHASE ONE TAGGING
#
#
######################################
#tags anything between CD and IN as N  ****NEW****
finalSent =  CD_UNK_IN_NounTagger(finalSent)
#tags anything between CD and PUNC as N  ****NEW****
finalSent =  CD_UNK_PUNC_NounTagger(finalSent)
#tags anything between PRP and "to"  that ends in "s" or "ed" as V  ****NEW****
finalSent =  PRP_s_toVerbTagger(finalSent)
#tags anything between DT and PUNC  that ends in "s" as NNS  ****NEW****
finalSent =  DT_s_PUNC_NounTagger(finalSent)
#tags anything ***at beginning of sent*** between DT and "that" as N. Tags "that" as WDT
finalSent = DT_UNK_that_NounTagger(finalSent)
#tags anything between "who" and "to" as V  ****NEW****
finalSent =  who_UNK_to_VerbTagger(finalSent)
#tags anything between PRP$ and IN as N  ****NEW****
finalSent =  PRPS_UNK_IN_NounTagger(finalSent)

#tags anything following "have" verbs that ends in "ed" as VBN
finalSent =  have_ed_VBNTagger(finalSent)



#tags anything ending in "s" followed by him/me/them as VBZ
finalSent = s_him_VBZTagger(finalSent)
#tags anything ending in "s" followed by "her" and a DT/CC/IN or PRP$ as a VBZ, and tags "her" as PRP
finalSent =  s_her_DT_VerbTagger(finalSent)

#tags anything ending in "ed" followed by him/me/them as VBD
finalSent =  ed_him_VBNTagger(finalSent)
#tags anything ending in "ed" followed by "her" and a DT/CC/IN or PRP$ as a VBD, and tags "her" as PRP
finalSent =  ed_her_DT_VerbTagger(finalSent)





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

finalSent = to_UNK_PRP_VerbTagger(finalSent)

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

finalSent = MD_UNK_PUNC_VerbTagger(finalSent)

finalSent = DT_UNK_WRB_NounTagger(finalSent)

finalSent = DT_UNK_V_NounTagger(finalSent)

finalSent =  N_UNK_up_VerbTagger(finalSent)

 #tags words between to/IN/PRP$ as N, and then tags "to" as IN
finalSent = IN_UNK_CC_NounTagger(finalSent)

#tags anything between who and N  that ends in "s" or "ed" as V  ****NEW****
finalSent =  who_s_N_VerbTagger(finalSent)




print(finalSent)