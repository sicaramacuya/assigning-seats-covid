from GrandStand import GrandStand
from BoxStand import BoxStand
from TelescopicStand import TelescopicStand
from Pods import Pod

class Coliseum():
    
    def __init__(self, name):
        self.name = name
        self.stands = list() # A list of all stands inside the coliseum

    def get_name(self):
        """This method will return the name."""
        return self.name

    def set_name(self, name):
        """This method will change the name."""
        self.name = name

    def get_stands(self):
        """This method will return the list of stands inside the coliseum."""
        return self.stands
    
    def show_stands(self):
        """This will show all stands in the stands list."""

        for i in self.stands:
            print(i.name)
            i.show_pods()

    def add_stand_to_coliseum(self, stand):
        """This method will add a new stand inside the colisum list of stands."""
        self.stands.append(stand)

    def remove_stand_of_coliseum(self, stand_id):
        """This method will remove stand from stands list that contain all the stands objects. The parameter should be the pods id."""
        found_stand = False

        # Loop through each stand in our stands list.
        for i in self.stands:

            # If we find them, remove them from the list.
            if i.id == stand_id:
                self.stands.remove(i)
                # set our indicator to True
                found_stand = True
       
        # If we looped through our list and did not find our stand, the indicator would never get change, so return 'Pod not found!'
        if not found_stand:
            print(f'Stand not found!')



if __name__ == "__main__":

    # Create a Coliseum that will have three Stands and each
    # of them will have some pods

    # Coliseum
    coliseum_humacao = Coliseum('Coliseum of Multiple Uses from Humacao')

    # Stands
    lateral_grand_stand_west = GrandStand('Lateral Grand Stand - West', 42, 17, 3)
    lateral_grand_stand_east = GrandStand('Lateral Grand Stand - East', 42, 17, 3)
    telescopic_stand_bottom = TelescopicStand('Telescopic Stand - South', 28, 11, 2)

    # Pods
    lateral_grand_stand_west.create_pod()
    lateral_grand_stand_west.create_pod()
    lateral_grand_stand_west.create_pod()

    lateral_grand_stand_east.create_pod()
    lateral_grand_stand_east.create_pod()
    lateral_grand_stand_east.create_pod()

    telescopic_stand_bottom.create_pod()
    telescopic_stand_bottom.create_pod()
    telescopic_stand_bottom.create_pod()

    # Cheking for pods...
    # print(f'{lateral_grand_stand_west.get_name()}')
    # lateral_grand_stand_west.show_pods()
    # print(f'{lateral_grand_stand_east.get_name()}')
    # lateral_grand_stand_east.show_pods()
    # print(f'{telescopic_stand_bottom.get_name()}')
    # telescopic_stand_bottom.show_pods()

    # Adding stands to stadium
    coliseum_humacao.add_stand_to_coliseum(lateral_grand_stand_west)
    coliseum_humacao.add_stand_to_coliseum(lateral_grand_stand_east)
    coliseum_humacao.add_stand_to_coliseum(telescopic_stand_bottom)

    # Cheking of what the stadium is made of
    coliseum_humacao.show_stands()