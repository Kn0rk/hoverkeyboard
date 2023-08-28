
import re
from typing import List
from hoverkeyboard.keyboard import Keyboard

from hoverkeyboard.layer import Layer, LayerName

def _get_key_sections(key_definitions):
    """Returns a list of key sections and a list of the centers of the keys"""
    key_sections=[]
    key_section_pattern=r"([0-9]\.[0-9]+),([0-9]\.[0-9]+):"
    
    last_section_index=0
    raw_splits=re.split(key_section_pattern,key_definitions)
    raw_splits=[split for split in raw_splits if split != ""]
    centers=[[float(raw_splits[i]),float(raw_splits[i+1])] for i in range(0,len(raw_splits),3)]

    return raw_splits[2::3],centers


def _fill_layers_with_actions(keyboard:Keyboard,key_definitions,centers):
    layer_names = keyboard.layer_names
    pattern="("+"|".join(layer_names)+"):"
    layer_pattern=re.compile(pattern,re.MULTILINE)
    for key_index in range(0,keyboard.number_of_keys):
         
        key_definition,center=key_definitions[key_index],centers[key_index]
        layer_definitions=re.split(layer_pattern,key_definition)
        layer_definitions=[definition for definition in layer_definitions if not definition.isspace() ]
        for layer_name,layer_definition in zip(layer_definitions[::2],layer_definitions[1::2]):
            layer_index = layer_names.index(layer_name)
            print(layer_definition)

            #keyboard.set_key_action


def _get_layer_list(layer_definitions):
    layer_list:List[LayerName] = []
    layer_name_pattern=re.compile(r"([a-zA-Z0-9]+):>")
    for line in layer_definitions:
        match = layer_name_pattern.match(line)
        if match:
            layer_name = match.group(1)
            layer_list.append(layer_name)
    return layer_list
def _get_sections(lines):
    sections=re.split(r"#-",lines,flags=re.MULTILINE)
    sections=[section for section in sections if section != ""]
    assert len(sections) == 3
    return sections


def parse(file:str):
    keyboard_definition = None
    layer_definitions = None 
    key_definitions=None
    key_definitions,layer_definitions,keyboard_definition=_get_sections(file)
    layer_list:List[LayerName] = _get_layer_list(layer_definitions)
    keyboard=Keyboard(len(key_definitions),layer_list)
    key_sections,centers = _get_key_sections(key_definitions)


