from Stand import Stand

class TelescopicStand(Stand):
    
    def __init__(self, name, row, column, num_pods):

        super().__init__(name, row, column, num_pods)
        self.stand_category = 'Telescopic Stand'



if __name__ == "__main__":
    pass