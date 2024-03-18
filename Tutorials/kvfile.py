from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btnAct(self):
        print(f"name: {self.name.text}\n Email: {self.email.text}")
        self.name.text = ''
        self.email.text = ''

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()