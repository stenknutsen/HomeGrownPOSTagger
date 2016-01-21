from nltk.tokenize import sent_tokenize
from nltk import*
from PhaseOneTagging import*
from PhaseTwoTagging import*
from PhaseThreeTagging import*
from PhaseFourTagging import*
from PhaseFiveTagging import*


s="The official and others who talked with NPR asked not to be identified since the Defense Department hasn't decided officially whether to try to withdraw the troops from the Sinai."
#s="The cart that Mother Courage and her three children pull in the original is now a battered truck, from which she sells pretty much anything soldiers and desperate civilians will buy. "
#s="The session is not about restoring his mental health; it's about bringing his testosterone level back to performance level, like Viagra for the psyche."
s="Nationalism is the result of identification and differentiation and it follows from the similarities and differences we see between ourselves and others."
s="The character also possesses a velvety purr, a deliberate choice for an actor who can rage with the best of them."
s="President Obama took a moment in his final State of the Union Address Tuesday to voice optimism that people have the power to bring an end to the worldwide menace of malaria."
s="The alcohol in wine evaporates more quickly than water and is mostly gone after 30 minutes' cooking."
s="Since then, aid workers have reported horrifying scenes of malnutrition and deprivation."
s="In the basement of a makeshift hospital, she came across two children lying on a bed."
s="After seven years of research and writing, Wouk had a draft of 1000 pages, which he presented to his wife who worked closely with him on all his books."
s="But while the companies were promising, Mr. Rubin invested in several technologies that had industry observers scratching their heads about his overall direction."
s="Though sentenced to five years in prison for the coup, Hitler wound up serving less than one year."####TWO INSTANCES BETWEEN "IN"
s="I drove to college so that my sister did not have to."
#s="He's a nice guy."
##s="He then emphasizes how investments in technology in particular might solve these problems."
#s ="Take his efforts to limit carbon emissions through the Environmental Protection Agency, or put a price on carbon."
#s=  "It was going to give people small sums of money to see whether the market forces, the information held by different people being aggregated in the market, could serve as a kind of predictive tool to lay alongside all the other predictive tools that people use."
#s="it was brillig, and the slithy toves did gyre and gimble in the wabe all mimsy were the borogoves and the mome raths outgrabe."
#**JUST**s="And, Levenson says that according to the prevailing science of the time, there was a clear explanation for that: another planet that we hadn't yet discovered, inside the orbit of Mercury, that could tug it just slightly off its expected course."
#s = "He emphasizes, a study suggests that's because the pain of loneliness activates the immune pattern of a primordial response commonly known as fight or flight or qualities of childhood."
s = "It was going to give people small sums of money to see whether the market forces, the information held by different people being aggregated in the market, could serve as a kind of predictive tool to lay alongside all the other predictive tools that people use."
#####s="Slowly, as the beautiful, unbound melodies introduced by his knife-edged saxophone remained in liquid currency, we realized that he had rewritten the rulebook."
##s="The rise of vegetables and focus on food waste are the culmination of more than a decade's worth of government, consumer and food and environmental activists' concerns that have finally trickled into the mainstream."
######s = "But the current process of diagnosis amounts to giving a questionnaire to parents and doctors."
#s="Iliff studied the glymphatic system in living mice by looking through a window created in the skull."
#s="The Justice Department has gained a reputation in recent years for forcing companies to pay big fines, while sparing the executives involved. "
##s="With North Korea announcing it conducted a nuclear test of a hydrogen bomb, China, India, Russia and other nations are condemning the move."
s="The intentions of all of our policy statements are the same: to translate the best available data on child health and development into recommendations that help parents, health care providers and policymakers work together to foster children's optimal well-being."
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
#s="In the past century, an earlier version of this fungus wiped out commercial plantings of a banana variety called Gros Michel that once dominated the global banana trade."
#s="At least 10 people are dead and more than a dozen wounded, after an explosion struck a historic district in Istanbul Tuesday morning."
#s="People who take certain popular medicines for heartburn, indigestion and acid reflux may want to proceed more cautiously, researchers reported Monday."
#s="Money aside, there is something alluring to many people about wandering a vast network of underground tunnels and operating massive high-tech machinery."
s="The new season will feature fewer celebrity and parody segments, largely because preschoolers often do not know the stars or understand the references."
#s="Your vision of a more fulfilling life, attained by purchasing it with money, was punched in the eye by the cruel jab of reality shortly after 10:59 p.m. Saturday, when you checked your Powerball ticket and saw that you had not won."
#s="Satirically pointed but slathered in the same vinegar as the rest of his jabs, it felt like part of the same sour meal."
#s="Lubina, the European sea bass, was sheathed in handsome golden scales of potato and bewitchingly sauced with a reduction of red wine and port swirled with butter."
#s="With unobstructed countryside views and a snug workspace kitted out with a wood stove and fireplace, the 19th-century cottage is a far cry from the urban din that Montagut finds both endlessly inspiring and draining."
##s="It's possible to drink too much beer, but can you eat too many cherries?"
#s="The California Air Resources Board has rejected Volkswagen's plan to recall cars with 2-liter diesel engines that trick emissions tests, saying the company's plan is incomplete. "
#s="Ten sailors were detained by Iranian authorities on Tuesday as they sailed from Kuwait to Bahrain aboard two small riverine patrol boats."
s="But Mr. Obama, who campaigned for president on promises of hope and change, and vowed when he took office to transform Washington and politics itself, accepted responsibility for falling far short of that goal."
#s="The company, based in Silicon Valley, is now valued at $50 billion, but many analysts rapturously say its efforts to reinvent TV could be worth several times more."
#s="And while much of the region is notable for sprawling meadows dotted with daffodils and storybook villages with cozy stone houses, Cheltenham feels more like a sophisticated metropolis."
#s="The idea is that doctors can focus on treating patients, since they no longer have to wade through heaps of insurance paperwork."
##JUST##s="In the kitchen of a small eatery in Reyhanli, Turkey, Abu Mohammed took a break from deboning the flank of a freshly slaughtered lamb to opine on grave matters happening just across the border in Syria."
#s="But even far from his home in Virginia and past his personal prime, the first president seemed quite at home creating a tradition."
#s="The main force pulling the average age to the older end of the spectrum is a decrease in the number of teen moms, the researchers say."
#s="Blessed with a rich and deep voice, the actor brought intelligence and humanity to a wide spectrum of roles, judiciously deploying what seemed to be a bottomless supply of frowns and smirks that endeared him to his fans."
s="There's a battle royale going on among the establishment candidates, all trying to edge the other out, especially in New Hampshire."
#s="Another submerged his hand in a pan of leftover chicken curry, to challenge his natural fastidiousness."
#s="It's possible to drink too much beer, but can you eat too many cherries?"
#s="In the case of Tesla, whose brand represents a kind of sustainable luxe, many vegans have complained that it makes no sense for an eco-friendly car to include animal products, given the significant amount of greenhouse gases the industrial agriculture sector emits."
s="President Obama vowed to close Guantanamo Bay shortly after he took office in 2009 and has made it a point in nearly all of his State of the Union addresses, most recently in Tuesday night's speech."
#s="The researchers found that the women judged as least attractive earned significantly lower grades, after controlling for their ACT scores."
#s="I recommend being sick in bed especially when you are not that sick."
#s="Recipes using wine are notably less common today than they were half a century ago, when every fondue pot and chafing dish released rich gusts of boozy vapor."
#s="A local medic has been surviving on the rehydration salts he gives patients, while a business school graduate picks grass to make soup for his 70-year-old father, consulting shepherds about which ones their long-since-slaughtered flocks liked best."
s="Too bad there are more than 340 shopping days till Christmas, because if it were just around the corner, I'd be urging you to buy Helen Ellis' off-the-wall stories for anyone on your list who loves satirical humor as twisted as screw-top bottles, and more effervescent than the stuff that pours out of them."
#s="The situation is so dire that some health officials in Brazil have suggested that women in places with high rates of Zika transmission should avoid getting pregnant."
#s="A mind-boggling stellar explosion is baffling astronomers, who say this cosmic beast is so immensely powerful that no one's sure exactly what made it go boom."
#s="Anders Kvernberg was deep in the vaults of the National Library of Norway when a beautiful atlas caught his eye."
s="As part of the landmark deal, Iran agreed to reduce its stockpile of uranium, remove centrifuges and allow for more intrusive inspection, among other things. "
#s="I agreed that it was a good idea and dutifully made the referral to the gastroenterologist."
#s="When the report came back a few weeks later, I was pleased to learn there were no polyps found."
#s="And tracking acts of violence against animals may help law enforcement intervene before that develops into violence against people."
s="Given these considerable challenges, it isn't surprising that cooking from scratch is the exception in our country's schools."
s="Just a few years later, the Plaza wound up in bankruptcy protection, part of a vast and humiliating restructuring of some $900 million of personal debt that Mr. Trump owed to a consortium of banks."
#s="Their feces can set off asthma symptoms and cause allergic reactions in some people."
#s="I like to give the dough a refrigerated rest, for a few hours at least, preferably overnight."
#s="At the spiritual heart of the pinboard is a small black and white snap of Susan Sontag that overlaps with a photograph of Virginia Woolf's ink-stained desktop."
#s="Thanks to the startup boom, a host of companies have recently sprung up that aim to make everything from headphones to ballerina flats perfectly personal, with intuitive sites and apps that allow you to explore your own preferences in great detail."
#s="Though more contemporary than the five museums built before it (three of which are in castles), this one, like the others, recreates, in a pleasurably primitive way, the experience of scaling a mountain."
#s="The terms were laid out last July by Iran, the U.S. and five other world powers."
#s="She carries a flip phone and for a while her family didn't have Internet at home."
#s="We now have something close to instant, unlimited, often free access to the history of recorded music."
s="I want to suggest a connective spirit of listening, so that we can become our own adventurous recommendation engines and get to know the back rooms of the inventory, the ones that might be otherwise hidden from you."
#s="When my relationship unraveled nearly two years ago, I decided to suspend my career as an actuary in Boston and take a long vacation in Costa Rica, where I planned to learn how to surf and do yoga."
#s="Our businesslike efforts to measure and improve quality are now blocking the altruism, indeed the love, that motivates people to enter the helping professions."
#s="One Palestinian official told Emily he wasn't aware of a previous case like this one, where a staffer for the negotiating team was accused of spying for Israel."

#s="Experts have not pointed to a single, dominant reason for this rise in homicides in Baltimore, nor have they definitively established any kind of causal link between the unrest in April after Freddie Gray's death and the increase in killings."
#s="After four weeks there, I was traveling by car with several friends I had met at surf school when we came upon a red-faced, middle-aged woman hitchhiking on the outskirts of a small village."
#s="On a freezing June night, fourteen-year-old Esme Grace huddles in her bedroom as a shotgun's blast reverberates over and over in the bowels of her family's lopsided, isolated house. "
#s="Doug Carmean, a Microsoft computer designer who commutes daily between Seattle and Redmond Wash said he had encountered the Tesla Autopilot offramp bug and found it scary."
s="We were reminded of that yesterday when SpaceX tried to land a Falcon 9 rocket on a barge in the Pacific."
#s="Fields was worried she had suffered a stroke or was showing signs of early dementia."

#s="Television executives have been frustrated because Mr. Sarandos has at times suggested Netflix shows would fare better than what is on cable and broadcast television."

s="The new guidelines emphasize a lifelong eating pattern that contains adequate essential nutrients, a caloric intake that supports a healthy body weight and foods that reduce the risk of chronic disease."
s="Armed Iranian military personnel boarded the two American vessels while other Iranians kept watch behind machine guns mounted on their vessels."
s="The justices raised the possibility of a broad decision by taking the unusual step of adding their own question to the case, asking the parties to address whether Mr. Obama had violated his constitutional obligations to enforce the nation's laws."
#s="Death in America is frequently compared unfavorably with death in other countries, where people may not be as focused on extending life with every possible intervention."
#s="The show regularly sends up expectations of female beauty but also takes on, for example, the complicated rivalries in certain kinds of relationships between women. "
#s="Their new alliance comes as the onetime detente between Trump and Cruz, the two top outsider candidates in the crowded race, has come to an end. "
#s="Everything had seemed to go wrong in Commander Price's final deployment, which commenced in September."
#s="Mr. Snyder, facing the biggest crisis of his tenure, cited repeated missteps by members of his administration, including misunderstanding regulations and failing to identify the presence of lead in Flint's drinking water."

#s="In the continental United States, the year was the second-warmest on record, punctuated by a December that was both the hottest and the wettest since record-keeping began."
s="Hillary Clinton dismissed a report that emails she sent on her private email server contained a high level of classified material."
s="The S&P even fell below the lows it reached last August, following China's decision to devalue its currency."
s="Universal public higher education recognizes that college must be affordable for all if it is to help drive our economy and our democracy."
s="Statistical analysis suggested all along that the claims were false, and that the slowdown was, at most, a minor blip in an inexorable trend, perhaps caused by a temporary increase in the absorption of heat by the Pacific Ocean."
s="What is striking, the scientists said, is that the orbits of all six loop outward in the same quadrant of the solar system and are tilted at about the same angle. "


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