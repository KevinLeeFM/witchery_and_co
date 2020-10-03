import witcheryco.cli.terminal as term
from witcheryco.cli.terminal import pal, log
from witcheryco.core.entities import *

version = '1.0'

player = None

class Door(Usable):
    def __init__(self, destin: Place, name='door'):
        super().__init__(name)
        self.destin = destin
    
    def get_actions(self):
        return [
            Action(
                self.enter,
                'Enter {name}'.format(name=self.name),
                'You entered {name} into {destin}'.format(
                    name=self.name,
                    destin=self.destin.get_name()
                )
            )
        ]
    
    def enter(self):
        global player
        player.move_to(self.destin)
    
def new_game():
    street_1 = Place('Wizarding Dr.', 'a rowdy and lively cobblestone street with wizards and witches abound')
    street_2 = Place('Magica St.', 'a rowdy and lively cobblestone street with wizards and witches abound. This looks like a commercial district')
    tavern = Place('Leaky Cauldron', 'a pub that\'s definitely not from Harry Potter')
    home = Place('your home', 'a modest but comfortable dwelling')
    home.add_usable(Door(street_1, name='front door'))
    street_1.add_usable(Door(home, name='your home\'s front door'))
    street_1.add_usable(Door(street_2, name='right to the street'))
    street_1.add_usable(Door(tavern, name='Leaky Cauldron'))
    street_2.add_usable(Door(street_1, name='left to the street'))
    tavern.add_usable(Door(street_1, name='exit to Leaky Cauldron'))

    global player
    player = Player(home)

    # main game loop
    while True:
        player.prompt_act()

def main():
    term.log(term.title('Witchery and Co.'), 'v. {version}'.format(version=version))
    term.prompt_choice_tree(
        '--- Menu ---',
        ('New game', lambda: new_game()),
        coerce=True
    )