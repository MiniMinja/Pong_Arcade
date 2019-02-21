import arcade

arcade.open_window(800, 600, "Simple Square")

arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
arcade.draw_rectangle_filled(100, 50, 30, 40, arcade.color.WHITE)
arcade.finish_render()

arcade.run()
