label ch1_main:
    show screen top_right_text
    show screen day_text
    $ current_line = 1
    $ helpy_owe = 50000
    $ playerMoney = 1000
    $ currentDay = "Mandag"
    default sayoriFirstChosen = False
    default natsukiFirstChosen = False
    $ persistent.current_day = 1

    # Rekter:
    # Golden Freddy

    # Lærer:
    # Glitchtrap
    # Foxy
    # Blækvard
    # Springtrap
    # Freddy
    # Toy Freddy
    # Baldi

    # Elever:
    # Eddy
    # Helpy
    # MC
    # Sakura
    # Ayano
    # Akira
    # Sayori
    # Natsuki
    # Funtime Foxy
    # Vanny
    # Svampebob
    # Yuri
    # Monika
    # Fnaf world Bonnie

    stop music fadeout 2.0

    scene bg bedroom
    with dissolve_scene_full

    play music t8

    "Fortæl mig dit navn"

    $ mc = renpy.input("")

    "MANDAG"

    "Du vågner op i din seng, du kigger op i luftet og glæder dig til dagen i dag"

    return