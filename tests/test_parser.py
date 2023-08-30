
import pytest
from hoverkeyboard.keyboard import Keyboard
from hoverkeyboard.layer import LayerName
from hoverkeyboard.parser import _fill_layers_with_actions, _get_key_sections, _get_layer_list, _get_sections, _set_layer_attributes


def test__get_key_sections():
    key_definitions = """0.28,0.15:
	        base:{}
               pre:
                print("xx section 1")
               action:
                    print('hoverkeyboard: No comand given')
        0.34,0.15:
	        base:{}
               pre:
                print("xx")
               action:
                    print('hoverkeyboard: No comand given')
        """
    key_sections,centers = _get_key_sections(key_definitions)
    assert len(key_sections) == 2
    assert len(centers) == 2
    assert centers[0] == pytest.approx([0.28,0.15])
    assert centers[1] == pytest.approx([0.34,0.15])
    assert "base:"in key_sections[0]
    assert "xx section 1"in key_sections[0]


def test__get_sections():
    lines = """#-KEYBOARD
        #-LAYERS
        base:>{var=1}
            pre:

    #-KEYS
        0.28,0.15:
            base:{}
               pre:
                print("xx section 1")
               action:
                    print('hoverkeyboard: No comand given')
        0.34,0.15:
            base:{}
               pre:
                print("xx")
               action:
                    print('hoverkeyboard: No comand given')
"""
    sections = _get_sections(lines)
    assert len(sections) == 3

def test__fill_layers_with_actions():
    key_definitions = ["""
            base:{"label":"test"}
               pre:
                print("xx section 1")
               action:
                    print('hoverkeyboard: No comand given')
            hover:{}
                pre:
                    print("xx")
        """,
        """
            base:{"label":"test2"}
               pre:
                print("xx section 1")
                action:
                    print('hoverkeyboard: No comand given')
                    """]
    layer_list = [
        LayerName("base"),
        LayerName("hover")
    ]
    centers = [[0.28,0.15],[0.34,0.15]]
    keyboard=Keyboard(2,layer_names=layer_list)
    _fill_layers_with_actions(keyboard,key_definitions,centers)
    assert keyboard.layers["base"].key_actions[0].text == "test"
    assert keyboard.layers["base"].key_actions[1].text == "test2"


def test__get_layer_list():
    layer_definition='\tbase:>{}\n\n'
    layer_list = _get_layer_list(layer_definition)
    assert layer_list == ["base"]

def test__set_layer_attributes():
    layer_definition='\tbase:>{}\n\n\tshift:>{"inherit_from":"base"}\n\n'
    keyboard=Keyboard(5,["base","shift"])
    _set_layer_attributes(keyboard,layer_definition)
    assert keyboard.layers["shift"].inherit_from == "base"
