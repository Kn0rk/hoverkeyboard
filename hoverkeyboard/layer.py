from typing import List, NewType
from hoverkeyboard.action import Action, ActionField

LayerName=NewType('LayerName',str)
LayerIndex=NewType('LayerIndex',int)
class Layer: 
    def __init__(self, name:LayerName,index:int,keyboard,
                 pre_action: str = None,
                    post_action: str = None,
                    action: str = None,
                    activation_time: int = None,
                    key_actions: List[Action] = None,
                    key_pre_actions: List[Action] = None,
                    key_post_actions: List[Action] = None,
                    inherit_from:LayerIndex=None
                 ):
        self.name:LayerName = name
        self.index = index
        self.keyboard = keyboard
        self.default_pre_action:Action  = pre_action
        self.post_action:Action = post_action
        self.action:Action      = action
        self.inherit_from:LayerIndex = inherit_from
        if key_actions is None:
            key_actions = [None for i in range(0,keyboard.number_of_keys)]
        assert len(key_actions) == keyboard.number_of_keys
        self.key_actions:List[Action] = key_actions
        
        if key_pre_actions == None:
            key_pre_actions = [None for i in range(0,keyboard.number_of_keys)]
        assert len(key_pre_actions) == keyboard.number_of_keys
        self.key_pre_actions:List[Action] = key_pre_actions

        if key_post_actions  ==  None:
            key_post_actions = [None for i in range(0,keyboard.number_of_keys)]
        assert len(key_post_actions) == keyboard.number_of_keys
        self.key_post_actions:List[Action] = key_post_actions


        self.activation_time = activation_time
    
    def set_key_action(self, key:int,action: Action):
        assert key < len(self.key_actions)
        self.key_actions[key] = action

    def get_field(self,field:ActionField):
        if field == ActionField.LABEL:
            return self.name
        elif field == ActionField.PRE_ACTION:
            return self.default_pre_action
        elif field == ActionField.ACTION:
            return self.action
        elif field == ActionField.POST_ACTION:
            return self.post_action
        else:
            raise ValueError("Unknown field: " + str(field))



    def get_action(self,key)->Action:
        return self.key_actions[key]

        