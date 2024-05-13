# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Character declaration

define mc = Character("[mcName]", color="#ff5252", voice_tag="mc.voice")
default mcGender = "mcFemale"

init python:
    def genderVoice(id):
        global mcGender
        voice_tag = _voice.tag
        if voice_tag == "mc.voice":
            return "voice/{}/{}.mp3".format(mcGender, id)
        return "voice/{}.mp3".format(id)
        
    config.auto_voice = genderVoice

define mcInner = Character("[mcName] (Inner)", color="#573939", voice_tag="mc.voice")
define AI = Character("AI", color="#6565ff", voice_tag="ai")

default pronoun = ""
default sub_pronoun1 = ""
default sub_pronoun2 = ""

# Transition declaration

define fadetoWhite = Fade(1, 1, 1, color="#FFF")                    # Usage Example
define fadetoBlack = Fade(1, 1, 1, color="#000")                    # show [image] with fadetoWhite

define eyeopen = ImageDissolve("eye.png", 1.0, 16, reverse=False)
define eyeclose = ImageDissolve("eye.png", 1.0, 16, reverse=True)

transform fadeInSlow:       # Usage Example
    alpha 0.0               # show [image] at fadeInSlow
    linear 1.0 alpha 10.0
    alpha 10.0

transform fadeOutSlow:      # Usage Example
    alpha 10.0               # show [image] at fadeOutSlow
    linear 1.0 alpha 0.0    # pause(1)
    alpha 0.0

transform large:
    xysize (900, 900)

define config.tag_transform = {"mc": large}

transform flipOn:
    xzoom -1.0

transform flipOff:
    xzoom 1.0

image bg gray animated:
    "bg gray" with dissolve
    pause(2)
    "bg gray 2" with dissolve
    pause(2)
    repeat

label slowTextfade(info):                   # Usage Example
    centered "{cps=9}{b}[info]{nw=2}"     # call slowTextfade("Enter Text Here")      
    show text "{b}[info]{nw=1}" as text1:
        alpha 1.0
        linear 0.5 alpha 0.0
    pause(0.5)
    hide text1
    return

# Preferences declaration

default preferences.text_cps = 35

label start:

    call slowTextfade("Can You Change History?")

    call slowTextfade("Or Will History Change You?")

    pause(1)

    play music "SCP-x7x.mp3" volume 0.25 fadein 1.0 fadeout 1.0

    scene bg gray animated with fadetoBlack

    "???" "It's nice to meet you."
    "???" "You must still be confused right after waking up."
    "???" "Do you remember your name?"

    menu:
        "Respond with?"

        "Yes":
            python:
                mcName = renpy.input("What should you be called? ")
                mcName = mcName.strip()
                if not mcName:
                    mcName = "Hans"
                mcName = mcName.capitalize()

        "Hans...":
            python:
                mcName = "Hans"

    pause(1)

    show mc speaking 2 at left, large, flipOn

    mc "Wait, who am I talking to right now?"

    show mc thinking 1

    "???" "You'll find out in due time."

    "???" "For now, focus on answering my questions."

    show mc speaking 2

    mc "That doesn't answer my question. Where am I?"

    show mc thinking 1

    $ first = True
    call ask_gender

    "???" "Now, my next question is-{nw}"

    "???" "I'm sorry.{nw=1}"

    "???" "It seems that our time is running out.{nw=1}"
    
    "???" "I wish you good luck in your journey.{nw=1}"

    show mc thinking 3


    scene bg black with fadetoBlack
    
    call skip

    call chapter_2

    call chapter_3

    call chapter_4

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

        "I'm a female":
            python:
                mcGender = "mcFemale"
                pronoun = "she"
                sub_pronoun1 ="her"
                sub_pronoun2 ="her"

        "Stop ignoring my questions." if first == True:
            $ first = False
            call ask_gender

    return
    
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

    return