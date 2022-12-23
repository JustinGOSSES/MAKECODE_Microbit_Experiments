def on_forever():
    basic.show_icon(IconNames.SNAKE)
    basic.clear_screen()
    basic.pause(500)
    music.play_melody("A", 120)
    basic.show_icon(IconNames.STICK_FIGURE)
    basic.clear_screen()
    basic.pause(500)
basic.forever(on_forever)
#music.play_melody("C", 500)
def on_button_pressed_a():
    music.play_melody("C", 500)
def on_button_pressed_b():
    music.ring_tone(Note.C)
input.on_button_pressed(Button.A, on_button_pressed_a)
# music.ring_tone(Note.C)
# basic.forever(on_forever)
input.on_button_pressed(Button.B, on_button_pressed_b)
