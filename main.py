def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

music.play(music.string_playable("- - - - - - - - ", 120),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    pass
basic.forever(on_forever)
