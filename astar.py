import msvcrt
import subprocess as sp
import time
import sys

game_map = [
"***********************************************************************",
"*                                                                     *",
"*   ********   *********   ***************   ********************     *",
"*   *      *   *       *   *             *   *                  *     *",
"*   *      *   *       *   *             *   *                  *     *",
"*   *      *   *       *   *             *   *                  *     *",
"*   *      *   *       *   *             *   *                  *     *",
"*   ********   *********   ***************   ********************     *",
"*                                ::                                   *",
"*   ****************************   ******************************     *",
"*   *                          *   *                            *     *",
"*   *                          *   *                            *     *",
"*   *                          *   *                            *     *",
"*   *                          *   *                            *     *",
"*   *                          *   *                            *     *",
"*   *                          *   *                            *     *",
"*   *                          *   *                            *     *",
"*   *                          *   *                            *     *",
"*   ****************************   ******************************     *",
"*                                                                     *",
"***********************************************************************"
]
game_map = [[x for x in s] for s in game_map]

char1 = 8
char2 = 33


dir = [
    (-1,  0),
    ( 0,  1),
    ( 1,  0),
    ( 0, -1),
]

#Distance calculation

def get_dist(a, b):
    # return (((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5)
    return (abs(a[0]-b[0])+abs(a[1]-b[1]))*10

# 10 22

# mulai 8, 20
# slesai 1, 5

start = (2, 1)
end = (char1, char2)

qu = []
qu.append((0, 0, start))

while len(qu) > 0:
    # Ghost Movement
    
    qu = sorted(qu, key = lambda x: x[0])
    
    h_dist, dist, pos = qu.pop(0)

    game_map[pos[0]][pos[1]] = '0'

    end = (char1, char2)
    get = ''

    # Character Movement
    
    get = msvcrt.getch()
    

    if get == chr(119).encode():
        if game_map[char1-1][char2]!='*':
            game_map[char1][char2]=' '
            game_map[char1-1][char2]='$'
            char1 = char1-1
        
        
    
    if get == chr(115).encode():
        if game_map[char1+1][char2]!='*':
            game_map[char1][char2]=' '
            game_map[char1+1][char2]='$'
            char1 = char1+1
        
    
    if get == chr(97).encode():
        if game_map[char1][char2-1]!='*':
            game_map[char1][char2]=' '
            game_map[char1][char2-1]='$'
            char2 = char2-1
        

    if get == chr(100).encode():
        if game_map[char1][char2+1]!='*':
            game_map[char1][char2]=' '
            game_map[char1][char2+1]='$'
            char2 = char2+1

    #Ghost Movement Calculation
    currheur = 99999
    tnpos =(1,1)
    for d in dir:
        npos = (pos[0]+d[0], pos[1]+d[1])
        if game_map[npos[0]][npos[1]] == ' ' or game_map[npos[0]][npos[1]] == '$'and\
            0 <= npos[0] < len(game_map) and\
            0 <= npos[1] < len(game_map[0]):
                nhdist = dist+get_dist(npos, end)
                if(nhdist<currheur):
                    currheur = nhdist
                    tnpos = npos
                    print(nhdist)
    qu.append((currheur, dist+1, tnpos))
    sp.call('cls',shell=True)
    for l in game_map:
        for r in l:
            #print(r,end='')
            sys.stdout.write(r)
        print()
    
    
    game_map[pos[0]][pos[1]] = ' '
    if pos == end:
        break
    
# std::priority_queue<pair<int, pair<int, int>>;

# vector<pair<int, pair<int, int>> vec;
# vec.push_back(make_pair(jarak, make_pair(koor)));