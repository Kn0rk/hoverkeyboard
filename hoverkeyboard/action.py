import logging
import os
import re
import tempfile
import time
import uuid
from subprocess import Popen, PIPE, STDOUT


from enum import Enum


class ActionField(Enum):
    """Docstring for ActionField."""
    LABEL = 1
    PRE_ACTION = 2
    ACTION = 3
    POST_ACTION = 4
    

class Action:
    @staticmethod
    def from_definition(definition):
        argument_pattern = r"""(\{[^\{\}]*\})"""
        arguments = re.findall(argument_pattern, definition, re.MULTILINE)
        assert len(arguments) == 1
        argument = arguments[0]
        argument_dict=eval(argument)
        # everything after the  argument is the command
        command = definition.replace(argument, "")  
        action_split_pattern=r"""(pre|post|action)"""
        action_split=re.split(action_split_pattern,command) 
        action_split=[split for split in action_split if not split.isspace() and split != ""]
        pre_action = None
        post_action = None
        action = None
        for i in range(0,len(action_split),2):
            match action_split[i]:
                case "pre":
                    pre_action = action_split[i+1]
                case "post":
                    post_action = action_split[i+1]
                case "action":
                    action = action_split[i+1]
                case _:
                    raise ValueError("Unknown action type: " + action_split[i])
        label="UNLABELED"
        if "label" in argument_dict:
            label = argument_dict["label"]
        return Action(label,action,pre_action,post_action)
        


    """docstring for Action."""
    def __init__(self, text=None, talon_command:str=None,pre_action:str=None,post_action:str=None):
        self.text = text
        self.talon_comand = talon_command
        self.pre_action = pre_action
        self.post_action = post_action

    def get_field(self,field:ActionField):
        if field == ActionField.LABEL:
            return self.text
        elif field == ActionField.PRE_ACTION:
            return self.pre_action
        elif field == ActionField.ACTION:
            return self.talon_comand
        elif field == ActionField.POST_ACTION:
            return self.post_action
        else:
            raise ValueError("Unknown field: " + str(field))



    def perform_action(self):
        key = self.text
        #os.system("xdotool key "+key)
        com = self.talon_comand.replace("'","\\'")

        p = Popen(['/home/knork/.talon/bin/repl'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        stdout_data = p.communicate(input=self.talon_comand.encode())[0]
        print(stdout_data)

        return
    #suenofgacuskijdqvyphebrhello how are you  s   
        print("Performing action: " + self.text + " with comand: " + self.talon_comand)
        folder=tempfile.gettempdir()
        # check if folder exists
        if not os.path.exists(folder+"/hoverkeyboard"):
            os.makedirs(folder+"/hoverkeyboard")
        # check if folder is empty
        if os.listdir(folder+"/hoverkeyboard") != []:
            for file in os.listdir(folder+"/hoverkeyboard"):
                if os.path.getmtime(folder+"/hoverkeyboard/"+file) < time.time()-5:
                    logging.warning("Old file is still present in temporary folder this might indicate that the command was not executed properly")
                    os.remove(folder+"/hoverkeyboard/"+file)
                else:
                    # TODO: wait for file to be deleted
                    logging.warning("File is still present in temporary folder this might indicate that the command was not executed properly")                
                
        # create file.look
        with open(folder+"/hoverkeyboard/"+str(uuid.uuid4()),"w") as f:
            f.write(self.talon_comand)

        os.system("xdotool key F10")

    