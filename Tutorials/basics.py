from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        # nested inner grid 

        self.inner = GridLayout()
        self.inner.cols = 2

        self.inner.add_widget(Label(text='Name:'))
        self.name = TextInput(multiline=False)
        self.inner.add_widget(self.name)

        self.inner.add_widget(Label(text='Email:'))
        self.email = TextInput(multiline=False)
        self.inner.add_widget(self.email)

        self.inner.add_widget(Label(text='Phone:'))
        self.phone = TextInput(multiline=False)
        self.inner.add_widget(self.phone)

        self.add_widget(self.inner)

        self.submit = Button(text='Submit', font_size=32)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)


    def pressed(self, instance):
        name = self.name.text
        email = self.email.text
        phone = self.phone.text
        print("pressed", name, email, phone)

        self.name.text = ''
        self.email.text = ''
        self.phone.text = ''


class MyApp(App):
    def build(self):
        # return Label(text="This is my first app!")
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()