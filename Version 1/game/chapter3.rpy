# SUBCHAPTER 1 CHARACTERS
define ds = Character("Diego Silang", color="#fcc603")
define sg1 = Character("Spanish Guard 1", color="#5100ff")
define sg2 = Character("Spanish Guard 2", color="#e100ff")
define cx = Character("Character X", color="#ff0000")
define h = Character("Hermano", color="#3c3c3c")

label chapter_3:

    show bg black
    call slowTextfade("Chapter 3")

    call slowTextfade("Revolts and Revolution")


    call slowTextfade("Diego Silang's Letter to the British")
    play music "/music/bg_chapter3.mp3" fadein 0.5 volume 0.2
    label subchapter1_3:
    
    scene bg ph-street
    with fade

    "..." "(MC teleports near Vigan City, October 1762 where Diego Silang is giving a Speech.)"
    
    show diego default
    with fade

    ds "My fellow Ilocanos, hear me! The British threaten our land, our homes, our very existence! But fear not, for we shall stand united against this tyranny!"
   
    hide diego

    show crowd
    with fade

    show guard default at left
    show guard default as guard2 at right
    "[sg1] (Accusing [mc])" "¡Basta de esta sedición! ¡Dispersar! ¡Dispersar!  (Enough of this sedition!  Disperse!  Disperse!)"
    
    "[sg2] (Pointing at [mc])" "¡Tú allí! ¿Qué estás haciendo aquí? ¡Pareces sospechoso!  (You there!  What are you doing here?  You look suspicious!)"
   
    "[mc] (Stammers while trying to explain)" "ah-eh…."
    
    sg1 "¡No hables! ¡Un espía británico, sin duda! ¡Intentando provocar problemas entre los leales ilocanos!  (Don't speak!  A British spy, no doubt!  Trying to stir up trouble among the loyal Ilocanos!)"
   
    "..." "(The Spanish Guards grab the MC roughly)"
   
    hide guard
    hide guard2
    show mc realization

    mc "¡No soy un espía! ¡Acabo de llegar! (Wait! I'm not a spy!  I... I just got here!)"
    "..." "(The Spanish Guards ignore him and drag him away.)"
   
    show mc speaking
    menu:

        "The spanish soldiers took hold of you..."

        "Try to escape":
            "..." "[mc] tried to escape but failed"
            jump textEvent4

        "Dont resist":
            jump textEvent4
    
    label textEvent4:
        scene bg prison
        with fade

    "..." "(Loud banging and yelling can be heard in the dark, small room. The MC sits on the cold ground, puzzled.)"

    show mc prison

    "[mc] (Inner Voice)" "Nasaan ako? Anong taon ito? Mukhang hindi maganda ito… "
   
    "[mc] (Whispering)" "Ano ang nangyayari? may away ba?"
    
    "someone" "Labas! ang Gobernadorcillo ay na patapon na! Pinalayas na ni Diego silang ang mga alagad ng espanya!"
   
    "..." "(Another character, also unshackled, emerges from a nearby cell and approaches [mc].)"
    
    hide mc

    show crowd
    cx "Anong nangyayari? Sino ka?"
   
    mc "Hi-hindi ko alam. kakarating ko lang dito. "
   
    hide crowd

    "..." "([mc], still fresh from his arrest, emerges from the prison with a group of cheering Ilocano rebels.)"
    
    scene bg cellar
    with fade
    "Ilocano Rebel" "Salamat kay Diego Silang, malayang tao ka! Ang mga asong Espanyol ay pinalayas na!"
    
    show mc thinking2

    mc "Diego Silang?  pinalayas niya ang mga Espanyol?"
   
    show speaker at right
    cx "Mukhang ganoon, kaibigan. Mukhang nagsimula na ang bagong simula!"
    hide speaker

    "..." "(The Ilocano rebel leads them through the crowd, pointing towards a platform where Diego Silang stands addressing the people.)"
    hide mc
    show diego default
    ds "Sa sobrang tagal, nagdusa tayo sa ilalim ng kamay na bakal ng Espanya! Pero wala na!"
    ds "Tayong mga Ilokano ay bumangon at inangkin ang ating kalayaan! Ngayon, isang bagong banta ang nagbabanta - ang Britanya!"
    ds "Pero hindi tayo magpapatalo! Ipaglalaban natin ang ating lupain, para sa ating kinabukasan!"

    show mc thinking at right
    mc "This is incredible! Gusto kong maging bahagi nito!"
   
    cx "Ako rin! Ipakita natin ang ang ating kakayahan."
    
    hide crowd
    "..." "([mc] and Character X throw themselves into supporting Diego Silang's cause. Their dedication and bravery earn them the respect of their fellow rebels and Diego Silang himself.)"
   
    show mc speaking2
    mc "Hindi alam ng mga espanyol kung anong naghihintay para sa kanila."
   
    show speaker at right
    cx "Sinabi mo pa! Handa na tayo para ipaglaban ang nararapat!"
    
    hide speaker
    "..." "(A cheer erupts from a nearby group of rebels.)"
   
    show mc default

    scene bg chap3hallway
    with fade

    show diego default
    "[ds]" "(Approaches [mc] and Character X with a satisfied smile on his face) Magaling! kayong dalawa! ang inyong dedikasyon ay talagang nakaka enganyo."
   
    show mc speaking at left    
    mc "Ginagawa lang namin ang aming parte, Diego Silang. Naniniwala kami sa iyong layunin."
   
    show crowd
    cx "Siyang Tunay! Ang malayang Ilocos ay isang kinabukasan may saysay na ipaglaban."
   
    ds "At yan ang kinabukasan na nais nating makamit!."
    hide crowd
    "..." "(One evening, a messenger arrives at Diego Silang's camp, bearing a sealed letter with the Bishop's mark.)"
   
    "[ds]" "(Breaks the seal and scans the contents) Hmm... nakapukaw ng pansin. Mukhang nais ng Obispo(bishop) na talakayin ang mga bagong pangyayaring ito.."
   
    show crowd
    cx "Ano ang ibig niyang iparating diego?"
   
    ds "Tinatanggihan niya ang aking mga kahilingan para sa awtonomiya ng Ilocano. Iginiit niya na tumindig tayo at sumuko sa pamumuno ng Espanyol."
    hide crowd
    show mc thinking at right
    with dissolve

    show diego default
    mc "Tipikal! Hindi sila makikinig sa dahilan."
   
    ds "Kung ganon ay pilitin natin sila na tayo ay pakinggan. Tatawag ako para sa isang pulong sa mga awtoridad ng Simbahan."
    ds "Titingnan natin kung handa silang makipag-ayos sa isang mapayapang rebolusyon..."
    ds "o kung digmaan na lang ang tanging landas na natitira."
   
    "..." "(The tension from the meeting with the Church lingers in the air as Diego Silang gathers with [mc] and Character X in a private room.)"
   
    ds "Ang ultimatum ng Simbahan... nag-iiwan ito sa atin ng mahihirap na pagpapasya. "
    show speaker at left
    cx "Isa lang ang pagpipilian Diego! makipag laban tayo! manindigan tayoct palayasin ang mga espanyol! ng sa gayon ay mapag tuonan natin ng pansin and britanya."
   
    mc "Sandali lamang, Character X. Paano kung may ibang paraan? Marahil maaari nating muling suriin ang ating relasyon sa mga Espanyol. Kung madiskarteng lapitan natin sila, siguro makukumbinsi natin sila na tulungan tayo laban sa British."
   
    cx "Magtiwala sa Espanyol? Pagkatapos ng lahat ng ginawa nila? Tatalikuran nila tayo sa sandaling wala na ang mga British!"
    
    ds "Ang mga pananaw ninyo ay parehong may katwiran. Ang pakikipaglaban nang mag-isa ay maaaring humantong sa ating pagka lipol. Gayunpaman, ang pagtitiwala sa Espanyol ay isang sugal…"
    
    hide mc
    hide crowd
    hide speaker
    "..." "(A moment of silence… decides to talk to them next time)"
   
    "..." "(Diego Silang calls for another meeting with [mc] and Character X.)"
    
    show speaker
    ds "Humanting ako ng isang mahirap na desisyon. Para sa kapakanan ng ating mga tao, ako ay... susuko sa mga awtoridad ng Britanya"
    
    show speaker as speaker2 at right
    cx "Sumuko? Pero Diego... hindi tayo pwedeng sumuko na lang!"
    
    show mc speaking2 at left
    
    ds "Ito ay hindi pagsuko, ngunit isang madiskarteng hakbang. (Iniabot ang isang selyadong sulat) Nag sulat ako ng liham sa British na isinasalaysay ang ating sitwasyon at nag-aalok ng aming tulong laban sa mga Espanyol. Ito ay Ihahatid ninyong dalawa sa Manila. "
   
    cx "Ayoko ng ganito Diego. May hindi tama  dito… "
   
    ds "Ako'y inyong Pagkatiwalaan. Ito lamang ang paraan upang iligtas ang Ilixoa. lumisan na kayo! ihatid ninyo ang liham at bumabalik kayo'ng ligtas."
    
    hide speaker

    hide speaker as speaker2
    "..." "([mc] and Character X leave Diego Silang's quarters)"
   
    "..." "(As they embark on their journey to Manila, a tense silence hangs between them. [mc] steals glances at the letter, their mind filled with doubt.)"
    
    show mc speaking2
    mc "Ano sa tingin mo X? nararapat ba talagang ihatid natin itong liham?"
    
    show speaker at right
    cx "Sa pag wawari ko ay hindi tama ang buong pangyayari. susuko si Diego … Bakit niya isasagawa ang mga ito."
    
    mc "Baka may tinatago siyang plano…"
   
    cx "O baka naglalaro siya sa magkabilang panig para sa kanyang sariling pakinabang."

    "..." "([mc] and Character X continue their journey, each grappling with their doubts and suspicions about Diego Silang's true intentions.)"
   
    "Character X & [mc] (Inner Voice)" "Anong layunin ng pag-aaklas kung sa huli ay susuko rin?"
    
    hide speaker as speaker2
    "[mc] (Inner Voice)" "Na i-abot na namin ang sulat, pero... wala. Walang tugon mula sa mga Briton, walang balita mula sa Vigan. Ano bang nangyayari? Nabigo ba ang plano ni Diego?"
    
    "..." "(One morning, news arrives like a whirlwind.  The British have appointed Diego Silang as the Governor of Ilocos!)"
   
    show crowd
    "Random People passing by" " Narinig mo ba ang balita? si diego silang ay itinanghal bilang gobernador ng ilocos..."
    
    show mc speaking at left

    "[mc] (Inner voice)" "Gobernador? Diego? Hindi tama 'yan! Sumalungat tayo sa mga Espanyol, hindi para maging mga tuta ng mga Briton!"
   
    show mc thinking at left
    "..." "([mc] spend his days holed up in a small inn, waiting for the time machine to activate.)"
   
    "[mc] (Inner voice)" "Ang time machine... hindi pa rin ito naa-activate. Bakit kaya? May mali ba akong ginawa? O kaya naman baka ay konektado ito sa tagumpay ng rebolusyon?"
   
    "Random People passing by" "Nag wagi si Diego Silang!"
   
   
    "..." "(As if triggered by the news, the time machine inside the [mc]'s room come to life)"
   
    "[mc] (Inner Voice)" "It's working! Ngunit... pwede na ba akong umalis? Nanalo si Diego sa isang laban, ngunit tunay bang malaya na ang Ilocos? Paano naman ang kanyang motibo? Ito ba ay tungkol lamang sa kalayaan, o may personal at mas malalim pang dahilan?"
    
    label subchapter2_3:
    
    scene bg black
    call slowTextfade("Hermano Pule's Cofradia de San Jose through Its Hymns")
    play music "/music/bg_chapter3.mp3" fadein 0.5 volume 0.2
    scene street request
    with fade
    
    "..." "(Hermano approaches [mc].)"
    
    show speaker as pule
    h "Ngayon lamang kita nakita dito,taga rito kaba?"
    
    show mc thinking2 at right
    mc "Ah hindi ho, dumadayo lang ako"
    
    h "Ako si Apolinario, Apolinario Dela cruz. Gusto mo bang sumama? May mga naghihintay sa akin at ipapakilala kita."
    
    menu:
        "Hermano Pule invites you to come with him..."

        "Go with him":     
            mc "Sigi ba, hindi rin naman ako pamilyar dito sa Tayabas."
            jump textEvent5

        "Dont go with him":
            "[mc] (Inner thoughts)" "I need to get information on this timeline to be able to get home"
            jump textEvent5
     
    label textEvent5:
        "..." "(Hermano and [mc] walked towards the group of people, as they wait for Hermano)"
    
    h "Sila nga pala ang aking mga kasamahan. Hermandad de la Archi-cofradía del Glorioso Señor San José y de la Virgen del Rosari. Iyan ang tawag samin."
    
    "..." "([mc] greets the confraternity)"
    
    h "Cofradia de la San Jose na lamang ang itawag mo. Alam kong mahirap kabisaduhin ang tawag samin."
    
    h "Hermano Pule nga pala ang tawag nila sa akin dito. Yun na lang din ang itawag mo sa akin."
    
    "..." "(Hermano walks with [mc] along and shows him books containing the brotherhoods’ usual activities.)"
    
    "..." "(Scanning the second book, he recognize the hymn called \“Dalit\”.)"
    
    "..." "(Hermano approaches [mc] as he noticed him glancing at the book.)"
    
    h "Iyan ang Dalit-, “Dalit sa Kaluwalhatian sa Langit sa Cararatnan ng mga Banal” talaga ang tawag diyan."
    
    mc "Kayo ho ba ang gumawa nito?"
    
    h "Hindi, si Fray Padro de Herrera ang sumulat niyan ngunit, ginamit lamang namin ito para sa kasamahan."
    
    "..." "(As [mc] heard this, he began to put together pieces with the facts that he had already known.)"
    
    mc "Sa maikling pagkakataong na nakasama ko ang mga taong sa panahon na ito aking naramdaman ko ang kanilang paghihirap."
    mc "Kahit sila ay nahihirapan ang kanilang pananampalataya ay mananatiling matibay."
    mc "Nang aking nakasama sa personal si Hermano Pule , unting-unti kong naiintindihan ang kanyang pananaw." 
    mc "Dahil dito aking napagtanto na ang hymn ay hindi lamang para sa pagsamba dahil ito rin ay ang mga ninanais ng mga tao na magkaroon ng Kalayaan, hustisya at ang pagkakaisa ng lahat."
    mc "ito ay hindi lamang  mga salita na isinulat o inawit kundi ito rin maaaring maging gabay upang magbigay-inspirasyon ng pagbabago at magpagaan sa diwa ng tao."
    
    mc "Hermano, nagpapasalamat ako sa pagtanggap niyo sakin."
    
    h "Teka bakit, saan ka ba pupunta?"
    
    hide mc
    "..." "(The time machine starts, [mc] suddenly disappears. He wonders where he should go next as he travel through spacetime.)"
    hide pule
    mc "Hala teka lang, saan nanaman ako dadalhin neto? Saan na naman ang susunod kong destinasyon?"
    
    "..." "([sub_pronoun2] and the time machine fades into existence.)"

    jump chapter_4