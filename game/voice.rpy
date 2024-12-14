init python:
    renpy.music.register_channel("voice", "voice", loop=False)
    
    def play_voice(character, line):
        if isinstance(line, int):
            voice_file = f"audio/voices/{character}/{line:03d}.ogg"
        else:
            voice_file = f"audio/voices/{character}/{line}.ogg"
        if renpy.loadable(voice_file):
            renpy.sound.play(voice_file, channel="voice")
        else:
            pass