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
define c = Character("Coach", color = "#ff0000")
define p = Character("Player", color = "#ff0000")
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
    show bass at right with dissolve
    with Pause(2)
    hide text
    scene black
    stop music
    show text "An nonspecific orchestra in Cleveland - Midnight." with dissolve
    with Pause(2)
    hide text
    with Pause(2)
    hide bass with moveoutleft
    "???: Hehehe! I've stollen the bases and now I'm stealing the bass'es!"
    "???: With this Europe will surely fall to us using the magical bass powers!"
    scene blue with dissolve
    show coach at right with moveinright
    c "Recruit!"
    c "We have a situation!"
    c "A non-specfic orchestra located in Cleveland Ohio has lost their only bass."
    c "The T.I.G.E.R. agents from Detroit are almost certainly behind this!"
    c "This is an infiltration mission to the heart of Detroit city to recover the bass and our bases."
    c "I need you to come with me and be stealthy as possible."
    menu:
        c "Are you a brave enough boy to go with me?"
        "Heck yes!":
            c "That's what I like to hear!"
        "Heck no!":
            c "Too bad, we are out of options."
            c "If we do not recover this bass Europe will totally fall to the space aliens!"
            c "Let's go!"
    scene black with dissolve
    show text "Thirty minutes later..." with dissolve
    with Pause(2)
    hide text with dissolve
    scene detroit with dissolve
    show bass
    show coach at right with moveinright
    c "We're here!"
    c "Look there it is!"
    show tiger happy at left with moveinleft
    t "HOW ARE YOU GENTLEMEN?"
    c "Oh no! A T.I.G.E.R. agent!"
    t "OH YES!"
    t "ALL YOUR BASS ARE BELONG TO US."
    c "I'm gonna take him out! Recruit you distract him!"
    hide coach with moveoutleft
    menu:
        "How will you distract the T.I.G.E.R.?"
        "Tell him a joke!":
            p "What did the T.I.G.E.R. Agent say to the Indians Mecha?"
            t "I DON'T KNOW?"
            show coach mecha at right with moveinright
            show tiger sad at left
            t "OH NO! I DIDN'T KNOW!"
            c "{i}Oh yes!{/i}"
            hide tiger sad with vpunch
        "Romance him!":
            p "T.I.G.E.R. senpai I..."
            p "I love you."
            t "SHUCKS!"
            t "I LOVE YOU TOO!"
            t "BUT I HAVE A GREATER LOVE!"
            p "What's that?"
            t "EVIL!"
            p "{i}Good point!{/i}"
            show coach mecha at right with moveinright
            show tiger sad at left
            t "OH NO! YOU RUSED ME!"
            c "{i}Oh yes!{/i}"
            hide tiger sad with vpunch
    c "Let's steal the bass back and get out of here!"

    scene black with dissolve
    show text "Chapter 3: Cuyahoga Catastrophy" with dissolve
    with Pause(2)
    hide text

    scene black with dissolve
    show text "Chapter 4: Indians IPA" with dissolve
    with Pause(2)
    hide text

    scene black with dissolve
    show text "Chapter 5: Mysterious Handsome Batter" with dissolve
    with Pause(2)
    hide text

    scene black with dissolve
    show text "Chapter 6: Three Reich's You're Out!" with dissolve
    with Pause(2)
    hide text

    scene black with dissolve
    show text "Chapter 7: Christmas in Cleveland" with dissolve
    with Pause(2)
    hide text

    scene black with dissolve
    show text "Chapter 8: Sweeping Detroit" with dissolve
    with Pause(2)
    hide text

    return

# Pregame Splashscreen
label splashscreen:
