from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class LoginWindow(Screen):
    pass

class HomeWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("navigation.kv")



class Navigation(App):
    def build(self):
        return kv
    
if __name__ == '__main__':
    Navigation().run()