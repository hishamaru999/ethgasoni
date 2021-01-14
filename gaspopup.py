from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate .kv design file
Builder.load_file('popup.kv')


# Define class
class MyLayout(Widget):
    pass

class GasApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    GasApp().run()