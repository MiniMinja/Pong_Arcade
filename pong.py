import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

WALL_SCALE = 40

PADDLE_SCALE = 3
PADDLE_SPEED = 10

BALL_SCALE = .05
BALL_SPEED = 3

class MyGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.running = True

    def setup(self):
        self.all_sprites = arcade.SpriteList()

        self.paddle_left = arcade.Sprite("paddle.png", PADDLE_SCALE)
        self.paddle_left.center_x = SCREEN_WIDTH/8
        self.paddle_left.center_y = SCREEN_HEIGHT/2
        self.all_sprites.append(self.paddle_left)

        self.ball = arcade.Sprite("ball.png", BALL_SCALE)
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        self.ball.change_x = -BALL_SPEED
        self.all_sprites.append(self.ball)

        self.top_wall = arcade.Sprite("wall1.png", WALL_SCALE)
        self.top_wall.center_x = SCREEN_WIDTH/2
        self.top_wall.center_y = SCREEN_HEIGHT + WALL_SCALE / 2
        self.bottom_wall = arcade.Sprite("wall1.png", WALL_SCALE)
        self.bottom_wall.center_x = SCREEN_WIDTH/2
        self.bottom_wall.center_y = -WALL_SCALE/2

        self.all_sprites.append(self.top_wall)
        self.all_sprites.append(self.bottom_wall)


    def moveAll(self):
        self.paddle_left.center_y += self.paddle_left.change_y
        self.ball.center_x += self.ball.change_x
        self.ball.center_y += self.ball.change_y

    def on_draw(self):
        if self.running:
            arcade.start_render()
            self.all_sprites.draw()

    def update(self, delta_time):
        if self.running:
            # self.physics_engine_paddle.update()
            # self.physics_engine_ball.update()
            self.moveAll()

            #check for collisions on paddle left and paddle right
            pl_hit = arcade.geometry.check_for_collision_with_list(self.paddle_left, self.all_sprites)
            if self.top_wall in pl_hit:
                self.paddle_left.center_y = self.top_wall.center_y - self.top_wall.height/2 - self.paddle_left.height / 2
            if self.bottom_wall in pl_hit:
                self.paddle_left.center_y = self.bottom_wall.center_y + self.bottom_wall.height / 2 + self.paddle_left.height / 2
            if self.ball in pl_hit:
                self.running = False


    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.paddle_left.change_y = PADDLE_SPEED
        elif key == arcade.key.DOWN:
            self.paddle_left.change_y = -PADDLE_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.paddle_left.change_y = 0
        elif key == arcade.key.DOWN:
            self.paddle_left.change_y = 0

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
