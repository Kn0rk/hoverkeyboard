from typing import List
from hoverkeyboard.button import PolygonButton
from hoverkeyboard.keyboard import Keyboard


def save_keyboard(keyboard:Keyboard, centers:List[float],file_name: str = "keyboard.board"):
    output = ''
    output += f'name={keyboard.name} keys\n'
    output += f'activation_time = {keyboard.activation_time}\n'
    output += "\n#- LAYER DEFINITIONS\n"
    for layer in keyboard.layers:
        output += f"""\t{layer.name}:>"""

        output += r"{"  + "}\n"
        if layer.default_pre_action:
            output+=r"\t\tpre:\n"
            output += f"\t\t{layer.default_pre_action.get_definition()}\n"
        if layer.action:
            output+=r"\t\taction:\n"
            output += f"\t\t{layer.action.get_definition()}\n"
        if layer.post_action:
            output+=r"\t\tpost:\n"
            output += f"\t\t{layer.post_action.get_definition()}\n"

    output += "\n#- KEY DEFINITIONS\n"
    for key_index in range(0,keyboard.number_of_keys):
        output += f'{centers[key_index][0]},{centers[key_index][1]}:\n'
        for layer in keyboard.layers:
            output += f'\t{layer.name}:\n'
            if layer.get_action(key_index):
                if layer.get_action(key_index).get_pre_action(False):
                    output += f'\t\tpre:\n'
                    output += f'\t\t\t{layer.key_pre_actions[key_index].get_definition()}\n'
                if layer.get_action(key_index).get_action(False):
                    output += f'\t\taction:\n'
                    output += f'\t\t\t{layer.key_actions[key_index].get_definition()}\n'
                if layer.get_action(key_index).get_post_action(False):              
                    output += f'\t\tpost:\n'
                    output += f'\t\t\t{layer.key_post_actions[key_index].get_definition()}\n'

    with open(file_name, 'w') as f:
        f.write(output)

