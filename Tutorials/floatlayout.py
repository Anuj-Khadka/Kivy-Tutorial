from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

class MyFloat(App):
    def build(self):
        return FloatLayout() 

if __name__ == '__main__':
    MyFloat().run()