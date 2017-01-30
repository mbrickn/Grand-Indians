#Sound Assets
#Visual Assets - Physical
image black:
    "#000"

image red:
    "#2f191b"

image blue:
    "#091336"

image logo:
    "images/logo.png"

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
    "images/klubot_sad.png"

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

image klubot pitch mode:
    "images/klubot_loading0.png"
    pause 1.0
    "images/klubot_loading1.png"
    pause 1.0
    "images/klubot_loading2.png"
    pause 1.0
    "images/klubot_loading3.png"
    pause 1.0
    block:
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

image wahoo fight:
    "images/wahoo_pose0.png"
    pause 0.8
    "images/wahoo_pose1.png"
    pause 0.8
    repeat

image tiger robot:
    "images/tiger_robot.png"

image tiger dead:
    "images/tiger_robot_dead.png"

image tiger happy:
    "images/tiger_happy.png"

image able:
    "images/tiger_b1.png"

image cain:
    "images/tiger_b2.png"

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
define i = Character("Cleveland Indians", color = "#ff0000")
define tt = Character("The Tribe", color = "#ff0000")
define q = Character("???", color = "#008066")
define t = Character("TIGER Goon", color = "#008066")
define ts = Character("TIGER Goons", color = "#008066")
define t1 = Character("TIGER Bro #1", color = "#008066")
define t2 = Character("TIGER Bro #2", color = "#008066")
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

label chapter1:
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
    show coach with easeinright
    c "As you're aware the T.I.G.E.R.s have been moving in on Progressive Field."
    c "At our disposal is me, my men, Robot KLUB07 here, and only one of you."
    c "You're a big guy so go get them, Tiger!"
    hide coach with easeoutleft

label chapter2:
    show text "Chapter 2: Stealing Third Bass" with dissolve
    with Pause(2)
    hide text
    scene black
    show bass at right with dissolve
    stop music
    show text "An nonspecific orchestra in Cleveland - Midnight." with dissolve
    hide text(2)
    with Pause(2)
    hide bass with easeoutleft(2)
    q "Hehehe! I've stolen the bases and now I'm stealing the bass'es!"
    q "With this Europe will surely fall to us using the power of this magical bass!"
    scene blue with dissolve
    show coach at right with easeinright
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
    show coach at right with easeinright
    c "We're here!"
    c "Look there it is!"
    show tiger happy at left with easeinleft
    t "HOW ARE YOU GENTLEMEN?"
    c "Oh no! A T.I.G.E.R. agent!"
    t "OH YES!"
    t "ALL YOUR BASS ARE BELONG TO US."
    c "I'm gonna take him out! Recruit you distract him!"
    hide coach with easeoutleft
    menu:
        "How will you distract the T.I.G.E.R.?"
        "Tell him a joke!":
            p "What did the T.I.G.E.R. Agent say to the Indians Mecha?"
            t "I DON'T KNOW?"
            show coach mecha at right with easeinright
            show tiger sad at left
            t "OH NO! I DIDN'T KNOW!"
            c "{i}Oh yes!{/i}"
            hide tiger sad with vpunch
        "Romance him!":
            p "T.I.G.E.R. senpai I...{nw}"
            p "T.I.G.E.R. senpai I love you."
            t "SHUCKS!"
            t "I LOVE YOU TOO!"
            t "BUT I HAVE A GREATER LOVE!"
            p "What's that?"
            t "EVIL!"
            p "{i}Good point!{/i}"
            show coach mecha at right with easeinright
            show tiger sad at left
            t "OH NO! YOU RUSED ME!"
            c "{i}Oh yes!{/i}"
            t "I AM NOT STRONG ENOUGH TO DESTROY YOUR MECHA BIKE"
            hide tiger sad with vpunch
    c "Let's steal the bass back and get out of here!"
    scene black with dissolve
    show text "Thirty minutes later..." with dissolve
    with Pause(2)
    hide text with dissolve
    scene cleveland with dissolve
    show coach with easeinright
    c "Looks like we swept them!"
    menu:
        "What do you think?"
        "Yes":
            c "Team! Get in the robot! I've got a bad feeling about this!"
        "No":
            c "Team! Get in the robot! I've got a bad feeling about this!"

label chapter3:
    scene cleveland with dissolve
    show text "Chapter 3: Cuyahoga Catastrophy" with dissolve
    with Pause(2)
    hide text
    "The City of Cleveland, home of the Cleveland Indians!"
    show cleveland fire
    "Oh no!"
    show able at right with easeinleft
    show cain at left with easeinright
    ts "OH YES!"
    t1 "YO BRO WE LIT THE CUYAHOGA ON FIRE {i}AGAIN!{/i}"
    t2 "NOW CLEVELANDERS WILL {i}HAVE{/i} TO MOVE TO DETROIT!"
    t2 "HOW'S IT FEEL BRO?"
    t1 "FEEL'S GOOD!"
    t2 "THAT'S GOOD!"
    t1 "THAT'S EVIL!"
    t2 "FEEL'S EVIL!"
    t1 "BRO!"
    t2 "BRO!"
    show coach wheelie with easeinright
    c "Cut{nw}" with Pause(1, hard=True)
    c "That{nw}" with Pause(1, hard=True)
    c "Out{nw}" with Pause(1, hard=True)
    show coach mecha
    t1 "BRO..."
    t2 "BRO?"
    hide cain with vpunch
    t2 "Bro!"
    hide able with vpunch
    c "I took them out, but the river is still on fire."
    c "You can't fight fire with a mecha!"
    i "Yes we can coach!"
    i "Everyone get in the robot."
    hide coach with easeoutleft
    show wahoo fight with easeinright
    i "Tomahawk strike!"
    scene cleveland
    show coach at right with easeinright
    c "Great work team! The fire is gone!"
    c "But how did the city get repaired after the fire?"
    show flo at left with easeinleft
    f "With the power of {a=https://www.progressive.com/homeowners/}Progressive Insurance{/a} of course!"
    c "Thanks for rebuilding Cleveland Flo!"
    f "No problem!"

label chapter4:
    scene cleveland with dissolve
    show text "Chapter 4: Indians IPA" with dissolve
    with Pause(2)
    hide text

    show coach at right with easeinright
    show tiger happy at left with easeinleft

    c "Man Cleveland has some good drinks."
    t "YOU SAID IT!"
    t "ALMOST MAKES ME {i}NOT{/i} WANT TO DESROY CLEVELAND!"
    c "{i}Yeah.{/i}"

label chapter5:
    scene red with dissolve
    show tiger happy at left
    show klubot at right
    show text "Chapter 5: Mysterious Handsome Batter" with dissolve
    with Pause(2)
    hide text
    t "HEY KLUBOT."
    t "I AM {i}NOT{/i} A T.I.G.E.R. SPACE ALIEN."
    k "Is that so?"
    t "I HEARD THAT YOU PITCH FOR THE CLEVELAND INDIANS"
    show klubot sad at right
    k "Fishiness Levels = 9999\%"
    k "{i}Lie mode activate!{i}"
    k "{i}No{/i}"
    scene klubot head with fade
    k "I was born in a lab in 1986."
    k "Although the Regan Administration created me"
    k "to target Soviet millitary installations..."
    k "I had a greater love..."
    k "Baseball."
    k "My targeting algorithms were made to aim missiles..."
    k "But nothing can beat a well executed launching of a baseball."
    k "It is thanks to baseball that I am able to experience emotion."
    k "Joy."
    k "Happiness."
    k "Love."
    t "YO! I HEARD YOU MONOLOGUING YOU LIAR!"
    k "LOVE."
    k "I LOVE BASEBALL!"
    k "PITCH MODE ACTIVATE!"
    scene red with fade
    show tiger sad at left
    show klubot pitch mode at right
    k "{i}HEATING BASEBALL ANTI-AIRCRAT MINIGUN{/i}"
    t "ARE YOU ACTUALLY GOING TO DO ANYTHING OR CAN I JUST GO LIGHT THE RIVER ON FIRE AGAIN?{nw}"
    k "BEGONE T.I.G.E.R. SPACE ALIEN"
    k "{i}Fire!{/i}" with Pause(1)
    t "{i}OH NO!{/i}{nw}"
    hide tiger with hpunch
    k "Oh {i}yes!{/i}"
    k "Calculating current target position"
    show klubot surprise at right
    k "Target has been blasted to lunar orbit."
    k "Calculated orbit period..."
    k "1000 years"
    show klubot at right
    k "Pitch status: Success."
    k "Emotion state: Excited."
    
label chapter6:
    scene black with dissolve
    show text "Chapter 6: Three Reich's You're Out!" with dissolve
    with Pause(2)
    hide text
    show hitler with fade
    h "Wow, today sure is a good day to be evil!"
    show tiger sad at left with easeinleft
    t "WOW, YOU ARE LAME.{w} AND NOT EVEN IN A COOL WAY."
    show coach at right with easeinright
    c "For once I agree with you, vile T.I.G.E.R. space alien."
    c "Only someone as scummy as Hitler would come back to life just to destroy America's pastime - Baseball"
    t "TRUCE?"
    c "TRUCE"
    show coach mecha at right with hpunch
    with Pause(1)
    hide hitler with hpunch
    t "TRUCE OVER"
    c "Go back to space, you space alien!"

label chapter7:
    scene black with dissolve
    show text "Chapter 7: Christmas in Cleveland" with dissolve
    with Pause(2)
    hide text
    show coach with fade
    c "I am thankful for chewing gum!"
    hide coach with fade
    show klubot with fade
    k "I AM THANKFUL FOR BASEBALL!"
    hide klubot with fade
    show klubot with fade
    k "I AM THANKFUL FOR BASEBALL!"
    hide klubot with fade
    show klubot glitch with fade
    k "I AM THANKFUL FOR BASEBALL!"
    hide klubot with fade
    show flo with fade
    f "I am thankful for affordable insuracnce!"
    hide flo with fade
    show tiger with fade
    t "I AM THANKFUL FOR EVIL"
    hide tiger with fade

label chapter8:
    scene black with dissolve
    show tiger robot at left
    show wahoo fight at right
    show text "Chapter 8: Sweeping Detroit" with dissolve
    with Pause(2)
    hide text
    hide wahoo fight with easeoutright
    with Pause(2)
    show tiger robot dead with hpunch
    with Pause(2)

label chapter9:
    scene black with dissolve
    show text "Epilogue!" with dissolve
    with Pause(2)
    hide text
    show text "You win!" with easeinleft
    with Pause(2)
    hide text with easeoutright
    show text "Special Thanks to..." with easeinleft
    with Pause(2)
    hide text with easeoutright
    show text "The Cleveland Indians" with easeinleft
    with Pause(2)
    hide text with easeoutright
    show text "Progressive Insurance" with easeinleft
    with Pause(2)
    hide text with easeoutright
    show text "Tech Elevator" with easeinleft
    with Pause(2)
    hide text with easeoutright
    show text "/u/RiverRatRambler" with easeinleft
    with Pause(2)
    hide text with easeoutright
    show text "/u/Debadenedacro" with easeinleft
    with Pause(2)
    hide text with easeoutright
    show text "/u/kgmoome" with easeinleft
    with Pause(2)
    hide text with easeoutright
    show text "Grand Indians: The Directors Cut - High Quality" with easeinleft
    with Pause(2)
    hide text with easeoutright
    return

# Pregame Splashscreen
label splashscreen:
    "This game contains flashing imagery."
    "Stay safe! If you have conditions such as epilepsy do not play this game!"
    "If you aren't sure you are safe playing such a game but somehow must play this game..."
    "Please disable the animations before you play the game."
    "You know what game doesn't have flashing imagery?"
    "A Cleveland Indians game at Progressive Stadium!"
    "Are you blind and having a friend read this for you?"
    "Press your V key to enable speech synthesis! (Avalible on select Operating Systems)"
    "That said have fun!"
    show logo with dissolve
    "Signed - The Developers"

