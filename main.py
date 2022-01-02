# Risk Main.py


debug_mode = 1

#from torch import *
from map import MapNode

# map object
# create a list of nodes, numbered 0 .. n.

# node object
# include a node number
# include a list of connections
# include a location for the image.
# store number of troops on cell.
# store owner of the cell.
# store which continent it belongs to.

# Make a list of cells belonging to each continent.

# define continent.
# 0 - North america
# 1 - south america
# 2 - Europe
# 3 - Africa
# 4 - Asia
# 5 - Australia


map_node_list = []

for node in range(0,42):
    x = MapNode()
    x.num = node
    map_node_list.append(x)
    if (node<9):
        x.continent=0
    elif(node<14):
        x.continent=1
    elif(node<22):
        x.continent=2
    elif(node<27):
        x.continent=3
    elif(node<38):
        x.continent=4
    else:
        x.continent=5
    

print(map_node_list)
for ii in range(0,42):
    print("Node num = ", map_node_list[ii].num )
    print("  Cont = ", map_node_list[ii].continent )

map_node_list[0].connect_list = [29,1,3]
map_node_list[1].connect_list = [0,1,2,3,4]
map_node_list[2].connect_list = [1,4,5,13]
map_node_list[3].connect_list = [0,1,4,6]
map_node_list[4].connect_list = [1,2,3,5,6,7]
map_node_list[5].connect_list = [2,4,7]
map_node_list[6].connect_list = [3,4,7,8]
map_node_list[7].connect_list = [4,5,6,8]
map_node_list[8].connect_list = [6,7,9]
map_node_list[9].connect_list = [8,10,11]
map_node_list[10].connect_list = [9,11,12]
map_node_list[11].connect_list = [9,10,12,20]
map_node_list[12].connect_list = [10,11]
map_node_list[13].connect_list = [2,14,15]
map_node_list[14].connect_list = [13,15,16,17]
map_node_list[15].connect_list = [13,14,16,18]
map_node_list[16].connect_list = [14,15,17,18,19]
map_node_list[17].connect_list = [26,30,32,14,16,19]
map_node_list[18].connect_list = [15,16,19,20]
map_node_list[19].connect_list = [16,17,18,20,21,32]
map_node_list[20].connect_list = [11,18,19,21,22,23]
map_node_list[21].connect_list = [19,20,23,32]
map_node_list[22].connect_list = [20,23,24]
map_node_list[23].connect_list = [20,21,22,25,32]
map_node_list[24].connect_list = [22,25]
map_node_list[25].connect_list = [23,24]
map_node_list[26].connect_list = [17,30,27,31]
map_node_list[27].connect_list = [26,28,31]
map_node_list[28].connect_list = [27,29,31]
map_node_list[29].connect_list = [0,28,31,34,35]
map_node_list[30].connect_list = [17,26,32,33]
map_node_list[31].connect_list = [26,27,28,29,34]
map_node_list[32].connect_list = [17,19,21,23,30,36]
map_node_list[33].connect_list = [30,34,36,37]
map_node_list[34].connect_list = [29,31,33,35]
map_node_list[35].connect_list = [29,34]
map_node_list[36].connect_list = [32,33,37]
map_node_list[37].connect_list = [33,36,38]
map_node_list[38].connect_list = [37,39,40]
map_node_list[39].connect_list = [38,40,41]
map_node_list[40].connect_list = [38,39,41]
map_node_list[41].connect_list = [39,40]


# write some checking code here to test previous, make sure if one
# node connects to others, they also connect back.
if debug_mode:
    for ii in range(0,42):
        #print("Node num = ", map_node_list[ii].num )
        #print("  Cont = ", map_node_list[ii].continent )
        list1 = map_node_list[ii].connect_list
        for list_item in list1:
            list2 = map_node_list[list_item].connect_list
            if(not(ii in list2)):
                print('Error in node', ii)
                print('points to ', list_item)
                print('Dest node does not point back')

    print('CHECK DONE')

# create grid with player owners.

# define allowed connections.
# each node has list of other nodes that are neighbours.


# define players

# randomly assign cells to players.

# foreach player
# randomly add soldiers to cells.


#
# Main loop
#

# take turns per player
# figure out points to start.
# points per territory
# max(3, (cells_owned/3))
# add for continents
# cash in cards ? force if 5 cards....

# let player assign troops to territories

# Attacks

# dice roll etc, blitz only.

# Check if winner ( > 70% of territory)

# end attack? or repeat.

# Give card if earned

# move troops?




