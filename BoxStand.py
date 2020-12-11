from Stand import Stand

class BoxStand(Stand):
    
    def __init__(self, name, row, column, num_pods):

        super().__init__(name, row, column, num_pods)
        self.stand_category = 'Box Stand'



if __name__ == "__main__":
    pass