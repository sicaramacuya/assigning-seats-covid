from abc import ABC
from Pods import Pod
from helper_module import print_newline

class Stand(ABC):

    def __init__(self, name, row, column, num_pods):
        self.name = name
        self.row = row # All the rows that it has with counting different pods
        self.column = column # All the columns
        self.num_pods = num_pods # Quantity of pods wanted for the stand.
        self.pod_rows = row
        self.pod_columns = int(self.column / self.num_pods) 
        self.pods = list() # A list of all pods inside the stand

    def create_pod(self):
        """This method will create and store pods inside the stand list."""
        
        pod = Pod(self.pod_rows, self.pod_columns)
        self.add_pod_to_stand(pod)
        
        return pod

    def get_pods(self):
        """This method will return a list of the pods for this stand."""
        
        return self.pods

    def show_pods(self):
        """This method will show all pods in the pods list."""

        for i in self.pods:
            i.show_pod()  
            print_newline()  

    def get_name(self):
        """This method will return the name."""
        return self.name

    def set_name(self, name):
        """This method will let you change the name."""
        self.name = name

    def get_row(self):
        """This method will return the row number."""
        return self.row

    def set_row(self, row):
        """This method will let you change the row number"""
        self.row = row

    def get_column(self):
        """This method will return the column number."""
        return self.column
 
    def set_column(self, column):
        """This method will let you change the column number"""
        self.row = column

    def get_num_pods(self):
        """This method will return the number of pods in this specific stand."""
        return self.num_pods

    def set_num_pods(self, num_pods):
        """This method will let you change the number of pods in this specific stand."""
        self.num_pods = num_pods

    def add_pod_to_stand(self, pod):
        """This method will add a pod to the stand list that contain all the pods objects."""
        self.pods.append(pod)

    def remove_pod_from_stand(self, pod_id):
        """This method will remove pod from stand list that contain all the pods objects. The parameter should be the pods id."""
        found_pod = False

        # Loop through each pod in our pods list.
        for i in self.pods:

            # If we find them, remove them from the list.
            if i.id == pod_id:
                self.pods.remove(i)
                # set our indicator to True
                found_pod = True
       
        # If we looped through our list and did not find our pod, the indicator would never get change, so return 'Pod not found!'
        if not found_pod:
            print(f'Pod not found!')


if __name__ == "__main__":  
    pass