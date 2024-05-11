# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The chapter starts here.

define hector = Character("Hector Santos", color="#ffd588", voice_tag="Hector")
define y = Character("Classmate \"Y", color="#8cbb6d",)

label chapter_1:
    show bg black with fadetoBlack

    call slowTextfade("Early Philippine History")

    call ch1sub_chapter1

    call ch1sub_chapter2

    call ch1sub_chapter3

    return

label ch1sub_chapter1:
    
    ## Scene 1

    call slowTextfade("The Laguna Copperplate Inscription")

    $ i = 0
    while i < 2:
        show bg campus dawn request with eyeopen:
            blur 5.0
        pause(1)
        show bg black with eyeclose
        pause(1)
        $ i =  i + 1
    $ i = 0
    show bg campus dawn request with eyeopen:
        blur 5.0
        easein 2.0 blur 0.0
        easein 1.0 blur 3.0
        easein 1.0 blur 0.0

    mc "Uhmm…… What happened?"

    mc "Where am I?"

    pause(2)

    "???" "Hello, MC."

    mcInner "Huh?"
    
    "???" "I am Triton-512, an AI designed to help you on your journey. Please take a look at your left wrist."

    show mc left arm request at left

    AI "I have been installed in this watch to help you throughout your journey. You can call me Triton."


    show bg campus dawn request:
            blur 0.0
            easein 1.0 blur 10.0
    
    AI "You must still be confused right after waking up."
    
    mcInner "..."
    
    show bg campus dawn request:
        blur 5.0
        easein 1.0 blur 0.0
    
    AI "How much do you remember?"

    menu:
        mcInner "..."

        "Not that much":
            mc "Not that much."

            AI "I see. Let me explain it for you."

        "...":
            mc "..."

            AI "I take it that you don't remember much. Let me explain it for you."

    AI "You have been transported to a different timeline. While transporting, I lost my function to travel to other timeline."

    AI "It also seems that you lost a portion of your memories, but that won't be a problem. For now, I ask that you help me regain my ability to timeleap."

    menu:
        mcInner "..."

        "What about my memory?":
            mc "What about my memory?"

            AI "Your memories will return to you as time goes on."

        "If I help you...":
            mc "If I help you...\nWill that bring me to my original timeline?"
            
            AI "Yes. That is part of my directives."

    AI "The only way to restore my ability to timeleap is for you to acquire something from this timeline."

    mc "Something?"

    AI "It may be a physical object or it may be an analysis of historical accounts."

    mc "That's pretty vague.\nIs there anything more I should know?"

    AI "The last thing I can tell you is that the timeline you have been transported to is related to the history of the Philippines."

    AI "And-{nw}"

    # watch turning off sfx

    AI "..."

    mc "Did it run out of battery or something?"

    hide mc left arm request

    mc "I guess I'll walk around."

    pause(1)

    mc "It looks like I'm in a university."

    show mc neutral at center

    pause(1)

    mc "And my clothes look familiar but my memories are still foggy"

    hide mc neutral

    show hector request at halfsize:
        xalign 1.0
        yalign 0.5
    
    mcInner "SHEESH!! Isn't that Hector? Hector Santos?!! The one responsible for the creation of Laguna Copperplate Inscription?"
    
    mcInner "I still remember him from one of our lessons in History. What is he doing here?"

    mcInner "Since I saw Hector, doesn't it mean that I'm in the late 20th century? And this university..."
    
    mcInner "Since Hector was present in this university this must be the old Ateneo de Manila where Hector studies…"
    
    mcInner "The watch said that I must acquire something from this timeline, so I assume that Hector has something to do with that. But what will that be?"

    mcInner "I still don't know what's the item that I need to obtain from Hector, but whatever it is I need to get close to him ASAP, so that I can return to my own timeline. "

    ## play footstep sound

    hide hector request

    show bg hallway request with fadetoBlack

    ## play footstep sound

    show hector request at fadeInSlow, right

    mc "Excuse me po, pwede po ba akong magtanong? I'm new po kasi sa bayang ito, at wala po akong matutuluyan right now."

    mc "Can you help me ba? Kahit pansamantala lang po."

    hector "Anong bang lengguwahe ang iyong ginagamit, mahirap intindihin ang iyong mga sinasabi." 

    hector "Para naman sagutin ang iyong tanong, mayroon akong alam kung saan ka maaaring makituloy ng pansamantala."

    hector "Sumama ka sa akin, dadalhin kita kung saan ako nananatili. Mayroon pa akong isang silid na hindi ginagamit."

    hector "Kung nais mo ay maaaring doon ka muna manatili."

    menu:
        mcInner "..."

        "Maraming salamat sa iyong pag-unawa.":
            mc "Maraming salamat sa iyong pag-unawa."

        "Maraming salamat sa iyong alok.":
            mc "Maraming salamat sa iyong alok."

    hector "Walang anuman. Tumutulong lamang ako sa kapwang Filipino."
    
    ## Scene 2

    show bg hector house request with fadetoBlack

    show hector request at left

    hector "Andito na tayo sa aking tahanan. Nakalimutan ko palang ipakilala ang aking sarili."

    show hector request at center
                                    #add slide to right transition
    hector "Ako si Hector Santos, isa akong mag-aaral sa Unibersidad ng Ateneo de Manila. Ano ang iyong pangalan? Paano ka napadpad sa loob ng unibersidad?"
    
    menu:
        mcInner "Paano ko ipapaliwanag ang sarili ko..."

        "Ako nga pala si [mcName]":
            mc "Where are my manners? HAHAHA Ako nga pala si [mcName], ako'y nagmula sa San Carlos Seminary. Mayroon kaming pagsusulit in which kailangan namin maghanap ng isang scholar or historian." 

        "Ako'y nagmula sa San Carlos Seminary":
            mc "Where are my manners? HAHAHA Ako nga pala si [mcName], ako'y nagmula sa San Carlos Seminary. Mayroon kaming pagsusulit in which kailangan namin maghanap ng isang scholar or historian." 
            
    mc "Pagmamasadan namin sila at gagawa kame ng report after. Funded naman ito ng eskwelahan so hinde ko na kailangan mag-worry sa gastusin." 
            
    mc "Oh, by the way may kilala po ba kayo na historian or kahit scholar?"

    hector "Ahh ganun ba? Isa nga pala ako sa mga iskolar ng Ateneo de Manila dalubhasa sa mga makasaysayang relikya. Kasalukuyan kong pinag-aaralan ang tungkol sa LCI para matukoy ko kung kailan ito ginawa."
    
    hector "Maaari kang sumali sa akin kung ito ang iyong ninanais."

    mc "Kung ito'y okay lang po sa inyo then happy po ako na sumama dahil malaking tulong po ito sa aking pagsusulit."

    hector "Ahh, bago ko pala makalimutan kailangan mo pang maghintay ng ilang araw para ika'y makasama sa akin."

    mc "Okay lang sa akin maghintay."

    mc "Ano nga pala ang LCI?"

    hector "Ayon sa isang dutch anthropologist na si Antoon Postma ang LCI ay isang semi-official certificate na nagpapawalang-sala sa utang ng isang nakatataas na opisyal."

    hector "Ang pagpapakawalang sala sa kanya at lahat ng kapamilya at mga inapo niya. Ang malaking halaga ng ginto ay hindi nabayaran ngunit tinalukran sa LCI."

    hector "Kasama ang iba pang mga opisyal bilang mga saksi, na ang ilan ay binanggit sa pangalan at hurisdiksyon."

    hector "Bilang isang piraso ng bagong ebidensya sa kasaysayan, itinatag ng LCI na ang mga isla ng pilipinas ay mahusay na umuunlad sa panahon ng kalakalan sa timog-silangang asya noong ika-sampung siglo."

    show hector request at fadeOutSlow
    pause(1)
    hide hector request

    show bg black with fadetoBlack

    call slowTextfade("Pagkatapos ng ilang araw")

    show bg hector house request with fadetoBlack

    show hector request at fadeInSlow, right

    hector "Tara. Dadalhin kita kung saan pinag-aaralan ng aking grupo ang LCI."

    show hector request at fadeOutSlow, right   

    show bg hector lci request with fadetoBlack

    show mob_character lci request as mobchar1 at left

    show mob_character lci request as mobchar2 at right

    show hector request at fadeInSlow, center

    hector "Mga ginoo. Ito nga pala si [mcName]. Siya ay mayroong pagsusulit kung saan kailangan niya tayong obserbahan. Sana ay wala kayong problema dito."

    "Scholar" "Maayos lang iyon Ginoong Hector. Magandang umaga sa iyo [mcName]." 

    "Scholar" "Sa tingin din po namin ay malapit nang matapos ang ating pagsasalin sa LCI. Ilang araw na lang at mapapala thala na natin ang ating nasaliksik dito."

    hector "Abay ito ay magandang balita! Ipagpatuloy na natin ito mga ginoo."

    show bg black with fadetoBlack

    show mob character lci request as mobchar1 at left, fadeOutSlow

    show mob character lci request as mobchar2 at right, fadeOutSlow

    show hector request at fadeOutSlow

    hide mobchar1
    hide mobchar2
    hide hector request

    ## SCENE 3

    call slowTextfade("Makalipas ng ilang araw")

    ## WIP IN PROGRESS

    show bg hector lci request with fadetoBlack

    show hector request at fadeInSlow

    hector "Ayon sa ating matinding pananaliksik tungkol sa LCI maari ko nang sabihin na ang LCI ay ginawa pabalik noong 900 AD. Ginagawa itong isa sa mga pinakaunang nakasulat na tala sa pilipinas."

    hector "Makakauwi na din tayo mga kaibigan!"

    show hector request at fadeOutSlow

    show bg hector house request with fadetoBlack

    show hector request at fadeInSlow, right

    mc "Ako'y namamangha sa iyong natuklasan, Thank you talaga sa opportunity na iyong binigay sakin."

    hector "Bago ka nga pala lumisan may inihanda akong regalo para sa iyo ikonsidera mo ito bilang isang munting regalo ng pamamaalam."

    # bag.png

    mc "MC: Ay nako, sana hindi na po kayo nag abala pa.. Pero thank you sa munting regalo niyo sakin, sa mga ala-ala na inyong ibinigay sakin tiyak na hindi ko malilimutan at salamat sa tulong na inyong binigay."

    mc "Once again thank you very much ginoong Hector at ako'y mauuna na hanggang sa muli nating pagkikita."

    hide hector request

    AI "You just obtained an item which can be used to partially repair and restore my timeleap ability so that you can travel back to your timeline."

    AI "Are you ready to go?"

    menu:
        mcInner "..."

        "Yes":
            mc "This journey was fun but I want to return to my original timeline."

        "No":
            AI "Unfortunately, we cannot remain in a timeline for longer than necessary."

    ## teleport effect

    show bg black with fadetoWhite



    return

label ch1sub_chapter2:

    call slowTextfade("Chau Ju Kua's Chu Fan Chi")

    $ i = 0
    while i < 2:
        show bg classroom request with eyeopen:
            blur 5.0
        pause(1)
        show bg black with eyeclose
        pause(1)
        $ i =  i + 1
    $ i = 0

    show bg classroom request with eyeopen:
        blur 5.0
        easein 2.0 blur 0.0
    
    show classmate y request at right, fadeInSlow

    y "Uhmm… Hello??? Gising na, kanina kapa natutulog."

    mc "Huh? Seryoso?"

    y "Ano ba ang napanaginipan mong maganda para makatulog ka nang ganun kahimbing sa loob silid aralan?"

    mc "I forgot most of it… pero naalala ko na nakikipag kwento ako sa isang historian na familiar ang mukha…"

    y "Di bale na ano ang napanaginipan mo, malapit nang magsimula ang klase buti nga napansin ko na tulog ka at nakapag desisyonan ko na gisingin ka hanggat hindi pa nakarating ang guro dito."

    mc "Thank you talaga dahil ginising mo ako."

    show classmate y request at right, fadeOutSlow

    # door open sfx
    # professor footsteps sfx

    show professor request at center, fadeInSlow

    "Professor" "Ang pagsusulit na gagawin ninyo sa araw na ito, ay magsusulat kayo ng personal na pagsusuri sa libro na nagngangalang “Chu Fan Chi” sa kadahilanang itinalaga ko to sa inyo na basahin kagabi."

    show professor request at center, fadeOutSlow
    pause(1)
    hide professor request
    show classmate y request at center, fadeInSlow

    mc "Nako hindi ko nabasa ang librong iyon at hindi ako nag-aral kagabi. Paano na ito ngayon?"

    y "Akong bahala sa'yo, ang librong “Chu Fan Chi” ay isinulat noong 1225 ng isang chinese nobleman na nagngangalang Chau-Ju-Kua. Itong libro ay isinalin sa pangalang “Records of Various Barbarous Nations”." 
    
    y "Ang librong ito ay nagsisilbing dokumentasyong kalakalan sa pagitan ng China at Pilipinas. Ito ay mga salaysay ng mga tao sa pilipinas at pagsasagawa ng kalakalan."

    y "May hindi ka ba naintindihan sa aking mga sinabi?"

    mc "Ohh, I understand it now. Maraming salamat sa pagpapaliwanag. Ngayon ay pwede ko nang gawin at tapusin ang pagsusulit na binigay satin."

    show classmate y request at center, fadeOutSlow
    pause(1)
    hide classmate y request

    ## insert monologue thats not in dialogue file for some reason

    pause(2)

    show bg black with fadetoWhite

    return

label ch1sub_chapter3:

    call slowTextfade("Antonio Pigafetta")

    show bg beach request with fadetoBlack

    mc "What's going on? Where am I?"

    AI "You have been transported onto another timeline."

    mc "What are you talking about?! I thought you'd been put right!"

    AI "Not exactly. you have been transported to another timeline, a timeline that isn't your own but closer to your original timeline."
    
    AI "You must once again find something from this timeline to repair me."

    mc "What?! What can I take from this timeline that can repair you?!"

    AI "It's something you will have to figure out on your own. My only hint is that it is not something physical."

    mc "What?"

    pause(1)

    # show spaniard on screen

    "???" "What are you doing here" #translate to spanish

    mc "Wait!"

    # punch sfx

    show bg black with fadetoBlack

    $ i = 0
    while i < 2:
        show bg storage room request with eyeopen:
            blur 5.0
        pause(1)
        show bg black with eyeclose
        pause(1)
        $ i =  i + 1
    $ i = 0

    show bg storage room request with eyeopen

    show mc left arm request at left

    mc "Why did you even bring me here in the first place?!"

    AI "I do not have much control over which timeline you're transported to."

    mc "So what do you want me to do?! Heck, forget what I ought to do, where did you even transport me to?!"

    AI "The only hint I can give is it is the year 1521."

    mc "C'mon! I need an answer now!"

    hide mc left arm request

    mcInner "1521? I'm pretty sure that's around the Battle of Mactan but I can't remember the people in that event."

    mc "Battle of Mactan... someone important died. Who was it?"

    show spaniard request at left

    "Spaniard" "¿Hablas español?"

    "AI(Whispering)" "Translation activated."

    mc "Sí, sí hablo español."

    "Spaniard" "¿Qué haces aquí cerca del campamento? (What are you doing here near the camp?)"
