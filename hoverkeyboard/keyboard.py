from typing import List, Set
from hoverkeyboard.action import Action, ActionField
from hoverkeyboard.button import PolygonButton

from hoverkeyboard.layer import Layer, LayerName


class Keyboard:
    def __init__(self, number_of_keys:int ,layer_names:List[LayerName],
                    pre_action: Action = None,
                    post_action: Action = None,
                    action: Action = None,
                    activation_time: int = 500,
                    name: str = "Keyboard"

                 ):
        self.active_layer = layer_names[0]
        self.name = name
        self.number_of_keys = number_of_keys
        self.layer_names=layer_names
        self.layers:Set[Layer] = {layer_name:Layer(layer_name,i,self) for i,layer_name in enumerate(layer_names)}
        

        self.pre_action:Action  = pre_action
        self.post_action:Action = post_action
        self.action:Action      = action

        
        self.activation_time = activation_time

    def set_key_action(self, layer_name:str,key_index:int,action: Action):
        assert layer_name in self.layer_names
        self.layers[layer_name].set_key_action(key_index,action)


    def key_pressed(self, key_index:int):
        print("key press "+str(key_index))

    def set_active_layer(self, layer_name: str):
        layer=self.layers[layer_name] 
        layer.activate()
    
    def get_key_action(self,key_index:int):
        return self.layers[self.active_layer].get_action(key_index)

    def derive_action_field(self,key_index:int,field_name:ActionField):
        active_layer_actions = self.layers[self.active_layer].get_action(key_index)
        if active_layer_actions and active_layer_actions.get_field(field_name):
            return active_layer_actions.get_field(field_name)
        

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
    