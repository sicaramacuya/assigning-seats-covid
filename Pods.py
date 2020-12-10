import numpy
import math
import helper_module


class Pod():
    """This class will create seats for people to sit down. Those seats are going to be called 'Pods'."""

    def __init__(self, row, column):
        """This constructur will create and store the attribute for a pod."""

        self.pod = self.create_pod(row, column)
        self.id = helper_module.generate_id()

    def show_pod(self):
        """This will display this pod."""

        print(self.pod)

    def create_pod(self, pod_row, pod_column):
        """It takes in two integer values; the number of rows and columns for the desire pod. Returns a matrix which have '0' where avaiable seats are and '2' where buffer seats are.'"""

        # Creating a matrix that represent the seats on a pod
        pod = numpy.zeros(shape=(pod_row, pod_column), dtype=int)

        # Total available rows in the pod where people can sit. It round the value to the greatest integer.
        total_avaliable_rows = math.ceil(pod_row/3)

        # Here it will be save the a row that will represent a buffer marker. A buffer marker is important because it will denote where a two buffer rows will start.
        buffer_row_marker = list()
        # Here it will be store in a list the actual number of the rows people can sit in the pot.
        actual_rows_people_sit = list()

        # This for loop will run the amount of total avaliable rows and each time it will store a row that represent a buffer marker to one list and the actual rows people can sit in the other list.
        # The 3*row represent sequence jump.
        # The specific reason why the jump is 3*row is because the distance from where the person sit and the next person sits is a little bit over the 6ft. recommended for social distance.
        # Each seat is 20in the leg room is also 20in so with two rows in between that adds up to eight feet and four inches. A row less and it will be just 5 feets.
        # ***THE VALUES HERE FOR THE ROW ARE THE INDEXES. STARTING FROM 0.***
        for row in range(total_avaliable_rows):
            # The plus 1 is because the first row is always going to be avaliable. 
            buffer_row_marker.append(1+(3*row))
            actual_rows_people_sit.append(3*row)

        # Changing the values from zero to 2's for the Buffer Rows
        for row in buffer_row_marker:
            for column in range(pod_column):

                # This run in the special case where the program can't add two buffer rows because there is just one row left.
                # The minus one is because the pod_row represent the actual number of rows. Meaning it doesn't represent the index. 
                if row == pod_row-1: 
                    pod[row][column] = 2

                # This run in the special case where the program can't add two buffer rows because there is no row left.
                # The break is to ignore adding the buffer rows and jump outside the elif and for loop.
                elif row == pod_row:
                    break

                # This run for everytime there is two rows that can be set as buffers.
                else:
                    pod[row][column] = 2
                    pod[row+1][column] = 2

        return pod

    def sitting_people(self, amount_people_sitting):
        """This function will deside where to sit people on the pod. The amount of people is an integer and the pod needs to be an object type matrix. After seatting everyone it will set some buffer seats for social distance."""



        # Finding the rows people can actually sit.
        total_avaliable_rows = math.ceil(len(self.pod)/3)
        actual_rows_people_sit = list()
        for row in range(total_avaliable_rows):
            actual_rows_people_sit.append(3*row)
        
        # Finding the amount of rows and columns the pod have.
        pod_num_column = len(self.pod[0]) 

        # Creating a variable that is goint to be use to know how many sits the row have left to allow some desition making.
        seats_left = pod_num_column

        # There is a social distance recommended by the CDC of 6 feets, considering that each seat is 20x20 inches and each
        # seat are side by side to satisfy this recommendation we need at least four seats in between the groups.
        social_distance_buffer_seats = 4

        # The reason why I went with this function is to have the ability of stopping all loops after sitting everyone. Break didn't work as intended and had to refactor the code.
        pod = self.sitting_logistic(amount_people_sitting, self.pod, actual_rows_people_sit, seats_left, social_distance_buffer_seats)

        self.pod = pod   

        return pod
 
    def sitting_logistic(self, amount_people_sitting, pod, actual_rows_people_sit, seats_left, social_distance_buffer_seats): 
        """This function is the one that is going to decide where to sit everyone."""

        for row in actual_rows_people_sit: # This goes through all rows people can sit.
            
            avaliable_seats_row = self.get_avaliable_seats_row(pod[row])
            occupied_seats = self.get_occupied_seats_row(pod[row])
            buffer_seats = self.get_buffer_seats_row(pod[row])
            avaliable_seats_pod = self.get_seats_avaliable_pod()

            # If avaliable seats are enough for the amount of people sitting and the buffer seats this will run.
            if avaliable_seats_row >= (amount_people_sitting + social_distance_buffer_seats):
                # This will run over each avaliable seat and change the value to represent is ocuppied '1' and to next amount of social_distance_buffer_seats as buffer seats '2'
                if pod[row][0] == 0: # This will mean the row is empty

                    # Loop over as many times needed to sit everyone using the avaliable_seat value as an index.
                    self.sit_people_empty_row(pod, row, amount_people_sitting)

                    # Loop over as many times needed to satisfy the social distance buffer seats amount.           
                    self.set_buffer_seat_empty_row(social_distance_buffer_seats, amount_people_sitting, pod, row)

                # This run when the row is not empty
                else: 

                    # Loop over as many times needed to sit everyone using the avaliable_seat value as an index.                  
                    self.sit_people_row(pod, row, occupied_seats,buffer_seats, amount_people_sitting)

                    # Updating the new ocuppied seats that have been set in the function from above.
                    occupied_seats += amount_people_sitting
                    
                    # Loop over as many times needed to satisfy the social distance buffer seats amount.
                    self.set_buffer_seat(social_distance_buffer_seats, occupied_seats, buffer_seats, pod,row)

                return pod

            # This will run when the avaliable sit are less than the people seatting plus the buffer seats.
            else:
                # This code cover the case when the people trying to sit get to the edge of the pod. The buffer seats will be ommited because the stair will work as the buffer.
                if avaliable_seats_row == amount_people_sitting:

                    # This run when the row is empty.
                    if pod[row][0] == 0:
                        self.sit_people_empty_row(pod, row, amount_people_sitting)

                        return pod

                    # This run where the row is not empty.
                    else:
                        self.sit_people_row(pod, row, occupied_seats, buffer_seats, amount_people_sitting)

                        return pod

                # This will run when there are not enough seats in the row but the amount people that want to be seated is less or equal that the actual seats in the whole row.
                elif avaliable_seats_row < amount_people_sitting and amount_people_sitting <= len(pod[0]):
                    # This will run when the pod is full. Meaning the group is to big for the avaliable seats.
                    if amount_people_sitting > avaliable_seats_pod:
                        print(f'The pod is full. This last group of {amount_people_sitting} can\'t be seated to big for the avaliable seats.')

                        return self.pod

                    # This code will run when there are no more row left to seat people. Is going to update that there is not enough space.
                    if (pod[row] == self.pod[-2]).all():
                        print('This group is to large for the amount of seats in any of the rows.')
                        print(f'There is still {avaliable_seats_pod} seats scatter through the pod but there is no {amount_people_sitting}\nseats side by side empty.')

                        return self.pod


                    # This pass will allow the program to jump for the next row and check for avaliable seats.
                    pass

                # This will run if the people that want to be seatted is larger that actual row length.
                elif amount_people_sitting > len(pod[0]):
                    print(f'The amount of people to be seatted is larger than the actual row.')
                    return pod
                
                # This will run when less than the actual amount for the social distance buffer seats are needed. 
                else: 
                    seats_left = self.get_avaliable_seats_row(pod[row])

                    # This statement will verify if the difference of the seat left and the people who want to sit is a positive number. The value that this difference will give back is the amount of buffer seats that are needed.
                    if (seats_left - amount_people_sitting) > 0:
                        # Seating people
                        self.sit_people_row(pod, row, occupied_seats, buffer_seats, amount_people_sitting)

                        # Updating the new ocuppied seats that have been set in the function from above.
                        occupied_seats += amount_people_sitting

                        # Calculating how many buffers are needed and then setting the seats as buffers.
                        buffer_seats_needed = seats_left - amount_people_sitting
                        self.set_buffer_seat(buffer_seats_needed, occupied_seats, buffer_seats, pod, row)

                        return pod

    










    def sitting_people_from_terminal(self, amount_people_sitting, terminal):
        """This function will deside where to sit people on the pod. The amount of people is an integer and the pod needs to be an object type matrix. After seatting everyone it will set some buffer seats for social distance."""



        # Finding the rows people can actually sit.
        total_avaliable_rows = math.ceil(len(self.pod)/3)
        actual_rows_people_sit = list()
        for row in range(total_avaliable_rows):
            actual_rows_people_sit.append(3*row)
        
        # Finding the amount of rows and columns the pod have.
        pod_num_column = len(self.pod[0]) 

        # Creating a variable that is goint to be use to know how many sits the row have left to allow some desition making.
        seats_left = pod_num_column

        # There is a social distance recommended by the CDC of 6 feets, considering that each seat is 20x20 inches and each
        # seat are side by side to satisfy this recommendation we need at least four seats in between the groups.
        social_distance_buffer_seats = 4

        # The reason why I went with this function is to have the ability of stopping all loops after sitting everyone. Break didn't work as intended and had to refactor the code.
        response = self.sitting_logistic_from_terminal(amount_people_sitting, self.pod, actual_rows_people_sit, seats_left, social_distance_buffer_seats, terminal)

        if response is None:
            pass
            
        else:
            self.pod = response   


    def sitting_logistic_from_terminal(self, amount_people_sitting, pod, actual_rows_people_sit, seats_left, social_distance_buffer_seats, terminal): 
        """This function is the one that is going to decide where to sit everyone."""

        for row in actual_rows_people_sit: # This goes through all rows people can sit.
            
            avaliable_seats_row = self.get_avaliable_seats_row(pod[row])
            occupied_seats = self.get_occupied_seats_row(pod[row])
            buffer_seats = self.get_buffer_seats_row(pod[row])
            avaliable_seats_pod = self.get_seats_avaliable_pod()

            # If avaliable seats are enough for the amount of people sitting and the buffer seats this will run.
            if avaliable_seats_row >= (amount_people_sitting + social_distance_buffer_seats):
                # This will run over each avaliable seat and change the value to represent is ocuppied '1' and to next amount of social_distance_buffer_seats as buffer seats '2'
                if pod[row][0] == 0: # This will mean the row is empty

                    # Loop over as many times needed to sit everyone using the avaliable_seat value as an index.
                    self.sit_people_empty_row(pod, row, amount_people_sitting)

                    # Loop over as many times needed to satisfy the social distance buffer seats amount.           
                    self.set_buffer_seat_empty_row(social_distance_buffer_seats, amount_people_sitting, pod, row)

                # This run when the row is not empty
                else: 

                    # Loop over as many times needed to sit everyone using the avaliable_seat value as an index.                  
                    self.sit_people_row(pod, row, occupied_seats,buffer_seats, amount_people_sitting)

                    # Updating the new ocuppied seats that have been set in the function from above.
                    occupied_seats += amount_people_sitting
                    
                    # Loop over as many times needed to satisfy the social distance buffer seats amount.
                    self.set_buffer_seat(social_distance_buffer_seats, occupied_seats, buffer_seats, pod,row)

                return pod

            # This will run when the avaliable sit are less than the people seatting plus the buffer seats.
            else:
                # This code cover the case when the people trying to sit get to the edge of the pod. The buffer seats will be ommited because the stair will work as the buffer.
                if avaliable_seats_row == amount_people_sitting:

                    # This run when the row is empty.
                    if pod[row][0] == 0:
                        self.sit_people_empty_row(pod, row, amount_people_sitting)

                        return pod

                    # This run where the row is not empty.
                    else:
                        self.sit_people_row(pod, row, occupied_seats, buffer_seats, amount_people_sitting)

                        return pod

                # This will run when there are not enough seats in the row but the amount people that want to be seated is less or equal that the actual seats in the whole row.
                elif avaliable_seats_row < amount_people_sitting and amount_people_sitting <= len(pod[0]):
                    # This will run when the pod is full. Meaning the group is to big for the avaliable seats.
                    if amount_people_sitting > avaliable_seats_pod:
                        #print(f'The pod is full. This last group of {amount_people_sitting} can\'t be seated to big for the avaliable seats.')
                        
                        terminal.jump_to_next_pod = True

                        return 

                    # This code will run when there are no more row left to seat people. Is going to update that there is not enough space.
                    if (pod[row] == self.pod[-2]).all():
                        #print('This group is to large for the amount of seats in any of the rows.')
                        #print(f'There is still {avaliable_seats_pod} seats scatter through the pod but there is no {amount_people_sitting}\nseats side by side empty.')

                        terminal.jump_to_next_pod = True

                        return 


                    # This pass will allow the program to jump for the next row and check for avaliable seats.
                    pass

                # This will run if the people that want to be seatted is larger that actual row length.
                elif amount_people_sitting > len(pod[0]):
                    #print(f'The amount of people to be seatted is larger than the actual row.')
                    return pod
                
                # This will run when less than the actual amount for the social distance buffer seats are needed. 
                else: 
                    seats_left = self.get_avaliable_seats_row(pod[row])

                    # This statement will verify if the difference of the seat left and the people who want to sit is a positive number. The value that this difference will give back is the amount of buffer seats that are needed.
                    if (seats_left - amount_people_sitting) > 0:
                        # Seating people
                        self.sit_people_row(pod, row, occupied_seats, buffer_seats, amount_people_sitting)

                        # Updating the new ocuppied seats that have been set in the function from above.
                        occupied_seats += amount_people_sitting

                        # Calculating how many buffers are needed and then setting the seats as buffers.
                        buffer_seats_needed = seats_left - amount_people_sitting
                        self.set_buffer_seat(buffer_seats_needed, occupied_seats, buffer_seats, pod, row)

                        return pod













    def get_id(self):
        """This method will return the id number."""
        return self.id

    def set_buffer_seat_empty_row(self, num_buffer_seats, amount_people_sitting, pod, row):
        """This function will set buffer seats as meany times passed for an empty row."""

        for i in range(num_buffer_seats): 
            # buffer_seat_index will start at the next seat after everyone is seated instead of starting at zero
            buffer_seat_index = amount_people_sitting + i 
            pod[row][buffer_seat_index] = 2

    def set_buffer_seat(self, num_buffer_seats, occupied_seats, buffer_seats, pod, row):
        """This function will set buffer seats as meany times passed for rows that are not empty."""

        for i in range(num_buffer_seats):
            # This seat_skip function like the one before. Is a jump to start on the next seat after the occupied and buffer seats.
            seat_skip = occupied_seats + buffer_seats
            buffer_seat_index = seat_skip + i
            pod[row][buffer_seat_index] = 2

    def sit_people_empty_row(self, pod, row, amount_people_sitting):
        """This function will sit people on an empty row."""

        # Loop over as many times needed to sit everyone using the avaliable_seat value as an index.
        for avaliable_seat in range(amount_people_sitting): 
            pod[row][avaliable_seat] = 1
        
        return pod

    def sit_people_row(self, pod, row, occupied_seats, buffer_seats, amount_people_sitting):
        """This function will sit people on the rows which are not already empty."""

        for avaliable_seat in range(amount_people_sitting):
            # This seat_skip is because we are not on an empty row so we have to account for the seats already taken and the ones that functions as buffers.
            seat_skip = occupied_seats + buffer_seats
            pod[row][seat_skip+avaliable_seat] = 1

    def get_seats_avaliable_pod(self):
        """This function return the amount of seats left in the entire pod."""

        # Finding the rows people can actually sit.
        total_avaliable_rows = math.ceil(len(self.pod)/3)
        actual_rows_people_sit = list()
        for row in range(total_avaliable_rows):
            actual_rows_people_sit.append(3*row)
            
        # Looking inside each row where people can actually sit and see the amount of places people can sit..
        avaliable_seats = 0
        for row in actual_rows_people_sit:
            for seat in self.pod[row]:
                if seat == 0:
                    avaliable_seats += 1
        
        return avaliable_seats

    def get_seats_occupied_pod(self):
        """This function return the amount of seats occupied in the entire pod."""

        # Finding the rows people can actually sit.
        total_avaliable_rows = math.ceil(len(self.pod)/3)
        actual_rows_people_sit = list()
        for row in range(total_avaliable_rows):
            actual_rows_people_sit.append(3*row) 

        # Looking inside each row where people can actually sit and see the amount of places people can sit..
        occupied_seats = 0
        for row in actual_rows_people_sit:
            for seat in self.pod[row]:
                if seat == 1: # People are seated there.
                    occupied_seats += 1
                if seat == 2: # This are seats that are buffer seats.
                    occupied_seats += 1
        
        return occupied_seats

    def get_people_on_seats(self):
        """This method will return the amount of people seated in the pod."""

        # Finding the rows people can actually sit.
        total_avaliable_rows = math.ceil(len(self.pod)/3)
        actual_rows_people_sit = list()
        for row in range(total_avaliable_rows):
            actual_rows_people_sit.append(3*row) 

        # Looking inside each row where people can actually sit and see the amount of places people can sit..
        people_seated = 0
        for row in actual_rows_people_sit:
            for seat in self.pod[row]:
                if seat == 1: # People are seated there.
                    people_seated += 1
        
        return people_seated

    def get_buffer_seats_pod(self):
        """This method will return the buffer seats in the entire pod but just the ones inside the rows people can sit."""

        # Finding the rows people can actually sit.
        total_avaliable_rows = math.ceil(len(self.pod)/3)
        actual_rows_people_sit = list()
        for row in range(total_avaliable_rows):
            actual_rows_people_sit.append(3*row) 

        # Looking inside each row where people can actually sit and see the amount of places people can sit..
        buffer_seats = 0
        for row in actual_rows_people_sit:
            for seat in self.pod[row]:
                if seat == 2: # This are seats that are buffer seats.
                    buffer_seats += 1
        
        return buffer_seats

    def get_total_buffer_seats_pod(self):
        """This method will return the value of buffer seats includding the rows that are mark as buffers."""

        # Looking inside each row where people can actually sit and see the amount of places people can sit..
        buffer_seats = 0
        for row in range(len(self.pod)):
            for seat in self.pod[row]:
                if seat == 2: # This are seats that are buffer seats.
                    buffer_seats += 1
        
        return buffer_seats 

    def get_total_seat_capacity_pod(self):
        """This method will return the amount of seats in the pod. Independently if they are occupied."""

        # Looking inside each row where people can actually sit and see the amount of places people can sit..
        seat_capacity = 0
        for row in range(len(self.pod)):
            for seat in self.pod[row]:
                if seat == 0: # This are seats that are empty seats.
                    seat_capacity += 1
                if seat == 1: # This are seats that are taken seats.
                    seat_capacity += 1
                if seat == 2: # This are seats that are buffer seats.
                    seat_capacity += 1
        
        return seat_capacity      

    def get_avaliable_seats_row(self, row):
        """This function will return the amount of avaliable seats in the row. The paramater is a row from the pod."""

        avaliable_seats = 0

        for seat in row:
            # This will add up; every avaliable seat, occupied seat and buffer seat. 
            if seat == 0:
                avaliable_seats += 1

        return avaliable_seats

    def get_occupied_seats_row(self, row):
        """This function will return the amount of occupied seats in the row. The paramater is a row from the pod."""

        occupied_seats = 0

        for seat in row:
            # This will add up; every avaliable seat, occupied seat and buffer seat. 
            if seat == 1:
                occupied_seats += 1

        return occupied_seats

    def get_buffer_seats_row(self, row):
        """This function will return the amount of buffer seats in the row. The paramater is a row from the pod."""

        buffer_seats = 0

        for seat in row:
            # This will add up; every avaliable seat, occupied seat and buffer seat. 
            if seat == 2:
                buffer_seats += 1

        return buffer_seats



if __name__ == '__main__':
    pass
    
    # test = numpy.zeros(shape=(10, 10), dtype=int)

    # print(test)
    # print("\t\t\t\t\t" + str(test).replace('\n','\n\t\t\t\t\t'))


    # grand_stand_pod_left = Pod(17,15)

    # grand_stand_pod_left.sitting_people(5)


    # grand_stand_pod_left.show_pod()
    # # print()

    # people = list()
    # for i in range(20):
    #     people.append(i)
    # people.append(5)


    # for i in people:
    #     print()
    #     print(i)
    #     print()

    #     # print('before')
    #     # print(grand_stand_pod_left.pod)
    #     print(grand_stand_pod_left.sitting_people(i))
    #     # print('after')
    #     # print(grand_stand_pod_left.pod)


    # print(len(grand_stand_pod_left.pod))
    # print(grand_stand_pod_left.pod[16])
    # print(grand_stand_pod_left.pod[-1])
    

    # x = numpy.array([[10, 5], [10, 6]])

    # print((x[-1] == x[0]).all())



    # grand_stand_pod_left.show_pod()