# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The chapter starts here.

label chapter_1:
    "Chapter 1 start"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show girl at right

    # These display lines of dialogue.

    h "This is the chapter 1 script file"

    hide girl

    show boy at left

    e "This is where the rest of chapter 1 dialogue will go"

    hide boy

    show girl at right
    with dissolve

    menu repeatChapter1:
        h "Did you understand"
        "Yes":
            h "..."
        "No":
            h "Restarting chapter 1"
            jump chapter_1

    h "Chapter 1 end"

    hide girl
    # This closes the chapter 1 file and puts the player back in the main script file

    return