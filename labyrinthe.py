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
#fonction pour verifier les cases autour de la position du joueur
def check_case_around(position):
    #tableau pour mettre l'index de la case suivante
    next_case=[]
    #x et y definisse la position
    x,y=position
    #les directions a tester en priorité
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        #les nouveaux index
        new_x = x+dx
        new_y = y+dy
        #j'évite que les cases testées sortent du tableau
        if 0 <= new_x < len(labyrinth) and 0 <= new_y < len(labyrinth[0]) and labyrinth[new_x][new_y] != "|":
            #j'ajoute a next_case les nouvelles coordonnées
            next_case.append((new_x, new_y))
    #je retourne les positions suivantes possibles
    return next_case

def move (player_position, next_position):
    #la position de joueur prend la nouvelle position retournée
    player_position = next_position
    return next_position

def case(next_position):
    #je retourne la valeur de la case a la position suivante pour voir si elle possede des grains de riz
    return labyrinth[next_position[0]][next_position[1]]


def solution_labyrinth (count_step, tab):
#tant que la valeur a la position du joueur n'est pas égale a celle de la position de G
    while player_position != G:
        #verifier les cases autour de la position du joueur
        check_case_around(player_position)
        #tant que les cases autour de la position du joueur est egale a 0 "grains de riz"
        while case[check_case_around(player_position)]==0:
            #si la valeur des cases autour de la position du joueur egale a 1"grain de riz"
            if case[check_case_around(player_position)]==1:
                #j'incremente la valeur de la case a l'index de position du joueur
                case[player_position]+=1
                #je bouge mon joueur a la position
                move(player_position)
                #j'incremente mon compteur de pas
                count_step+=1
        #tant que les cases autour de la position du joueur est egale a 1 "grains de riz"
        while case[check_case_around(player_position)]==1:
            # je bouge mon joueur a la position
            move(player_position)
            count_step+=1
            #je retourne un index
            check_case_around(player_position)
            # si la valeur des cases autour de la position du joueur egale a 0"grain de riz"
            if case[check_case_around(player_position)]==0:
                #si le tableau contient deux elements c'est a dire deux positions
                if tab.length == 2:
                    case[player_position]+=1
                    move(player_position,check_case_around(player_position),tab)
            count_step+=1
neighbors = check_case_around(player_position)
print("Neighboring positions:", neighbors)
print("Total steps:", count_step)
solution_labyrinth(count_step,labyrinth)