#Sound Assets
#Visual Assets - Physical
image black:
    "#000"

image red:
    "#ff0000"

image blue:
    "#0004ae"

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
    pause 1.0
    "images/klubot_loading1.png"
    pause 1.0
    "images/klubot_loading2.png"
    pause 1.0
    "images/klubot_loading3.png"
    pause 1.0
    repeat

image klubot calc:
    "images/klubot_calc0.png"
    pause 0.2
    "images/klubot_calc1.png"
    pause 0.2
    repeat

image klubot sad:
    "images/klubot_sad"

# Textual Assets
define k = Character("KLUB07", color = "#ff0000", what_font="fonts/league_orbitron/Orbitron Medium.otf")
define w = Character("Mecha Wahoo", color = "#ff0000", what_font="fonts/league_orbitron/Orbitron Medium.otf")
define c = Character("Coach Tito", color = "#ff0000") #Terry Francona
define f = Character("Flo", color = "#0004ae")
define t = Character("TIGER Goon", color = "#008066")

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
    show text "Chapter 1: Indians Assemble" with fade
    with Pause(2)
    hide text
    k "ayy lmao"
    show klubot calc at right with moveinright
    k "ayy lmao"

    show text "Chapter 1: Indians Assemble" with fade
    with Pause(2)
    hide text

    show text "Chapter 2: Stealing Third Bass" with fade
    with Pause(2)
    hide text

    show text "Chapter 1: Indians Assemble" with fade
    with Pause(2)
    hide text

    show text "Chapter 3: Cyahoga Catastrophy" with fade
    with Pause(2)
    hide text

    show text "Chapter 4: Indians IPA" with fade
    with Pause(2)
    hide text

    show text "Chapter 5: Mysterious Handsom Batter" with fade
    with Pause(2)
    hide text

    show text "Chapter 6: Three Reich's You're Out!" with fade
    with Pause(2)
    hide text

    show text "Chapter 7: Christmas in Cleveland" with fade
    with Pause(2)
    hide text

    show text "Chapter 8: Sweeping Detroit" with fade
    with Pause(2)
    hide text

    return

# Pregame Splashscreen
label splashscreen:
