from typing import List, Set
from hoverkeyboard.action import Action
from hoverkeyboard.button import PolygonButton

from layer import Layer


class Keyboard:
    def __init__(self, layers: List[Layer],number_of_keys: int,
                    pre_action: Action = None,
                    post_action: Action = None,
                    action: Action = None,
                    activation_time: int = 500,
                    name: str = "Keyboard"

                 ):
        self.layers = layers
        self.active_layer = 0
        self.name = name
        self.number_of_keys = number_of_keys

        self.pre_action:Action  = pre_action
        self.post_action:Action = post_action
        self.action:Action      = action

        
        self.activation_time = activation_time

    
    def set_layer(self, layer_name: str):
        layer=self.layers[layer_name] 
        layer.activate()
    
    def get_key_actions(self,key):
        pre,action,post = self.layers[self.active_layer].get_actions(key)
        layer_index = self.active_layer-1
        while layer_index >= 0:
            if pre and action and post:
                break
            lower_pre,lower_action,lower_post = self.layers[layer_index].get_actions(key)
            if pre == None:
                pre = lower_pre
            if action == None:
                action = lower_action
            if post == None:
                post = lower_post

        if pre == None:
            pre = self.pre_action
        if action==None:
            action = self.action
        if post == None:
            post = self.post_action
        return pre,action,post

    


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
    