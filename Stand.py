from abc import ABC

class Stand(ABC):

    def __init__(self):
        self.name = None
        self.row = None
        self.column = None
        self.num_pods = None
        self.stand = list()

    def get_name(self):
        """This method will return the name."""
        return self.name

    def set_name(self, name):
        """This method will let you change the name."""
        self.name = name

    def get_row(self):
        """This method will return the row number.""""
        return self.row

    def set_row(self, row)
        """This method will let you change the row number"""
        self.row = row

    def get_column(self):
        """This method will return the column number.""""
        return self.column
 
    def set_column(self, column)
        """This method will let you change the column number"""
        self.row = column

    def get_num_pods(self):
        """This method will return the number of pods in this specific stand.""""
        return self.num_pods

    def set_num_pods(self, num_pods):
        """This method will let you change the number of pods in this specific stand."""
        self.num_pods = num_pods

    def get_stand(self):
        """This method will return the stand list that contain all the pods objects."""
        return self.stand

    def add_pod_to_stand(self, pod):
        """This method will add a pod to the stand list that contain all the pods objects."""
        self.stand.append(pod)

    def remove_pod_from_stand(self, pod_id):
        """This method will remove pod from stand list that contain all the pods objects. The parameter should be the pods id."""
        found_pod = False

        # Loop through each pod in our stand list.
        for i in self.stand:

            # If we find them, remove them from the list.
            if i.id == pod_id:
                self.stand.remove(i)
                # set our indicator to True
                found_hero = True
       
        # If we looped through our list and did not find our pod, the indicator would never get change, so return 'Pod not found!'
        if not found_pod:
            print(f'Pod not found!')


if __name__ == "__main__":
    
    eric = GrandStand('Eric Javier')

    eric.show_name()