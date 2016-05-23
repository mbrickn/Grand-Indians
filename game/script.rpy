#Sound Assets
#Visual Assets - Physical
image black:
    "#000"

image red:
    "#2f191b"

image blue:
    "#091336"

image team:
    "images/team.png"

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

image klubot head:
    "images/klubot_head.png"

image klubot glitch:
    "images/klubot_glitch.png"

image klubot surprise:
    "images/klubot_surprise.png"

image klubot sad:
    "images/klubot_sad"

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

image coach:
    "images/coach0.png"
    pause 0.8
    "images/coach0.png"
    pause 0.8
    repeat

image coach wheelie:
    "images/coach_wheelie.png"

image coach mecha:
    "images/coach_mecha0.png"
    pause 0.8
    "images/coach_mecha1.png"
    pause 0.8
    repeat

image tiger robot:
    "images/tiger_robot.png"

image tiger dead:
    "images/tiger_robot_dead.png"

image tiger happy:
    "images/tiger_happy.png"

image tiger sad:
    "images/tiger_sad.png"

image hitler:
    "images/hitler.png"

# Textual Assets
define k = Character("KLUB07", color = "#ff0000", what_font="fonts/league_orbitron/Orbitron Medium.otf")
define w = Character("Mecha Wahoo", color = "#ff0000", what_font="fonts/league_orbitron/Orbitron Medium.otf")
define c = Character("Coach Tito", color = "#ff0000")
define f = Character("Flo", color = "#0004ae")
define t = Character("TIGER Goon", color = "#008066")
define tr = Character("TIGER Robot", color = "#008066")

# Initiate pregame settings
init python:
    config.developer = False # Set to False at Release
    config.debug = True # Set to False at Release
    config.rollback_enabled = False # Disabled due to UX concerns

# The game starts here.
label start:
    scene cleveland
    stop music

    show text "Chapter 1: Indians Assemble" with dissolve
    with Pause(2)
    hide text with dissolve

    show text "The year is 2016." with dissolve
    with Pause(2)
    show text "The alien invasion started in Detroit." with dissolve
    with Pause(4)
    show text "Spreading quickly across the world all cities fell." with dissolve
    with Pause(4)
    show text "Except Cleveland Ohio." with dissolve
    with Pause(2)
    show text "Knowing of the treachery of alien T.I.G.E.R. spies present in Detroit." with dissolve
    with Pause(4)
    show text "The CLEVELAND INDIANS had long served as an anti-alien defence force." with dissolve
    with Pause(4)
    show text "Can you help them strike out some alien baddies?" with dissolve
    with Pause(4)
    hide text with dissolve

    scene blue with dissolve
    c "Welcome recruit!"
    show coach with moveinright
    c "As you're aware the T.I.G.E.R.s have been moving in on Progressive Field."
    c "At our disposal is me, my men, Robot KLUB07 here, and only one of you."
    c "You're a big guy so go get them, Tiger!"
    hide coach with moveoutleft

    show text "Chapter 2: Stealing Third Bass" with dissolve
    with Pause(2)
    hide text
    scene black
    stop music
    show text "An nonspecific orchestra in Cleveland - Midnight." with dissolve
    with Pause(2)
    hide text
    with Pause(2)
    show bass with moveinleft
    hide bass with moveoutright
    "???: Hehehe! I've stollen the bases and now I'm stealing the bass'es!"
    with Pause(2)

    show text "Chapter 3: Cuyahoga Catastrophy" with dissolve
    with Pause(2)
    hide text

    show text "Chapter 4: Indians IPA" with dissolve
    with Pause(2)
    hide text

    show text "Chapter 5: Mysterious Handsom Batter" with dissolve
    with Pause(2)
    hide text

    show text "Chapter 6: Three Reich's You're Out!" with dissolve
    with Pause(2)
    hide text

    show text "Chapter 7: Christmas in Cleveland" with dissolve
    with Pause(2)
    hide text

    show text "Chapter 8: Sweeping Detroit" with dissolve
    with Pause(2)
    hide text

    return

# Pregame Splashscreen
label splashscreen:
