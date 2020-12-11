from Coliseum import Coliseum
from Stand import Stand
from GrandStand import GrandStand
from BoxStand import BoxStand
from TelescopicStand import TelescopicStand
from Pods import Pod
from helper_module import print_newline

class Terminal():

    def __init__(self, name):   
        self.name = name
        self.jump_to_next_pod = False

    def create_coliseum(self):
        """This method will create a new coliseum and return it. Name must be a string."""
        
        name = input('Whats the name for the Coliseum?\n- ')
        return Coliseum(name)

    def show_coliseum_report(self, coliseum):
        """This method will print and extensive report of the coliseum."""

        quantity_stands = 0
        quantity_pods = 0
        quantitiy_avaliable_seats_people_can_sit_coliseum = 0
        quantity_seats_occupied_coliseum = 0
        quantity_people_seated_coliseum = 0
        quantity_buffer_seats_for_rows_people_sit = 0
        full_seat_coliseum_capacity = 0 # This is the seat capacity for the rows people can actually seat of the whole coliseum. Independently if they are occupied or not.
        buffer_seats_coliseum = 0

        for stand in coliseum.stands:
            quantity_stands += 1
            for pod in stand.pods:
                quantity_pods += 1
                quantitiy_avaliable_seats_people_can_sit_coliseum += pod.get_seats_avaliable_pod()
                quantity_seats_occupied_coliseum += pod.get_seats_occupied_pod()
                quantity_people_seated_coliseum += pod.get_people_on_seats()
                quantity_buffer_seats_for_rows_people_sit += pod.get_buffer_seats_pod() 
                full_seat_coliseum_capacity += pod.get_total_seat_capacity_pod()
                buffer_seats_coliseum += pod.get_total_buffer_seats_pod()

        print(f'The {coliseum.name} have:\n')
        print(f'\tSTANDS:')
        print(f'\t\tQuantity of Stands:\t\t\t\t\t{quantity_stands}\n')
        print(f'\tPODS:')
        print(f'\t\tQuantity of Pods:\t\t\t\t\t{quantity_pods}')
        print(f'\tSEATS:')
        print(f'\t\tColiseum Capacity (Including Buffer Rows):\t\t{full_seat_coliseum_capacity}')
        print(f'\t\tBuffer Seats (Including Buffer Rows):\t\t\t{buffer_seats_coliseum}')
        print(f'\t\tAvaliable Seats:\t\t\t\t\t{quantitiy_avaliable_seats_people_can_sit_coliseum}')
        print(f'\t\tPeople Seated:\t\t\t\t\t\t{quantity_people_seated_coliseum}')
        print(f'\t\tBuffer Seats (Excluding Buffer Rows):\t\t\t{quantity_buffer_seats_for_rows_people_sit}')
        print(f'\t\tOccupied Seats:\t\t\t\t\t\t{quantity_seats_occupied_coliseum}')

    def show_coliseum_layout(self, coliseum):
        """This method will display a more readable layout of the coliseum"""

        quantity_stands = 0

        quantitiy_avaliable_seats_people_can_sit_coliseum = 0
        quantity_seats_occupied_coliseum = 0
        quantity_people_seated_coliseum = 0

        quantity_buffer_seats_for_rows_people_sit = 0 # Buffer Seats (Excluding Buffer Rows)
        buffer_seats_coliseum = 0

        # Collecting Information
        for stand in coliseum.stands:
            quantity_stands += 1
            for pod in stand.pods:
                quantitiy_avaliable_seats_people_can_sit_coliseum += pod.get_seats_avaliable_pod()
                quantity_seats_occupied_coliseum += pod.get_seats_occupied_pod()
                quantity_people_seated_coliseum += pod.get_people_on_seats()
                quantity_buffer_seats_for_rows_people_sit += pod.get_buffer_seats_pod() 
                buffer_seats_coliseum += pod.get_total_buffer_seats_pod()

        # Displaying Information
        print(f'Coliseum: {coliseum.name}')
        print(f'\tStands: {quantity_stands}')
        for stand in coliseum.stands:
            print(f'\t\tCategory: {stand.stand_category}')
            print(f'\t\t\tName: {stand.name}')
            for pod in stand.pods:
                print(f'\t\t\t\tPod Id: {pod.get_id()}')
                print("\t\t\t\t\t" + str(pod.pod).replace('\n','\n\t\t\t\t\t'))

    def seatting_people(self, coliseum, amount_people_sitting):
        """This method will sit people inside the coliseum."""

        for stand in coliseum.stands:
            for pod in stand.pods:

                self.jump_to_next_pod = False

                # Here we are passing the terminal object to manipulate the attribute jump_to_next_pod from inside the method of the Pod type object.
                pod.sitting_people_from_terminal(amount_people_sitting, self)
                
                # In the case the pod was full this value was going to be changed inside sitting_people_from_terminal() and allow the program to move to the next pod.
                if self.jump_to_next_pod == True:
                    pass
                
                else:
                    if amount_people_sitting > 1:
                        print(f'The group of {amount_people_sitting} is seated.')

                    elif amount_people_sitting == 1:
                        print(f'The person was seated.')

                    print_newline()

                    return

        print(f'Is not possible to sit {amount_people_sitting} in the entire coliseum!')

    def create_grand_stand(self):
        """This method will prompt user to create a GrandStand object and return it."""
        
        name = input('Whats the name for the GrandStand?\n- ')
        row = int(input('How many rows the entire stand will have?\n- '))
        column = int(input('How many columns the entire stand will have?\n- '))
        num_pods = int(input('How many pods you want?\n- '))
        return GrandStand(name, row, column, num_pods)

    def create_box_stand(self):
        """This method will promt user to create a BoxStand object and return it."""

        name = input('Whats the name for the BoxStand?\n- ')
        row = int(input('How many rows the entire stand will have?\n- '))
        column = int(input('How many columns the entire stand will have?\n- '))
        num_pods = int(input('How many pods you want?\n- '))
        return BoxStand(name, row, column, num_pods)

    def create_telescopic_stand(self):
        """This method will promt user to create a TelescopicStand object and return it."""

        name = input('Whats the name for the TelescopicStand?\n- ')
        row = int(input('How many rows the entire stand will have?\n- '))
        column = int(input('How many columns the entire stand will have?\n- '))
        num_pods = int(input('How many pods you want?\n- '))
        return TelescopicStand(name, row, column, num_pods)

    def create_pod(self, row, column):
        """This method will create a new pod and return it."""

        # row = int(input('How many rows the Pod will have?\n- '))
        row = row
        # column = int(input('How many column the Pod will have?\n- '))
        column = column
        
        return Pod(row, column)

    def built_coliseum(self):
        """This method will prompt to built an entire coliseum and return it."""

        print(f'Lets built the Coliseum...')
        coliseum = self.create_coliseum()

        print(f'So, now...')
        amount = int(input((f'How many GrandStand you want?\n- ')))
        for _ in range(amount):
            # Creating and appending the grand stand to the coliseum.
            grand_stand = self.create_grand_stand()
            coliseum.add_stand_to_coliseum(grand_stand)

            # Creating and appending the pods to the grand stand.
            amount = grand_stand.num_pods
            for _ in range(amount):
                pod = self.create_pod(grand_stand.pod_rows, grand_stand.pod_columns)
                grand_stand.add_pod_to_stand(pod)    
        
        amount = int(input((f'How many BoxStand you want?\n- ')))
        for _ in range(amount):
            # Creating and appending the box stand to the coliseum.            
            box_stand = self.create_box_stand()
            coliseum.add_stand_to_coliseum(box_stand)

            # Creating and appending the pods to the box stand.
            amount = box_stand.num_pods
            for _ in range(amount):
                pod = self.create_pod(box_stand.pod_rows, box_stand.pod_columns)
                box_stand.add_pod_to_stand(pod)

        amount = int(input((f'How many TelescopicStand you want?\n- ')))
        for _ in range(amount):
            # Creating and appending the telescopic stand to the ccoliseum.
            telescopic_stand = self.create_telescopic_stand()
            coliseum.add_stand_to_coliseum(telescopic_stand)

            # Creating and appending the pods to the telescopic stand.
            amount = telescopic_stand.num_pods
            for _ in range(amount):
                pod = self.create_pod(telescopic_stand.pod_rows, telescopic_stand.pod_columns)
                telescopic_stand.add_pod_to_stand(pod)

        return coliseum



if __name__ == "__main__":
    
    # Creating a terminal.
    terminal_001 = Terminal('Terminnal 001')


    # Creating a coliseum.
    humacao_arena = terminal_001.built_coliseum()

    print(f'The coliseum has been created. Now you can start sitting people.\n\n\n')

    # Loop that only stop when user wants to quit.
    quit_terminal = False
    while quit_terminal == False:

        user_response = int(input(f'[1]\tFull Report\t\t[2]\tColiseum Layout\t\t[3]\tSeating People\t\t[9]\tQuit Terminal\n- '))

        # Show Full Report
        if user_response == 1:
            terminal_001.show_coliseum_report(humacao_arena)

        # Show Coliseum Layout
        elif user_response == 2:
            terminal_001.show_coliseum_layout(humacao_arena)

        # Seating People
        elif user_response == 3:
            amount_people_sitting = int(input(f'Whats the amount of people you want to sit?\n- '))
            terminal_001.seatting_people(humacao_arena, amount_people_sitting)

        # This will run when user wants to quit program.
        elif user_response == 9:
            quit_terminal = True

        # More space, more readable.
        print('\n\n\n')