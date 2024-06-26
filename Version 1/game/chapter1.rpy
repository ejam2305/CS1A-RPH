# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The chapter starts here.

define hector = Character("Hector Santos", color="#ffd588", voice_tag="Hector")
define y = Character("Classmate \"Y\"", color="#8cbb6d",)

label chapter_1:
    
    show bg black with fadetoBlack

    call slowTextfade("Early Philippine History")

    call ch1sub_chapter1

    call ch1sub_chapter2

    call ch1sub_chapter3

    return

label ch1sub_chapter1:

    call slowTextfade("The Laguna Copperplate Inscription")

    play music "Stay the Course.mp3" volume 0.3 fadein 1.0 fadeout 1.0

    $ i = 0
    while i < 2:
        show bg campus dawn with eyeopen:
            matrixcolor ContrastMatrix(2.0 - i)
            blur 5.0
        pause(2 - i)
        show bg black with eyeclose
        $ i =  i + 1
    $ i = 0
    show bg campus dawn with eyeopen:
        matrixcolor ContrastMatrix(1.0)
        blur 0.0

    play sound "<from 0 to 8>Clock.mp3"

    show mc thinking 1 at left, large, fadeInSlow

    pause(1)

    show mc thinking 2

    mc "Uhmm... What happened?"

    mc "Where am I?"

    show mc thinking 1

    pause(1)

    "???" "Hello, MC."

    show mc thinking 1 at flipOn

    mcInner "Huh?"
    
    "???" "I am Triton-512, an AI designed to help you on your journey. Please take a look at your left wrist."

    show mc left arm 1 at flipOff

    AI "I have been installed in this watch to help you throughout your journey. You can call me Triton."

    show bg campus dawn :
            blur 0.0
            easein 1.0 blur 10.0
    
    AI "You must still be confused right after waking up."
    
    mcInner "..."
    
    show bg campus dawn :
        blur 10.0
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

    mc "That's pretty vague. Is there anything more I should know?"

    AI "The last thing I can tell you is that the timeline you have been transported to is related to the history of the Philippines."

    play sound "<from 0.5 to 1.5>Watch Off.mp3" volume 0.25 fadeout 1.0

    AI "And-{nw}"

    AI "..."

    mc "..."

    mc "Did it run out of battery or something?"

    mc "I guess I'll walk around."

    pause(1)

    show mc thinking 1 at center, flipOn

    play sound "Footstep Concrete Slowed.mp3" volume 0.5

    mc "It looks like I'm in a university."

    show mc thinking 2

    pause(1)

    mc "And my clothes look familiar but my memories are still foggy."

    pause(1)

    stop sound

    show mc realization 1 at left

    show hector at right, flipOn:
        matrixcolor BrightnessMatrix(-0.7)
    
    mcInner "SHEESH!! Isn't that Hector? Hector Santos?!! The one responsible for the creation of Laguna Copperplate Inscription?"
    
    show mc thinking 2

    hide hector with dissolve

    mcInner "I still remember him from one of our lessons in History. What is he doing here?"

    show mc thinking 3

    mcInner "Since I saw Hector, doesn't it mean that I'm in the late 20th century? And this university..."

    mcInner "Since Hector was present in this university this must be the old Ateneo de Manila where Hector studies…"
    
    mcInner "The watch said that I must acquire something from this timeline, so I assume that Hector has something to do with that. But what will that be?"

    mcInner "I still don't know what's the item that I need to obtain from Hector, but whatever it is I need to get close to him ASAP, so that I can return to my own timeline. "

    play sound "<from 0.0 to 3.0>Footstep Concrete.mp3" volume 0.25 fadeout 1.0

    hide mc with dissolve

    stop music

    pause(1)


    scene bg hallway with fadetoBlack


    play music "SCP-x6x.mp3" volume 0.3 fadein 1.0 fadeout 1.0

    show mc neutral 1 at left, large, fadeInSlow:
        xzoom -1

    show hector at right, large, fadeInSlow

    mc "Excuse me po, pwede po ba akong magtanong? I'm new po kasi sa bayang ito, at wala po akong matutuluyan right now."

    show mc speaking 1

    mc "Can you help me ba? Kahit pansamantala lang po."

    hector "Anong bang lengguwahe ang iyong ginagamit, mahirap intindihin ang iyong mga sinasabi." 

    hector "Para naman sagutin ang iyong tanong, mayroon akong alam kung saan ka maaaring makituloy ng pansamantala."

    hector "Sumama ka sa akin, dadalhin kita kung saan ako nananatili. Mayroon pa akong isang silid na hindi ginagamit."

    hector "Kung nais mo ay maaaring doon ka muna manatili."

    show mc thinking 3

    menu:
        mcInner "..."

        "Thank you for your understanding.":

            show mc speaking 1

            mc "Thank you for your understanding."

        "Maraming salamat sa iyong alok but...":

            show mc speaking 1

            mc "Maraming salamat sa iyong alok but on naalala ko na meron na pala akong matitirhan kasama ng kaibigan ko sa Ateneo."

            show mc neutral 1

            hector "Ahh, ganoon ba? Ano pala ang pangalan ng iyong kaibigan? Tutulungan kitang hanapin siya."

            show mc realization 1

            mcInner "..."

            show mc speaking 1

            mc "Uhhhh, kaibigan ko po si Eliezer Villa."

            show mc neutral 1
            
            hector "Hmm. Wala akong kilalang Eliezer. Tara, dadalhin kita sa faculty. Makakatulong sa iyo maghanap ang aming mga maestro."

            show mc speaking 1

            mc "Ahh... You don't have to do that po..."

            show mc thinking 1

            hector "..."

            hector "Paumanhin, ngunit kailangan mo akong samahan sa faculty. Bawal ang mga tagalabas sa loob ng Unibersidad. Kung ayaw mo parin sumama ay mapipilitan akong tumawag ng guwardiya."

            show mc realization 1

            hide hector with dissolve

            show mc thinking 2

            pause (0.5)

            hide mc with dissolve


            scene bg black with fadetoBlack
 

            stop music

            play sound "<from 0 to 8>Clock.mp3" loop

            call slowTextfade("You Failed")

            AI "Initiating rewind protocol{nw=0.5}"

            pause(1)

            stop sound

            jump ch1sub_chapter1

    show mc neutral 1

    hector "Walang anuman. Tumutulong lamang ako sa kapwang Filipino."

    show mc speaking 1

    mc "Oh by the way, ako nga pala si [mcName]."
    
    mc "Ano ang pangalan mo?"

    show mc neutral 1
    
    hector "Ako nga pala si Hector Santos, isa akong mag-aaral sa Unibersidad ng Ateneo de Manila."

    hide hector with dissolve

    show mc thinking 3

    pause(0.5)

    hide mc with dissolve

    stop music


    scene bg hector house with fadetoBlack


    play music "Morning.mp3" volume 0.3 fadein 1.0 fadeout 1.0

    show mc neutral 1 at left, large, fadeInSlow:
        xzoom -1.0

    show hector at right, large, fadeInSlow

    hector "Andito na tayo sa aking tahanan. Bago ka makikitira dito, sagutin mo muna ang aking tanong."

    hector "Paano ka napadpad sa loob ng unibersidad?"
    
    show mc thinking 1

    menu:
        mcInner "Paano ko ipapaliwanag ang sarili ko..."

        "Mayroon kaming pagsusulit":

            show mc speaking 1

            mc "Ako'y nagmula sa San Carlos Seminary. Mayroon kaming pagsusulit in which kailangan namin maghanap ng isang scholar or historian." 

        "Isa akong time-traveller":

            show mc speaking 1

            mc "To be honest with you, isa akong time-traveller at nanggaling ako sa ibang timeline."

            hector "..."

            hector "Mukha ba akong uto-uto sayo?"

            hector "Noong una palang iniisip ko na kahina-hinalang tao ka. Ngayon ay nakumpirma na ang na sa aking isip."

            hector "Mga guwardiya!! Tulong!"

            show mc realization

            
            scene bg black with fadetoBlack


            stop music

            play sound "<from 0 to 8>Clock.mp3" loop

            call slowTextfade("You failed")

            AI "Initiating rewind protocol{nw=0.5}"

            pause(1)

            stop sound

            jump ch1sub_chapter1
            
    mc "Pagmamasadan namin sila at gagawa kame ng report after. Funded naman ito ng eskwelahan so hinde ko na kailangan mag-worry sa gastusin." 
            
    mc "Oh, by the way may kilala po ba kayo na historian or kahit scholar?"

    show mc neutral 1

    hector "Ahh ganun ba? Isa nga pala ako sa mga iskolar ng Ateneo de Manila dalubhasa sa mga makasaysayang relikya. Kasalukuyan kong pinag-aaralan ang tungkol sa LCI para matukoy ko kung kailan ito ginawa."
    
    hector "Maaari kang sumali sa akin kung ito ang iyong ninanais."

    show mc speaking 1

    mc "Kung ito'y okay lang po sa inyo then happy po ako na sumama dahil malaking tulong po ito sa aking pagsusulit."

    show mc neutral 1

    hector "Ahh, bago ko pala makalimutan kailangan mo pang maghintay ng ilang araw para ika'y makasama sa akin."

    show mc speaking 1

    mc "Okay lang sa akin maghintay."

    mc "Ano nga pala ang LCI?"

    show mc neutral 1

    hector "Ayon sa isang dutch anthropologist na si Antoon Postma ang LCI ay isang semi-official certificate na nagpapawalang-sala sa utang ng isang nakatataas na opisyal."

    hector "Ang pagpapakawalang sala sa kanya at lahat ng kapamilya at mga inapo niya. Ang malaking halaga ng ginto ay hindi nabayaran ngunit tinalukran sa LCI."

    hector "Kasama ang iba pang mga opisyal bilang mga saksi, na ang ilan ay binanggit sa pangalan at hurisdiksyon."

    hector "Bilang isang piraso ng bagong ebidensya sa kasaysayan, itinatag ng LCI na ang mga isla ng pilipinas ay mahusay na umuunlad sa panahon ng kalakalan sa timog-silangang asya noong ika-sampung siglo."

    hide hector with dissolve

    hide mc with dissolve

    show bg black with fadetoBlack

    call slowTextfade("Pagkatapos ng ilang araw")


    scene bg hector house with fadetoBlack


    show hector at right, large, fadeInSlow

    show mc neutral 1 at left, large, fadeInSlow:
        xzoom -1.0

    hector "Tara. Dadalhin kita kung saan pinag-aaralan ng aking grupo ang LCI."

    hide mc with dissolve

    hide hector with dissolve


    scene bg classroom with fadetoBlack


    show silouette as mobchar1 at left, large, fadeInSlow

    show silouette as mobchar2 at right, large, fadeInSlow

    show hector at center, large, fadeInSlow

    hector "Mga ginoo. Ito nga pala si [mcName]. Siya ay mayroong pagsusulit kung saan kailangan niya tayong obserbahan. Sana ay wala kayong problema dito."

    "Scholar" "Maayos lang iyon Ginoong Hector. Magandang umaga sa iyo [mcName]." 

    "Scholar" "Sa tingin din po namin ay malapit nang matapos ang ating pagsasalin sa LCI. Ilang araw na lang at mapapala thala na natin ang ating nasaliksik dito."

    hector "Abay ito ay magandang balita! Ipagpatuloy na natin ang ating pag-sasaliksik mga ginoo."

    hide mobchar1 with dissolve

    hide mobchar2 with dissolve

    hide hector with dissolve

    show bg black with fadetoBlack

    call slowTextfade("Makalipas ng ilang araw")


    scene bg classroom with fadetoBlack


    show hector at right, large, fadeInSlow

    hector "Ayon sa ating matinding pananaliksik tungkol sa LCI maari ko nang sabihin na ang LCI ay ginawa pabalik noong 900 AD. Ginagawa itong isa sa mga pinakaunang nakasulat na tala sa pilipinas."

    hector "Makakauwi na din tayo mga kaibigan!"

    hide hector with dissolve


    scene bg hector house with fadetoBlack


    show hector at right, large, fadeInSlow

    show mc speaking 1 at left, large, fadeInSlow:
        xzoom -1.0

    mc "Ako'y namamangha sa iyong natuklasan, Thank you talaga sa opportunity na iyong binigay sakin."

    show mc neutral 1

    hector "Bago ka nga pala lumisan may inihanda akong regalo para sa iyo ikonsidera mo ito bilang isang munting regalo ng pamamaalam."

    show mc speaking 1

    mc "MC: Ay nako, sana hindi na po kayo nag abala pa.. Pero thank you sa munting regalo niyo sakin, sa mga ala-ala na inyong ibinigay sakin tiyak na hindi ko malilimutan at salamat sa tulong na inyong binigay."

    mc "Once again thank you very much ginoong Hector at ako'y mauuna na hanggang sa muli nating pagkikita."

    hide mc with dissolve

    hide hector with dissolve


    scene bg black with fadetoBlack


    play music "Intrepid.mp3" volume 0.3 fadein 1.0 fadeout 1.0

    show mc thinking 1 at right, large, fadeInSlow

    AI "You just obtained an item which can be used to partially repair and restore my timeleap ability so that you can travel back to your timeline."

    AI "Are you ready to go?"

    show mc thinking 3 at center, large

    menu:
        mcInner "..."

        "Yes":
            show mc thinking 1
            mc "This journey was fun but I want to return to my original timeline."

        "No":
            show mc thinking 1
            AI "Unfortunately, we cannot remain in a timeline for longer than necessary."

    pause(1)

    scene bg white with fadetoWhite


    stop music

    return

label ch1sub_chapter2:


    scene bg black with fadetoBlack


    call slowTextfade("Chau Ju Kua's Chu Fan Chi")

    play music "Comfortable Mystery 2.mp3" volume 0.3 fadein 1.0 fadeout 1.0

    $ i = 0
    while i < 2:
        show bg classroom with eyeopen:
            blur 5.0
        pause(1)
        show bg black with eyeclose
        pause(1)
        $ i =  i + 1
    $ i = 0

    show bg classroom with eyeopen:
        blur 5.0
        easein 2.0 blur 0.0
    
    play sound "<from 0 to 8>Clock.mp3"

    show classmate y at right, fadeInSlow

    y "Uhmm… Hello??? Gising na, kanina kapa natutulog."

    mc "Huh? Seryoso?"

    y "Ano ba ang napanaginipan mong maganda para makatulog ka nang ganun kahimbing sa loob silid aralan?"

    mc "I forgot most of it… pero naalala ko na nakikipag kwento ako sa isang historian na familiar ang mukha…"

    y "Di bale na ano ang napanaginipan mo, malapit nang magsimula ang klase buti nga napansin ko na tulog ka at nakapag desisyonan ko na gisingin ka hanggat hindi pa nakarating ang guro dito."

    mc "Thank you talaga dahil ginising mo ako."

    hide classmate with dissolve

    play sound "Door Open.mp3"

    pause(0.5)

    play sound "<from 0.0 to 1.5>Footstep Concrete.mp3"

    pause(0.5)

    "Professor" "Ang pagsusulit na gagawin ninyo sa araw na ito, ay magsusulat kayo ng personal na pagsusuri sa libro na nagngangalang “Chu Fan Chi” sa kadahilanang itinalaga ko to sa inyo na basahin kagabi."

    show classmate y at center, fadeInSlow

    mc "Nako hindi ko nabasa ang librong iyon at hindi ako nag-aral kagabi. Paano na ito ngayon?"

    y "Akong bahala sa'yo, ang librong “Chu Fan Chi” ay isinulat noong 1225 ng isang chinese nobleman na nagngangalang Chau-Ju-Kua. Itong libro ay isinalin sa pangalang “Records of Various Barbarous Nations”." 
    
    y "Ang librong ito ay nagsisilbing dokumentasyong kalakalan sa pagitan ng China at Pilipinas. Ito ay mga salaysay ng mga tao sa pilipinas at pagsasagawa ng kalakalan."

    y "May hindi ka ba naintindihan sa aking mga sinabi?"

    mc "Ohh, I understand it now. Maraming salamat sa pagpapaliwanag. Ngayon ay pwede ko nang gawin at tapusin ang pagsusulit na binigay satin."

    hide classmate with dissolve


    scene bg white with fadetoWhite


    stop music

    return



label ch1sub_chapter3:


    scene bg black with fadetoBlack


    call slowTextfade("Antonio Pigafetta's Voyage Around the World")


    scene bg beach with fadetoBlack

    play music "Stay the Course.mp3" volume 0.3 fadein 1.0 fadeout 1.0

    play sound "<from 0 to 8>Clock.mp3"

    mc "What's going on? Where am I?"

    AI "You have been transported onto another timeline."

    mc "What are you talking about?! I thought you'd been put right!"

    AI "Not exactly. you have been transported to another timeline, a timeline that isn't your own but closer to your original timeline."
    
    AI "You must once again find something from this timeline to repair me."

    mc "What?! What can I take from this timeline that can repair you?!"

    AI "It's something you will have to figure out on your own. My only hint is that it is not something physical."

    mc "What?"

    pause(1)

    show spaniard at center

    "???" "What are you doing here!" #translate to spanish

    mc "Wait!"

    # punch sfx


    scene bg black with fadetoBlack

    play music "SCP-x5x.mp3" volume 0.3 fadein 1.0 fadeout 1.0

    $ i = 0
    while i < 2:
        show bg storage room with eyeopen:
            blur 5.0
        pause(1)
        show bg black with eyeclose
        pause(1)
        $ i =  i + 1
    $ i = 0

    show bg storage room with eyeopen:
        blur 0.0

    show mc left arm 1 at left, large

    mc "Why did you even bring me here in the first place?!"

    AI "I do not have much control over which timeline you're transported to."

    mc "So what do you want me to do?! Heck, forget what I ought to do, where did you even transport me to?!"

    AI "The only hint I can give is it is the year 1521."

    mc "C'mon! I need an answer now!"

    hide mc

    show mc thinking 3 at center, large

    mcInner "1521? I'm pretty sure that's around the Battle of Mactan but I can't remember the people in that event."

    mc "Battle of Mactan... someone important died. Who was it?"

    show spaniard at left, fadeInSlow:
        yoffset(200)
        xysize (1080, 1080)

    show mc thinking 2 at right, large

    "Spaniard" "¿Hablas español?"

    "AI (Whispering)" "Translation activated."

    mc "Sí, sí hablo español."

    "Spaniard" "Has sido capturado por la tripulación directamente bajo la corona española. (You have been captured by the crew directly under the Spanish crown.)"

    "Spaniard" "No debes mentir o arderás en el infierno. (You must not lie or you will burn in hell.)"

    "Spaniard" "¿Qué haces aquí cerca del campamento? (What are you doing here near the camp?)"

    show mc thinking 3

    menu:
        mcInner "Ano sasabihin ko dito..."

        "I am just a traveller":
            mc "¡Soy sólo un viajero! Me acerqué a tu campamento porque vi luz y fuego y quería compañía. (I am just a traveller! I just got close to your camp because I saw light and fire and wanted company.)"

            "Spaniard" "¡Mentiras! No llevas nada, ¿cómo puedes ser un viajero? (Lies! You are carrying nothing, how can you be a traveller.)"

            "Spaniard" "¡Debes ser un enemigo! Te tiramos por la borda por mentirte delante de Dios. (You must be an enemy! We will throw you overboard for lying in front of God.)"

            hide mc with dissolve

            hide spaniard with dissolve

            show bg black with fadetoBlack

            stop music

            play sound "<from 0 to 8>Clock.mp3" loop

            call slowTextfade("You Died")

            AI "Initiating rewind protocol{nw=0.5}"

            pause(1)

            stop sound

            jump ch1sub_chapter3

        "I am a stranded slave":
            mc "Soy un esclavo abandonado por mis dueños chinos. ¡Por favor ten compasion! (I am a stranded slave left behind by my Chinese owners. Please have mercy!)"
            
            mc "Puedo trabajar para usted, fui traductor para mis dueños anteriores. (I can work for you, I was a translator for my previous owners.)"

            "Spaniard" "¿Un esclavo varado que sabe traducir dices? (A stranded slave that knows how to translate you say?)"

            "Spaniard" "Alégrate, nuestra misericordiosa tripulación te acogerá. Recuerda esto, tu vida fue salvada por la tripulación de Magallanes. (Be glad, our merciful crew will take you in. Remember this, your life was saved by the crew of Magellan.)"

        "I am a Chinese merchant":
            mc "¡Solo soy un comerciante que pasa! Quería vender mis mercancías a vuestra tripulación porque sé que los barcos españoles dan buen dinero. (I am just a merchant passing by! I wanted to sell your crew my wares because I know Spanish ships bring good money.)"
            
            "Spaniard" "¡Mentiras! No llevas mercancías, ¿cómo puedes ser comerciante? (Lies! You are carrying no wares, how can you be a merchant.)"

            "Spaniard" "¡Debes ser un enemigo! Te tiramos por la borda por mentirte delante de Dios. (You must be an enemy! We will throw you overboard for lying in front of God.)"

            hide mc with dissolve

            hide spaniard with dissolve

            show bg black with fadetoBlack

            stop music

            play sound "<from 0 to 8>Clock.mp3" loop

            call slowTextfade("You Died")

            AI "Initiating rewind protocol{nw=0.5}"

            pause(1)

            stop sound

            jump ch1sub_chapter3

    show bg black with fadetoBlack


    scene bg storage room with fadetoBlack


    show slave 1 at left

    "Slave 1" "Kamusta ka? Nais mo ba maging malaya? (How are you? Do you want to be free?)"

    mc "Oo (Yes)"

    "Slave 1" "Wag mong ibahagi sa mga Kastila ang tungkol sa ating usapan. (Don't tell the Spaniards about our conversation.)"


    scene bg storage room with fadetoBlack


    "Spaniard 1" "¡Los nativos son demasiado vulgares para ser colonizados! ¡Ni siquiera pueden vestirse con ropa! (The natives are too vulgar to be colonized! They can't even dress up in clothes!)"

    "Spaniard 2" "¡Así es! ¡Y su tecnología es demasiado primaria! Realmente están en la era de la oscuridad. (That's right! And their technology is too primal! They are truly in the age of darkness.)"

    mcInner "Hindi ito ang itinuro sa amin sa history class. Wala silang sinabi tungkol sa pag-aalaga ng mga Kastila sa mga katutubo."
    
    mcInner "Ang paglalarawan nila sa mga Native Filipinos na 'barbaro' at 'walang kultura' ay biased dahil hindi nila naisip na maintindihan ang pamumuhay ng mga Pilipino sa mga isla."

    pause(1)

    mcInner "Ah! Tama! Naalala ko nga ang libro namin noon sa history class, may nakasulat na 'Journey'. Pero sino nga ba 'yon? Tsaka anong libro nga ba ulit iyon? Bakit 'di ko matandaan?! Nakakainis naman, hindi ko alam kung sino dapat kong kausapin."

    
    scene bg black with fadetoBlack


    call slowTextfade("In Cebu")


    scene bg beach with fadetoBlack


    show spaniard at right:
        xysize(1080, 1080)
        yoffset(250)

    show slave 1 at center

    show mc thinking 1 at left

    "In a village near the beach"

    "Spaniard" "Somos españoles, ¿podemos saber quién es el representante de este pueblo?"

    "Slave 1" "Ang sabi nila ay \"Kame ang mga kastila, maaari ba naming malaman kung sino ang kinatawan ng nayong ito?\""

    "Villager" "Ako po iyon."

    "Spaniard" "¿Sabes que los dioses que adoras no son ciertos? Deberías convertirte al cristianismo."

    "Slave 1" "Alam niyo bang hindi totoo ang mga diyos na sinasamba niyo? Dapat kayo manampalataya sa christianismo."

    "Villager" "Abay sino kayo para sabihan kame kung sino dapat ang aming sinasamba!"

    "Spaniard" "Puede que no sepa tu idioma, pero reconozco a un hereje cuando lo veo. (I may not know your language, but I know a heretic when I see one.)"

    "Spaniard" "Kill the heretics!"

    hide spaniard with dissolve

    hide slave with dissolve

    show bg black

    show mc thinking 3

    play sound "Fighting.mp3" loop

    mcInner "If this happened in my time, they'd be wanted criminals."

    stop sound


    scene bg beach with fadetoBlack


    show spaniard at center, fadeInSlow

    show spaniard at left, fadeInSlow as spaniard2

    show mc thinking 1 at right, fadeInSlow

    "Spaniard 1" "Qué tontos son estos nativos. (Such fools these natives are.)"

    "Spaniard 2" "Ya sabes lo que dicen: \"aquellos que obstinadamente creen en mentiras y engaños seguirán creyéndolo, (You know what they say, “Those who stubbornly believe lies and deceit will continue to do so,)"

    "Spaniard 2" "Incluso bajo la amenaza de la muerte y el sufrimiento eterno en el infierno.\" (even under the threat of death and eternal suffering in hell.)"

    "Spaniard 1" "¿Eh? (Huh?)"

    "Spaniard 2" "No importa. Vámonos de aquí. (Never mind. Let us get out of here.)"

    hide spaniard2 with dissolve

    pause(1)

    show spaniard at center:
        xysize(1080, 1080)
        yoffset(200)

    "Spaniard 1" "Hey!"

    show mc realization 1

    "Spaniard 1" "Ven aquí, nos vamos. No intentes ser inteligente con nosotros, (Come here, we are leaving. Don't try to be smart with us,)"

    show mc thinking 1

    "Spaniard 1" "Porque si lo haces, haremos lo mismo que les hicimos a estos bárbaros de aquí. ¿Comprendido? (Because if you do, we will do to you what we did to these barbarians here. Understood?)"

    show mc speaking 3

    mc "S-Sí… (O-Okay…)"

    hide spaniard with dissolve

    mcInner "We were never told in history class that the Spanish burned down villages because of their refusal to convert. I wonder… the history I have learned is truly biased against my ancestors!"
    
    mcInner "Nothing was ever mentioned, heck, nothing was even referenced about such atrocities as the one I have just witnessed. It really makes me wonder who actually is responsible for writing history in such a way that travesties like these are forgotten?"

    mcInner "The people that have committed the atrocity? The Americans who came in after them? Or was it written by the very people who descended from the very people that the Spanish unjustly and cruelly treated?"

    AI "So, what are your feelings about history being warped by those who wrote them?"

    menu:
        mcInner "..."

        "It's wrong!":
            mc "It's wrong!"

        "It's not wrong...":
            mc "It's not wrong but..."

    AI "In any case, this is not why you are here. You are here to repair me so you can return from whence you came. You are not here to correct the wrongs of the past."

    mc "And if I want to correct history?"

    AI "You cannot. It is an unspoken rule of time travel that the traveler must not meddle with what has already taken place. Doing so can cause complications."

    hide mc with dissolve

    stop music


    scene bg ship with fadetoBlack


    play music "Southern Gothic.mp3" volume 0.5 fadein 1.0 fadeout 1.0

    show magellan at center, large, fadeInSlow

    show pigafetta at right, fadeInSlow:
        xysize(800, 800)

    "Magellan" "Como habrás notado, nos estamos preparando para una batalla. (As you may have noticed, we are preparing for a battle.)"

    "Magellan" "Nuestro enemigo es un obstinado bárbaro de Mactán y su tribu de salvajes. (Our enemy is a stubborn barbarian from Mactan and his cohort tribe of savages.)"

    "Magellan" "Se ha negado tontamente a obedecernos a nosotros y a nuestros aliados, (He has foolishly refused to obey us and our Allies,)" 
    
    "Magellan" "E iremos a esa isla para darles una lección a él y a sus bárbaros incivilizados. (And we will go over to that island to teach him and his uncivilized barbarians a lesson.)"

    "Slave 1 (Shouting)" "Baliw ba kayo?"

    "Slave 2" "Hindi tayo magkakaroon ng pagkakataon laban sa kanya at sa kanyang mga tauhan sa isang labanan!"

    "Slave 3" "Gusto nilang kalabanin natin siya at ang tribo niya?! Ito ay mapangahas! Papatayin nila tayong lahat!"

    "Slave 4" "Kung ako ay tanga, masasabi kong magandang plano ang pakikipaglaban sa kanilang tribo, ngunit hindi ako ganoong katanga! Siya at ang kanyang mga tauhan ay mahusay na mandirigma! Baka patay na tayo bago pa natin siya masulyapan!"

    play sound "Gunshot.mp3" volume 0.35

    show magellan firing

    mc "!"

    pause(1)

    "Magellan" "¡Qué cobardes sois! ¿Qué hay que temer frente a un grupo de salvajes incivilizados y poco inteligentes? (What cowards you are! What is there to fear in the face of a group of uncivilized and unintelligent savages?)"

    show magellan

    mcInner "We are on our way to what will become the Battle of Mactan. Lapu-Lapu and his men will force the Spaniards to retreat, and Magellan would meet his end as a result of a poisoned arrow. Should I warn him or should I just keep my thoughts to myself?"

    menu:
        mcInner "Should I warn Magellan?"

        "Yes":
            mc "..."

        "No":
            mc "..."


    scene bg storage room with fadetoBlack


    "Slave 2" "Magkakaroon ba tayo ng pagkakataon laban sa kanya? Kung paniniwalaan ang mga kuwento, siya at ang kanyang mga tauhan ay magaling sa paghahanap at pagsasamantala ng kahinaan sa hanay ng kanilang mga kalaban!"

    "Slave 3" "Ewan ko sa inyo, pero mas gugustuhin ko pang tumakas dito kaysa ilaban si Lapu-Lapu at ang kanyang mga tauhan."

    "Slave 2" "Baka pwede tayong makiusap sa kanila–{nw}"

    "Slave 4" "Ang pagsusumamo ay hindi makabubuti sa atin. Kung mayroon man, ang tanging kalayaan na makukuha natin ay kung nagpasya silang patayin tayo, at sa gayon ay mapalaya ang ating mga kaluluwa."

    "Slave 5" "Maaaring magandang ideya ang pag-aalsa. Sakupin natin ang barkong ito at–"

    "Slave 1" "Napaka-walang muwang talaga kayong mga tao. Sa tingin niyo ba ay papayag ang mga Kastila sa anumang hilingin natin sa kanila?! Mapapatay nila tayo kung gusto nila!"

    "Slave 2" "Anong ibig mong sabihin?"

    "Slave 1" "Walang sinuman sa inyo ang may makatwirang mungkahi, at kung tayo'y susunod sa mga plano na iyong iminungkahi, tayo ay masentensiyahan ng kamatayan dahil sa pagtataksil, kaduwagan o pagsuway, marahil lahat ng ito!"

    "Slave 1" "Subukan na lang natin mabuhay."

    mc "..."

    mcInner "How would things turn out if Magellan survives the battle? I wonder..."


    scene bg ship with fadetoBlack


    show pigafetta at center, large, fadeInSlow:
        xzoom -1.0

    show mc speaking 3 at right, large, fadeInSlow

    mc "Señor, tengo algo que decirle... (Sir, I have something to tell you...)"

    mc "Este jefe y sus hombres son guerreros expertos que se especializan en explotar las debilidades de sus enemigos. (This chief and his men are expert warriors who specialize in exploiting their enemies' weaknesses.)"

    mc "Ten mucho cuidado si decides luchar contra ellos. (We should be more careful in this fight.)"

    "???" "..."

    "???" "WAHAHAHAHAHAHAHA!!{nw=0.5}"

    "???" "Te aseguro, muchacho, que estamos muy por delante de ellos en tecnología y tácticas. (I assure you, boy, that we are way ahead of them in technology and tactics.)"

    "???" "Sus lanzas y flechas no son rival para nuestra armadura, y nuestras armas pueden penetrar su armadura de madera fácilmente. (Their spears and arrows are no match for our armor, and our guns can penetrate their wooden armor easily.)"

    "???" "¡Además estamos encabezados por el gran capitán Magallanes! Como has visto antes, ¡su presencia fue excepcional! (What's more is we are headed by the great captain Magellan! As you have seen earlier, his presence was outstanding!)"

    "Pigafetta" "¡Yo, Antonio Pigafetta, estoy feliz de haber podido acompañarlo en este viaje alrededor del mundo! (I, Antonio Pigafetta, am glad to have been able to accompany him on this voyage around the world!)"

    "Pigafetta" "No hay de qué preocuparse, los aplastaremos. (There is no need to worry, we will crush them.)"

    hide magellan with dissolve

    stop music


    scene bg beach with fadetoBlack



    play music "Stay the Course.mp3" volume 0.3 fadein 1.0 fadeout 1.0

    AI "Are you still there?"

    mc "Yes."

    AI "What are your thoughts regarding this part of history?"

    mc "Here we are. Two sides. Magellan believes his weaponry and tactics are sufficient enough to defeat Lapu-Lapu and his men, accompanying them is Antonio Pigafetta, who is currently writing an account of their voyage, the first around-the-world voyage."

    mc "They will soon find out that their weapons and tactics are insufficient against Lapu-Lapu's tactics and sheer numbers, despite their biased preconceptions that the natives are uneducated, uncivilized and are technologically stagnated."

    mc "But what is confusing is that at some point, objective oversight gave way to emotions and confusion in the heat of battle."
    
    mc "For one, it's not even known as to whether Lapu-Lapu actually struck the blow that killed Magellan, or whether it was a lucky potshot from one of his men."

    mc "Heck, was Lapu-Lapu actually leading his men or was he on the sidelines? Recorded history tells us this much, but did events really pan out the way they did according to every account of this historical event? Being here only raises more questions…"

    AI "Would you like to see what happens?"

    mc "Would anyone even believe me if I recounted what I saw here? I'd rather not witness it at all."


    scene bg white with fadetoWhite


    return