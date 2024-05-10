# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Character declaration

define mc = Character("[mcName]", color="#ffc8c8", voice_tag="[mcGender]")
define mcInner = Character("[mcName]", color="", voice_tag="[mcGender]")
define AI = Character("AI", color="#c8c8ff", voice_tag="ai")

# Transition declaration

define fadetoWhite = Fade(1, 1, 1, color="#FFF")
define fadetoBlack = Fade(1, 1, 1, color="#000")

transform fadeInSlow:       # Usage Example
    alpha 0.0               # show [image] at fadeInSlow
    easein 1.0 alpha 1.0

transform fadeOutSlow:      # Usage Example
    alpha 1.0               # show [image] at fadeOutSlow
    easein 1.0 alpha 0.0    # pause(1)
                            # hide [image]

label slowTextfade(info):                   # Usage Example
    centered "{cps=2.5}{b}[info]{nw=2}"     # call slowTextfade("Enter Text Here")
    show text "{b}[info]{nw=2}" as text1        
    hide text1 with fadetoBlack
    return

# Preferences declaration

default preferences.text_cps = 20



label start:
    call slowTextfade("Lorem Ipsum")

    call slowTextfade("Dolor Sit Amet")

    pause(2)

    "???" "It's nice to meet you."
    "???" "You must still be confused right after waking up."
    "???" "Do you remember your name?"

    menu:
        "Respond with?"

        "Yes":
            python:
                mcName = renpy.input("What should you be called? ")
                if(mcName == ""):
                    mcName = "Self"
            
        "No":
            "???" "That's too bad."
            python:
                mcName = "Self"


    show bg white with fadetoBlack

    pause(1)

    mc "Wait, who am I talking to right now?"

    "???" "You'll find out in due time."

    "???" "For now, focus on answering my questions."

    mc "That doesn't answer my question. Where am I?"

    call ask_gender

    "???" "I'm sorry but our time is running out."
    
    "???" "I wish you good luck in your journey"

    show bg black with fadetoBlack

    call chapter_1

    call chapter_2

    call chapter_3

    call chapter_4

    call chapter_5

    return



label ask_gender:
    "???" "Do you remember your gender?"

    menu:
        "Respond with?"

        "I'm a male":
            python:
                mcGender = "mcMale"

        "I'm a female":
            python:
                mcGender = "mcFemale"

        "Stop ignoring my questions.":
            call ask_gender
    
    return