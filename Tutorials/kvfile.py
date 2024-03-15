from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class NewGrid(GridLayout):
    def __init__(self):
        pass

class JournalieApp(App):
    def build(self):
        return NewGrid()


if __name__ == '__main__':
    JournalieApp().run()