# Kivy Pong
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector


# PongBall class - for the game ball
class PongBall(Widget):
    # velocity of the ball
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use the ball.velocity
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # move function will move the ball one step. used to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()

