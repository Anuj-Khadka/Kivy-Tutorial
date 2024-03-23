from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.popup import PopUp
from kivy.uix.floatlayout import FloatLayout


class Widgets(Widget):
    pass

class PU(FloatLayout):
    pass

class PopUp(App):
    def build(self):
        return Widgets()

def showPopUp():
    pass    



if __name__ == '__main__':
    PopUp().run()