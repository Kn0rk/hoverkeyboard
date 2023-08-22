from typing import List

from hoverkeyboard.button import PolygonButton


class Layer: 
    def __init__(self, name: str, buttons: List[PolygonButton]):
        self.name = name
        self.buttons = buttons
    
    def activate(self):
        for button in self.buttons:
            button.draw()
        