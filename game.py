from die import roll_die
import random

initial_money = 100
money = initial_money
bets_on_table = 0
pass_line_bet = 10

craps_rolls = [2, 3, 12]
that_number = 7
point_on = False
point = 0
pass_line = False
odds_bet = False
bet_on_6 = False
bet_on_8 = False
total_rolls = 0
roll = 0
limit = 50

def print_game_status():
    print(f'Total rolls: {total_rolls}')
    print(f'Money count: {money}')
    print(f'Point on: {point_on}')
    # print(f'Bet on pass line: {pass_line}')
    print('\n')

def print_money_status():
    print(f'Money in hand: {money}')
    print(f'Bets on table: {bets_on_table}')
    print(f'Total accounted for: {money + bets_on_table}')
    # print(f'Net: {money + bets_on_table}')

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

def reset_game():
    global point_on
    global point
    global pass_line
    global odds_bet
    global bet_on_6
    global bet_on_8
    point_on = False
    point = 0
    pass_line = False
    odds_bet = False
    bet_on_6 = False
    bet_on_8 = False

def seven_out():
    reset_game()
    global money
    global bet_on_6
    global bet_on_8
    global odds_bet

    if bet_on_6 or bet_on_8:
        money -= 12
    if odds_bet:
        money -= 10
    money -= pass_line_bet

def rolls_with_point_established():
    global roll
    global point_on
    global point
    global money
    global pass_line
    global pass_line_bet
    global bet_on_6
    global bet_on_8
    global odds_bet
    reset_roll()
    shoot_dice()
    print(f'Point is on: {point} and roll was {roll}')
    if (roll == point) and (point == 6 or point == 8) and (odds_bet):
        print('Point cleared 6 or 8. Pay the line and odds, clear bets')
        print(f'Money before: {money}')
        money += pass_line_bet # Pass line payout
        money += 12 # Odds line payout (5 : 6)
        print(f'Money after: {money}')
        reset_game()
    elif roll == 6 and bet_on_6 and roll != point:
        print('Point not cleared, but paying the 6')
        print(f'Money before: {money}')
        money += 14
        print(f'Money after: {money}')
    elif roll == 8 and bet_on_8 and roll != point:
        print('Point not cleared, but paying the 8')
        print(f'Money before: {money}')
        money += 14
        print(f'Money after: {money}')
    elif roll == point:
        print('Point cleared, line paid')
        print(f'Money before: {money}')
        money += pass_line_bet
        print(f'Money after: {money}')
        reset_game()
    elif roll == 7: # Seven out
        print('Seven out')
        print(f'Money before: {money}')
        money -= pass_line_bet # Lose pass line bet
        if bet_on_6 or bet_on_8: # Lose bets on 6 or 8
            print('Lose pass line, lose 6 or 8')
            money -= 12
        if odds_bet: # Lose odds bet
            print('Lose odds')
            money -= 10
        print(f'Money after: {money}')
        reset_game()



while(total_rolls < limit): 
    reset_roll() # Simulates stickman giving dice (back) to shooter
    if not pass_line:
        print(f'Placing pass line bet')
        money -= pass_line_bet
        bets_on_table += pass_line_bet
        pass_line = True
        print_money_status()
    # Coming out roll
    print('Coming out')
    shoot_dice()

    # Point is off
    # Point off, 7 or 11 win and pay the line
    if (not point_on and roll == that_number or roll == 11):
        print(f'Winner with 7 or 11 ({roll})')
        print(f'Money before: {money}')
        money += pass_line_bet
        print(f'Money after: {money}')
        print_money_status()
    
    # Point off, craps roll (2, 3, or 12)
    elif (not point_on and roll in craps_rolls):
        print(f'Loser with 2, 3, 12 ({roll})')
        print(f'Money before: {money}')
        money -= pass_line_bet
        print(f'Money after: {money}')
        pass_line = False
        print_money_status()

    # Point off, roll establishes point (not a 2, 3, or 12) 
    elif (not point_on and roll not in craps_rolls):
        point_on = True
        point = roll
        print(f'Point is established: {point}')
    
    # If the point is not established, make another "come out" roll
    if (not point_on):
        print('Point not established, rolling with point off\n')
        continue
    
    # If the point is established, check to see if point is 6
    elif (point == 6): # If point is 6, bet on 8, odds behind
        bet_on_8 = True
        odds_bet = True
        print(f'Point is 6 ({point}) and bet is on 8. Odds backed')
        # print(f'Money before: {money}')
        money -= 12
        money -= 10
        bets_on_table += 12
        bets_on_table += 10
        # print(f'Money after: {money}')
        print_money_status()
    elif (point == 8): # If point is 8, bet on 6, odds behind
        bet_on_6 = True
        odds_bet = True
        print(f'Point is 8 ({point}) and bet is on 6. Odds backed')
        # print(f'Money before: {money}')
        money -= 12
        money -= 10
        bets_on_table += 12
        bets_on_table += 10
        # print(f'Money after: {money}')
        print_money_status()
    # If point is not a 6 or 8, place a random bet on 6 or 8, no odds
    else:
        coin_flip = random.randint(1,2)
        if coin_flip % 2 == 0:
            bet_on_8 = True
            print(f'Point established on {point}, betting on 8')
            # print(f'Money before: {money}')
            money -= 12
            bets_on_table += 12
            print_money_status()
            # print(f'Money after: {money}')
        else:
            bet_on_6 = True
            print(f'Point established on {point}, betting on 6')
            # print(f'Money before: {money}')
            money -= 12
            bets_on_table += 12
            print_money_status()
            # print(f'Money after: {money}')

    reset_roll() # Simulates stickman giving dice back to shooter

    shoot_dice() # Roll with point on

    # Point established logic
    while (point_on and total_rolls < limit):
        print('\nRolling with point established')
        rolls_with_point_established()
    
    if not point_on:
        print('Point is off, come out\n')
        continue

# print_game_status()

# if money < initial_money:
#     print('Lost money :(')
# else:
#     print('Gained or broke even')