def mainboard(p):

    baseline = f'|    |    |    |'
    line1 = baseline[:2] + p[1][1] + baseline[3:7] + p[2][1] + baseline[8:12] + p[3][1] + baseline[13:]
    line2 = baseline[:2] + p[4][1] + baseline[3:7] + p[5][1] + baseline[8:12] + p[6][1] + baseline[13:]
    line3 = baseline[:2] + p[7][1] + baseline[3:7] + p[8][1] + baseline[8:12] + p[9][1] + baseline[13:]
    print(f'----------------')
    print(f'|1   |2   |3   |')
    print(line1)
    print(f'----------------')
    print(f'|4   |5   |6   |')
    print(line2)
    print(f'----------------')
    print(f'|7   |8   |9   |')
    print(line3)
    print('----------------')


def compare(p,dchoose):
    if (p[1][1] == dchoose and p[2][1] == dchoose and p[3][1] == dchoose) or (
            p[4][1] == dchoose and p[5][1] == dchoose and p[6][1] == dchoose) or (
            p[7][1] == dchoose and p[8][1] == dchoose and p[9][1] == dchoose) or (
            p[1][1] == dchoose and p[4][1] == dchoose and p[7][1] == dchoose) or (
            p[2][1] == dchoose and p[5][1] == dchoose and p[8][1] == dchoose) or (
            p[3][1] == dchoose and p[6][1] == dchoose and p[9][1] == dchoose) or (
            p[1][1] == dchoose and p[5][1] == dchoose and p[9][1] == dchoose) or (
            p[3][1] == dchoose and p[5][1] == dchoose and p[7][1] == dchoose):
        return 'Congratulations'
    else:
        pass


def players(first_p,second_p,first_c,second_c):
    #global play
    dic = {1: [True, ' '], 2: [True, ' '], 3: [True, ' '], 4: [True, ' '], 5: [True, ' '], 6: [True, ' '], 7: [True, ' '], 8: [True, ' '], 9: [True, ' ']}
    for i in range(1,11):
        if i == 10:
            return 'Match Drawn'
            
        if (i % 2) == 1:
            while True:
                play = input(f"hey {first_p}, it's your turn. please select a number between 1 to 9 : ")
                
                try:
                    if (int(play) >= 0 and int(play) <= 9) and dic[int(play)][0]:
                        dic[int(play)][1] = first_c
                        dic[int(play)][0] = False
                        break
                    elif int(play) > 9:
                        print('please type a number between 1-9')
                    else:
                        print('this position is already used. please type another number')

                except:
                    print('please type a number between 1-9')

            winner = compare(dic,first_c)
            
            if winner == 'Congratulations':
                return f'hey {first_p} Congratulations. you win'
            else:
                mainboard(dic)
        if (i % 2) == 0:
            while True:
                play = input(f"hey {second_p}, it's your turn. please select a number between 1 to 9 : ")
                
                try:
                    if (int(play) >= 0 and int(play) <= 9) and dic[int(play)][0]:
                        dic[int(play)][1] = second_c
                        dic[int(play)][0] = False
                        break
                    elif int(play) > 9:
                        print('please type a number between 1-9')
                    else:
                        print('this position is already used. please type another number')

                except:
                    print('please type a number between 1-9')


            winner = compare(dic,second_c)
            if winner == 'Congratulations':
                return f'hey {second_p} Congratulations . you win'
            else:
                mainboard(dic)


first_player = input('what is your name ? ')
first_choose = ''

while True:
    first_choose = ''
    choose = input("choose your symbol between 'o' or 'x' : ")
    first_choose = first_choose + choose
    
    if first_choose == 'o'.lower() or 'o'.upper():
        first_choose = choose
        break
        
    elif first_choose == 'x'.lower() or 'x'.upper():
        first_choose = choose
        break
        
    else:
        print('invalid input')
        
second_player = input('what is your name ? ')
second_choose = ''

if first_choose == 'x'.lower():
    second_choose = second_choose + 'o'
    print(f"hey {second_player} your symbol is 'o' ")
    
elif first_choose == 'x'.upper():
    second_choose = second_choose + 'O'
    print(f"hey {second_player} your symbol is 'O' ")
    
elif first_choose == 'o'.lower():
    second_choose = second_choose + 'x'
    print(f"hey {second_player} your symbol is 'x' ")
    
elif first_choose == 'o'.upper():
    second_choose = second_choose + 'X'
    print(f"hey {second_player} your symbol is 'X' ")
    
var10 = players(first_player,second_player,first_choose,second_choose)
print(var10)

while True:
    input_for_play_again = input('wanna play again ?? please type yes or no ')
    if input_for_play_again == 'yes'.lower() or input_for_play_again == 'yes'.upper() or input_for_play_again == 'y'.lower() or input_for_play_again == 'y'.upper():
        var10 = players(first_player,second_player,first_choose,second_choose)
        print(var10)
        
    else:
        break

