import witcheryco.cli.terminal as term
from witcheryco.cli.terminal import pal, log
from abc import ABC, abstractmethod

class Action:
    def __init__(self, action, name: str, msg_acted: str):
        self.name = name
        self.action = action
        self.msg_acted = msg_acted
    
    def get_name(self):
        return self.name
    
    def get_action(self):
        return self.action
    
    def act(self):
        term.log_action(self.msg_acted)
        self.action()

class Usable(ABC):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def get_actions(self):
        pass

class Place:
    def __init__(self, name, descrip, *usables):
        self.name = name
        self.descrip = descrip
        self.usables = list(usables)
    
    def add_usable(self, usable: Usable):
        self.usables += [usable]
    
    def get_usables(self):
        return self.usables

    def get_name(self):
        return self.name
    
    def get_descrip(self):
        return self.descrip

class Player:
    def __init__(self, at: Place):
        self.at = None
        self.move_to(at)
    
    def get_at(self):
        return self.at
    
    def prompt_act(self):
        actions = []

        # get all possible actions that the player could do in their location
        for usable in self.at.get_usables():
            actions += usable.get_actions()
        
        # convert action objects to tuples of (name_of_choice, function to execute) that can be interpreted by prompt_choice_tree()
        action_as_choice = [(action.get_name(), action.act) for action in actions]

        term.prompt_choice_tree('Actions:', menu_list=action_as_choice, coerce=True)

    
    def move_to(self, destin: Place):
        self.at = destin
        term.log(
            '----------------\nYou are in {name}, {descrip}.'.format(
                name=pal.yellow.bg_default(destin.get_name()),
                descrip=destin.get_descrip()
            )
        )

        term.log('You see: ' + ", ".join(
            [usable.get_name() for usable in self.at.get_usables()])
        )