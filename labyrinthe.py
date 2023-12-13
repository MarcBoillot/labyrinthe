labyrinth =
    (S,■,0,0,0,0,0),
    (0,■,0,■,■,0,■),
    (0,■,0,■,G,0,0),
    (0,0,0,0,■,■,0),
    (0,■,0,■,0,0,0),
    (0,■,0,0,0,■,0),
count_step=0
G = (4,2)
player_position = (0,0)
S = (0,0)
def check_case_around(x,y):
    next_case=[]
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        new_x = (x+dx)
        new_y = (y+dy)
        if new_x in next_case && new_y in next_case:
            next_case = (new_x,new_y)
    return next_case

def move (player_position):
    player_position = check_case_around(player_position)


def solution_labyrinth ():
    global player_position, count_step
    while player_position != G:
        while check_case_around(player_position)=0:
            if (case(check_case_around(player_position))=1):
                case(check_case_around(player_position))+=1
                move(player_position)
                count_step+=1
        while (case(check_case_around(player_position))=1):
            move(player_position)
            count_step+=1
            check_case_around(player_position)
            if case(check_case_around(player_position))=0):
                if tab.length = 2:
                    case(check_case_around(player_position))+=1
                    move(player_position,check_case_around(player_position),tab)
                    count_step++
    print("total steps, count_step")
solution_labyrinth()