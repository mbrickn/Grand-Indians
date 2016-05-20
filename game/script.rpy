#Sound Assets
#Visual Assets - Physical
image black:
    "#000"

image danger:
    "images/danger.png"

image cleveland:
    "images/cleveland.png"

image cleveland fire:
    "images/cleveland_fire.png"

image detroit:
    "images/detroit.png"

image bass:
    "images/bass.png"

image title:
    "images/title0.png"
    pause 1.0
    "images/title1.png"
    pause 1.0
    repeat

# Doesn't actually repeat for some reason.
#image spinball:
#    "images/spinball.png"
#    block:
#        linear 5 rotate -360
#        repeat

#Visual Assets - Characters

image flo:
    "images/flo.png"

image klubot:
    "images/klubot.png"

image klubot loading:
    "images/klubot_loading0.png"
    pause 1.5
    "images/klubot_loading1.png"
    pause 1.5
    "images/klubot_loading2.png"
    pause 1.5
    "images/klubot_loading3.png"
    pause 1.5
    repeat

# Textual Assets

# Initiate pregame settings
init python:
    config.developer = False # Set to False at Release
    config.debug = True # Set to False at Release
    config.rollback_enabled = False # Disabled due to UX concerns

# The game starts here.
label start:
    scene black
    stop music
    show text "The year is 2016." with fade
    with Pause(2)
    show text "The alien invasion started in Detroit." with fade
    with Pause(2)
    show text "Spreading quickly across the world all cities fell." with fade
    with Pause(2)
    show text "Except Cleveland Ohio." with fade
    with Pause(2)
    show text "Knowing of the treachery of alien T.I.G.E.R. spies present in Detroit." with fade
    with Pause(2)
    show text "The CLEVELAND INDIANS had long served as an anti-alien defence force." with fade
    with Pause(2)
    show text "Can you help them strike out some alien baddies?" with fade
    with Pause(2)
    hide text
    show klubot loading
    "ayy lmao"
    return

# Pregame Splashscreen
label splashscreen:
