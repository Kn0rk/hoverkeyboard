from typing import List
from hoverkeyboard.action import Action

from hoverkeyboard.button import PolygonButton


class Layer: 
    def __init__(self, name: str,index:int,keyboard,
                 pre_action: str = None,
                    post_action: str = None,
                    action: str = None,
                    activation_time: int = None,
                    key_actions: List[Action] = None,
                    key_pre_actions: List[Action] = None,
key_post_actions: List[Action] = None,
                 ):
        self.name = name
        self.index = index
        self.keyboard = keyboard
        self.pre_action:Action  = pre_action
        self.post_action:Action = post_action
        self.action:Action      = action
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
    
    def get_actions(self,key):
        pre = self.key_pre_actions[key]
        action = self.key_actions[key]
        post = self.key_post_actions[key]
        if pre == None:
            pre = self.pre_action
        if action  ==  None:
            action = self.action
        if post == None:
            post = self.post_action
        return pre,action,post 

        