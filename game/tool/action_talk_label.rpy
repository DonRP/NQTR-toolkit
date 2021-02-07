define talk_ch = None
default talk_image = None
default talk_end_image = None
# used in talk_menu, alliniterno there are the possible choices that you can make in a dialog with a certain ch
# is structured like this:
# 'alice'   :   [("Choice 1", "label_one"), ("Choice 2", "label_two")]
default talkch_choices = {}

label talk:
    if (talk_image != None):
        scene expression (talk_image)

    if(talk_ch == None):
        call error_label
        call screen room_navigation
    if(talk_ch == "alice"):
        mc "Ciao [a]"
        a "Ciao, mi dire qualcosa?"
    else:
        "Now is busy test later."
    call talk_menu

    jump talk_end

# Opens the choice menu, with the various dialogs you can currently do with a ch
label talk_menu:
    if (talk_ch in talkch_choices.keys()): 
        $ talk_choices = talkch_choices[talk_ch]
    else:
        $ talk_choices = []

    $ talk_choices.append((_("Back"), "talk_back"))
    $ menu_result = menu(talk_choices)
    $ del talk_choices
    jump expression menu_result
    return

# Best way to exit a dialogue
label talk_end:
    if (talk_end_image != None):
        scene expression (talk_end_image)

    call screen room_navigation

# Display a random phrase and then end the conversation
label talk_back:
    $ num = renpy.random.randint(1, 7)
    if num == 1:
        mc "OK, I'm off. See you."
    elif num == 2:
        mc "It's getting late. See you."
    elif num == 3:
        mc "Sorry, but I have to go now. Bye."
    elif num == 4:
        mc "Good talk. We should do this more often."
    elif num == 5:
        mc "I just remembered something. Gotta go! Bye."
    elif num == 6:
        mc "I won't keep you any longer. Bye."
    elif num == 7:
        mc "I was supposed to tell you something else.... But I don't remember."
        mc "Patience when it comes back to me I'll let you know, bye."

    $ del num
    jump talk_end
