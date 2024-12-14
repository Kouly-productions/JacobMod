init python:
    menu_trans_time = 1

    splash_message_default = "Hav en terning klar."

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    Movie(size=(config.screen_width, config.screen_height), play="videos/funOpening.webm", loop=True)


image menu_bg_evil:
    topleft
    Movie(size=(config.screen_width, config.screen_height), play="videos/openingEvil.webm", loop=True)

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.40)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 100
    ycenter 500
    zoom 0.58
    menu_art_move(0.58, 750, 0.38)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 220
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.38)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1150
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 0.80)
    
image menu_art_eddy:
    subpixel True
    "gui/menu_art_eddy.png"
    xcenter 400
    ycenter 480
    zoom 1.00
    menu_art_move(1.00, 1000, 0.50)

image menu_art_ayano:
    subpixel True
    "gui/menu_art_ayano.png"
    xcenter 400
    ycenter 490
    zoom 1.00
    menu_art_move(1.00, 1000, 0.45)

image menu_art_akira:
    subpixel True
    "gui/menu_art_akira.png"
    xcenter 460
    ycenter 490
    zoom 1.00
    menu_art_move(1.00, 1000, 0.45)

image menu_art_sakura:
    subpixel True
    "gui/menu_art_sakura.png"
    xcenter 320
    ycenter 490
    zoom 1.00
    menu_art_move(1.00, 1000, 0.45)

image menu_art_foxy:
    subpixel True
    "gui/menu_art_foxy.png"
    xcenter 1180
    ycenter 500
    zoom 0.90
    menu_art_move(1.00, 1000, 0.45)
    
image menu_art_toyFreddy:
    subpixel True
    "gui/menu_art_toyFreddy.png"
    xcenter 1100
    ycenter 470
    zoom 1.00
    menu_art_move(1.00, 1000, 0.55)

image menu_art_baldi:
    subpixel True
    "gui/menu_art_baldi.png"
    xcenter 1000
    ycenter 500
    zoom 0.90
    menu_art_move(1.00, 1000, 0.45)

image menu_art_freddy:
    subpixel True
    "gui/menu_art_freddy.png"
    xcenter 900
    ycenter 470
    zoom 1.00
    menu_art_move(1.00, 1000, 0.55)

image menu_art_squidward:
    subpixel True
    "gui/menu_art_squidward.png"
    xcenter 780
    ycenter 500
    zoom 1.00
    menu_art_move(1.00, 1000, 0.45)

image menu_art_gf:
    subpixel True
    "gui/menu_art_gf.png"
    xcenter 1000
    ycenter 350
    zoom 1.00
    menu_art_move(1.00, 1000, 0.50)

image menu_art_helpy:
    subpixel True
    "gui/menu_art_helpy.png"
    xcenter 250
    ycenter 430
    zoom 1.00
    menu_art_move(1.00, 1000, 0.60)

image menu_art_bg:
    subpixel True
    "gui/menu_art_bg.png"
    xcenter 170
    ycenter 530
    zoom 1.00
    menu_art_move(1.00, 1000, 0.40)

image menu_art_n_evil:
    subpixel True
    "gui/menu_art_n_evil.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.38)

image menu_art_s_evil:
    subpixel True
    "gui/menu_art_s_evil.png"
    xcenter 350
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.48)

image menu_art_shikuza_evil:
    subpixel True
    "gui/menu_art_shikuza_evil.png"
    xcenter 950
    ycenter 400
    zoom 1.00
    menu_art_move(1.00, 1000, 0.50)

image menu_art_ayano_evil:
    subpixel True
    "gui/menu_art_ayano_evil.png"
    xcenter 700
    ycenter 490
    zoom 1.00
    menu_art_move(1.00, 1000, 0.55)

image menu_art_akira_evil:
    subpixel True
    "gui/menu_art_akira_evil.png"
    xcenter 530
    ycenter 490
    zoom 1.00
    menu_art_move(1.00, 1000, 0.55)

image menu_art_sakura_evil:
    subpixel True
    "gui/menu_art_sakura_evil.png"
    xcenter 850
    ycenter 490
    zoom 1.00
    menu_art_move(1.00, 1000, 0.55)

image menu_nav:
#    "gui/overlay/main_menu_dark.png"
#    menu_nav_movex
    pass

image menu_logo:
#    "gui/logo_dark.png"
#    subpixel True
#    xcenter 240
#    ycenter 120
#    zoom 0.60
#    menu_logo_move
    pass

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

label splashscreen:
    python:
        process_list = []
        currentuser = ""

        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass

            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)

                    if user:
                        currentuser = user
            except:
                pass


    if config.version != persistent.oldversion:
        $ restore_relevant_characters()
        $ persistent.oldversion = config.version
        $ renpy.save_persistent()

    $ basedir = config.basedir.replace('\\', '/')

    if persistent.autoload:
        jump autoload

    $ config.allow_skipping = False

    show white

    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default

    #$ config.main_menu_music = audio.t1

    #$ renpy.music.play(config.main_menu_music)

    $ starttime = datetime.datetime.now()

    show intro with Dissolve(0.5, alpha=True)

    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())

    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)

    show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)

    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())

    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)

    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())

    $ config.allow_skipping = True

    return

label autoload:

    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen

            del _old_game_menu_screen

        if "_old_history" in globals():
            _history = _old_history

            del _old_history

        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if renpy.get_return_stack():
        $ renpy.pop_call()

    jump expression persistent.autoload

label before_main_menu:

    #$ config.main_menu_music = audio.t1

    return

label readonly:

    scene black

    "The game cannot be run because you are trying to run it from a read-only location."

    "Please copy the DDLC application to your desktop or other accessible location and try again."

    $ renpy.quit()

    return

