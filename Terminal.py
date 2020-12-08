from Coliseum import Coliseum
from Stand import Stand
from GrandStand import GrandStand
from BoxStand import BoxStand
from TelescopicStand import TelescopicStand
from Pods import Pod

class Terminal():

    def __init__(self, name):   
        self.name = name
        self.__built_coliseum_answers = list()
    
    def create_coliseum(self):
        """This method will create a new coliseum. Name must be a string."""
        
        name = input('Whats the name for the Coliseum?')
        return Coliseum(name)

    def create_grand_stand(self):
        """This method will prompt user to create a GrandStand object."""
        
        name = input('Whats the name for the GrandStand?')
        row = int(input('How many rows the hole stand will have?'))
        column = int(input('How many columns the stand will have?'))
        num_pods = int(input('How many pods you want?'))
        return GrandStand(name, row, column, num_pods)

    def create_box_stand(self):
        """This method will promt user to create a BoxStand object."""

        name = input('Whats the name for the BoxStand?')
        row = int(input('How many rows the hole stand will have?'))
        column = int(input('How many columns the stand will have?'))
        num_pods = int(input('How many pods you want?'))
        return BoxStand(name, row, column, num_pods)

    def create_telescopic_stand(self):
        """This method will promt user to create a TelescopicStand object."""

        name = input('Whats the name for the TelescopicStand?')
        row = int(input('How many rows the hole stand will have?'))
        column = int(input('How many columns the stand will have?'))
        num_pods = int(input('How many pods you want?'))
        return TelescopicStand(name, row, column, num_pods)

    def create_pod(self):
        """This method will create a new pod"""

        row = int(input('How many rows the Pod will have?'))
        column = int(input('How many column the Pod will have?'))
        return Pod(row, column)

    def built_coliseum(self):
        """This method will prompt to built an entire coliseum"""

        print(f'Lets built the Coliseum...')
        self.create_coliseum()

        print(f'So, now...')
        amount = int(input((f'How many GrandStand you want?')))
        for _ in range(amount):
            self.create_grand_stand()
        
        amount = int(input((f'How many BoxStand you want?')))
        for _ in range(amount):
            self.create_box_stand()

        amount = int(input((f'How many TelescopicStand you want?')))
        for _ in range(amount):
            self.create_telescopic_stand()

        print(f'Now for the pods')
        amount = int(input(f''))


if __name__ == "__main__":
    new_terminal = Terminal('Terminal')
    humacao_arena = new_terminal.create_coliseum()
    print(humacao_arena.get_name())

