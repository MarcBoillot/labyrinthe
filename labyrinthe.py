labyrinth = [
    ("S","|",".",".",".",".","."),
    (".","|",".","|","|",".","|"),
    (".","|",".","|","G",".","."),
    (".",".",".",".","|","|","."),
    (".","|",".","|",".",".","."),
    (".","|",".",".",".","|",".")
    ]
count_step=0
G=(4,2)
S = (0,0)
player_position = S
def check_case_around(position):
    next_case=[]
    x,y=position
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        new_x = x+dx
        new_y = y+dy
        if 0 <= new_x < len(labyrinth) and 0 <= new_y < len(labyrinth[0]) and labyrinth[new_x][new_y] != "|":
            next_case.append((new_x, new_y))
    return next_case

def move (player_position, next_position):

    player_position = next_position
    return next_position

def case(next_position):
    return labyrinth[next_position[0]][next_position[1]]


def solution_labyrinth (count_step, tab):

    while player_position != G:
        check_case_around(player_position)
        while check_case_around(player_position)==0:
            if case(check_case_around(player_position))==1:
                case[player_position]+=1
                move(player_position)
                count_step+=1
        while case(check_case_around(player_position))==1:
            move(player_position)
            count_step+=1
            check_case_around(player_position)
            if case(check_case_around(player_position))==0:
                if tab.length == 2:
                    case[player_position]+=1
                    move(player_position,check_case_around(player_position),tab)
            count_step+=1
print("Total steps:", count_step)
solution_labyrinth(count_step,labyrinth)