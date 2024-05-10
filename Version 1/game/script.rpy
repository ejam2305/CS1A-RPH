# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Character declaration

define mc = Character("[mcName]", color="#ffc8c8", voice_tag="[mcGender]")
define mcInner = Character("[mcName]", color="", voice_tag="[mcGender]")
define AI = Character("AI", color="#c8c8ff", voice_tag="ai")

define pronoun = " " #he she
define sub_pronoun1 = " " #his her
define sub_pronoun2 = " " #him


# Transition declaration

define fadetoWhite = Fade(1, 1, 1, color="#FFF")
define fadetoBlack = Fade(1, 1, 1, color="#000")


# Preferences declaration

default preferences.text_cps = 20



label start:
    centered "{cps=2.5}{b}Lorem Ipsum{nw=2}"
    show text "{b}Lorem Ipsum{nw}" as text1
    hide text1 with fadetoBlack

    centered "{cps=2.5}{b}{color=#FFF}Dolor Sit Amet{nw=2}"
    show text "{b}Dolor Sit Amet" as text1
    hide text1 with fadetoBlack

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





    "???" "You will now move to the chapter 1 script file"

    call chapter_1

    show boy at left
    with dissolve
    mc "You are back at the main script file"

    menu repeatMain:
        mc "Repeat from Game Start?"
        "Yes":
            jump start
        "No":
            mc "..."

    mc "Game End"

    # This ends the game.

    return



label ask_gender:
    "???" "Do you remember your gender?"

    menu:
        "Respond with?"

        "I'm a male":
            python:
                mcGender = "mcMale"
                pronoun = "he"
                sub_pronoun1 = "his"
                sub_pronoun2 = "him"
            call skip

        "I'm a female":
            python:
                mcGender = "mcFemale"
                pronoun = "she"
                sub_pronoun1 ="her"
                sub_pronoun2 ="her"
            call skip

        "Stop ignoring my questions.":
            call ask_gender
    
#Debugging purposes
label skip:
    menu:
        "Choose Chapter"

        "Chapter 1":
            call chapter_1

        "Chapter 2":
            call chapter_2

        "Chapter 3":
            call chapter_3

        "Chapter 4":
            call chapter_4

        "Chapter 5":
            call chapter_5
    return