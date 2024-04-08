# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eliezer", color="#c8c8ff")
define h = Character("Hans", color="#b47643c7")

# The game starts here.

label start:

    "Game Starting"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show boy at left

    # These display lines of dialogue.s

    e "This is the main script file"

    hide boy

    show girl at right
    h "You will now move to the chapter 1 script file"
    hide girl

    call chapter_1

    show boy at left
    with dissolve
    e "You are back at the main script file"

    menu repeatMain:
        e "Repeat from Game Start?"
        "Yes":
            jump start
        "No":
            e "..."

    e "Game End"

    # This ends the game.

    return
