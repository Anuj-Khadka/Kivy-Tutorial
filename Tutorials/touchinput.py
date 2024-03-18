from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Touch(Widget):
    btn = ObjectProperty(None)

    def on_touch_move(self, touch):
        print("You touched", touch) 
    def on_touch_down(self, touch):
        print("You down")
        self.btn.opacity = 0.9
        self.btn.color = 0.2, 0.4, 0.7, 0.9
    def on_touch_up(self, touch):
        print("You up")
        self.btn.opacity = 1
        self.btn.color = 1,1,1,1

class TouchInput(App):
    def build(self):
        return Touch()
    
if __name__ == '__main__':
    TouchInput().run()