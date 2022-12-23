# This is a game to press the A button when the sprite is near it.
sprite = game.create_sprite(2, 2)
def makeNewSprite(X,Y):
    spriteB = game.create_sprite(X, Y)
def on_button_pressed_a():
    if sprite.get(LedSpriteProperty.X) == 2:
        music.play_melody("A", 100)
        score_position = game.score()-1
        game.add_score(1)
        makeNewSprite(score_position,0)
        #score = game.score()
    else:
        music.play_melody("C", 500)
        game.game_over()
        def on_button_pressed_a2():
            pass
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_forever():
    sprite.move(1)
    if game.score() == 2:
        basic.pause(300)
    elif game.score() > 2:
         basic.pause(189.5498)
    else:
        basic.pause(500)
    sprite.if_on_edge_bounce()
basic.forever(on_forever)
