
import re

from hoverkeyboard.layer import Layer

def _get_key_sections(key_definitions):
    key_sections=[]
    key_section_pattern=r"([0-9]\.[0-9]+),([0-9]\.[0-9]+):"
    
    last_section_index=0
    raw_splits=re.split(key_section_pattern,key_definitions)
    raw_splits=[split for split in raw_splits if split != ""]
    centers=[[float(raw_splits[i]),float(raw_splits[i+1])] for i in range(0,len(raw_splits),3)]

    return raw_splits[2::3],centers


def _fill_layers_with_actions(layer_list,key_definitions):
    layer_names = [layer.name for layer in layer_list]

def _get_layer_list(layer_definitions):
    layer_list = []
    layer_name_pattern=re.compile(r"([a-zA-Z0-9]+):>")
    for line in layer_definitions:
        match = layer_name_pattern.match(line)
        if match:
            layer_name = match.group(1)
            layer_list.append(Layer(layer_name,len(layer_list),None))

def parse(file:str):
    keyboard_definition = None
    layer_definitions = None 
    key_definitions=None
    sections=[key_definitions,layer_definitions,keyboard_definition]
    last_section=0
    last_section_index=0
    for line_index,line in enumerate(file):
        if line.startswith("#-"):
            section=sections[last_section]
            section=file[last_section_index:line_index]
            last_section_index=line_index+1
            last_section+=1

    layer_list = _get_layer_list(layer_definitions)


