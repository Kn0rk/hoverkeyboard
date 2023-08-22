from typing import List
from hoverkeyboard.action import Action
from hoverkeyboard.button import PolygonButton

from layer import Layer


class Keyboard:
    def __init__(self, layers: List[Layer]):
        self.layer = {}

    def set_layer(self, layer_name: str):
        layer=self.layer[layer_name] 
        layer.activate()

def load_board_file(root, canvas,file):
    with open(file,"r") as f:
        data = f.read()
    lines = data.split('\n')
    layer_name = None
    setup = None
    command = None
    
    layer = {}


    for line in lines:
        if line.startswith("0") and line.endswith(':'):
            x = float(line.split(',')[0])
            y = float(line[:-1].split(',')[1])
            layer_name=None


        elif line.endswith(":"):
            button= create_button(canvas,layer_name,setup,command)
            if button:
                layer[layer_name].append(button)
            setup = []
            command = []
            layer_name = line[:-1].lstrip()
            if layer_name not in layer:
                layer[layer_name]=[]
        elif line.endswith('-'):
            setup=command
            command=[]
        command.append(line)
        
def create_button(canvas,layer_name,setup,command):
    action=Action()
    PolygonButton(canvas,[],[x,y],)
    