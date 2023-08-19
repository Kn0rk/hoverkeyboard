import logging
import os
import tempfile
import time
import uuid
from subprocess import Popen, PIPE, STDOUT


class Action:
    """docstring for Action."""
    def __init__(self, text, comand:str=None):
        self.text = text
        if comand is None:
            self.comand = r"print('No comand given')"
        else:
            self.comand = comand

    def get_comand_name(self):
        return self.comand

    def get_action_name(self):
        return self.text

    def perform_action(self):
        key = self.text
        #os.system("xdotool key "+key)
        com = self.comand.replace("'","\\'")

        p = Popen(['/home/knork/.talon/bin/repl'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        stdout_data = p.communicate(input=self.comand.encode())[0]
    

        return
    #suenofgacuskijdqvyphebrhello how are you  s   
        print("Performing action: " + self.text + " with comand: " + self.comand)
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
            f.write(self.comand)

        os.system("xdotool key F10")

    