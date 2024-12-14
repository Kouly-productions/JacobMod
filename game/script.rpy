label start:
    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True
    
    call ch1_main from _call_ch1_main
    call ch2_main from _call_ch2_main
    call ch3_main from _call_ch3_main
    call ch4_main from _call_ch4_main
    call ch5_main from _call_ch5_main