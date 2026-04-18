import os
from kivy.app import App
from kivy.lang import Builder
from hover.HoverWidgets import HoverButton
from kivy.factory import Factory

Factory.register('HoverButton', cls=HoverButton)

class StakeApp(App):
    def build(self):
        kv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "GUIs", "HomeScreen.kv")
        return Builder.load_file(kv_path)

    
if __name__ == "__main__":
    StakeApp().run()