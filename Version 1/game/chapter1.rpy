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
            pause(1)

        "...":
            pause(1)

    ### -- WORK IN PROGRESS --

    AI "I see. Let me explain it for you."

    AI "You have been transported to a different timeline. While transporting, I lost my function to travel to another timeline."

    AI "The only way you can return is if you can obtain an artifact here in this timeline."

    hide mc left arm request

    mcInner "SHEESH!! Isn't that Hector? Hector Santos?!! The one responsible for the creation of Laguna Copperplate Inscription? I still remember him from one of our lessons in History. What is he doing here?"

    AI "To be able to restore my ability to timeleap you must acquire something from this timeline, it may be an analysis or a realization of historical accounts or an item from that point of time."

    mcInner "Since I saw Hector, doesn't it mean that I'm in the late 20th century? And this university…"
    
    mcInner "Since Hector was present in this university this must be the old Ateneo de Manila where Hector studies…"
    
    mcInner "The watch said that I must acquire something from this timeline, so I assume that Hector has something to do with that. But what will that be?"

    mcInner " I still don't know what's the item that I need to obtain from Hector, but whatever it is I need to be close to him ASAP, so that I can return to my own timeline. "

    ## play footstep sound

    show bg hallway request with fadetoBlack

    ## play footstep sound

    show hector request at fadeInSlow, left

    mcInner "Excuse me po, pwede po ba akong magtanong? I'm new po kasi sa bayang ito, at wala po akong matutuluyan RN. Can you help me ba? Kahit pansamantala lang po."

    hector " Anong bang lengguwahe ang yong pinagsasabi, kakaunti lamang ang naintindihan ko sa mga sinabi mo. Para naman sagutin ang iyong tanong, maari ka munang maki tuloy sa aming tahanan pansamantala."

    return