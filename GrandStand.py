from Stand import Stand
from Pods import Pod

class GrandStand(Stand):

    def __init__(self, name, row, column, num_pods):

        super().__init__(name, row, column, num_pods)
        self.stand_category = 'Grand Stand'



if __name__ == "__main__":
    
    lateral_grand_stand_west = GrandStand('Lateral Grand Stand - West', 42, 17, 3)
    print(lateral_grand_stand_west.get_name())

    lateral_grand_stand_west_pod_1 = Pod(lateral_grand_stand_west.pod_rows,lateral_grand_stand_west.pod_columns)
    lateral_grand_stand_west_pod_2 = Pod(lateral_grand_stand_west.pod_rows,lateral_grand_stand_west.pod_columns)
    lateral_grand_stand_west_pod_3 = Pod(lateral_grand_stand_west.pod_rows,lateral_grand_stand_west.pod_columns)


    lateral_grand_stand_west.add_pod_to_stand(lateral_grand_stand_west_pod_1)
    lateral_grand_stand_west.add_pod_to_stand(lateral_grand_stand_west_pod_2)
    lateral_grand_stand_west.add_pod_to_stand(lateral_grand_stand_west_pod_3)

    lateral_grand_stand_west.remove_pod_from_stand(lateral_grand_stand_west_pod_3.get_id())

    for i in lateral_grand_stand_west.get_pods():
        print(i.pod)