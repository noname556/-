def reset():
    game_map=[]
    for i in range(9):
        game_map.append("-")
    return game_map
def maping(game_map):
        x=int(input())
        y=int(input())
        if x == 1 and y == 1:
            game_map[0] = "O"
        elif x == 1 and y == 2:
            game_map[1] = "O"
        elif x == 1 and y == 3:
            game_map[2] = "O"
        elif x == 2 and y == 1:
            game_map[3] = "O"
        elif x == 2 and y == 2:
            game_map[4] = "O"
        elif x == 2 and y == 3:
            game_map[5] = "O"
        elif x == 2 and y == 1:
            game_map[6] = "O"
        elif x == 2 and y == 2:
            game_map[7] = "O"
        elif x == 2 and y == 3:
            game_map[8] = "O"
        return map
def print_map(game_map):
    print(game_map[0] +"|"+ game_map[1] +"|"+ game_map[2])
    print(game_map[3] +"|"+ game_map[4] +"|"+ game_map[5])
    print(game_map[6] +"|"+ game_map[7] +"|"+ game_map[8])
def check(count):
    for i in range(9):
        if game_map[i]=="-":
            break
        else:
            count=count+1
    return count

game_map = reset()
print_map(game_map)

while 0+0!=1:
    #maping()
    a="0"

    b=int(input())
    if game_map[b]!="-":
        print("이미 말이 놓여진 칸입니다.")

    else:
        game_map[b] = a
        print_map(game_map)
    count=0
    check(count)
    if count==9:
        break
    elif game_map[0] == "o" and game_map[1] == "o" and game_map[2] == "o":
        break
    elif game_map[3] == "o" and game_map[4] == "o" and game_map[5] == "o":
        break
    elif game_map[6] == "o" and game_map[7] == "o" and game_map[8] == "o":
        break
    elif game_map[0] == "o" and game_map[3] == "o" and game_map[6] == "o":
        break
    elif game_map[1] == "o" and game_map[4] == "o" and game_map[7] == "o":
        break
    elif game_map[2] == "o" and game_map[5] == "o" and game_map[8] == "o":
        break
    elif game_map[0] == "o" and game_map[5] == "o" and game_map[8] == "o":
        break
    elif game_map[2] == "o" and game_map[5] == "o" and game_map[6] == "o":
        break