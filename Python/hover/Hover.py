from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.uix.widget import Widget

class HoverBehavior(object):
    #class die bepaalt hoe elementen reageren als de muis
    #er overheen hovert
    hovered = BooleanProperty(False)
    _hoverable = True #boolean

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    #bepalen of de muis op een widget hovert
    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        
        if hasattr(self, "focus") and self.focus:
            return

        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        
        self.hovered = inside
