# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The chapter starts here.

define hector = Character("Hector Santos", color="#ffd588", voice_tag="Hector")

label chapter_1:
    show bg black with fadetoBlack

    call slowTextfade("Early Philippine History")

    call sub_chapter1



    return

label sub_chapter1:
    
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
    
    "???" "I am [[AI Name], an AI designed to help you on your journey. Please take a look at your left wrist."

    show mc left arm request at left

    AI "I have been installed in this watch to help you throughout your journey. You can call me [[AI Name]]."


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

    AI "You have been transported to a different timeline. While transporting, I lost my function to travel to another timeline."

    AI "It also seems that you lost a portion of your memories, but that won't be a problem. For now, I ask that you help me regain my ability to timeleap."

    menu:
        mcInner "..."

        "What about my memory?":
            mc "What about my memory?"

            AI "Your memories will return to you as time goes on."

        "If I help you...":
            mc "If I help you...\nWill that bring me to my original timeline?"
            
            AI "Yes. That is part of my directive."

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

    mc "And my clothes look familiar but-{nw}"

    hide mc neutral

    show hector request at halfsize:
        xalign 1.0
        yalign 0.5
    
    mcInner "SHEESH!! Isn't that Hector? Hector Santos?!! The one responsible for the creation of Laguna Copperplate Inscription?"
    
    mcInner "I still remember him from one of our lessons in History. What is he doing here?"

    mcInner "Since I saw Hector, doesn't it mean that I'm in the late 20th century? And this university..."
    
    mcInner "Since Hector was present in this university this must be the old Ateneo de Manila where Hector studies…"
    
    mcInner "The watch said that I must acquire something from this timeline, so I assume that Hector has something to do with that. But what will that be?"

    mcInner " I still don't know what's the item that I need to obtain from Hector, but whatever it is I need to get close to him ASAP, so that I can return to my own timeline. "

    ## play footstep sound

    hide hector request

    show bg hallway request with fadetoBlack

    ## play footstep sound

    show hector request at fadeInSlow, right

    mc "Excuse me po, pwede po ba akong magtanong? I'm new po kasi sa bayang ito, at wala po akong matutuluyan right now."

    mc "Can you help me ba? Kahit pansamantala lang po."

    hector "Anong bang lengguwahe ang iyong ginagamit, mahirap intindihin ang iyong mga sinasabi." 

    hector "Para naman sagutin ang iyong tanong, mayroon akong alam kung saan ka maaaring makituloy ng pansamantala."

    hector "Sumama ka saakin. Dadalhin kita kung saan ako nananatili. Mayroon pa akong isang kuwartong hindi nagagagamit."

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
    hector "Ako si Hector Santos. Ako ay nag-aaral sa Ateneo de Manila. Ano ang iyong pangalan? Paano ka napadpad sa loob ng unibersidad?"
    
    menu:
        mcInner "Paano ko ipapaliwanag ang sarili ko..."

        "Ako si [mcName]":
            mc "Where are my manners? HAHAHA Ako nga pala si [mcName], ako'y nagmula sa San Carlos Seminary. Mayroon kaming pagsusulit in which kailangan namin maghanap ng isang scholar or historian." 
            
            mc "Pagmamasadan namin sila at gagawa kame ng report after. Funded naman ito ng eskwelahan so hinde ko na kailangan mag-worry sa gastusin." 
            
            mc "Oh, by the way may kilala po ba kayo na historian or kahit scholar?"

        "Nasa unibersidad ako dahil...":
            mc "Nasa unibersidad ako dahil mayroon kaming pagsusulit in which kailangan namin maghanap ng isang scholar or historian."

            mc "Where are my manners? HAHAHA Ako nga pala si [mcName], ako'y nagmula sa San Carlos Seminary."

            mc "Kailangan kong maghanap ng isang scholar o historian dahil pagmamasadan namin sila at gagawa kame ng report after. Funded naman ito ng eskwelahan so hinde ko na kailangan mag-worry sa gastusin."

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

    show bg hector house request at fadeInSlow

    show hector request at fadeInSlow, right

    hector "Tara. Dadalhin kita kung saan pinag-aaralan ng aking grupo ang LCI."

    show hector request at fadeOutSlow, right   

    show bg hector lci request at fadeOutSlow

    hide hector request

    show mob_character lci request at left

    show mob_character lci request as mobchar2 at right

    show hector request at fadeInSlow, center

    hector "Mga ginoo. Ito nga pala si [mcName]. Siya ay mayroong pagsusulit kung saan kailangan niya tayong obserbahan. Sana ay wala kayong problema dito."

    "Scholar" "Maayos lang iyon Ginoong Hector. Magandang umaga sa iyo [mcName]." 

    "Scholar" "Sa tingin din po namin ay malapit nang matapos ang ating pagsalin sa LCI. Ilang araw nalang at mapapalathala na natin ang ating nasaliksik dito."

    hector "Abay ito ay magandang balita! Ipatpatuloy na natin ito mga ginoo."

    show bg black with fadetoBlack
    show mob character lci request at fadeOutSlow
    show mob character lci request as mobchar2 at fadeOutSlow
    show hector request at fadeOutSlow

    hide mob character lci request
    hide mobchar2
    hide hector request

    ## SCENE 3

    call slowTextfade("Makalipas ng ilang araw")

    ## WIP IN PROGRESS

    show bg hector lci request at fadeInSlow

    show hector request at fadeInSlow

    hector "Ayon sa ating matinding pananaliksik tungkol sa LCI maari ko nang sabihin na ang LCI ay ginawa pabalik noong 900 AD. Ginagawa itong isa sa mga pinakaunang nakasulat na tala sa pilipinas."

    hector "Makakauwi na din tayo mga kaibigan!"

    show hector request at fadeOutSlow

    show bg hector house request at fadeInSlow

    show hector request at fadeInSlow, right

    mc "Ako'y namamangha sa iyong natuklasan, Thank you talaga sa opportunity na iyong binigay sakin."

    hector "Bago ka nga pala lumisan may inihanda akong regalo para sa iyo ikonsidera mo ito bilang isang munting regalo ng pamamaalam."

    # bag.png

    mc "MC: Ay nako, sana hindi na po kayo nag abala pa.. Pero thank you sa munting regalo niyo sakin, sa mga ala-ala na inyong ibinigay sakin tiyak na hindi ko malilimutan at salamat sa tulong na inyong binigay."

    mc "Once again thank you very much ginoong Hector at ako'y mauuna na hanggang sa muli nating pagkikita."

    AI "You just obtained an item which can be used to partially repair and restore my timeleap ability so that you can travel back to your timeline."

    AI "Are you ready to go?"

    menu:
        mcInner "..."

        "Yes":
            mc "Goodbye Mr. Hector Santos."

        "No":
            AI "Unfortunately, we cannot remain in a timeline for longer than necessary."

    ## teleport effect

    return