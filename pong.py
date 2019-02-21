import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

PADDLE_SCALE = 3

class MyGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.all_sprites = arcade.SpriteList()

        self.paddle_left = arcade.Sprite("paddle.png", PADDLE_SCALE)
        self.paddle_left.center_x = SCREEN_WIDTH/2
        self.paddle_left.center_y = SCREEN_HEIGHT/2

        self.all_sprites.append(self.paddle_left)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()

    def update(self, delta_time):
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
