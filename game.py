from die import roll_die

initial_money = 100
money = initial_money
pass_line_bet = 10

craps_rolls = [2, 3, 12]
that_number = 7
point_on = False
point = 0
pass_line = True
odds_bet = False
bet_on_6 = False
bet_on_8 = False
total_rolls = 0
roll = 0
limit = 100

def print_game_status():
    print(f'Total rolls: {total_rolls}')
    print(f'Money count: {money}')
    print(f'Point on: {point_on}')
    # print(f'Bet on pass line: {pass_line}')
    print('\n')

def reset_roll():
    global roll
    roll = 0

def shoot_dice():
    global roll
    global total_rolls
    dice1 = roll_die()
    dice2 = roll_die()
    roll = dice1 + dice2
    total_rolls += 1

def payout_6_or_8():
    global money
    money += 14

def seven_out():
    global point_on
    global point
    global money
    global odds_bet
    global bet_on_6
    global bet_on_8

    if bet_on_8 or bet_on_6:
        bet_on_6 == False
        bet_on_8 == False
        money -= 12
    if odds_bet:
        odds_bet = False
        money -= 10
    money -= pass_line_bet
    point_on = False
    point = 0

while(total_rolls < limit): 
    # Coming out roll
    shoot_dice()
    if (not point_on and roll == that_number or roll == 11):
        # print('Winner!')
        # print(roll)
        money += pass_line_bet
        # print_game_status()
    elif(not point_on and roll not in craps_rolls):
        point_on = True
        point = roll
        # print('Point is established')
        # print(f'Point is {point}')
        # print_game_status()
    else:
        # print('Loser, sorry')
        # print(roll)
        money -= pass_line_bet
        # print_game_status()

    reset_roll()

    while(point_on and total_rolls < limit):
        # print(f'Point is {point}')
        if point == 6 and odds_bet == False and bet_on_8 == False:
            odds_bet = True
            money -= 10
            bet_on_8 = True
            money -= 12
            # print('Bets placed on 8 and odds')
        if point == 8 and odds_bet == False and bet_on_6 == False:
            odds_bet = True
            money -= 10
            bet_on_6 = True
            money -= 12
            # print('Bets placed on 6 and odds')

        shoot_dice()
        if roll == point:
            # print('Winner!')
            # print(f'Roll is {roll}, point is {roll}')
            point_on = False
            point = 0
            money += pass_line_bet
            # print_game_status()
        elif roll == that_number:
            # print('Oh no 7 out')
            # print(f'Roll is {roll}')
            seven_out()
            # print_game_status()
        elif roll == 6 or roll == 8:
            # print('Winner!')
            # print(f'Roll is {roll}')
            payout_6_or_8()
            # print_game_status()
        else:
            continue
            # print('No result')
            # print(f'Roll is {roll}')
            # print_game_status()

print_game_status()

# if money < initial_money:
#     print('Lost money :(')
# else:
#     print('Gained or broke even')