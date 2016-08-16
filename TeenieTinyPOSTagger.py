from nltk.tokenize import sent_tokenize
from nltk import*
from PhaseOneTagging import*
from PhaseTwoTagging import*
from PhaseThreeTagging import*
from PhaseFourTagging import*
from PhaseFiveTagging import*


s="Over the course of several hours after Omar Mateen attacked the Pulse nightclub and took hostages, he told police negotiators that he planned to strap bombs to four people, Mayor Buddy Dyer said."




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

#Tags anything starting with an int as CD
finalSent =  int_Tagger(finalSent)

finalSent = tinyDictionaryTagger(finalSent)
#tags unique morphological/orthographical endings (minus a few exceptions)
finalSent = endingClusterTagger(finalSent)
#tags unique morphological/orthographical endings (minus a few exceptions)
finalSent = endingClusterTagger(finalSent)
#
#
#END PHASE ONE TAGGING
#
#
######################################

#                                           *****NEW*****
finalSent = whether_to_UNK_to_Tagger(finalSent)

#tags words ending in "est" following "the" as JJS  ****NEW****
finalSent = the_est_AdjectiveTagger(finalSent)
#tags words ending in "er" followed by "than" as JJS  ****NEW****
finalSent =  er_than_AdjectiveTagger(finalSent)
#tags words ending in "*ed" after "which" as V and "which" as WDT  *****NEW*****
finalSent = which_ded_VerbTagger(finalSent)
#tags words after "will" and before "." or ";" or ":" as VB, and "will" as MD  ****NEW****
finalSent =  will_UNK_PUNC_VerbTagger(finalSent)
#tags words ending in "ls" after PRP as V  *****NEW*****
finalSent = PRP_ls_VerbTagger(finalSent)
#tags words ending in "*ed" after PRP as V  *****NEW*****
finalSent = PRP_ded_VerbTagger(finalSent)
#tags words ending in "*ed" before IN as V  *****NEW*****
finalSent = ded_IN_VerbTagger(finalSent)
#tags words ending in "*ed" before PRP$ as V
finalSent = ded_PRPS_VerbTagger(finalSent)
#tags words ending in "*ed" before DT as V
finalSent =  ded_DT_VerbTagger(finalSent)



#tags words ending in "*ed" after "have" verbs as VBN  ****NEW****
finalSent = have_ded_VerbTagger(finalSent)

#tags anything between PRP's as V   *****NEW*****
finalSent = PRP_UNK_PRP_VerbTagger(finalSent)
#
finalSent = at_times_Tagger(finalSent)
#
finalSent = MD_UNK_better_IN_Tagger(finalSent)
#tags IN "that" as DT
finalSent = IN_that_Tagger(finalSent)
#tags words between CD and "there" as NNS
finalSent =  CD_UNK_there_PUNC_Tagger(finalSent)
#tags "own" as JJ when precede by PRP$
finalSent = PRPS_own_AdjectiveTagger(finalSent)
#tags words between DT's as N
finalSent =  DT_UNK_DT_NounTagger(finalSent)
#tags "so that" as IN IN
finalSent= so_that_PrepositionTagger(finalSent)
#tags words ending in "ism(s)" followed by "that" as N
finalSent = ism_that_NounTagger(finalSent)
#tags words afet IN ending in "ine" as N
finalSent = IN_ine_NounTagger(finalSent)
#tags words between CD and "ing" as NNS VBG
finalSent = CD_UNK_ing_on_Tagger(finalSent)
#tags words between CD and "'" as NNS POS and N
finalSent = CD_UNK_PUNC_UNK_Tagger(finalSent)
#
finalSent = to_UNK_how_to_UNK_Tagger(finalSent)
#tags words between that and PRP as V
finalSent = that_UNK_PRP_to_Tagger(finalSent)
#tags words between "that" and "to" as V
finalSent = that_UNK_to_VerbTagger(finalSent)
#tags words ending in "s" following DT CD as NNS
finalSent = DT_CD_s_NounTagger(finalSent)
#tags words between PRP$ and "can" as N and "can" as MD
finalSent = PRPS_UNK_can_NounTagger(finalSent)
#tags words after DT and "able" as N
finalSent = DT_able_UNK_NounTagger(finalSent)
#
finalSent = PRPS_UNK_s_UNK_PUNC_Tagger(finalSent)
#tags words  and between PRP and into as V
finalSent = PRP_UNK_into_VerbTagger(finalSent)
#tags words  and between that and into as V
finalSent = that_UNK_into_VerbTagger(finalSent)
#
finalSent =  DT_UNK_UNK_PUNC_N_Tagger(finalSent)
#tags words between "who" and "ly" IN as V, RB
finalSent = who_UNK_ly_IN_Tagger(finalSent)
##tags "which" followed by PRP as WDT
finalSent = which_PRP_WDTTagger(finalSent)
#tags words between "be so" and "that" as J
finalSent = be_so_UNK_that_Tagger(finalSent)
#tags words between "who" and DT as V
finalSent = who_UNK_DT_VerbTagger(finalSent)
#tags words between PRP$/DT and "who" as N
finalSent = PRPS_UNK_who_NounTagger(finalSent)
#tags DT UNK that as DT N WDT
finalSent =  DT_UNK_that_WDTTagger(finalSent)
#tags words ending in "ed" between "another" and PRP$ as V
finalSent = another_ed_PRPS_VerbTagger(finalSent)
##tags "ing" as VBG when followed by "for"
finalSent = ing_for_VerbTagger(finalSent)
#tags words between IN and "," ending in "ble" and UNK, as J and N
finalSent =  IN_able_UNK_PUNC_Tagger(finalSent)

#tags word between IN, N and "." as N
finalSent = IN_N_UNK_PUNC_Tagger(finalSent)
#tags words between "IN" and "." as J and N
finalSent =  IN_UNK_UNK_PUNC_Tagger(finalSent)
#tags words between "have" and PRP as V
finalSent = have_UNK_PRP_VerbTagger(finalSent)
#tags words between IN and DT as J and N  NOT SURE ON THIS ONE. . . .
finalSent = IN_UNK_UNK_DT_Tagger(finalSent)
#tags words between a comma and DT and ending in "ed" as V
finalSent = COMMA_ed_DT_VerbTagger(finalSent)
#tags words between "DT" and "." as J and N
finalSent = ing_what_UNK_to_Tagger(finalSent)
#tags words between "DT" and "." as J and N
finalSent = DT_UNK_UNK_PUNC_Tagger(finalSent)
#tags words between POS/PRP$  and V as N
finalSent =  be_ble_IN_AdjectiveTagger(finalSent)
#tags words between "to" and "IN" as V, and then tags "to" as TO
finalSent = to_UNK_IN_VerbTagger(finalSent)
#tags words between "can" and IN as V, and then tags "can" as MD
finalSent = can_UNK_IN_VerbTagger(finalSent)
#tags "that" between V and N as IN  ********MIGHT BE MOVED FURTHER DOWN AT SOME POINT
finalSent =  V_that_N_PrepositionTagger(finalSent)
#tags words between IN and IN and ending in "ent" or "es" as N *****replaced OLD VERSION 1.14.2016********
finalSent = IN_UNK_IN_NounTagger(finalSent)
#tags words between PRP$ and "to" as N
finalSent = PRPS_UNK_to_NounTagger(finalSent)
#tags words between a comma and DT and ending in "ing" as VBG
finalSent = COMMA_ing_DT_VerbTagger(finalSent)
#tags words between "be" verbs  and PUNC at end of sentence as JJ
finalSent = be_UNK_PUNC_AdjectiveTagger(finalSent)
##tags "can" as MD when followed by PRP
finalSent = can_PRP_MDTagger(finalSent)
#tags words between PRP and PRPS  as V
finalSent = PRP_UNK_PRPS_VerbTagger(finalSent)
#tags words between IN and PRP($) ending in "ing" as VBG
finalSent = IN_ing_PRP_VerbTagger(finalSent)
#tags words between IN and "." as N
finalSent = IN_UNK_PUNC_NounTagger(finalSent)
#tags words between MD and "to" as V
finalSent = MD_UNK_to_VerbTagger(finalSent)
#tags anything ***at beginning of sent*** followed by "who" as NNS
finalSent =  UNK_who_NounTagger(finalSent)
#tags words ending inbetween CD and V as N
finalSent =  CD_UNK_V_NounTagger(finalSent)
#tags anything between d and out as V  MODIFIED 1.16.2016**** changed from "ed" to "d" and removed need for UNK target
finalSent =  d_out_VerbTagger(finalSent)
#tags anything between CD and IN as N
finalSent =  CD_UNK_IN_NounTagger(finalSent)
#tags anything between CD and PUNC as N
finalSent =  CD_UNK_PUNC_NounTagger(finalSent)
#tags anything between PRP and "to"  that ends in "s" or "ed" as V
finalSent =  PRP_s_toVerbTagger(finalSent)
#tags anything between DT and PUNC  that ends in "s" as NNS
finalSent =  DT_s_PUNC_NounTagger(finalSent)
#tags anything ***at beginning of sent*** between DT and "that" as N. Tags "that" as WDT****MADE OBSOLETE BY
#finalSent = DT_UNK_that_NounTagger(finalSent)**********************************************DT_UNK_THAT_WDTTagger
#tags anything between "who" and "to" as V
finalSent =  who_UNK_to_VerbTagger(finalSent)
#tags anything between PRP$ and IN as N
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
finalSent = to_AUX_TOtagger(finalSent)
finalSent = to_be_VBGTagger(finalSent)
finalSent = PRP_isVBZTagger(finalSent)
finalSent = existentialThereTagger(finalSent)
finalSent = her_DT_PRPTagger(finalSent)
#
#
#
#
finalSent = to_DT_VerbTagger(finalSent)
finalSent = to_UNK_PRP_VerbTagger(finalSent)
finalSent = DT_noun_POSTagger(finalSent)#########THIS WILL NEED TO BE CHANGED . .. . .
finalSent = DT_IN_NounTagger(finalSent)
finalSent = N_DT_VerbTagger(finalSent)
finalSent = DT_PuctuationNounTagger(finalSent)
finalSent = N_by_VerbTagger(finalSent)
finalSent = MD_as_VerbTagger(finalSent)
finalSent = IN_that_PucntuationTagging(finalSent)
finalSent = that_P_VThatTagger(finalSent)
finalSent = modal_VB_DTTagger(finalSent)
finalSent = can_might_will_VBTagger(finalSent)


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
#tags anything between who and N  that ends in "s" or "ed" as V
finalSent =  who_s_N_VerbTagger(finalSent)
##tags words ending in "ial" followed by N as JJ
finalSent =  ial_N_JJTagger(finalSent)
#tags anything between RB and DT  that ends in "ed" as V
finalSent =  RB_ed_DT_VerbTagger(finalSent)
#tags words between J and IN as N
finalSent = J_UNK_IN_VerbTagger(finalSent)
#tags words between "who" and J as V
finalSent = who_UNK_J_VerbTagger(finalSent)
#tags words between "to" and "too as V, and then tags "to" as TO
finalSent = IN_UNK_CC_NounTagger(finalSent)
#tags words between PRP and "too" as V
finalSent = PRP_UNK_to_VerbTagger(finalSent)
#tags words between JJ and PUNC as N
finalSent =  JJ_UNK_PUNC_NounTagger(finalSent)
#tags words between "be" verb and TO as JJ
finalSent = be_UNK_TO_AdjectiveTagger(finalSent)
#tags words between POS/PRP$  and V as N
finalSent = POS_UNK_V_NounTagger(finalSent)
#tags words between J and RB as N
finalSent = J_UNK_RB_NounTagger(finalSent)
#tags words between RB and PRP$ as V  ********TRIAL ONLY****
finalSent = RB_UNK_PRPS_VerbTagger(finalSent)
#tags words after V and IN ending in "ing" as VBG  ********TRIAL ONLY*****
finalSent = V_IN_ing_VerbTagger(finalSent)
#tags words between PRPS and V  as N
finalSent = PRPS_UNK_V_NounTagger(finalSent)
#tags words between N and "that" DT as V and IN
finalSent = N_UNK_that_DT_Tagger(finalSent)
#tags word between IN/PRP$, N and "." as J
finalSent =  IN_UNK_N_PUNC_Tagger(finalSent)
#tags "to" as TO between V and "."
finalSent =  V_to_PUNC_TOTagger(finalSent)
#tags words between DT and "," N as N
finalSent = DT_UNK_PUNC_N_Tagger(finalSent)
#tags words following V and RB and ending in "ing" as VBG
finalSent = V_RB_ing_VerbTagger(finalSent)
##tags "around" followed by DT or N as IN
finalSent = around_DT_PrepositionTagger(finalSent)
#tags words between "that"(WDT) and "out" as V
finalSent =  that_UNK_out_VerbTagger(finalSent)
#tags words between IN and N "that" as J
finalSent = IN_UNK_N_that_Tagger(finalSent)
#tags "that" between N and V as WDT
finalSent = N_that_V_WDTTagger(finalSent)
#tags wprds ending in "ing" and between N and PRP$ as VBG
finalSent = N_ing_PRPS_VerbTagger(finalSent)
#tags words between J "to" and "there as TO V
finalSent = J_to_UNK_there_Tagger(finalSent)
#tags words between MD and "off" as V and "off" as RB
finalSent = MD_UNK_off_NounTagger(finalSent)
#tags words between IN NN and as J when ending in comma or period
finalSent = IN_UNK_NN_PUNC_Tagger(finalSent)
#tags words between RB and "up" as V and tags "up" as IN
finalSent = RB_UNK_up_VerbTagger(finalSent)
#tags words between IN and V as N
finalSent = IN_UNK_V_NounTagger(finalSent)
#tags words between PRP$ and N as J
finalSent = PRPS_UNK_N_AdjectiveTagger(finalSent)
#tags words between CD and RB as NNS
finalSent = CD_UNK_RB_NounTagger(finalSent)
#tags words after "a" and before "," as J N  *******TRIAL ONLY***********
finalSent = a_UNK_UNK_PUNC_Tagger(finalSent)
#
finalSent =  to_UNK_N_that_Tagger(finalSent)
#
finalSent = the_UNK_RB_UNK_a_Tagger(finalSent)
#
finalSent = IN_UNK_PUNC_so_Tagger(finalSent)
#
finalSent = at_times_UNK_VerbTagger(finalSent)
#tags words ending in "*ed" before RB as VBN  ****NEW****
finalSent = ded_RB_VerbTagger(finalSent)



###The following two functions must be in this order
#tags "to" between J and V as TO
finalSent = J_to_V_TOTagger(finalSent)
#tags UNK between J and V as N
finalSent = J_UNK_V_NounTagger(finalSent)


#tags words between "DT" and "IN" as J and N
finalSent =  DT_UNK_UNK_IN_Tagger(finalSent)
#tags words between PRP "to" and N as V  **********TRIAL ONLY*************
finalSent = PRP_to_UNK_N_Tagger(finalSent)
#tags words  and between N and TO as V
finalSent = N_UNK_TO_VerbTagger(finalSent)

##the following two fuctions must reamin in this order . . . . .
#tags words between DT and "to V" as N TO
finalSent = DT_UNK_to_V_Tagger(finalSent)
#tags words between DT and V as J N
finalSent = DT_UNK_UNK_V_Tagger(finalSent)


#tags words between PRP and TO
finalSent = PRP_UNK_TO_VerbTagger(finalSent)


#####PHASE FIVE************
#tags N around "and"
finalSent = IN_N_and_UNK_PUNC_Tagger(finalSent)
#
finalSent =  when_PRPS_N_UNK_RB_Tagger(finalSent)

#####################################################
#
#
#
#
#Funcions from here down trump anything above
#
#
#
#tags words no longer/sooner V as RB/RBR ****KEEP AT END
finalSent =  no_longer_V_RBRTagger(finalSent)
#tags "as UNK as" as RB JJ IN
finalSent = as_UNK_as_AdjectiveTagger(finalSent)
#tags "more UNK than" as RBR JJ IN
finalSent = more_UNK_than_AdjectiveTagger(finalSent)

print(finalSent)