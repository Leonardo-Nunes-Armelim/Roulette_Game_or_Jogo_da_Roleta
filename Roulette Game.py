import pygame as pg
import random as rd

# Cores do Jogo
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_red = (180, 0, 0)
green = (0, 255, 0)
dark_green = (0, 180, 0)
blue = (0, 0, 255)
gray = (75, 75, 75)

# Setup da tela do Jogo
window = pg.display.set_mode((1130, 600))
window.fill(dark_green)

# Inicializando fonte
pg.font.init()
# Escolhendo uma fonte e tamanho
font = pg.font.SysFont("Times New Roman", 25)
font_coins = pg.font.SysFont("Times New Roman", 40)
font_bet = pg.font.SysFont("Times New Roman", 100)
font_spin = pg.font.SysFont("Times New Roman", 50)

# Board
def board(window, number, number_1, number_2, number_3, number_4, number_5):
    # Table
    pg.draw.rect(window, white, (8, 8, 717, 330), 1)
    # 0
    pg.draw.rect(window, dark_green, (10, 10, 50, 224))
    pg.draw.rect(window, white, (10, 10, 50, 224), 1)
    text_0 = font.render('0', True, white)
    text_0 = pg.transform.rotate(text_0, 90)
    window.blit(text_0, (20, 115))
    # 1
    pg.draw.rect(window, red, (61, 160, 50, 74))
    pg.draw.rect(window, white, (61, 160, 50, 74), 1)
    text_1 = font.render('1', True, white)
    text_1 = pg.transform.rotate(text_1, 90)
    window.blit(text_1, (70, 190))
    # 2
    pg.draw.rect(window, black, (61, 85, 50, 74))
    pg.draw.rect(window, white, (61, 85, 50, 74), 1)
    text_2 = font.render('2', True, white)
    text_2 = pg.transform.rotate(text_2, 90)
    window.blit(text_2, (70, 115))
    # 3
    pg.draw.rect(window, red, (61, 10, 50, 74))
    pg.draw.rect(window, white, (61, 10, 50, 74), 1)
    text_3 = font.render('3', True, white)
    text_3 = pg.transform.rotate(text_3, 90)
    window.blit(text_3, (70, 40))
    # 4
    pg.draw.rect(window, black, (112, 160, 50, 74))
    pg.draw.rect(window, white, (112, 160, 50, 74), 1)
    text_4 = font.render('4', True, white)
    text_4 = pg.transform.rotate(text_4, 90)
    window.blit(text_4, (121, 190))
    # 5
    pg.draw.rect(window, red, (112, 85, 50, 74))
    pg.draw.rect(window, white, (112, 85, 50, 74), 1)
    text_5 = font.render('5', True, white)
    text_5 = pg.transform.rotate(text_5, 90)
    window.blit(text_5, (121, 115))
    # 6
    pg.draw.rect(window, black, (112, 10, 50, 74))
    pg.draw.rect(window, white, (112, 10, 50, 74), 1)
    text_6 = font.render('6', True, white)
    text_6 = pg.transform.rotate(text_6, 90)
    window.blit(text_6, (121, 40))
    # 7
    pg.draw.rect(window, red, (163, 160, 50, 74))
    pg.draw.rect(window, white, (163, 160, 50, 74), 1)
    text_7 = font.render('7', True, white)
    text_7 = pg.transform.rotate(text_7, 90)
    window.blit(text_7, (172, 190))
    # 8
    pg.draw.rect(window, black, (163, 85, 50, 74))
    pg.draw.rect(window, white, (163, 85, 50, 74), 1)
    text_8 = font.render('8', True, white)
    text_8 = pg.transform.rotate(text_8, 90)
    window.blit(text_8, (172, 115))
    # 9
    pg.draw.rect(window, red, (163, 10, 50, 74))
    pg.draw.rect(window, white, (163, 10, 50, 74), 1)
    text_9 = font.render('9', True, white)
    text_9 = pg.transform.rotate(text_9, 90)
    window.blit(text_9, (172, 40))
    # 10
    pg.draw.rect(window, black, (214, 160, 50, 74))
    pg.draw.rect(window, white, (214, 160, 50, 74), 1)
    text_10 = font.render('10', True, white)
    text_10 = pg.transform.rotate(text_10, 90)
    window.blit(text_10, (223, 185))
    # 11
    pg.draw.rect(window, black, (214, 85, 50, 74))
    pg.draw.rect(window, white, (214, 85, 50, 74), 1)
    text_11 = font.render('11', True, white)
    text_11 = pg.transform.rotate(text_11, 90)
    window.blit(text_11, (223, 110))
    # 12
    pg.draw.rect(window, red, (214, 10, 50, 74))
    pg.draw.rect(window, white, (214, 10, 50, 74), 1)
    text_12 = font.render('12', True, white)
    text_12 = pg.transform.rotate(text_12, 90)
    window.blit(text_12, (223, 35))
    # 13
    pg.draw.rect(window, black, (265, 160, 50, 74))
    pg.draw.rect(window, white, (265, 160, 50, 74), 1)
    text_13 = font.render('13', True, white)
    text_13 = pg.transform.rotate(text_13, 90)
    window.blit(text_13, (274, 185))
    # 14
    pg.draw.rect(window, red, (265, 85, 50, 74))
    pg.draw.rect(window, white, (265, 85, 50, 74), 1)
    text_14 = font.render('14', True, white)
    text_14 = pg.transform.rotate(text_14, 90)
    window.blit(text_14, (274, 110))
    # 15
    pg.draw.rect(window, black, (265, 10, 50, 74))
    pg.draw.rect(window, white, (265, 10, 50, 74), 1)
    text_15 = font.render('15', True, white)
    text_15 = pg.transform.rotate(text_15, 90)
    window.blit(text_15, (274, 35))
    # 16
    pg.draw.rect(window, red, (316, 160, 50, 74))
    pg.draw.rect(window, white, (316, 160, 50, 74), 1)
    text_16 = font.render('16', True, white)
    text_16 = pg.transform.rotate(text_16, 90)
    window.blit(text_16, (325, 185))
    # 17
    pg.draw.rect(window, black, (316, 85, 50, 74))
    pg.draw.rect(window, white, (316, 85, 50, 74), 1)
    text_17 = font.render('17', True, white)
    text_17 = pg.transform.rotate(text_17, 90)
    window.blit(text_17, (325, 110))
    # 18
    pg.draw.rect(window, red, (316, 10, 50, 74))
    pg.draw.rect(window, white, (316, 10, 50, 74), 1)
    text_18 = font.render('18', True, white)
    text_18 = pg.transform.rotate(text_18, 90)
    window.blit(text_18, (325, 35))
    # 19
    pg.draw.rect(window, red, (367, 160, 50, 74))
    pg.draw.rect(window, white, (367, 160, 50, 74), 1)
    text_19 = font.render('19', True, white)
    text_19 = pg.transform.rotate(text_19, 90)
    window.blit(text_19, (376, 185))
    # 20
    pg.draw.rect(window, black, (367, 85, 50, 74))
    pg.draw.rect(window, white, (367, 85, 50, 74), 1)
    text_20 = font.render('20', True, white)
    text_20 = pg.transform.rotate(text_20, 90)
    window.blit(text_20, (376, 110))
    # 21
    pg.draw.rect(window, red, (367, 10, 50, 74))
    pg.draw.rect(window, white, (367, 10, 50, 74), 1)
    text_21 = font.render('21', True, white)
    text_21 = pg.transform.rotate(text_21, 90)
    window.blit(text_21, (376, 35))
    # 22
    pg.draw.rect(window, black, (418, 160, 50, 74))
    pg.draw.rect(window, white, (418, 160, 50, 74), 1)
    text_22 = font.render('22', True, white)
    text_22 = pg.transform.rotate(text_22, 90)
    window.blit(text_22, (427, 185))
    # 23
    pg.draw.rect(window, red, (418, 85, 50, 74))
    pg.draw.rect(window, white, (418, 85, 50, 74), 1)
    text_23 = font.render('23', True, white)
    text_23 = pg.transform.rotate(text_23, 90)
    window.blit(text_23, (427, 110))
    # 24
    pg.draw.rect(window, black, (418, 10, 50, 74))
    pg.draw.rect(window, white, (418, 10, 50, 74), 1)
    text_24 = font.render('24', True, white)
    text_24 = pg.transform.rotate(text_24, 90)
    window.blit(text_24, (427, 35))
    # 25
    pg.draw.rect(window, red, (469, 160, 50, 74))
    pg.draw.rect(window, white, (469, 160, 50, 74), 1)
    text_25 = font.render('25', True, white)
    text_25 = pg.transform.rotate(text_25, 90)
    window.blit(text_25, (478, 185))
    # 26
    pg.draw.rect(window, black, (469, 85, 50, 74))
    pg.draw.rect(window, white, (469, 85, 50, 74), 1)
    text_26 = font.render('26', True, white)
    text_26 = pg.transform.rotate(text_26, 90)
    window.blit(text_26, (478, 110))
    # 27
    pg.draw.rect(window, red, (469, 10, 50, 74))
    pg.draw.rect(window, white, (469, 10, 50, 74), 1)
    text_27 = font.render('27', True, white)
    text_27 = pg.transform.rotate(text_27, 90)
    window.blit(text_27, (478, 35))
    # 28
    pg.draw.rect(window, black, (520, 160, 50, 74))
    pg.draw.rect(window, white, (520, 160, 50, 74), 1)
    text_28 = font.render('28', True, white)
    text_28 = pg.transform.rotate(text_28, 90)
    window.blit(text_28, (529, 185))
    # 29
    pg.draw.rect(window, black, (520, 85, 50, 74))
    pg.draw.rect(window, white, (520, 85, 50, 74), 1)
    text_29 = font.render('29', True, white)
    text_29 = pg.transform.rotate(text_29, 90)
    window.blit(text_29, (529, 110))
    # 30
    pg.draw.rect(window, red, (520, 10, 50, 74))
    pg.draw.rect(window, white, (520, 10, 50, 74), 1)
    text_30 = font.render('30', True, white)
    text_30 = pg.transform.rotate(text_30, 90)
    window.blit(text_30, (529, 35))
    # 31
    pg.draw.rect(window, black, (571, 160, 50, 74))
    pg.draw.rect(window, white, (571, 160, 50, 74), 1)
    text_31 = font.render('31', True, white)
    text_31 = pg.transform.rotate(text_31, 90)
    window.blit(text_31, (580, 185))
    # 32
    pg.draw.rect(window, red, (571, 85, 50, 74))
    pg.draw.rect(window, white, (571, 85, 50, 74), 1)
    text_32 = font.render('32', True, white)
    text_32 = pg.transform.rotate(text_32, 90)
    window.blit(text_32, (580, 110))
    # 33
    pg.draw.rect(window, black, (571, 10, 50, 74))
    pg.draw.rect(window, white, (571, 10, 50, 74), 1)
    text_33 = font.render('33', True, white)
    text_33 = pg.transform.rotate(text_33, 90)
    window.blit(text_33, (580, 35))
    # 34
    pg.draw.rect(window, red, (622, 160, 50, 74))
    pg.draw.rect(window, white, (622, 160, 50, 74), 1)
    text_34 = font.render('34', True, white)
    text_34 = pg.transform.rotate(text_34, 90)
    window.blit(text_34, (631, 185))
    # 35
    pg.draw.rect(window, black, (622, 85, 50, 74))
    pg.draw.rect(window, white, (622, 85, 50, 74), 1)
    text_35 = font.render('35', True, white)
    text_35 = pg.transform.rotate(text_35, 90)
    window.blit(text_35, (631, 110))
    # 36
    pg.draw.rect(window, red, (622, 10, 50, 74))
    pg.draw.rect(window, white, (622, 10, 50, 74), 1)
    text_36 = font.render('36', True, white)
    text_36 = pg.transform.rotate(text_36, 90)
    window.blit(text_36, (631, 35))
    # 1º
    pg.draw.rect(window, dark_green, (673, 160, 50, 74))
    pg.draw.rect(window, white, (673, 160, 50, 74), 1)
    text_1c = font.render('1º', True, white)
    text_1c = pg.transform.rotate(text_1c, 90)
    window.blit(text_1c, (682, 185))
    # 2º
    pg.draw.rect(window, dark_green, (673, 85, 50, 74))
    pg.draw.rect(window, white, (673, 85, 50, 74), 1)
    text_2c = font.render('2º', True, white)
    text_2c = pg.transform.rotate(text_2c, 90)
    window.blit(text_2c, (682, 110))
    # 3º
    pg.draw.rect(window, dark_green, (673, 10, 50, 74))
    pg.draw.rect(window, white, (673, 10, 50, 74), 1)
    text_3c = font.render('3º', True, white)
    text_3c = pg.transform.rotate(text_3c, 90)
    window.blit(text_3c, (682, 35))
    # 1st 12
    pg.draw.rect(window, dark_green, (61, 235, 203, 50))
    pg.draw.rect(window, white, (61, 235, 203, 50), 1)
    text_1st_12 = font.render('1st 12', True, white)
    window.blit(text_1st_12, (130, 245))
    # 1 to 18
    pg.draw.rect(window, dark_green, (61, 286, 101, 50))
    pg.draw.rect(window, white, (61, 286, 101, 50), 1)
    text_1_to_18 = font.render('1 to 18', True, white)
    window.blit(text_1_to_18, (75, 298))
    # Even
    pg.draw.rect(window, dark_green, (163, 286, 101, 50))
    pg.draw.rect(window, white, (163, 286, 101, 50), 1)
    text_even = font.render('EVEN', True, white)
    window.blit(text_even, (180, 298))
    # 2nd 12
    pg.draw.rect(window, dark_green, (265, 235, 203, 50))
    pg.draw.rect(window, white, (265, 235, 203, 50), 1)
    text_2nd_12 = font.render('2nd 12', True, white)
    window.blit(text_2nd_12, (334, 245))
    # Red
    pg.draw.rect(window, red, (265, 286, 101, 50))
    pg.draw.rect(window, white, (265, 286, 101, 50), 1)
    text_red = font.render('RED', True, white)
    window.blit(text_red, (290, 298))
    # Black
    pg.draw.rect(window, black, (367, 286, 101, 50))
    pg.draw.rect(window, white, (367, 286, 101, 50), 1)
    text_black = font.render('BLACK', True, white)
    window.blit(text_black, (375, 298))
    # 3rd 12
    pg.draw.rect(window, dark_green, (469, 235, 203, 50))
    pg.draw.rect(window, white, (469, 235, 203, 50), 1)
    text_3rd_12 = font.render('3rd 12', True, white)
    window.blit(text_3rd_12, (538, 245))
    # Odd
    pg.draw.rect(window, dark_green, (469, 286, 101, 50))
    pg.draw.rect(window, white, (469, 286, 101, 50), 1)
    text_odd = font.render('ODD', True, white)
    window.blit(text_odd, (492, 298))
    # 19 to 36
    pg.draw.rect(window, dark_green, (571, 286, 101, 50))
    pg.draw.rect(window, white, (571, 286, 101, 50), 1)
    text_19_to_36 = font.render('19 to 36', True, white)
    window.blit(text_19_to_36, (578, 298))
    # Money Square
    pg.draw.rect(window, white, (8, 488, 1114, 104), 1)
    # $1
    pg.draw.rect(window, dark_green, (10, 490, 100, 100))
    pg.draw.rect(window, white, (10, 490, 100, 100), 1)
    text_1_coin = font_coins.render('$1', True, white)
    window.blit(text_1_coin, (40, 520))
    # $5
    pg.draw.rect(window, dark_green, (111, 490, 100, 100))
    pg.draw.rect(window, white, (111, 490, 100, 100), 1)
    text_5_coins = font_coins.render('$5', True, white)
    window.blit(text_5_coins, (141, 520))
    # $10
    pg.draw.rect(window, dark_green, (212, 490, 100, 100))
    pg.draw.rect(window, white, (212, 490, 100, 100), 1)
    text_10_coins = font_coins.render('$10', True, white)
    window.blit(text_10_coins, (235, 520))
    # $25
    pg.draw.rect(window, dark_green, (313, 490, 100, 100))
    pg.draw.rect(window, white, (313, 490, 100, 100), 1)
    text_25_coins = font_coins.render('$25', True, white)
    window.blit(text_25_coins, (335, 520))
    # $50
    pg.draw.rect(window, dark_green, (414, 490, 100, 100))
    pg.draw.rect(window, white, (414, 490, 100, 100), 1)
    text_50_coins = font_coins.render('$50', True, white)
    window.blit(text_50_coins, (435, 520))
    # $100
    pg.draw.rect(window, dark_green, (515, 490, 100, 100))
    pg.draw.rect(window, white, (515, 490, 100, 100), 1)
    text_100_coins = font_coins.render('$100', True, white)
    window.blit(text_100_coins, (525, 520))
    # $250
    pg.draw.rect(window, dark_green, (616, 490, 100, 100))
    pg.draw.rect(window, white, (616, 490, 100, 100), 1)
    text_150_coins = font_coins.render('$250', True, white)
    window.blit(text_150_coins, (626, 520))
    # $500
    pg.draw.rect(window, dark_green, (717, 490, 100, 100))
    pg.draw.rect(window, white, (717, 490, 100, 100), 1)
    text_500_coins = font_coins.render('$500', True, white)
    window.blit(text_500_coins, (727, 520))
    # $1.000
    pg.draw.rect(window, dark_green, (818, 490, 100, 100))
    pg.draw.rect(window, white, (818, 490, 100, 100), 1)
    text_1000_coins = font_coins.render('$1K', True, white)
    window.blit(text_1000_coins, (835, 520))
    # $5.000
    pg.draw.rect(window, dark_green, (919, 490, 100, 100))
    pg.draw.rect(window, white, (919, 490, 100, 100), 1)
    text_5000_coins = font_coins.render('$5K', True, white)
    window.blit(text_5000_coins, (935, 520))
    # $10.000
    pg.draw.rect(window, dark_green, (1020, 490, 100, 100))
    pg.draw.rect(window, white, (1020, 490, 100, 100), 1)
    text_10000_coins = font_coins.render('$10K', True, white)
    window.blit(text_10000_coins, (1025, 520))
    # Players Score
    pg.draw.rect(window, white, (726, 8, 396, 207), 1)
    pg.draw.rect(window, dark_green, (728, 10, 392, 50))
    pg.draw.rect(window, white, (728, 10, 392, 50), 1)
    text_ps_title = font.render('Players Score', True, white)
    window.blit(text_ps_title, (850, 20))
    # Players 1 Score
    pg.draw.rect(window, dark_green, (728, 61, 235, 50))
    pg.draw.rect(window, white, (728, 61, 235, 50), 1)
    text_ps1_title = font.render('Players 1: $', True, white)
    window.blit(text_ps1_title, (735, 73))
    pg.draw.rect(window, dark_green, (964, 61, 156, 50))
    pg.draw.rect(window, white, (964, 61, 156, 50), 1)
    # Players 2 Score
    pg.draw.rect(window, dark_green, (728, 112, 235, 50))
    pg.draw.rect(window, white, (728, 112, 235, 50), 1)
    text_ps2_title = font.render('Players 2: $', True, white)
    window.blit(text_ps2_title, (735, 123))
    pg.draw.rect(window, dark_green, (964, 112, 156, 50))
    pg.draw.rect(window, white, (964, 112, 156, 50), 1)
    # Players 3 Score
    pg.draw.rect(window, dark_green, (728, 163, 235, 50))
    pg.draw.rect(window, white, (728, 163, 235, 50), 1)
    text_ps3_title = font.render('Players 3: $', True, white)
    window.blit(text_ps3_title, (735, 173))
    pg.draw.rect(window, dark_green, (964, 163, 156, 50))
    pg.draw.rect(window, white, (964, 163, 156, 50), 1)
    # Bet
    pg.draw.rect(window, dark_green, (8, 339, 717, 148))
    pg.draw.rect(window, white, (8, 339, 717, 148), 1)
    text_bet_title = font_bet.render('Bet: $', True, white)
    window.blit(text_bet_title, (20, 360))
    # Spin Number
    pg.draw.rect(window, white, (726, 216, 396, 271), 1)
    if number == 0:
        pg.draw.rect(window, dark_green, (728, 218, 200, 200))
        pg.draw.rect(window, white, (728, 218, 200, 200), 1)
    elif number in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        pg.draw.rect(window, black, (728, 218, 200, 200))
        pg.draw.rect(window, white, (728, 218, 200, 200), 1)
    else:
        pg.draw.rect(window, red, (728, 218, 200, 200))
        pg.draw.rect(window, white, (728, 218, 200, 200), 1)
    if number >= 10:
        text_spin = font_bet.render(str(number), True, white)
        window.blit(text_spin, (776, 266))
    else:
        text_spin = font_bet.render(str(number), True, white)
        window.blit(text_spin, (800, 266))
    # Spin
    pg.draw.rect(window, dark_green, (929, 218, 191, 99))
    pg.draw.rect(window, white, (929, 218, 191, 99), 1)
    text_end_bet = font.render('Spin', True, white)
    window.blit(text_end_bet, (995, 250))
    # End Bets
    pg.draw.rect(window, dark_green, (929, 318, 191, 100))
    pg.draw.rect(window, white, (929, 318, 191, 100), 1)
    text_end_bet = font.render('Finish Bet', True, white)
    window.blit(text_end_bet, (970, 355))
    # Last Numbers Drawn 1º
    if number_1 == 0:
        pg.draw.rect(window, dark_green, (1042, 419, 78, 66))
        pg.draw.rect(window, white, (1042, 419, 78, 66), 1)
        text_number_1 = font_coins.render(str(number_1), True, white)
        window.blit(text_number_1, (1070, 430))
    elif number_1 in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        pg.draw.rect(window, black, (1042, 419, 78, 66))
        pg.draw.rect(window, white, (1042, 419, 78, 66), 1)
        if number_1 >= 10:
            text_number_1 = font_coins.render(str(number_1), True, white)
            window.blit(text_number_1, (1060, 430))
        else:
            text_number_1 = font_coins.render(str(number_1), True, white)
            window.blit(text_number_1, (1070, 430))
    else:
        pg.draw.rect(window, red, (1042, 419, 78, 66))
        pg.draw.rect(window, white, (1042, 419, 78, 66), 1)
        if number_1 >= 10:
            text_number_1 = font_coins.render(str(number_1), True, white)
            window.blit(text_number_1, (1060, 430))
        else:
            text_number_1 = font_coins.render(str(number_1), True, white)
            window.blit(text_number_1, (1070, 430))
    # Last Numbers Drawn 2º
    if number_2 == 0:
        pg.draw.rect(window, dark_green, (962, 419, 79, 66))
        pg.draw.rect(window, white, (962, 419, 79, 66), 1)
        text_number_2 = font_coins.render(str(number_2), True, white)
        window.blit(text_number_2, (991, 430))
    elif number_2 in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        pg.draw.rect(window, black, (962, 419, 79, 66))
        pg.draw.rect(window, white, (962, 419, 79, 66), 1)
        if number_2 >= 10:
            text_number_2 = font_coins.render(str(number_2), True, white)
            window.blit(text_number_2, (981, 430))
        else:
            text_number_2 = font_coins.render(str(number_2), True, white)
            window.blit(text_number_2, (991, 430))
    else:
        pg.draw.rect(window, red, (962, 419, 79, 66))
        pg.draw.rect(window, white, (962, 419, 79, 66), 1)
        if number_2 >= 10:
            text_number_2 = font_coins.render(str(number_2), True, white)
            window.blit(text_number_2, (981, 430))
        else:
            text_number_2 = font_coins.render(str(number_2), True, white)
            window.blit(text_number_2, (991, 430))
    # Last Numbers Drawn 3º
    if number_3 == 0:
        pg.draw.rect(window, dark_green, (883, 419, 79, 66))
        pg.draw.rect(window, white, (883, 419, 79, 66), 1)
        text_number_3 = font_coins.render(str(number_3), True, white)
        window.blit(text_number_3, (912, 430))
    elif number_3 in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        pg.draw.rect(window, black, (883, 419, 79, 66))
        pg.draw.rect(window, white, (883, 419, 79, 66), 1)
        if number_3 >= 10:
            text_number_3 = font_coins.render(str(number_3), True, white)
            window.blit(text_number_3, (902, 430))
        else:
            text_number_3 = font_coins.render(str(number_3), True, white)
            window.blit(text_number_3, (912, 430))
    else:
        pg.draw.rect(window, red, (883, 419, 79, 66))
        pg.draw.rect(window, white, (883, 419, 79, 66), 1)
        if number_3 >= 10:
            text_number_3 = font_coins.render(str(number_3), True, white)
            window.blit(text_number_3, (902, 430))
        else:
            text_number_3 = font_coins.render(str(number_3), True, white)
            window.blit(text_number_3, (912, 430))
    # Last Numbers Drawn 4º
    if number_4 == 0:
        pg.draw.rect(window, dark_green, (806, 419, 77, 66))
        pg.draw.rect(window, white, (806, 419, 77, 66), 1)
        text_number_4 = font_coins.render(str(number_4), True, white)
        window.blit(text_number_4, (835, 430))
    elif number_4 in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        pg.draw.rect(window, black, (806, 419, 77, 66))
        pg.draw.rect(window, white, (806, 419, 77, 66), 1)
        if number_4 >= 10:
            text_number_4 = font_coins.render(str(number_4), True, white)
            window.blit(text_number_4, (825, 430))
        else:
            text_number_4 = font_coins.render(str(number_4), True, white)
            window.blit(text_number_4, (835, 430))
    else:
        pg.draw.rect(window, red, (806, 419, 77, 66))
        pg.draw.rect(window, white, (806, 419, 77, 66), 1)
        if number_4 >= 10:
            text_number_4 = font_coins.render(str(number_4), True, white)
            window.blit(text_number_4, (825, 430))
        else:
            text_number_4 = font_coins.render(str(number_4), True, white)
            window.blit(text_number_4, (835, 430))
    # Last Numbers Drawn 5º
    if number_5 == 0:
        pg.draw.rect(window, dark_green, (728, 419, 77, 66))
        pg.draw.rect(window, white, (728, 419, 77, 66), 1)
        text_number_5 = font_coins.render(str(number_5), True, white)
        window.blit(text_number_5, (758, 430))
    elif number_5 in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        pg.draw.rect(window, black, (728, 419, 77, 66))
        pg.draw.rect(window, white, (728, 419, 77, 66), 1)
        if number_5 >= 10:
            text_number_5 = font_coins.render(str(number_5), True, white)
            window.blit(text_number_5, (748, 430))
        else:
            text_number_5 = font_coins.render(str(number_5), True, white)
            window.blit(text_number_5, (758, 430))
    else:
        pg.draw.rect(window, red, (728, 419, 77, 66))
        pg.draw.rect(window, white, (728, 419, 77, 66), 1)
        if number_5 >= 10:
            text_number_5 = font_coins.render(str(number_5), True, white)
            window.blit(text_number_5, (748, 430))
        else:
            text_number_5 = font_coins.render(str(number_5), True, white)
            window.blit(text_number_5, (758, 430))

def board_hover(window):
    # 0
    if mouse_x >= 10 and mouse_x <= 60 and mouse_y >= 10 and mouse_y <= 234:
        pg.draw.rect(window, green, (10, 10, 50, 224))
        pg.draw.rect(window, white, (10, 10, 50, 224), 1)
        text_0 = font.render('0', True, white)
        text_0 = pg.transform.rotate(text_0, 90)
        window.blit(text_0, (20, 115))
    # 1
    if mouse_x >= 61 and mouse_x <= 111 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, dark_red, (61, 160, 50, 74))
        pg.draw.rect(window, white, (61, 160, 50, 74), 1)
        text_1 = font.render('1', True, white)
        text_1 = pg.transform.rotate(text_1, 90)
        window.blit(text_1, (70, 190))
    # 2
    if mouse_x >= 61 and mouse_x <= 111 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, gray, (61, 85, 50, 74))
        pg.draw.rect(window, white, (61, 85, 50, 74), 1)
        text_2 = font.render('2', True, white)
        text_2 = pg.transform.rotate(text_2, 90)
        window.blit(text_2, (70, 115))
    # 3
    if mouse_x >= 61 and mouse_x <= 111 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, dark_red, (61, 10, 50, 74))
        pg.draw.rect(window, white, (61, 10, 50, 74), 1)
        text_3 = font.render('3', True, white)
        text_3 = pg.transform.rotate(text_3, 90)
        window.blit(text_3, (70, 40))
    # 4
    if mouse_x >= 112 and mouse_x <= 162 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, gray, (112, 160, 50, 74))
        pg.draw.rect(window, white, (112, 160, 50, 74), 1)
        text_4 = font.render('4', True, white)
        text_4 = pg.transform.rotate(text_4, 90)
        window.blit(text_4, (121, 190))
    # 5
    if mouse_x >= 112 and mouse_x <= 162 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, dark_red, (112, 85, 50, 74))
        pg.draw.rect(window, white, (112, 85, 50, 74), 1)
        text_5 = font.render('5', True, white)
        text_5 = pg.transform.rotate(text_5, 90)
        window.blit(text_5, (121, 115))
    # 6
    if mouse_x >= 112 and mouse_x <= 162 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, gray, (112, 10, 50, 74))
        pg.draw.rect(window, white, (112, 10, 50, 74), 1)
        text_6 = font.render('6', True, white)
        text_6 = pg.transform.rotate(text_6, 90)
        window.blit(text_6, (121, 40))
    # 7
    if mouse_x >= 163 and mouse_x <= 213 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, dark_red, (163, 160, 50, 74))
        pg.draw.rect(window, white, (163, 160, 50, 74), 1)
        text_7 = font.render('7', True, white)
        text_7 = pg.transform.rotate(text_7, 90)
        window.blit(text_7, (172, 190))
    # 8
    if mouse_x >= 163 and mouse_x <= 213 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, gray, (163, 85, 50, 74))
        pg.draw.rect(window, white, (163, 85, 50, 74), 1)
        text_8 = font.render('8', True, white)
        text_8 = pg.transform.rotate(text_8, 90)
        window.blit(text_8, (172, 115))
    # 9
    if mouse_x >= 163 and mouse_x <= 213 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, dark_red, (163, 10, 50, 74))
        pg.draw.rect(window, white, (163, 10, 50, 74), 1)
        text_9 = font.render('9', True, white)
        text_9 = pg.transform.rotate(text_9, 90)
        window.blit(text_9, (172, 40))
    # 10
    if mouse_x >= 214 and mouse_x <= 264 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, gray, (214, 160, 50, 74))
        pg.draw.rect(window, white, (214, 160, 50, 74), 1)
        text_10 = font.render('10', True, white)
        text_10 = pg.transform.rotate(text_10, 90)
        window.blit(text_10, (223, 185))
    # 11
    if mouse_x >= 214 and mouse_x <= 264 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, gray, (214, 85, 50, 74))
        pg.draw.rect(window, white, (214, 85, 50, 74), 1)
        text_11 = font.render('11', True, white)
        text_11 = pg.transform.rotate(text_11, 90)
        window.blit(text_11, (223, 110))
    # 12
    if mouse_x >= 214 and mouse_x <= 264 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, dark_red, (214, 10, 50, 74))
        pg.draw.rect(window, white, (214, 10, 50, 74), 1)
        text_12 = font.render('12', True, white)
        text_12 = pg.transform.rotate(text_12, 90)
        window.blit(text_12, (223, 35))
    # 13
    if mouse_x >= 265 and mouse_x <= 315 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, gray, (265, 160, 50, 74))
        pg.draw.rect(window, white, (265, 160, 50, 74), 1)
        text_13 = font.render('13', True, white)
        text_13 = pg.transform.rotate(text_13, 90)
        window.blit(text_13, (274, 185))
    # 14
    if mouse_x >= 265 and mouse_x <= 315 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, dark_red, (265, 85, 50, 74))
        pg.draw.rect(window, white, (265, 85, 50, 74), 1)
        text_14 = font.render('14', True, white)
        text_14 = pg.transform.rotate(text_14, 90)
        window.blit(text_14, (274, 110))
    # 15
    if mouse_x >= 265 and mouse_x <= 315 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, gray, (265, 10, 50, 74))
        pg.draw.rect(window, white, (265, 10, 50, 74), 1)
        text_15 = font.render('15', True, white)
        text_15 = pg.transform.rotate(text_15, 90)
        window.blit(text_15, (274, 35))
    # 16
    if mouse_x >= 316 and mouse_x <= 366 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, dark_red, (316, 160, 50, 74))
        pg.draw.rect(window, white, (316, 160, 50, 74), 1)
        text_16 = font.render('16', True, white)
        text_16 = pg.transform.rotate(text_16, 90)
        window.blit(text_16, (325, 185))
    # 17
    if mouse_x >= 316 and mouse_x <= 366 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, gray, (316, 85, 50, 74))
        pg.draw.rect(window, white, (316, 85, 50, 74), 1)
        text_17 = font.render('17', True, white)
        text_17 = pg.transform.rotate(text_17, 90)
        window.blit(text_17, (325, 110))
    # 18
    if mouse_x >= 316 and mouse_x <= 366 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, dark_red, (316, 10, 50, 74))
        pg.draw.rect(window, white, (316, 10, 50, 74), 1)
        text_18 = font.render('18', True, white)
        text_18 = pg.transform.rotate(text_18, 90)
        window.blit(text_18, (325, 35))
    # 19
    if mouse_x >= 367 and mouse_x <= 417 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, dark_red, (367, 160, 50, 74))
        pg.draw.rect(window, white, (367, 160, 50, 74), 1)
        text_19 = font.render('19', True, white)
        text_19 = pg.transform.rotate(text_19, 90)
        window.blit(text_19, (376, 185))
    # 20
    if mouse_x >= 367 and mouse_x <= 417 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, gray, (367, 85, 50, 74))
        pg.draw.rect(window, white, (367, 85, 50, 74), 1)
        text_20 = font.render('20', True, white)
        text_20 = pg.transform.rotate(text_20, 90)
        window.blit(text_20, (376, 110))
    # 21
    if mouse_x >= 367 and mouse_x <= 417 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, dark_red, (367, 10, 50, 74))
        pg.draw.rect(window, white, (367, 10, 50, 74), 1)
        text_21 = font.render('21', True, white)
        text_21 = pg.transform.rotate(text_21, 90)
        window.blit(text_21, (376, 35))
    # 22
    if mouse_x >= 418 and mouse_x <= 468 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, gray, (418, 160, 50, 74))
        pg.draw.rect(window, white, (418, 160, 50, 74), 1)
        text_22 = font.render('22', True, white)
        text_22 = pg.transform.rotate(text_22, 90)
        window.blit(text_22, (427, 185))
    # 23
    if mouse_x >= 418 and mouse_x <= 468 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, dark_red, (418, 85, 50, 74))
        pg.draw.rect(window, white, (418, 85, 50, 74), 1)
        text_23 = font.render('23', True, white)
        text_23 = pg.transform.rotate(text_23, 90)
        window.blit(text_23, (427, 110))
    # 24
    if mouse_x >= 418 and mouse_x <= 468 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, gray, (418, 10, 50, 74))
        pg.draw.rect(window, white, (418, 10, 50, 74), 1)
        text_24 = font.render('24', True, white)
        text_24 = pg.transform.rotate(text_24, 90)
        window.blit(text_24, (427, 35))
    # 25
    if mouse_x >= 469 and mouse_x <= 519 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, dark_red, (469, 160, 50, 74))
        pg.draw.rect(window, white, (469, 160, 50, 74), 1)
        text_25 = font.render('25', True, white)
        text_25 = pg.transform.rotate(text_25, 90)
        window.blit(text_25, (478, 185))
    # 26
    if mouse_x >= 469 and mouse_x <= 519 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, gray, (469, 85, 50, 74))
        pg.draw.rect(window, white, (469, 85, 50, 74), 1)
        text_26 = font.render('26', True, white)
        text_26 = pg.transform.rotate(text_26, 90)
        window.blit(text_26, (478, 110))
    # 27
    if mouse_x >= 469 and mouse_x <= 519 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, dark_red, (469, 10, 50, 74))
        pg.draw.rect(window, white, (469, 10, 50, 74), 1)
        text_27 = font.render('27', True, white)
        text_27 = pg.transform.rotate(text_27, 90)
        window.blit(text_27, (478, 35))
    # 28
    if mouse_x >= 520 and mouse_x <= 570 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, gray, (520, 160, 50, 74))
        pg.draw.rect(window, white, (520, 160, 50, 74), 1)
        text_28 = font.render('28', True, white)
        text_28 = pg.transform.rotate(text_28, 90)
        window.blit(text_28, (529, 185))
    # 29
    if mouse_x >= 520 and mouse_x <= 570 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, gray, (520, 85, 50, 74))
        pg.draw.rect(window, white, (520, 85, 50, 74), 1)
        text_29 = font.render('29', True, white)
        text_29 = pg.transform.rotate(text_29, 90)
        window.blit(text_29, (529, 110))
    # 30
    if mouse_x >= 520 and mouse_x <= 570 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, dark_red, (520, 10, 50, 74))
        pg.draw.rect(window, white, (520, 10, 50, 74), 1)
        text_30 = font.render('30', True, white)
        text_30 = pg.transform.rotate(text_30, 90)
        window.blit(text_30, (529, 35))
    # 31
    if mouse_x >= 571 and mouse_x <= 621 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, gray, (571, 160, 50, 74))
        pg.draw.rect(window, white, (571, 160, 50, 74), 1)
        text_31 = font.render('31', True, white)
        text_31 = pg.transform.rotate(text_31, 90)
        window.blit(text_31, (580, 185))
    # 32
    if mouse_x >= 571 and mouse_x <= 621 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, dark_red, (571, 85, 50, 74))
        pg.draw.rect(window, white, (571, 85, 50, 74), 1)
        text_32 = font.render('32', True, white)
        text_32 = pg.transform.rotate(text_32, 90)
        window.blit(text_32, (580, 110))
    # 33
    if mouse_x >= 571 and mouse_x <= 621 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, gray, (571, 10, 50, 74))
        pg.draw.rect(window, white, (571, 10, 50, 74), 1)
        text_33 = font.render('33', True, white)
        text_33 = pg.transform.rotate(text_33, 90)
        window.blit(text_33, (580, 35))
    # 34
    if mouse_x >= 622 and mouse_x <= 672 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, dark_red, (622, 160, 50, 74))
        pg.draw.rect(window, white, (622, 160, 50, 74), 1)
        text_34 = font.render('34', True, white)
        text_34 = pg.transform.rotate(text_34, 90)
        window.blit(text_34, (631, 185))
    # 35
    if mouse_x >= 622 and mouse_x <= 672 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, gray, (622, 85, 50, 74))
        pg.draw.rect(window, white, (622, 85, 50, 74), 1)
        text_35 = font.render('35', True, white)
        text_35 = pg.transform.rotate(text_35, 90)
        window.blit(text_35, (631, 110))
    # 36
    if mouse_x >= 622 and mouse_x <= 672 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, dark_red, (622, 10, 50, 74))
        pg.draw.rect(window, white, (622, 10, 50, 74), 1)
        text_36 = font.render('36', True, white)
        text_36 = pg.transform.rotate(text_36, 90)
        window.blit(text_36, (631, 35))
    # 1º
    if mouse_x >= 673 and mouse_x <= 723 and mouse_y >= 160 and mouse_y <= 234:
        pg.draw.rect(window, green, (673, 160, 50, 74))
        pg.draw.rect(window, white, (673, 160, 50, 74), 1)
        text_1c = font.render('1º', True, white)
        text_1c = pg.transform.rotate(text_1c, 90)
        window.blit(text_1c, (682, 185))
    # 2º
    if mouse_x >= 673 and mouse_x <= 723 and mouse_y >= 85 and mouse_y <= 159:
        pg.draw.rect(window, green, (673, 85, 50, 74))
        pg.draw.rect(window, white, (673, 85, 50, 74), 1)
        text_2c = font.render('2º', True, white)
        text_2c = pg.transform.rotate(text_2c, 90)
        window.blit(text_2c, (682, 110))
    # 3º
    if mouse_x >= 673 and mouse_x <= 723 and mouse_y >= 10 and mouse_y <= 84:
        pg.draw.rect(window, green, (673, 10, 50, 74))
        pg.draw.rect(window, white, (673, 10, 50, 74), 1)
        text_3c = font.render('3º', True, white)
        text_3c = pg.transform.rotate(text_3c, 90)
        window.blit(text_3c, (682, 35))
    # 1st 12
    if mouse_x >= 61 and mouse_x <= 264 and mouse_y >= 235 and mouse_y <= 285:
        pg.draw.rect(window, green, (61, 235, 203, 50))
        pg.draw.rect(window, white, (61, 235, 203, 50), 1)
        text_1st_12 = font.render('1st 12', True, white)
        window.blit(text_1st_12, (130, 245))
    # 1 to 18
    if mouse_x >= 61 and mouse_x <= 162 and mouse_y >= 286 and mouse_y <= 336:
        pg.draw.rect(window, green, (61, 286, 101, 50))
        pg.draw.rect(window, white, (61, 286, 101, 50), 1)
        text_1_to_18 = font.render('1 to 18', True, white)
        window.blit(text_1_to_18, (75, 298))
    # Even
    if mouse_x >= 163 and mouse_x <= 264 and mouse_y >= 286 and mouse_y <= 336:
        pg.draw.rect(window, green, (163, 286, 101, 50))
        pg.draw.rect(window, white, (163, 286, 101, 50), 1)
        text_even = font.render('EVEN', True, white)
        window.blit(text_even, (180, 298))
    # 2nd 12
    if mouse_x >= 265 and mouse_x <= 468 and mouse_y >= 235 and mouse_y <= 285:
        pg.draw.rect(window, green, (265, 235, 203, 50))
        pg.draw.rect(window, white, (265, 235, 203, 50), 1)
        text_2nd_12 = font.render('2nd 12', True, white)
        window.blit(text_2nd_12, (334, 245))
    # Red
    if mouse_x >= 265 and mouse_x <= 366 and mouse_y >= 286 and mouse_y <= 336:
        pg.draw.rect(window, dark_red, (265, 286, 101, 50))
        pg.draw.rect(window, white, (265, 286, 101, 50), 1)
        text_red = font.render('RED', True, white)
        window.blit(text_red, (290, 298))
    # Black
    if mouse_x >= 367 and mouse_x <= 468 and mouse_y >= 286 and mouse_y <= 336:
        pg.draw.rect(window, gray, (367, 286, 101, 50))
        pg.draw.rect(window, white, (367, 286, 101, 50), 1)
        text_black = font.render('BLACK', True, white)
        window.blit(text_black, (375, 298))
    # 3rd 12
    if mouse_x >= 469 and mouse_x <= 672 and mouse_y >= 235 and mouse_y <= 285:
        pg.draw.rect(window, green, (469, 235, 203, 50))
        pg.draw.rect(window, white, (469, 235, 203, 50), 1)
        text_3rd_12 = font.render('3rd 12', True, white)
        window.blit(text_3rd_12, (538, 245))
    # Odd
    if mouse_x >= 469 and mouse_x <= 570 and mouse_y >= 286 and mouse_y <= 336:
        pg.draw.rect(window, green, (469, 286, 101, 50))
        pg.draw.rect(window, white, (469, 286, 101, 50), 1)
        text_odd = font.render('ODD', True, white)
        window.blit(text_odd, (492, 298))
    # 19 to 36
    if mouse_x >= 571 and mouse_x <= 672 and mouse_y >= 286 and mouse_y <= 336:
        pg.draw.rect(window, green, (571, 286, 101, 50))
        pg.draw.rect(window, white, (571, 286, 101, 50), 1)
        text_19_to_36 = font.render('19 to 36', True, white)
        window.blit(text_19_to_36, (578, 298))
    # $1
    if mouse_x >= 10 and mouse_x <= 110 and mouse_y >= 490 and mouse_y <= 590:
        pg.draw.rect(window, green, (10, 490, 100, 100))
        pg.draw.rect(window, white, (10, 490, 100, 100), 1)
        text_1_coin = font_coins.render('$1', True, white)
        window.blit(text_1_coin, (40, 520))
    # $5
    if mouse_x >= 111 and mouse_x <= 211 and mouse_y >= 490 and mouse_y <= 590:
        pg.draw.rect(window, green, (111, 490, 100, 100))
        pg.draw.rect(window, white, (111, 490, 100, 100), 1)
        text_1_coin = font_coins.render('$5', True, white)
        window.blit(text_1_coin, (141, 520))
    # $10
    if mouse_x >= 212 and mouse_x <= 312 and mouse_y >= 490 and mouse_y <= 590:
        pg.draw.rect(window, green, (212, 490, 100, 100))
        pg.draw.rect(window, white, (212, 490, 100, 100), 1)
        text_1_coin = font_coins.render('$10', True, white)
        window.blit(text_1_coin, (235, 520))
    # $25
    if mouse_x >= 313 and mouse_x <= 413 and mouse_y >= 490 and mouse_y <= 590:
        pg.draw.rect(window, green, (313, 490, 100, 100))
        pg.draw.rect(window, white, (313, 490, 100, 100), 1)
        text_1_coin = font_coins.render('$25', True, white)
        window.blit(text_1_coin, (335, 520))
    # $50
    if mouse_x >= 414 and mouse_x <= 514 and mouse_y >= 490 and mouse_y <= 590:
        pg.draw.rect(window, green, (414, 490, 100, 100))
        pg.draw.rect(window, white, (414, 490, 100, 100), 1)
        text_1_coin = font_coins.render('$50', True, white)
        window.blit(text_1_coin, (435, 520))
    # $100
    if mouse_x >= 515 and mouse_x <= 615 and mouse_y >= 490 and mouse_y <= 590:
        pg.draw.rect(window, green, (515, 490, 100, 100))
        pg.draw.rect(window, white, (515, 490, 100, 100), 1)
        text_1_coin = font_coins.render('$100', True, white)
        window.blit(text_1_coin, (525, 520))
    # $250
    if mouse_x >= 616 and mouse_x <= 716 and mouse_y >= 490 and mouse_y <= 590:
        pg.draw.rect(window, green, (616, 490, 100, 100))
        pg.draw.rect(window, white, (616, 490, 100, 100), 1)
        text_1_coin = font_coins.render('$250', True, white)
        window.blit(text_1_coin, (626, 520))
    # $500
    if mouse_x >= 717 and mouse_x <= 817 and mouse_y >= 490 and mouse_y <= 590:
        pg.draw.rect(window, green, (717, 490, 100, 100))
        pg.draw.rect(window, white, (717, 490, 100, 100), 1)
        text_1_coin = font_coins.render('$500', True, white)
        window.blit(text_1_coin, (727, 520))
    # $1.000
    if mouse_x >= 818 and mouse_x <= 918 and mouse_y >= 490 and mouse_y <= 590:
        pg.draw.rect(window, green, (818, 490, 100, 100))
        pg.draw.rect(window, white, (818, 490, 100, 100), 1)
        text_1_coin = font_coins.render('$1K', True, white)
        window.blit(text_1_coin, (835, 520))
    # $5.000
    if mouse_x >= 918 and mouse_x <= 1018 and mouse_y >= 490 and mouse_y <= 590:
        pg.draw.rect(window, green, (919, 490, 100, 100))
        pg.draw.rect(window, white, (919, 490, 100, 100), 1)
        text_1_coin = font_coins.render('$5K', True, white)
        window.blit(text_1_coin, (935, 520))
    # $10.000
    if mouse_x >= 1020 and mouse_x <= 1120 and mouse_y >= 490 and mouse_y <= 590:
        pg.draw.rect(window, green, (1020, 490, 100, 100))
        pg.draw.rect(window, white, (1020, 490, 100, 100), 1)
        text_1_coin = font_coins.render('$10K', True, white)
        window.blit(text_1_coin, (1025, 520))
    # Spin
    if mouse_x >= 929 and mouse_x <= 1120 and mouse_y >= 218 and mouse_y <= 317:
        pg.draw.rect(window, green, (929, 218, 191, 99))
        pg.draw.rect(window, white, (929, 218, 191, 99), 1)
        text_end_bet = font.render('Spin', True, white)
        window.blit(text_end_bet, (995, 250))
    # End Bets
    if mouse_x >= 929 and mouse_x <= 1120 and mouse_y >= 318 and mouse_y <= 418:
        pg.draw.rect(window, green, (929, 318, 191, 100))
        pg.draw.rect(window, white, (929, 318, 191, 100), 1)
        text_end_bet = font.render('Finish Bet', True, white)
        window.blit(text_end_bet, (970, 355))

def spin(last_click_right, click_right, number, mouse_x, mouse_y, number_1, number_2, number_3, number_4, number_5, player_1_delta, player_2_delta, player_3_delta):
    if click_right == True and last_click_right == False and mouse_x >= 929 and mouse_x <= 1120 and mouse_y >= 218 and mouse_y <= 317:
        number_5 = number_4
        number_4 = number_3
        number_3 = number_2
        number_2 = number_1
        number_1 = number
        number = rd.randint(0, 36)
        player_1_delta = 0
        player_2_delta = 0
        player_3_delta = 0
    else:
        number = number
    return number, number_1, number_2, number_3, number_4, number_5, player_1_delta, player_2_delta, player_3_delta

def finish_bet(last_click_right, click_right, mouse_x, mouse_y, chosed_bet, player_turn, bet_value):
    # End Bets
    chosed_bet = chosed_bet
    if mouse_x >= 929 and mouse_x <= 1120 and mouse_y >= 318 and mouse_y <= 418 and last_click_right == False and click_right == True:
        #pg.draw.rect(window, green, (929, 318, 191, 100))
        #pg.draw.rect(window, white, (929, 318, 191, 100), 1)
        #text_end_bet = font.render('Finish Bet', True, white)
        #window.blit(text_end_bet, (970, 355))
        chosed_bet = None
        if player_turn == 'player_1':
            player_turn = 'player_2'
        elif player_turn == 'player_2':
            player_turn = 'player_3'
        elif player_turn == 'player_3':
            player_turn = 'player_1'
        bet_value = 0
    return chosed_bet, player_turn, bet_value

def setup_money_numbers(bet_value, player_1_score, player_2_score, player_3_score, player_1_delta, player_2_delta, player_3_delta):
    # Bet Value
    if int(bet_value) <= 999:
        bet_value_str = str(bet_value)
    elif int(bet_value) <= 9999:
        bet_value_str = str(bet_value)[:1] + '.' + str(bet_value)[1:]
    elif int(bet_value) <= 99999:
        bet_value_str = str(bet_value)[:2] + '.' + str(bet_value)[2:]
    elif int(bet_value) <= 999999:
        bet_value_str = str(bet_value)[:3] + '.' + str(bet_value)[3:]
    elif int(bet_value) >= 1000000:
        bet_value_str = str(bet_value)[:1] + '.' + str(bet_value)[1:4] + '.' + str(bet_value)[4:]
    # Player 1 Score
    if player_1_score == 0:
        player_1_score_str = str(player_1_score)
    elif player_1_score <= 999:
        player_1_score_str = str(player_1_score)
    elif player_1_score <= 9999:
        player_1_score_str = str(player_1_score)[:1] + '.' + str(player_1_score)[1:]
    elif player_1_score <= 99999:
        player_1_score_str = str(player_1_score)[:2] + '.' + str(player_1_score)[2:]
    elif player_1_score <= 999999:
        player_1_score_str = str(player_1_score)[:3] + '.' + str(player_1_score)[3:]
    elif player_1_score >= 1000000:
        player_1_score_str = str(player_1_score)[:1] + '.' + str(player_1_score)[1:4] + '.' + str(player_1_score)[4:]
    # Player 2 Score
    if player_2_score == 0:
        player_2_score_str = str(player_2_score)
    elif player_2_score <= 999:
        player_2_score_str = str(player_2_score)
    elif player_2_score <= 9999:
        player_2_score_str = str(player_2_score)[:1] + '.' + str(player_2_score)[1:]
    elif player_2_score <= 99999:
        player_2_score_str = str(player_2_score)[:2] + '.' + str(player_2_score)[2:]
    elif player_2_score <= 999999:
        player_2_score_str = str(player_2_score)[:3] + '.' + str(player_2_score)[3:]
    elif player_2_score >= 1000000:
        player_2_score_str = str(player_2_score)[:1] + '.' + str(player_2_score)[1:4] + '.' + str(player_2_score)[4:]
    # Player 3 Score
    if player_3_score == 0:
        player_3_score_str = str(player_3_score)
    elif player_3_score <= 999:
        player_3_score_str = str(player_3_score)
    elif player_3_score <= 9999:
        player_3_score_str = str(player_3_score)[:1] + '.' + str(player_3_score)[1:]
    elif player_3_score <= 99999:
        player_3_score_str = str(player_3_score)[:2] + '.' + str(player_3_score)[2:]
    elif player_3_score <= 999999:
        player_3_score_str = str(player_3_score)[:3] + '.' + str(player_3_score)[3:]
    elif player_3_score >= 1000000:
        player_3_score_str = str(player_3_score)[:1] + '.' + str(player_3_score)[1:4] + '.' + str(player_3_score)[4:]
    # Player 1 Delta
    if player_1_delta <= -1000000:
        player_1_delta_str = '-' + str(player_1_delta * (-1))[:1] + '.' + str(player_1_delta * (-1))[1:4] + '.' + str(player_1_delta * (-1))[4:]
    elif player_1_delta <= -100000:
        player_1_delta_str = '-' + str(player_1_delta * (-1))[:3] + '.' + str(player_1_delta * (-1))[3:]
    elif player_1_delta <= -10000:
        player_1_delta_str = '-' + str(player_1_delta * (-1))[:2] + '.' + str(player_1_delta * (-1))[2:]
    elif player_1_delta <= -1000:
        player_1_delta_str = '-' + str(player_1_delta * (-1))[:1] + '.' + str(player_1_delta * (-1))[1:]
    elif player_1_delta >= -999 and player_1_delta < 0:
        player_1_delta_str = str(player_1_delta)
    elif player_1_delta == 0:
        player_1_delta_str = str(player_1_delta)
    elif player_1_delta <= 999 and player_1_delta > 0:
        player_1_delta_str = '+' + str(player_1_delta)
    elif player_1_delta <= 9999 and player_1_delta > 0:
        player_1_delta_str = '+' + str(player_1_delta)[:1] + '.' + str(player_1_delta)[1:]
    elif player_1_delta <= 99999 and player_1_delta > 0:
        player_1_delta_str = '+' + str(player_1_delta)[:2] + '.' + str(player_1_delta)[2:]
    elif player_1_delta <= 999999 and player_1_delta > 0:
        player_1_delta_str = '+' + str(player_1_delta)[:3] + '.' + str(player_1_delta)[3:]
    elif player_1_delta >= 1000000:
        player_1_delta_str = '+' + str(player_1_delta)[:1] + '.' + str(player_1_delta)[1:4] + '.' + str(player_1_delta)[4:]
    # Player 2 Delta
    if player_2_delta <= -1000000:
        player_2_delta_str = '-' + str(player_2_delta * (-1))[:1] + '.' + str(player_2_delta * (-1))[1:4] + '.' + str(player_2_delta * (-1))[4:]
    elif player_2_delta <= -100000:
        player_2_delta_str = '-' + str(player_2_delta * (-1))[:3] + '.' + str(player_2_delta * (-1))[3:]
    elif player_2_delta <= -10000:
        player_2_delta_str = '-' + str(player_2_delta * (-1))[:2] + '.' + str(player_2_delta * (-1))[2:]
    elif player_2_delta <= -1000:
        player_2_delta_str = '-' + str(player_2_delta * (-1))[:1] + '.' + str(player_2_delta * (-1))[1:]
    elif player_2_delta >= -999 and player_2_delta < 0:
        player_2_delta_str = str(player_2_delta)
    elif player_2_delta == 0:
        player_2_delta_str = str(player_2_delta)
    elif player_2_delta <= 999 and player_2_delta > 0:
        player_2_delta_str = '+' + str(player_2_delta)
    elif player_2_delta <= 9999 and player_2_delta > 0:
        player_2_delta_str = '+' + str(player_2_delta)[:1] + '.' + str(player_2_delta)[1:]
    elif player_2_delta <= 99999 and player_2_delta > 0:
        player_2_delta_str = '+' + str(player_2_delta)[:2] + '.' + str(player_2_delta)[2:]
    elif player_2_delta <= 999999 and player_2_delta > 0:
        player_2_delta_str = '+' + str(player_2_delta)[:3] + '.' + str(player_2_delta)[3:]
    elif player_2_delta >= 1000000:
        player_2_delta_str = '+' + str(player_2_delta)[:1] + '.' + str(player_2_delta)[1:4] + '.' + str(player_2_delta)[4:]
    # Player 2 Delta
    if player_3_delta <= -1000000:
        player_3_delta_str = '-' + str(player_3_delta * (-1))[:1] + '.' + str(player_3_delta * (-1))[1:4] + '.' + str(player_3_delta * (-1))[4:]
    elif player_3_delta <= -100000:
        player_3_delta_str = '-' + str(player_3_delta * (-1))[:3] + '.' + str(player_3_delta * (-1))[3:]
    elif player_3_delta <= -10000:
        player_3_delta_str = '-' + str(player_3_delta * (-1))[:2] + '.' + str(player_3_delta * (-1))[2:]
    elif player_3_delta <= -1000:
        player_3_delta_str = '-' + str(player_3_delta * (-1))[:1] + '.' + str(player_3_delta * (-1))[1:]
    elif player_3_delta >= -999 and player_3_delta < 0:
        player_3_delta_str = str(player_3_delta)
    elif player_3_delta == 0:
        player_3_delta_str = str(player_3_delta)
    elif player_3_delta <= 999 and player_3_delta > 0:
        player_3_delta_str = '+' + str(player_3_delta)
    elif player_3_delta <= 9999 and player_3_delta > 0:
        player_3_delta_str = '+' + str(player_3_delta)[:1] + '.' + str(player_3_delta)[1:]
    elif player_3_delta <= 99999 and player_3_delta > 0:
        player_3_delta_str = '+' + str(player_3_delta)[:2] + '.' + str(player_3_delta)[2:]
    elif player_3_delta <= 999999 and player_3_delta > 0:
        player_3_delta_str = '+' + str(player_3_delta)[:3] + '.' + str(player_3_delta)[3:]
    elif player_3_delta >= 1000000:
        player_3_delta_str = '+' + str(player_3_delta)[:1] + '.' + str(player_3_delta)[1:4] + '.' + str(player_3_delta)[4:]

    return bet_value_str, player_1_score_str, player_2_score_str, player_3_score_str, player_1_delta_str, player_2_delta_str, player_3_delta_str

def money_values_render(bet_value_str, player_1_score_str, player_2_score_str, player_3_score_str, player_1_delta_str, player_2_delta_str, player_3_delta_str):
    # Bet Value
    text_bet_title = font_bet.render(bet_value_str, True, white)
    window.blit(text_bet_title, (270, 360))
    # Player 1 Score
    text_ps1_title = font.render(player_1_score_str, True, white)
    window.blit(text_ps1_title, (855, 73))
    # Player 2 Score
    text_ps2_title = font.render(player_2_score_str, True, white)
    window.blit(text_ps2_title, (855, 123))
    # Player 3 Score
    text_ps3_title = font.render(player_3_score_str, True, white)
    window.blit(text_ps3_title, (855, 173))
    # Player 1 Delta
    if player_1_delta_str == '0':
        text_player_1_delta = font.render(player_1_delta_str, True, white)
        window.blit(text_player_1_delta, (970, 73))
    elif player_1_delta_str[:1] == '-':
        text_player_1_delta = font.render(player_1_delta_str, True, red)
        window.blit(text_player_1_delta, (970, 73))
    else:
        text_player_1_delta = font.render(player_1_delta_str, True, green)
        window.blit(text_player_1_delta, (970, 73))
    # Player 1 Delta
    if player_2_delta_str == '0':
        text_player_2_delta = font.render(player_2_delta_str, True, white)
        window.blit(text_player_2_delta, (970, 123))
    elif player_2_delta_str[:1] == '-':
        text_player_2_delta = font.render(player_2_delta_str, True, red)
        window.blit(text_player_2_delta, (970, 123))
    else:
        text_player_2_delta = font.render(player_2_delta_str, True, green)
        window.blit(text_player_2_delta, (970, 123))
    # Player 3 Delta
    if player_3_delta_str == '0':
        text_player_3_delta = font.render(player_3_delta_str, True, white)
        window.blit(text_player_3_delta, (970, 173))
    elif player_3_delta_str[:1] == '-':
        text_player_3_delta = font.render(player_3_delta_str, True, red)
        window.blit(text_player_3_delta, (970, 173))
    else:
        text_player_3_delta = font.render(player_3_delta_str, True, green)
        window.blit(text_player_3_delta, (970, 173))

def click_bet(window, last_click_right, click_right, chosed_bet):
    # 0
    if mouse_x >= 10 and mouse_x <= 60 and mouse_y >= 10 and mouse_y <= 234 and last_click_right == False and click_right == True or chosed_bet == '0':
        pg.draw.rect(window, blue, (10, 10, 50, 224))
        pg.draw.rect(window, white, (10, 10, 50, 224), 1)
        text_0 = font.render('0', True, white)
        text_0 = pg.transform.rotate(text_0, 90)
        window.blit(text_0, (20, 115))
        chosed_bet = '0'
    # 1
    if mouse_x >= 61 and mouse_x <= 111 and mouse_y >= 160 and mouse_y <= 234 and last_click_right == False and click_right == True or chosed_bet == '1':
        pg.draw.rect(window, blue, (61, 160, 50, 74))
        pg.draw.rect(window, white, (61, 160, 50, 74), 1)
        text_1 = font.render('1', True, white)
        text_1 = pg.transform.rotate(text_1, 90)
        window.blit(text_1, (70, 190))
        chosed_bet = '1'
    # 2
    if mouse_x >= 61 and mouse_x <= 111 and mouse_y >= 85 and mouse_y <= 159 and last_click_right == False and click_right == True or chosed_bet == '2':
        pg.draw.rect(window, blue, (61, 85, 50, 74))
        pg.draw.rect(window, white, (61, 85, 50, 74), 1)
        text_2 = font.render('2', True, white)
        text_2 = pg.transform.rotate(text_2, 90)
        window.blit(text_2, (70, 115))
        chosed_bet = '2'
    # 3
    if mouse_x >= 61 and mouse_x <= 111 and mouse_y >= 10 and mouse_y <= 84 and  last_click_right == False and click_right == True or chosed_bet == '3':
        pg.draw.rect(window, blue, (61, 10, 50, 74))
        pg.draw.rect(window, white, (61, 10, 50, 74), 1)
        text_3 = font.render('3', True, white)
        text_3 = pg.transform.rotate(text_3, 90)
        window.blit(text_3, (70, 40))
        chosed_bet = '3'
    # 4
    if mouse_x >= 112 and mouse_x <= 162 and mouse_y >= 160 and mouse_y <= 234 and last_click_right == False and click_right == True or chosed_bet == '4':
        pg.draw.rect(window, blue, (112, 160, 50, 74))
        pg.draw.rect(window, white, (112, 160, 50, 74), 1)
        text_4 = font.render('4', True, white)
        text_4 = pg.transform.rotate(text_4, 90)
        window.blit(text_4, (121, 190))
        chosed_bet = '4'
    # 5
    if mouse_x >= 112 and mouse_x <= 162 and mouse_y >= 85 and mouse_y <= 159 and last_click_right == False and click_right == True or chosed_bet == '5':
        pg.draw.rect(window, blue, (112, 85, 50, 74))
        pg.draw.rect(window, white, (112, 85, 50, 74), 1)
        text_5 = font.render('5', True, white)
        text_5 = pg.transform.rotate(text_5, 90)
        window.blit(text_5, (121, 115))
        chosed_bet = '5'
    # 6
    if mouse_x >= 112 and mouse_x <= 162 and mouse_y >= 10 and mouse_y <= 84 and last_click_right == False and click_right == True or chosed_bet == '6':
        pg.draw.rect(window, blue, (112, 10, 50, 74))
        pg.draw.rect(window, white, (112, 10, 50, 74), 1)
        text_6 = font.render('6', True, white)
        text_6 = pg.transform.rotate(text_6, 90)
        window.blit(text_6, (121, 40))
        chosed_bet = '6'
    # 7
    if mouse_x >= 163 and mouse_x <= 213 and mouse_y >= 160 and mouse_y <= 234 and last_click_right == False and click_right == True or chosed_bet == '7':
        pg.draw.rect(window, blue, (163, 160, 50, 74))
        pg.draw.rect(window, white, (163, 160, 50, 74), 1)
        text_7 = font.render('7', True, white)
        text_7 = pg.transform.rotate(text_7, 90)
        window.blit(text_7, (172, 190))
        chosed_bet = '7'
    # 8
    if mouse_x >= 163 and mouse_x <= 213 and mouse_y >= 85 and mouse_y <= 159 and last_click_right == False and click_right == True or chosed_bet == '8':
        pg.draw.rect(window, blue, (163, 85, 50, 74))
        pg.draw.rect(window, white, (163, 85, 50, 74), 1)
        text_8 = font.render('8', True, white)
        text_8 = pg.transform.rotate(text_8, 90)
        window.blit(text_8, (172, 115))
        chosed_bet = '8'
    # 9
    if mouse_x >= 163 and mouse_x <= 213 and mouse_y >= 10 and mouse_y <= 84 and last_click_right == False and click_right == True or chosed_bet == '9':
        pg.draw.rect(window, blue, (163, 10, 50, 74))
        pg.draw.rect(window, white, (163, 10, 50, 74), 1)
        text_9 = font.render('9', True, white)
        text_9 = pg.transform.rotate(text_9, 90)
        window.blit(text_9, (172, 40))
        chosed_bet = '9'
    # 10
    if mouse_x >= 214 and mouse_x <= 264 and mouse_y >= 160 and mouse_y <= 234 and  last_click_right == False and click_right == True or chosed_bet == '10':
        pg.draw.rect(window, blue, (214, 160, 50, 74))
        pg.draw.rect(window, white, (214, 160, 50, 74), 1)
        text_10 = font.render('10', True, white)
        text_10 = pg.transform.rotate(text_10, 90)
        window.blit(text_10, (223, 185))
        chosed_bet = '10'
    # 11
    if mouse_x >= 214 and mouse_x <= 264 and mouse_y >= 85 and mouse_y <= 159 and  last_click_right == False and click_right == True or chosed_bet == '11':
        pg.draw.rect(window, blue, (214, 85, 50, 74))
        pg.draw.rect(window, white, (214, 85, 50, 74), 1)
        text_11 = font.render('11', True, white)
        text_11 = pg.transform.rotate(text_11, 90)
        window.blit(text_11, (223, 110))
        chosed_bet = '11'
    # 12
    if mouse_x >= 214 and mouse_x <= 264 and mouse_y >= 10 and mouse_y <= 84 and  last_click_right == False and click_right == True or chosed_bet == '12':
        pg.draw.rect(window, blue, (214, 10, 50, 74))
        pg.draw.rect(window, white, (214, 10, 50, 74), 1)
        text_12 = font.render('12', True, white)
        text_12 = pg.transform.rotate(text_12, 90)
        window.blit(text_12, (223, 35))
        chosed_bet = '12'
    # 13
    if mouse_x >= 265 and mouse_x <= 315 and mouse_y >= 160 and mouse_y <= 234 and  last_click_right == False and click_right == True or chosed_bet == '13':
        pg.draw.rect(window, blue, (265, 160, 50, 74))
        pg.draw.rect(window, white, (265, 160, 50, 74), 1)
        text_13 = font.render('13', True, white)
        text_13 = pg.transform.rotate(text_13, 90)
        window.blit(text_13, (274, 185))
        chosed_bet = '13'
    # 14
    if mouse_x >= 265 and mouse_x <= 315 and mouse_y >= 85 and mouse_y <= 159 and  last_click_right == False and click_right == True or chosed_bet == '14':
        pg.draw.rect(window, blue, (265, 85, 50, 74))
        pg.draw.rect(window, white, (265, 85, 50, 74), 1)
        text_14 = font.render('14', True, white)
        text_14 = pg.transform.rotate(text_14, 90)
        window.blit(text_14, (274, 110))
        chosed_bet = '14'
    # 15
    if mouse_x >= 265 and mouse_x <= 315 and mouse_y >= 10 and mouse_y <= 84 and  last_click_right == False and click_right == True or chosed_bet == '15':
        pg.draw.rect(window, blue, (265, 10, 50, 74))
        pg.draw.rect(window, white, (265, 10, 50, 74), 1)
        text_15 = font.render('15', True, white)
        text_15 = pg.transform.rotate(text_15, 90)
        window.blit(text_15, (274, 35))
        chosed_bet = '15'
    # 16
    if mouse_x >= 316 and mouse_x <= 366 and mouse_y >= 160 and mouse_y <= 234 and  last_click_right == False and click_right == True or chosed_bet == '16':
        pg.draw.rect(window, blue, (316, 160, 50, 74))
        pg.draw.rect(window, white, (316, 160, 50, 74), 1)
        text_16 = font.render('16', True, white)
        text_16 = pg.transform.rotate(text_16, 90)
        window.blit(text_16, (325, 185))
        chosed_bet = '16'
    # 17
    if mouse_x >= 316 and mouse_x <= 366 and mouse_y >= 85 and mouse_y <= 159 and  last_click_right == False and click_right == True or chosed_bet == '17':
        pg.draw.rect(window, blue, (316, 85, 50, 74))
        pg.draw.rect(window, white, (316, 85, 50, 74), 1)
        text_17 = font.render('17', True, white)
        text_17 = pg.transform.rotate(text_17, 90)
        window.blit(text_17, (325, 110))
        chosed_bet = '17'
    # 18
    if mouse_x >= 316 and mouse_x <= 366 and mouse_y >= 10 and mouse_y <= 84 and  last_click_right == False and click_right == True or chosed_bet == '18':
        pg.draw.rect(window, blue, (316, 10, 50, 74))
        pg.draw.rect(window, white, (316, 10, 50, 74), 1)
        text_18 = font.render('18', True, white)
        text_18 = pg.transform.rotate(text_18, 90)
        window.blit(text_18, (325, 35))
        chosed_bet = '18'
    # 19
    if mouse_x >= 367 and mouse_x <= 417 and mouse_y >= 160 and mouse_y <= 234 and  last_click_right == False and click_right == True or chosed_bet == '19':
        pg.draw.rect(window, blue, (367, 160, 50, 74))
        pg.draw.rect(window, white, (367, 160, 50, 74), 1)
        text_19 = font.render('19', True, white)
        text_19 = pg.transform.rotate(text_19, 90)
        window.blit(text_19, (376, 185))
        chosed_bet = '19'
    # 20
    if mouse_x >= 367 and mouse_x <= 417 and mouse_y >= 85 and mouse_y <= 159 and  last_click_right == False and click_right == True or chosed_bet == '20':
        pg.draw.rect(window, blue, (367, 85, 50, 74))
        pg.draw.rect(window, white, (367, 85, 50, 74), 1)
        text_20 = font.render('20', True, white)
        text_20 = pg.transform.rotate(text_20, 90)
        window.blit(text_20, (376, 110))
        chosed_bet = '20'
    # 21
    if mouse_x >= 367 and mouse_x <= 417 and mouse_y >= 10 and mouse_y <= 84 and  last_click_right == False and click_right == True or chosed_bet == '21':
        pg.draw.rect(window, blue, (367, 10, 50, 74))
        pg.draw.rect(window, white, (367, 10, 50, 74), 1)
        text_21 = font.render('21', True, white)
        text_21 = pg.transform.rotate(text_21, 90)
        window.blit(text_21, (376, 35))
        chosed_bet = '21'
    # 22
    if mouse_x >= 418 and mouse_x <= 468 and mouse_y >= 160 and mouse_y <= 234 and  last_click_right == False and click_right == True or chosed_bet == '22':
        pg.draw.rect(window, blue, (418, 160, 50, 74))
        pg.draw.rect(window, white, (418, 160, 50, 74), 1)
        text_22 = font.render('22', True, white)
        text_22 = pg.transform.rotate(text_22, 90)
        window.blit(text_22, (427, 185))
        chosed_bet = '22'
    # 23
    if mouse_x >= 418 and mouse_x <= 468 and mouse_y >= 85 and mouse_y <= 159 and  last_click_right == False and click_right == True or chosed_bet == '23':
        pg.draw.rect(window, blue, (418, 85, 50, 74))
        pg.draw.rect(window, white, (418, 85, 50, 74), 1)
        text_23 = font.render('23', True, white)
        text_23 = pg.transform.rotate(text_23, 90)
        window.blit(text_23, (427, 110))
        chosed_bet = '23'
    # 24
    if mouse_x >= 418 and mouse_x <= 468 and mouse_y >= 10 and mouse_y <= 84 and  last_click_right == False and click_right == True or chosed_bet == '24':
        pg.draw.rect(window, blue, (418, 10, 50, 74))
        pg.draw.rect(window, white, (418, 10, 50, 74), 1)
        text_24 = font.render('24', True, white)
        text_24 = pg.transform.rotate(text_24, 90)
        window.blit(text_24, (427, 35))
        chosed_bet = '24'
    # 25
    if mouse_x >= 469 and mouse_x <= 519 and mouse_y >= 160 and mouse_y <= 234 and  last_click_right == False and click_right == True or chosed_bet == '25':
        pg.draw.rect(window, blue, (469, 160, 50, 74))
        pg.draw.rect(window, white, (469, 160, 50, 74), 1)
        text_25 = font.render('25', True, white)
        text_25 = pg.transform.rotate(text_25, 90)
        window.blit(text_25, (478, 185))
        chosed_bet = '25'
    # 26
    if mouse_x >= 469 and mouse_x <= 519 and mouse_y >= 85 and mouse_y <= 159 and  last_click_right == False and click_right == True or chosed_bet == '26':
        pg.draw.rect(window, blue, (469, 85, 50, 74))
        pg.draw.rect(window, white, (469, 85, 50, 74), 1)
        text_26 = font.render('26', True, white)
        text_26 = pg.transform.rotate(text_26, 90)
        window.blit(text_26, (478, 110))
        chosed_bet = '26'
    # 27
    if mouse_x >= 469 and mouse_x <= 519 and mouse_y >= 10 and mouse_y <= 84 and  last_click_right == False and click_right == True or chosed_bet == '27':
        pg.draw.rect(window, blue, (469, 10, 50, 74))
        pg.draw.rect(window, white, (469, 10, 50, 74), 1)
        text_27 = font.render('27', True, white)
        text_27 = pg.transform.rotate(text_27, 90)
        window.blit(text_27, (478, 35))
        chosed_bet = '27'
    # 28
    if mouse_x >= 520 and mouse_x <= 570 and mouse_y >= 160 and mouse_y <= 234 and  last_click_right == False and click_right == True or chosed_bet == '28':
        pg.draw.rect(window, blue, (520, 160, 50, 74))
        pg.draw.rect(window, white, (520, 160, 50, 74), 1)
        text_28 = font.render('28', True, white)
        text_28 = pg.transform.rotate(text_28, 90)
        window.blit(text_28, (529, 185))
        chosed_bet = '28'
    # 29
    if mouse_x >= 520 and mouse_x <= 570 and mouse_y >= 85 and mouse_y <= 159 and  last_click_right == False and click_right == True or chosed_bet == '29':
        pg.draw.rect(window, blue, (520, 85, 50, 74))
        pg.draw.rect(window, white, (520, 85, 50, 74), 1)
        text_29 = font.render('29', True, white)
        text_29 = pg.transform.rotate(text_29, 90)
        window.blit(text_29, (529, 110))
        chosed_bet = '29'
    # 30
    if mouse_x >= 520 and mouse_x <= 570 and mouse_y >= 10 and mouse_y <= 84 and  last_click_right == False and click_right == True or chosed_bet == '30':
        pg.draw.rect(window, blue, (520, 10, 50, 74))
        pg.draw.rect(window, white, (520, 10, 50, 74), 1)
        text_30 = font.render('30', True, white)
        text_30 = pg.transform.rotate(text_30, 90)
        window.blit(text_30, (529, 35))
        chosed_bet = '30'
    # 31
    if mouse_x >= 571 and mouse_x <= 621 and mouse_y >= 160 and mouse_y <= 234 and  last_click_right == False and click_right == True or chosed_bet == '31':
        pg.draw.rect(window, blue, (571, 160, 50, 74))
        pg.draw.rect(window, white, (571, 160, 50, 74), 1)
        text_31 = font.render('31', True, white)
        text_31 = pg.transform.rotate(text_31, 90)
        window.blit(text_31, (580, 185))
        chosed_bet = '31'
    # 32
    if mouse_x >= 571 and mouse_x <= 621 and mouse_y >= 85 and mouse_y <= 159 and  last_click_right == False and click_right == True or chosed_bet == '32':
        pg.draw.rect(window, blue, (571, 85, 50, 74))
        pg.draw.rect(window, white, (571, 85, 50, 74), 1)
        text_32 = font.render('32', True, white)
        text_32 = pg.transform.rotate(text_32, 90)
        window.blit(text_32, (580, 110))
        chosed_bet = '32'
    # 33
    if mouse_x >= 571 and mouse_x <= 621 and mouse_y >= 10 and mouse_y <= 84 and  last_click_right == False and click_right == True or chosed_bet == '33':
        pg.draw.rect(window, blue, (571, 10, 50, 74))
        pg.draw.rect(window, white, (571, 10, 50, 74), 1)
        text_33 = font.render('33', True, white)
        text_33 = pg.transform.rotate(text_33, 90)
        window.blit(text_33, (580, 35))
        chosed_bet = '33'
    # 34
    if mouse_x >= 622 and mouse_x <= 672 and mouse_y >= 160 and mouse_y <= 234 and  last_click_right == False and click_right == True or chosed_bet == '34':
        pg.draw.rect(window, blue, (622, 160, 50, 74))
        pg.draw.rect(window, white, (622, 160, 50, 74), 1)
        text_34 = font.render('34', True, white)
        text_34 = pg.transform.rotate(text_34, 90)
        window.blit(text_34, (631, 185))
        chosed_bet = '34'
    # 35
    if mouse_x >= 622 and mouse_x <= 672 and mouse_y >= 85 and mouse_y <= 159 and  last_click_right == False and click_right == True or chosed_bet == '35':
        pg.draw.rect(window, blue, (622, 85, 50, 74))
        pg.draw.rect(window, white, (622, 85, 50, 74), 1)
        text_35 = font.render('35', True, white)
        text_35 = pg.transform.rotate(text_35, 90)
        window.blit(text_35, (631, 110))
        chosed_bet = '35'
    # 36
    if mouse_x >= 622 and mouse_x <= 672 and mouse_y >= 10 and mouse_y <= 84 and  last_click_right == False and click_right == True or chosed_bet == '36':
        pg.draw.rect(window, blue, (622, 10, 50, 74))
        pg.draw.rect(window, white, (622, 10, 50, 74), 1)
        text_36 = font.render('36', True, white)
        text_36 = pg.transform.rotate(text_36, 90)
        window.blit(text_36, (631, 35))
        chosed_bet = '36'
    # 1º
    if mouse_x >= 673 and mouse_x <= 723 and mouse_y >= 160 and mouse_y <= 234 and  last_click_right == False and click_right == True or chosed_bet == '1º':
        pg.draw.rect(window, blue, (673, 160, 50, 74))
        pg.draw.rect(window, white, (673, 160, 50, 74), 1)
        text_1c = font.render('1º', True, white)
        text_1c = pg.transform.rotate(text_1c, 90)
        window.blit(text_1c, (682, 185))
        chosed_bet = '1º'
    # 2º
    if mouse_x >= 673 and mouse_x <= 723 and mouse_y >= 85 and mouse_y <= 159 and  last_click_right == False and click_right == True or chosed_bet == '2º':
        pg.draw.rect(window, blue, (673, 85, 50, 74))
        pg.draw.rect(window, white, (673, 85, 50, 74), 1)
        text_2c = font.render('2º', True, white)
        text_2c = pg.transform.rotate(text_2c, 90)
        window.blit(text_2c, (682, 110))
        chosed_bet = '2º'
    # 3º
    if mouse_x >= 673 and mouse_x <= 723 and mouse_y >= 10 and mouse_y <= 84 and  last_click_right == False and click_right == True or chosed_bet == '3º':
        pg.draw.rect(window, blue, (673, 10, 50, 74))
        pg.draw.rect(window, white, (673, 10, 50, 74), 1)
        text_3c = font.render('3º', True, white)
        text_3c = pg.transform.rotate(text_3c, 90)
        window.blit(text_3c, (682, 35))
        chosed_bet = '3º'
    # 1st 12
    if mouse_x >= 61 and mouse_x <= 264 and mouse_y >= 235 and mouse_y <= 285 and  last_click_right == False and click_right == True or chosed_bet == '1st 12':
        pg.draw.rect(window, blue, (61, 235, 203, 50))
        pg.draw.rect(window, white, (61, 235, 203, 50), 1)
        text_1st_12 = font.render('1st 12', True, white)
        window.blit(text_1st_12, (130, 245))
        chosed_bet = '1st 12'
    # 1 to 18
    if mouse_x >= 61 and mouse_x <= 162 and mouse_y >= 286 and mouse_y <= 336 and  last_click_right == False and click_right == True or chosed_bet == '1 to 18':
        pg.draw.rect(window, blue, (61, 286, 101, 50))
        pg.draw.rect(window, white, (61, 286, 101, 50), 1)
        text_1_to_18 = font.render('1 to 18', True, white)
        window.blit(text_1_to_18, (75, 298))
        chosed_bet = '1 to 18'
    # Even
    if mouse_x >= 163 and mouse_x <= 264 and mouse_y >= 286 and mouse_y <= 336 and  last_click_right == False and click_right == True or chosed_bet == 'EVEN':
        pg.draw.rect(window, blue, (163, 286, 101, 50))
        pg.draw.rect(window, white, (163, 286, 101, 50), 1)
        text_even = font.render('EVEN', True, white)
        window.blit(text_even, (180, 298))
        chosed_bet = 'EVEN'
    # 2nd 12
    if mouse_x >= 265 and mouse_x <= 468 and mouse_y >= 235 and mouse_y <= 285 and  last_click_right == False and click_right == True or chosed_bet == '2nd 12':
        pg.draw.rect(window, blue, (265, 235, 203, 50))
        pg.draw.rect(window, white, (265, 235, 203, 50), 1)
        text_2nd_12 = font.render('2nd 12', True, white)
        window.blit(text_2nd_12, (334, 245))
        chosed_bet = '2nd 12'
    # Red
    if mouse_x >= 265 and mouse_x <= 366 and mouse_y >= 286 and mouse_y <= 336 and  last_click_right == False and click_right == True or chosed_bet == 'RED':
        pg.draw.rect(window, blue, (265, 286, 101, 50))
        pg.draw.rect(window, white, (265, 286, 101, 50), 1)
        text_red = font.render('RED', True, white)
        window.blit(text_red, (290, 298))
        chosed_bet = 'RED'
    # Black
    if mouse_x >= 367 and mouse_x <= 468 and mouse_y >= 286 and mouse_y <= 336 and  last_click_right == False and click_right == True or chosed_bet == 'BLACK':
        pg.draw.rect(window, blue, (367, 286, 101, 50))
        pg.draw.rect(window, white, (367, 286, 101, 50), 1)
        text_black = font.render('BLACK', True, white)
        window.blit(text_black, (375, 298))
        chosed_bet = 'BLACK'
    # 3rd 12
    if mouse_x >= 469 and mouse_x <= 672 and mouse_y >= 235 and mouse_y <= 285 and  last_click_right == False and click_right == True or chosed_bet == '3rd 12':
        pg.draw.rect(window, blue, (469, 235, 203, 50))
        pg.draw.rect(window, white, (469, 235, 203, 50), 1)
        text_3rd_12 = font.render('3rd 12', True, white)
        window.blit(text_3rd_12, (538, 245))
        chosed_bet = '3rd 12'
    # Odd
    if mouse_x >= 469 and mouse_x <= 570 and mouse_y >= 286 and mouse_y <= 336 and  last_click_right == False and click_right == True or chosed_bet == 'ODD':
        pg.draw.rect(window, blue, (469, 286, 101, 50))
        pg.draw.rect(window, white, (469, 286, 101, 50), 1)
        text_odd = font.render('ODD', True, white)
        window.blit(text_odd, (492, 298))
        chosed_bet = 'ODD'
    # 19 to 36
    if mouse_x >= 571 and mouse_x <= 672 and mouse_y >= 286 and mouse_y <= 336 and  last_click_right == False and click_right == True or chosed_bet == '19 to 36':
        pg.draw.rect(window, blue, (571, 286, 101, 50))
        pg.draw.rect(window, white, (571, 286, 101, 50), 1)
        text_19_to_36 = font.render('19 to 36', True, white)
        window.blit(text_19_to_36, (578, 298))
        chosed_bet = '19 to 36'
    return chosed_bet

def bet_calculation(bet_value, chosed_bet, last_click_right, click_right, player_1_score, player_2_score, player_3_score, player_turn):
    # $1
    if mouse_x >= 10 and mouse_x <= 110 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and chosed_bet != None:
        if player_turn == 'player_1':
            if player_1_score - 1 >= 0:
                bet_value += 1
                player_1_score -= 1
            else:
                pass
        elif player_turn == 'player_2':
            if player_2_score - 1 >= 0:
                bet_value += 1
                player_2_score -= 1
            else:
                pass
        elif player_turn == 'player_3':
            if player_3_score - 1 >= 0:
                bet_value += 1
                player_3_score -= 1
            else:
                pass
    # $5
    if mouse_x >= 111 and mouse_x <= 211 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and chosed_bet != None:
        if player_turn == 'player_1':
            if player_1_score - 5 >= 0:
                bet_value += 5
                player_1_score -= 5
            else:
                pass
        elif player_turn == 'player_2':
            if player_2_score - 5 >= 0:
                bet_value += 5
                player_2_score -= 5
            else:
                pass
        elif player_turn == 'player_3':
            if player_3_score - 5 >= 0:
                bet_value += 5
                player_3_score -= 5
            else:
                pass
    # $10
    if mouse_x >= 212 and mouse_x <= 312 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and chosed_bet != None:
        if player_turn == 'player_1':
            if player_1_score - 10 >= 0:
                bet_value += 10
                player_1_score -= 10
            else:
                pass
        elif player_turn == 'player_2':
            if player_2_score - 10 >= 0:
                bet_value += 10
                player_2_score -= 10
            else:
                pass
        elif player_turn == 'player_3':
            if player_3_score - 10 >= 0:
                bet_value += 10
                player_3_score -= 10
            else:
                pass
    # $25
    if mouse_x >= 313 and mouse_x <= 413 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and chosed_bet != None:
        if player_turn == 'player_1':
            if player_1_score - 25 >= 0:
                bet_value += 25
                player_1_score -= 25
            else:
                pass
        elif player_turn == 'player_2':
            if player_2_score - 25 >= 0:
                bet_value += 25
                player_2_score -= 25
            else:
                pass
        elif player_turn == 'player_3':
            if player_3_score - 25 >= 0:
                bet_value += 25
                player_3_score -= 25
            else:
                pass
    # $50
    if mouse_x >= 414 and mouse_x <= 514 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and chosed_bet != None:
        if player_turn == 'player_1':
            if player_1_score - 50 >= 0:
                bet_value += 50
                player_1_score -= 50
            else:
                pass
        elif player_turn == 'player_2':
            if player_2_score - 50 >= 0:
                bet_value += 50
                player_2_score -= 50
            else:
                pass
        elif player_turn == 'player_3':
            if player_3_score - 50 >= 0:
                bet_value += 50
                player_3_score -= 50
            else:
                pass
    # $100
    if mouse_x >= 515 and mouse_x <= 615 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and chosed_bet != None:
        if player_turn == 'player_1':
            if player_1_score - 100 >= 0:
                bet_value += 100
                player_1_score -= 100
            else:
                pass
        elif player_turn == 'player_2':
            if player_2_score - 100 >= 0:
                bet_value += 100
                player_2_score -= 100
            else:
                pass
        elif player_turn == 'player_3':
            if player_3_score - 100 >= 0:
                bet_value += 100
                player_3_score -= 100
            else:
                pass
    # $250
    if mouse_x >= 616 and mouse_x <= 716 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and chosed_bet != None:
        if player_turn == 'player_1':
            if player_1_score - 250 >= 0:
                bet_value += 250
                player_1_score -= 250
            else:
                pass
        elif player_turn == 'player_2':
            if player_2_score - 250 >= 0:
                bet_value += 250
                player_2_score -= 250
            else:
                pass
        elif player_turn == 'player_3':
            if player_3_score - 250 >= 0:
                bet_value += 250
                player_3_score -= 250
            else:
                pass
    # $500
    if mouse_x >= 717 and mouse_x <= 817 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and chosed_bet != None:
        if player_turn == 'player_1':
            if player_1_score - 500 >= 0:
                bet_value += 500
                player_1_score -= 500
            else:
                pass
        elif player_turn == 'player_2':
            if player_2_score - 500 >= 0:
                bet_value += 500
                player_2_score -= 500
            else:
                pass
        elif player_turn == 'player_3':
            if player_3_score - 500 >= 0:
                bet_value += 500
                player_3_score -= 500
            else:
                pass
    # $1.000
    if mouse_x >= 818 and mouse_x <= 918 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and chosed_bet != None:
        if player_turn == 'player_1':
            if player_1_score - 1000 >= 0:
                bet_value += 1000
                player_1_score -= 1000
            else:
                pass
        elif player_turn == 'player_2':
            if player_2_score - 1000 >= 0:
                bet_value += 1000
                player_2_score -= 1000
            else:
                pass
        elif player_turn == 'player_3':
            if player_3_score - 1000 >= 0:
                bet_value += 1000
                player_3_score -= 1000
            else:
                pass
    # $5.000
    if mouse_x >= 918 and mouse_x <= 1018 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and chosed_bet != None:
        if player_turn == 'player_1':
            if player_1_score - 5000 >= 0:
                bet_value += 5000
                player_1_score -= 5000
            else:
                pass
        elif player_turn == 'player_2':
            if player_2_score - 5000 >= 0:
                bet_value += 5000
                player_2_score -= 5000
            else:
                pass
        elif player_turn == 'player_3':
            if player_3_score - 5000 >= 0:
                bet_value += 5000
                player_3_score -= 5000
            else:
                pass
    # $10.000
    if mouse_x >= 1020 and mouse_x <= 1120 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and chosed_bet != None:
        if player_turn == 'player_1':
            if player_1_score - 10000 >= 0:
                bet_value += 10000
                player_1_score -= 10000
            else:
                pass
        elif player_turn == 'player_2':
            if player_2_score - 10000 >= 0:
                bet_value += 10000
                player_2_score -= 10000
            else:
                pass
        elif player_turn == 'player_3':
            if player_3_score - 10000 >= 0:
                bet_value += 10000
                player_3_score -= 10000
            else:
                pass
    return bet_value, player_1_score, player_2_score, player_3_score

def player_turn_game(window, player_turn, player_1_score_str, player_2_score_str, player_3_score_str):
    # Players 1 Score
    if player_turn == 'player_1':
        pg.draw.rect(window, blue, (728, 61, 235, 50))
        pg.draw.rect(window, white, (728, 61, 235, 50), 1)
        text_ps1_title = font.render('Players 1: $' + player_1_score_str, True, white)
        window.blit(text_ps1_title, (735, 73))
    # Players 2 Score
    if player_turn == 'player_2':
        pg.draw.rect(window, blue, (728, 112, 235, 50))
        pg.draw.rect(window, white, (728, 112, 235, 50), 1)
        text_ps2_title = font.render('Players 2: $' + player_2_score_str, True, white)
        window.blit(text_ps2_title, (735, 123))
    # Players 3 Score
    if player_turn == 'player_3':
        pg.draw.rect(window, blue, (728, 163, 235, 50))
        pg.draw.rect(window, white, (728, 163, 235, 50), 1)
        text_ps3_title = font.render('Players 3: $' + player_3_score_str, True, white)
        window.blit(text_ps3_title, (735, 173))

def pl1_all_bet_data(player_1_score, player_turn, pl1_bet_value, last_click_right, click_right, chosed_bet, pl1_bet_numbers, pl1_bet_1st_12, pl1_bet_2nd_12, pl1_bet_3rd_12, pl1_bet_1_to_18, pl1_bet_even, pl1_bet_red, pl1_bet_black, pl1_bet_odd, pl1_bet_19_to_36, pl1_bet_1c, pl1_bet_2c, pl1_bet_3c):
    # $1
    if player_turn == 'player_1' and  mouse_x >= 10 and mouse_x <= 110 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_1_score - 1 >= 0:
        try:
            pl1_bet_numbers[int(chosed_bet)] += 1
        except:
            if chosed_bet == '1st 12':
                pl1_bet_1st_12 += 1
            elif chosed_bet == '2nd 12':
                pl1_bet_2nd_12 += 1
            elif chosed_bet == '3rd 12':
                pl1_bet_3rd_12 += 1
            elif chosed_bet == '1 to 18':
                pl1_bet_1_to_18 += 1
            elif chosed_bet == 'EVEN':
                pl1_bet_even += 1
            elif chosed_bet == 'RED':
                pl1_bet_red += 1
            elif chosed_bet == 'BLACK':
                pl1_bet_black += 1
            elif chosed_bet == 'ODD':
                pl1_bet_odd += 1
            elif chosed_bet == '19 to 36':
                pl1_bet_19_to_36 += 1
            elif chosed_bet == '1º':
                pl1_bet_1c += 1
            elif chosed_bet == '2º':
                pl1_bet_2c += 1
            elif chosed_bet == '3º':
                pl1_bet_3c += 1
    # $5
    if player_turn == 'player_1' and mouse_x >= 111 and mouse_x <= 211 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_1_score - 5 >= 0:
        try:
            pl1_bet_numbers[int(chosed_bet)] += 5
        except:
            if chosed_bet == '1st 12':
                pl1_bet_1st_12 += 5
            elif chosed_bet == '2nd 12':
                pl1_bet_2nd_12 += 5
            elif chosed_bet == '3rd 12':
                pl1_bet_3rd_12 += 5
            elif chosed_bet == '1 to 18':
                pl1_bet_1_to_18 += 5
            elif chosed_bet == 'EVEN':
                pl1_bet_even += 5
            elif chosed_bet == 'RED':
                pl1_bet_red += 5
            elif chosed_bet == 'BLACK':
                pl1_bet_black += 5
            elif chosed_bet == 'ODD':
                pl1_bet_odd += 5
            elif chosed_bet == '19 to 36':
                pl1_bet_19_to_36 += 5
            elif chosed_bet == '1º':
                pl1_bet_1c += 5
            elif chosed_bet == '2º':
                pl1_bet_2c += 5
            elif chosed_bet == '3º':
                pl1_bet_3c += 5
    # $10
    if player_turn == 'player_1' and mouse_x >= 212 and mouse_x <= 312 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_1_score - 10 >= 0:
        try:
            pl1_bet_numbers[int(chosed_bet)] += 10
        except:
            if chosed_bet == '1st 12':
                pl1_bet_1st_12 += 10
            elif chosed_bet == '2nd 12':
                pl1_bet_2nd_12 += 10
            elif chosed_bet == '3rd 12':
                pl1_bet_3rd_12 += 10
            elif chosed_bet == '1 to 18':
                pl1_bet_1_to_18 += 10
            elif chosed_bet == 'EVEN':
                pl1_bet_even += 10
            elif chosed_bet == 'RED':
                pl1_bet_red += 10
            elif chosed_bet == 'BLACK':
                pl1_bet_black += 10
            elif chosed_bet == 'ODD':
                pl1_bet_odd += 10
            elif chosed_bet == '19 to 36':
                pl1_bet_19_to_36 += 10
            elif chosed_bet == '1º':
                pl1_bet_1c += 10
            elif chosed_bet == '2º':
                pl1_bet_2c += 10
            elif chosed_bet == '3º':
                pl1_bet_3c += 10
    # $25
    if player_turn == 'player_1' and mouse_x >= 313 and mouse_x <= 413 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_1_score - 25 >= 0:
        try:
            pl1_bet_numbers[int(chosed_bet)] += 25
        except:
            if chosed_bet == '1st 12':
                pl1_bet_1st_12 += 25
            elif chosed_bet == '2nd 12':
                pl1_bet_2nd_12 += 25
            elif chosed_bet == '3rd 12':
                pl1_bet_3rd_12 += 25
            elif chosed_bet == '1 to 18':
                pl1_bet_1_to_18 += 25
            elif chosed_bet == 'EVEN':
                pl1_bet_even += 25
            elif chosed_bet == 'RED':
                pl1_bet_red += 25
            elif chosed_bet == 'BLACK':
                pl1_bet_black += 25
            elif chosed_bet == 'ODD':
                pl1_bet_odd += 25
            elif chosed_bet == '19 to 36':
                pl1_bet_19_to_36 += 25
            elif chosed_bet == '1º':
                pl1_bet_1c += 25
            elif chosed_bet == '2º':
                pl1_bet_2c += 25
            elif chosed_bet == '3º':
                pl1_bet_3c += 25
    # $50
    if player_turn == 'player_1' and mouse_x >= 414 and mouse_x <= 514 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_1_score - 50 >= 0:
        try:
            pl1_bet_numbers[int(chosed_bet)] += 50
        except:
            if chosed_bet == '1st 12':
                pl1_bet_1st_12 += 50
            elif chosed_bet == '2nd 12':
                pl1_bet_2nd_12 += 50
            elif chosed_bet == '3rd 12':
                pl1_bet_3rd_12 += 50
            elif chosed_bet == '1 to 18':
                pl1_bet_1_to_18 += 50
            elif chosed_bet == 'EVEN':
                pl1_bet_even += 50
            elif chosed_bet == 'RED':
                pl1_bet_red += 50
            elif chosed_bet == 'BLACK':
                pl1_bet_black += 50
            elif chosed_bet == 'ODD':
                pl1_bet_odd += 50
            elif chosed_bet == '19 to 36':
                pl1_bet_19_to_36 += 50
            elif chosed_bet == '1º':
                pl1_bet_1c += 50
            elif chosed_bet == '2º':
                pl1_bet_2c += 50
            elif chosed_bet == '3º':
                pl1_bet_3c += 50
    # $100
    if player_turn == 'player_1' and mouse_x >= 515 and mouse_x <= 615 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_1_score - 100 >= 0:
        try:
            pl1_bet_numbers[int(chosed_bet)] += 100
        except:
            if chosed_bet == '1st 12':
                pl1_bet_1st_12 += 100
            elif chosed_bet == '2nd 12':
                pl1_bet_2nd_12 += 100
            elif chosed_bet == '3rd 12':
                pl1_bet_3rd_12 += 100
            elif chosed_bet == '1 to 18':
                pl1_bet_1_to_18 += 100
            elif chosed_bet == 'EVEN':
                pl1_bet_even += 100
            elif chosed_bet == 'RED':
                pl1_bet_red += 100
            elif chosed_bet == 'BLACK':
                pl1_bet_black += 100
            elif chosed_bet == 'ODD':
                pl1_bet_odd += 100
            elif chosed_bet == '19 to 36':
                pl1_bet_19_to_36 += 100
            elif chosed_bet == '1º':
                pl1_bet_1c += 100
            elif chosed_bet == '2º':
                pl1_bet_2c += 100
            elif chosed_bet == '3º':
                pl1_bet_3c += 100
    # $250
    if player_turn == 'player_1' and mouse_x >= 616 and mouse_x <= 716 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_1_score - 250 >= 0:
        try:
            pl1_bet_numbers[int(chosed_bet)] += 250
        except:
            if chosed_bet == '1st 12':
                pl1_bet_1st_12 += 250
            elif chosed_bet == '2nd 12':
                pl1_bet_2nd_12 += 250
            elif chosed_bet == '3rd 12':
                pl1_bet_3rd_12 += 250
            elif chosed_bet == '1 to 18':
                pl1_bet_1_to_18 += 250
            elif chosed_bet == 'EVEN':
                pl1_bet_even += 250
            elif chosed_bet == 'RED':
                pl1_bet_red += 250
            elif chosed_bet == 'BLACK':
                pl1_bet_black += 250
            elif chosed_bet == 'ODD':
                pl1_bet_odd += 250
            elif chosed_bet == '19 to 36':
                pl1_bet_19_to_36 += 250
            elif chosed_bet == '1º':
                pl1_bet_1c += 250
            elif chosed_bet == '2º':
                pl1_bet_2c += 250
            elif chosed_bet == '3º':
                pl1_bet_3c += 250
    # $500
    if player_turn == 'player_1' and mouse_x >= 717 and mouse_x <= 817 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_1_score - 500 >= 0:
        try:
            pl1_bet_numbers[int(chosed_bet)] += 500
        except:
            if chosed_bet == '1st 12':
                pl1_bet_1st_12 += 500
            elif chosed_bet == '2nd 12':
                pl1_bet_2nd_12 += 500
            elif chosed_bet == '3rd 12':
                pl1_bet_3rd_12 += 500
            elif chosed_bet == '1 to 18':
                pl1_bet_1_to_18 += 500
            elif chosed_bet == 'EVEN':
                pl1_bet_even += 500
            elif chosed_bet == 'RED':
                pl1_bet_red += 500
            elif chosed_bet == 'BLACK':
                pl1_bet_black += 500
            elif chosed_bet == 'ODD':
                pl1_bet_odd += 500
            elif chosed_bet == '19 to 36':
                pl1_bet_19_to_36 += 500
            elif chosed_bet == '1º':
                pl1_bet_1c += 500
            elif chosed_bet == '2º':
                pl1_bet_2c += 500
            elif chosed_bet == '3º':
                pl1_bet_3c += 500
    # $1.000
    if player_turn == 'player_1' and mouse_x >= 818 and mouse_x <= 918 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_1_score - 1000 >= 0:
        try:
            pl1_bet_numbers[int(chosed_bet)] += 1000
        except:
            if chosed_bet == '1st 12':
                pl1_bet_1st_12 += 1000
            elif chosed_bet == '2nd 12':
                pl1_bet_2nd_12 += 1000
            elif chosed_bet == '3rd 12':
                pl1_bet_3rd_12 += 1000
            elif chosed_bet == '1 to 18':
                pl1_bet_1_to_18 += 1000
            elif chosed_bet == 'EVEN':
                pl1_bet_even += 1000
            elif chosed_bet == 'RED':
                pl1_bet_red += 1000
            elif chosed_bet == 'BLACK':
                pl1_bet_black += 1000
            elif chosed_bet == 'ODD':
                pl1_bet_odd += 1000
            elif chosed_bet == '19 to 36':
                pl1_bet_19_to_36 += 1000
            elif chosed_bet == '1º':
                pl1_bet_1c += 1000
            elif chosed_bet == '2º':
                pl1_bet_2c += 1000
            elif chosed_bet == '3º':
                pl1_bet_3c += 1000
    # $5.000
    if player_turn == 'player_1' and mouse_x >= 918 and mouse_x <= 1018 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_1_score - 5000 >= 0:
        try:
            pl1_bet_numbers[int(chosed_bet)] += 5000
        except:
            if chosed_bet == '1st 12':
                pl1_bet_1st_12 += 5000
            elif chosed_bet == '2nd 12':
                pl1_bet_2nd_12 += 5000
            elif chosed_bet == '3rd 12':
                pl1_bet_3rd_12 += 5000
            elif chosed_bet == '1 to 18':
                pl1_bet_1_to_18 += 5000
            elif chosed_bet == 'EVEN':
                pl1_bet_even += 5000
            elif chosed_bet == 'RED':
                pl1_bet_red += 5000
            elif chosed_bet == 'BLACK':
                pl1_bet_black += 5000
            elif chosed_bet == 'ODD':
                pl1_bet_odd += 5000
            elif chosed_bet == '19 to 36':
                pl1_bet_19_to_36 += 5000
            elif chosed_bet == '1º':
                pl1_bet_1c += 5000
            elif chosed_bet == '2º':
                pl1_bet_2c += 5000
            elif chosed_bet == '3º':
                pl1_bet_3c += 5000
    # $10.000
    if player_turn == 'player_1' and mouse_x >= 1020 and mouse_x <= 1120 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_1_score - 10000 >= 0:
        try:
            pl1_bet_numbers[int(chosed_bet)] += 10000
        except:
            if chosed_bet == '1st 12':
                pl1_bet_1st_12 += 10000
            elif chosed_bet == '2nd 12':
                pl1_bet_2nd_12 += 10000
            elif chosed_bet == '3rd 12':
                pl1_bet_3rd_12 += 10000
            elif chosed_bet == '1 to 18':
                pl1_bet_1_to_18 += 10000
            elif chosed_bet == 'EVEN':
                pl1_bet_even += 10000
            elif chosed_bet == 'RED':
                pl1_bet_red += 10000
            elif chosed_bet == 'BLACK':
                pl1_bet_black += 10000
            elif chosed_bet == 'ODD':
                pl1_bet_odd += 10000
            elif chosed_bet == '19 to 36':
                pl1_bet_19_to_36 += 10000
            elif chosed_bet == '1º':
                pl1_bet_1c += 10000
            elif chosed_bet == '2º':
                pl1_bet_2c += 10000
            elif chosed_bet == '3º':
                pl1_bet_3c += 10000
    return pl1_bet_value, pl1_bet_numbers, pl1_bet_1st_12, pl1_bet_2nd_12, pl1_bet_3rd_12, pl1_bet_1_to_18, pl1_bet_even, pl1_bet_red, pl1_bet_black, pl1_bet_odd, pl1_bet_19_to_36, pl1_bet_1c, pl1_bet_2c, pl1_bet_3c

def pl2_all_bet_data(player_2_score, player_turn, pl2_bet_value, last_click_right, click_right, chosed_bet, pl2_bet_numbers, pl2_bet_1st_12, pl2_bet_2nd_12, pl2_bet_3rd_12, pl2_bet_1_to_18, pl2_bet_even, pl2_bet_red, pl2_bet_black, pl2_bet_odd, pl2_bet_19_to_36, pl2_bet_1c, pl2_bet_2c, pl2_bet_3c):
    # $1
    if player_turn == 'player_2' and  mouse_x >= 10 and mouse_x <= 110 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_2_score - 1 >= 0:
        try:
            pl2_bet_numbers[int(chosed_bet)] += 1
        except:
            if chosed_bet == '1st 12':
                pl2_bet_1st_12 += 1
            elif chosed_bet == '2nd 12':
                pl2_bet_2nd_12 += 1
            elif chosed_bet == '3rd 12':
                pl2_bet_3rd_12 += 1
            elif chosed_bet == '1 to 18':
                pl2_bet_1_to_18 += 1
            elif chosed_bet == 'EVEN':
                pl2_bet_even += 1
            elif chosed_bet == 'RED':
                pl2_bet_red += 1
            elif chosed_bet == 'BLACK':
                pl2_bet_black += 1
            elif chosed_bet == 'ODD':
                pl2_bet_odd += 1
            elif chosed_bet == '19 to 36':
                pl2_bet_19_to_36 += 1
            elif chosed_bet == '1º':
                pl2_bet_1c += 1
            elif chosed_bet == '2º':
                pl2_bet_2c += 1
            elif chosed_bet == '3º':
                pl2_bet_3c += 1
    # $5
    if player_turn == 'player_2' and mouse_x >= 111 and mouse_x <= 211 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_2_score - 5 >= 0:
        try:
            pl2_bet_numbers[int(chosed_bet)] += 5
        except:
            if chosed_bet == '1st 12':
                pl2_bet_1st_12 += 5
            elif chosed_bet == '2nd 12':
                pl2_bet_2nd_12 += 5
            elif chosed_bet == '3rd 12':
                pl2_bet_3rd_12 += 5
            elif chosed_bet == '1 to 18':
                pl2_bet_1_to_18 += 5
            elif chosed_bet == 'EVEN':
                pl2_bet_even += 5
            elif chosed_bet == 'RED':
                pl2_bet_red += 5
            elif chosed_bet == 'BLACK':
                pl2_bet_black += 5
            elif chosed_bet == 'ODD':
                pl2_bet_odd += 5
            elif chosed_bet == '19 to 36':
                pl2_bet_19_to_36 += 5
            elif chosed_bet == '1º':
                pl2_bet_1c += 5
            elif chosed_bet == '2º':
                pl2_bet_2c += 5
            elif chosed_bet == '3º':
                pl2_bet_3c += 5
    # $10
    if player_turn == 'player_2' and mouse_x >= 212 and mouse_x <= 312 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_2_score - 10 >= 0:
        try:
            pl2_bet_numbers[int(chosed_bet)] += 10
        except:
            if chosed_bet == '1st 12':
                pl2_bet_1st_12 += 10
            elif chosed_bet == '2nd 12':
                pl2_bet_2nd_12 += 10
            elif chosed_bet == '3rd 12':
                pl2_bet_3rd_12 += 10
            elif chosed_bet == '1 to 18':
                pl2_bet_1_to_18 += 10
            elif chosed_bet == 'EVEN':
                pl2_bet_even += 10
            elif chosed_bet == 'RED':
                pl2_bet_red += 10
            elif chosed_bet == 'BLACK':
                pl2_bet_black += 10
            elif chosed_bet == 'ODD':
                pl2_bet_odd += 10
            elif chosed_bet == '19 to 36':
                pl2_bet_19_to_36 += 10
            elif chosed_bet == '1º':
                pl2_bet_1c += 10
            elif chosed_bet == '2º':
                pl2_bet_2c += 10
            elif chosed_bet == '3º':
                pl2_bet_3c += 10
    # $25
    if player_turn == 'player_2' and mouse_x >= 313 and mouse_x <= 413 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_2_score - 25 >= 0:
        try:
            pl2_bet_numbers[int(chosed_bet)] += 25
        except:
            if chosed_bet == '1st 12':
                pl2_bet_1st_12 += 25
            elif chosed_bet == '2nd 12':
                pl2_bet_2nd_12 += 25
            elif chosed_bet == '3rd 12':
                pl2_bet_3rd_12 += 25
            elif chosed_bet == '1 to 18':
                pl2_bet_1_to_18 += 25
            elif chosed_bet == 'EVEN':
                pl2_bet_even += 25
            elif chosed_bet == 'RED':
                pl2_bet_red += 25
            elif chosed_bet == 'BLACK':
                pl2_bet_black += 25
            elif chosed_bet == 'ODD':
                pl2_bet_odd += 25
            elif chosed_bet == '19 to 36':
                pl2_bet_19_to_36 += 25
            elif chosed_bet == '1º':
                pl2_bet_1c += 25
            elif chosed_bet == '2º':
                pl2_bet_2c += 25
            elif chosed_bet == '3º':
                pl2_bet_3c += 25
    # $50
    if player_turn == 'player_2' and mouse_x >= 414 and mouse_x <= 514 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_2_score - 50 >= 0:
        try:
            pl2_bet_numbers[int(chosed_bet)] += 50
        except:
            if chosed_bet == '1st 12':
                pl2_bet_1st_12 += 50
            elif chosed_bet == '2nd 12':
                pl2_bet_2nd_12 += 50
            elif chosed_bet == '3rd 12':
                pl2_bet_3rd_12 += 50
            elif chosed_bet == '1 to 18':
                pl2_bet_1_to_18 += 50
            elif chosed_bet == 'EVEN':
                pl2_bet_even += 50
            elif chosed_bet == 'RED':
                pl2_bet_red += 50
            elif chosed_bet == 'BLACK':
                pl2_bet_black += 50
            elif chosed_bet == 'ODD':
                pl2_bet_odd += 50
            elif chosed_bet == '19 to 36':
                pl2_bet_19_to_36 += 50
            elif chosed_bet == '1º':
                pl2_bet_1c += 50
            elif chosed_bet == '2º':
                pl2_bet_2c += 50
            elif chosed_bet == '3º':
                pl2_bet_3c += 50
    # $100
    if player_turn == 'player_2' and mouse_x >= 515 and mouse_x <= 615 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_2_score - 100 >= 0:
        try:
            pl2_bet_numbers[int(chosed_bet)] += 100
        except:
            if chosed_bet == '1st 12':
                pl2_bet_1st_12 += 100
            elif chosed_bet == '2nd 12':
                pl2_bet_2nd_12 += 100
            elif chosed_bet == '3rd 12':
                pl2_bet_3rd_12 += 100
            elif chosed_bet == '1 to 18':
                pl2_bet_1_to_18 += 100
            elif chosed_bet == 'EVEN':
                pl2_bet_even += 100
            elif chosed_bet == 'RED':
                pl2_bet_red += 100
            elif chosed_bet == 'BLACK':
                pl2_bet_black += 100
            elif chosed_bet == 'ODD':
                pl2_bet_odd += 100
            elif chosed_bet == '19 to 36':
                pl2_bet_19_to_36 += 100
            elif chosed_bet == '1º':
                pl2_bet_1c += 100
            elif chosed_bet == '2º':
                pl2_bet_2c += 100
            elif chosed_bet == '3º':
                pl2_bet_3c += 100
    # $250
    if player_turn == 'player_2' and mouse_x >= 616 and mouse_x <= 716 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_2_score - 250 >= 0:
        try:
            pl2_bet_numbers[int(chosed_bet)] += 250
        except:
            if chosed_bet == '1st 12':
                pl2_bet_1st_12 += 250
            elif chosed_bet == '2nd 12':
                pl2_bet_2nd_12 += 250
            elif chosed_bet == '3rd 12':
                pl2_bet_3rd_12 += 250
            elif chosed_bet == '1 to 18':
                pl2_bet_1_to_18 += 250
            elif chosed_bet == 'EVEN':
                pl2_bet_even += 250
            elif chosed_bet == 'RED':
                pl2_bet_red += 250
            elif chosed_bet == 'BLACK':
                pl2_bet_black += 250
            elif chosed_bet == 'ODD':
                pl2_bet_odd += 250
            elif chosed_bet == '19 to 36':
                pl2_bet_19_to_36 += 250
            elif chosed_bet == '1º':
                pl2_bet_1c += 250
            elif chosed_bet == '2º':
                pl2_bet_2c += 250
            elif chosed_bet == '3º':
                pl2_bet_3c += 250
    # $500
    if player_turn == 'player_2' and mouse_x >= 717 and mouse_x <= 817 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_2_score - 500 >= 0:
        try:
            pl2_bet_numbers[int(chosed_bet)] += 500
        except:
            if chosed_bet == '1st 12':
                pl2_bet_1st_12 += 500
            elif chosed_bet == '2nd 12':
                pl2_bet_2nd_12 += 500
            elif chosed_bet == '3rd 12':
                pl2_bet_3rd_12 += 500
            elif chosed_bet == '1 to 18':
                pl2_bet_1_to_18 += 500
            elif chosed_bet == 'EVEN':
                pl2_bet_even += 500
            elif chosed_bet == 'RED':
                pl2_bet_red += 500
            elif chosed_bet == 'BLACK':
                pl2_bet_black += 500
            elif chosed_bet == 'ODD':
                pl2_bet_odd += 500
            elif chosed_bet == '19 to 36':
                pl2_bet_19_to_36 += 500
            elif chosed_bet == '1º':
                pl2_bet_1c += 500
            elif chosed_bet == '2º':
                pl2_bet_2c += 500
            elif chosed_bet == '3º':
                pl2_bet_3c += 500
    # $1.000
    if player_turn == 'player_2' and mouse_x >= 818 and mouse_x <= 918 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_2_score - 1000 >= 0:
        try:
            pl2_bet_numbers[int(chosed_bet)] += 1000
        except:
            if chosed_bet == '1st 12':
                pl2_bet_1st_12 += 1000
            elif chosed_bet == '2nd 12':
                pl2_bet_2nd_12 += 1000
            elif chosed_bet == '3rd 12':
                pl2_bet_3rd_12 += 1000
            elif chosed_bet == '1 to 18':
                pl2_bet_1_to_18 += 1000
            elif chosed_bet == 'EVEN':
                pl2_bet_even += 1000
            elif chosed_bet == 'RED':
                pl2_bet_red += 1000
            elif chosed_bet == 'BLACK':
                pl2_bet_black += 1000
            elif chosed_bet == 'ODD':
                pl2_bet_odd += 1000
            elif chosed_bet == '19 to 36':
                pl2_bet_19_to_36 += 1000
            elif chosed_bet == '1º':
                pl2_bet_1c += 1000
            elif chosed_bet == '2º':
                pl2_bet_2c += 1000
            elif chosed_bet == '3º':
                pl2_bet_3c += 1000
    # $5.000
    if player_turn == 'player_2' and mouse_x >= 918 and mouse_x <= 1018 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_2_score - 5000 >= 0:
        try:
            pl2_bet_numbers[int(chosed_bet)] += 5000
        except:
            if chosed_bet == '1st 12':
                pl2_bet_1st_12 += 5000
            elif chosed_bet == '2nd 12':
                pl2_bet_2nd_12 += 5000
            elif chosed_bet == '3rd 12':
                pl2_bet_3rd_12 += 5000
            elif chosed_bet == '1 to 18':
                pl2_bet_1_to_18 += 5000
            elif chosed_bet == 'EVEN':
                pl2_bet_even += 5000
            elif chosed_bet == 'RED':
                pl2_bet_red += 5000
            elif chosed_bet == 'BLACK':
                pl2_bet_black += 5000
            elif chosed_bet == 'ODD':
                pl2_bet_odd += 5000
            elif chosed_bet == '19 to 36':
                pl2_bet_19_to_36 += 5000
            elif chosed_bet == '1º':
                pl2_bet_1c += 5000
            elif chosed_bet == '2º':
                pl2_bet_2c += 5000
            elif chosed_bet == '3º':
                pl2_bet_3c += 5000
    # $10.000
    if player_turn == 'player_2' and mouse_x >= 1020 and mouse_x <= 1120 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_2_score - 10000 >= 0:
        try:
            pl2_bet_numbers[int(chosed_bet)] += 10000
        except:
            if chosed_bet == '1st 12':
                pl2_bet_1st_12 += 10000
            elif chosed_bet == '2nd 12':
                pl2_bet_2nd_12 += 10000
            elif chosed_bet == '3rd 12':
                pl2_bet_3rd_12 += 10000
            elif chosed_bet == '1 to 18':
                pl2_bet_1_to_18 += 10000
            elif chosed_bet == 'EVEN':
                pl2_bet_even += 10000
            elif chosed_bet == 'RED':
                pl2_bet_red += 10000
            elif chosed_bet == 'BLACK':
                pl2_bet_black += 10000
            elif chosed_bet == 'ODD':
                pl2_bet_odd += 10000
            elif chosed_bet == '19 to 36':
                pl2_bet_19_to_36 += 10000
            elif chosed_bet == '1º':
                pl2_bet_1c += 10000
            elif chosed_bet == '2º':
                pl2_bet_2c += 10000
            elif chosed_bet == '3º':
                pl2_bet_3c += 10000
    return pl2_bet_value, pl2_bet_numbers, pl2_bet_1st_12, pl2_bet_2nd_12, pl2_bet_3rd_12, pl2_bet_1_to_18, pl2_bet_even, pl2_bet_red, pl2_bet_black, pl2_bet_odd, pl2_bet_19_to_36, pl2_bet_1c, pl2_bet_2c, pl2_bet_3c

def pl3_all_bet_data(player_3_score, player_turn, pl3_bet_value, last_click_right, click_right, chosed_bet, pl3_bet_numbers, pl3_bet_1st_12, pl3_bet_2nd_12, pl3_bet_3rd_12, pl3_bet_1_to_18, pl3_bet_even, pl3_bet_red, pl3_bet_black, pl3_bet_odd, pl3_bet_19_to_36, pl3_bet_1c, pl3_bet_2c, pl3_bet_3c):
    # $1
    if player_turn == 'player_3' and  mouse_x >= 10 and mouse_x <= 110 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_3_score - 1 >= 0:
        try:
            pl3_bet_numbers[int(chosed_bet)] += 1
        except:
            if chosed_bet == '1st 12':
                pl3_bet_1st_12 += 1
            elif chosed_bet == '2nd 12':
                pl3_bet_2nd_12 += 1
            elif chosed_bet == '3rd 12':
                pl3_bet_3rd_12 += 1
            elif chosed_bet == '1 to 18':
                pl3_bet_1_to_18 += 1
            elif chosed_bet == 'EVEN':
                pl3_bet_even += 1
            elif chosed_bet == 'RED':
                pl3_bet_red += 1
            elif chosed_bet == 'BLACK':
                pl3_bet_black += 1
            elif chosed_bet == 'ODD':
                pl3_bet_odd += 1
            elif chosed_bet == '19 to 36':
                pl3_bet_19_to_36 += 1
            elif chosed_bet == '1º':
                pl3_bet_1c += 1
            elif chosed_bet == '2º':
                pl3_bet_2c += 1
            elif chosed_bet == '3º':
                pl3_bet_3c += 1
    # $5
    if player_turn == 'player_3' and mouse_x >= 111 and mouse_x <= 211 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_3_score - 5 >= 0:
        try:
            pl3_bet_numbers[int(chosed_bet)] += 5
        except:
            if chosed_bet == '1st 12':
                pl3_bet_1st_12 += 5
            elif chosed_bet == '2nd 12':
                pl3_bet_2nd_12 += 5
            elif chosed_bet == '3rd 12':
                pl3_bet_3rd_12 += 5
            elif chosed_bet == '1 to 18':
                pl3_bet_1_to_18 += 5
            elif chosed_bet == 'EVEN':
                pl3_bet_even += 5
            elif chosed_bet == 'RED':
                pl3_bet_red += 5
            elif chosed_bet == 'BLACK':
                pl3_bet_black += 5
            elif chosed_bet == 'ODD':
                pl3_bet_odd += 5
            elif chosed_bet == '19 to 36':
                pl3_bet_19_to_36 += 5
            elif chosed_bet == '1º':
                pl3_bet_1c += 5
            elif chosed_bet == '2º':
                pl3_bet_2c += 5
            elif chosed_bet == '3º':
                pl3_bet_3c += 5
    # $10
    if player_turn == 'player_3' and mouse_x >= 212 and mouse_x <= 312 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_3_score - 10 >= 0:
        try:
            pl3_bet_numbers[int(chosed_bet)] += 10
        except:
            if chosed_bet == '1st 12':
                pl3_bet_1st_12 += 10
            elif chosed_bet == '2nd 12':
                pl3_bet_2nd_12 += 10
            elif chosed_bet == '3rd 12':
                pl3_bet_3rd_12 += 10
            elif chosed_bet == '1 to 18':
                pl3_bet_1_to_18 += 10
            elif chosed_bet == 'EVEN':
                pl3_bet_even += 10
            elif chosed_bet == 'RED':
                pl3_bet_red += 10
            elif chosed_bet == 'BLACK':
                pl3_bet_black += 10
            elif chosed_bet == 'ODD':
                pl3_bet_odd += 10
            elif chosed_bet == '19 to 36':
                pl3_bet_19_to_36 += 10
            elif chosed_bet == '1º':
                pl3_bet_1c += 10
            elif chosed_bet == '2º':
                pl3_bet_2c += 10
            elif chosed_bet == '3º':
                pl3_bet_3c += 10
    # $25
    if player_turn == 'player_3' and mouse_x >= 313 and mouse_x <= 413 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_3_score - 25 >= 0:
        try:
            pl3_bet_numbers[int(chosed_bet)] += 25
        except:
            if chosed_bet == '1st 12':
                pl3_bet_1st_12 += 25
            elif chosed_bet == '2nd 12':
                pl3_bet_2nd_12 += 25
            elif chosed_bet == '3rd 12':
                pl3_bet_3rd_12 += 25
            elif chosed_bet == '1 to 18':
                pl3_bet_1_to_18 += 25
            elif chosed_bet == 'EVEN':
                pl3_bet_even += 25
            elif chosed_bet == 'RED':
                pl3_bet_red += 25
            elif chosed_bet == 'BLACK':
                pl3_bet_black += 25
            elif chosed_bet == 'ODD':
                pl3_bet_odd += 25
            elif chosed_bet == '19 to 36':
                pl3_bet_19_to_36 += 25
            elif chosed_bet == '1º':
                pl3_bet_1c += 25
            elif chosed_bet == '2º':
                pl3_bet_2c += 25
            elif chosed_bet == '3º':
                pl3_bet_3c += 25
    # $50
    if player_turn == 'player_3' and mouse_x >= 414 and mouse_x <= 514 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_3_score - 50 >= 0:
        try:
            pl3_bet_numbers[int(chosed_bet)] += 50
        except:
            if chosed_bet == '1st 12':
                pl3_bet_1st_12 += 50
            elif chosed_bet == '2nd 12':
                pl3_bet_2nd_12 += 50
            elif chosed_bet == '3rd 12':
                pl3_bet_3rd_12 += 50
            elif chosed_bet == '1 to 18':
                pl3_bet_1_to_18 += 50
            elif chosed_bet == 'EVEN':
                pl3_bet_even += 50
            elif chosed_bet == 'RED':
                pl3_bet_red += 50
            elif chosed_bet == 'BLACK':
                pl3_bet_black += 50
            elif chosed_bet == 'ODD':
                pl3_bet_odd += 50
            elif chosed_bet == '19 to 36':
                pl3_bet_19_to_36 += 50
            elif chosed_bet == '1º':
                pl3_bet_1c += 50
            elif chosed_bet == '2º':
                pl3_bet_2c += 50
            elif chosed_bet == '3º':
                pl3_bet_3c += 50
    # $100
    if player_turn == 'player_3' and mouse_x >= 515 and mouse_x <= 615 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_3_score - 100 >= 0:
        try:
            pl3_bet_numbers[int(chosed_bet)] += 100
        except:
            if chosed_bet == '1st 12':
                pl3_bet_1st_12 += 100
            elif chosed_bet == '2nd 12':
                pl3_bet_2nd_12 += 100
            elif chosed_bet == '3rd 12':
                pl3_bet_3rd_12 += 100
            elif chosed_bet == '1 to 18':
                pl3_bet_1_to_18 += 100
            elif chosed_bet == 'EVEN':
                pl3_bet_even += 100
            elif chosed_bet == 'RED':
                pl3_bet_red += 100
            elif chosed_bet == 'BLACK':
                pl3_bet_black += 100
            elif chosed_bet == 'ODD':
                pl3_bet_odd += 100
            elif chosed_bet == '19 to 36':
                pl3_bet_19_to_36 += 100
            elif chosed_bet == '1º':
                pl3_bet_1c += 100
            elif chosed_bet == '2º':
                pl3_bet_2c += 100
            elif chosed_bet == '3º':
                pl3_bet_3c += 100
    # $250
    if player_turn == 'player_3' and mouse_x >= 616 and mouse_x <= 716 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_3_score - 250 >= 0:
        try:
            pl3_bet_numbers[int(chosed_bet)] += 250
        except:
            if chosed_bet == '1st 12':
                pl3_bet_1st_12 += 250
            elif chosed_bet == '2nd 12':
                pl3_bet_2nd_12 += 250
            elif chosed_bet == '3rd 12':
                pl3_bet_3rd_12 += 250
            elif chosed_bet == '1 to 18':
                pl3_bet_1_to_18 += 250
            elif chosed_bet == 'EVEN':
                pl3_bet_even += 250
            elif chosed_bet == 'RED':
                pl3_bet_red += 250
            elif chosed_bet == 'BLACK':
                pl3_bet_black += 250
            elif chosed_bet == 'ODD':
                pl3_bet_odd += 250
            elif chosed_bet == '19 to 36':
                pl3_bet_19_to_36 += 250
            elif chosed_bet == '1º':
                pl3_bet_1c += 250
            elif chosed_bet == '2º':
                pl3_bet_2c += 250
            elif chosed_bet == '3º':
                pl3_bet_3c += 250
    # $500
    if player_turn == 'player_3' and mouse_x >= 717 and mouse_x <= 817 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_3_score - 500 >= 0:
        try:
            pl3_bet_numbers[int(chosed_bet)] += 500
        except:
            if chosed_bet == '1st 12':
                pl3_bet_1st_12 += 500
            elif chosed_bet == '2nd 12':
                pl3_bet_2nd_12 += 500
            elif chosed_bet == '3rd 12':
                pl3_bet_3rd_12 += 500
            elif chosed_bet == '1 to 18':
                pl3_bet_1_to_18 += 500
            elif chosed_bet == 'EVEN':
                pl3_bet_even += 500
            elif chosed_bet == 'RED':
                pl3_bet_red += 500
            elif chosed_bet == 'BLACK':
                pl3_bet_black += 500
            elif chosed_bet == 'ODD':
                pl3_bet_odd += 500
            elif chosed_bet == '19 to 36':
                pl3_bet_19_to_36 += 500
            elif chosed_bet == '1º':
                pl3_bet_1c += 500
            elif chosed_bet == '2º':
                pl3_bet_2c += 500
            elif chosed_bet == '3º':
                pl3_bet_3c += 500
    # $1.000
    if player_turn == 'player_3' and mouse_x >= 818 and mouse_x <= 918 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_3_score - 1000 >= 0:
        try:
            pl3_bet_numbers[int(chosed_bet)] += 1000
        except:
            if chosed_bet == '1st 12':
                pl3_bet_1st_12 += 1000
            elif chosed_bet == '2nd 12':
                pl3_bet_2nd_12 += 1000
            elif chosed_bet == '3rd 12':
                pl3_bet_3rd_12 += 1000
            elif chosed_bet == '1 to 18':
                pl3_bet_1_to_18 += 1000
            elif chosed_bet == 'EVEN':
                pl3_bet_even += 1000
            elif chosed_bet == 'RED':
                pl3_bet_red += 1000
            elif chosed_bet == 'BLACK':
                pl3_bet_black += 1000
            elif chosed_bet == 'ODD':
                pl3_bet_odd += 1000
            elif chosed_bet == '19 to 36':
                pl3_bet_19_to_36 += 1000
            elif chosed_bet == '1º':
                pl3_bet_1c += 1000
            elif chosed_bet == '2º':
                pl3_bet_2c += 1000
            elif chosed_bet == '3º':
                pl3_bet_3c += 1000
    # $5.000
    if player_turn == 'player_3' and mouse_x >= 918 and mouse_x <= 1018 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_3_score - 5000 >= 0:
        try:
            pl3_bet_numbers[int(chosed_bet)] += 5000
        except:
            if chosed_bet == '1st 12':
                pl3_bet_1st_12 += 5000
            elif chosed_bet == '2nd 12':
                pl3_bet_2nd_12 += 5000
            elif chosed_bet == '3rd 12':
                pl3_bet_3rd_12 += 5000
            elif chosed_bet == '1 to 18':
                pl3_bet_1_to_18 += 5000
            elif chosed_bet == 'EVEN':
                pl3_bet_even += 5000
            elif chosed_bet == 'RED':
                pl3_bet_red += 5000
            elif chosed_bet == 'BLACK':
                pl3_bet_black += 5000
            elif chosed_bet == 'ODD':
                pl3_bet_odd += 5000
            elif chosed_bet == '19 to 36':
                pl3_bet_19_to_36 += 5000
            elif chosed_bet == '1º':
                pl3_bet_1c += 5000
            elif chosed_bet == '2º':
                pl3_bet_2c += 5000
            elif chosed_bet == '3º':
                pl3_bet_3c += 5000
    # $10.000
    if player_turn == 'player_3' and mouse_x >= 1020 and mouse_x <= 1120 and mouse_y >= 490 and mouse_y <= 590 and last_click_right == False and click_right == True and player_3_score - 10000 >= 0:
        try:
            pl3_bet_numbers[int(chosed_bet)] += 10000
        except:
            if chosed_bet == '1st 12':
                pl3_bet_1st_12 += 10000
            elif chosed_bet == '2nd 12':
                pl3_bet_2nd_12 += 10000
            elif chosed_bet == '3rd 12':
                pl3_bet_3rd_12 += 10000
            elif chosed_bet == '1 to 18':
                pl3_bet_1_to_18 += 10000
            elif chosed_bet == 'EVEN':
                pl3_bet_even += 10000
            elif chosed_bet == 'RED':
                pl3_bet_red += 10000
            elif chosed_bet == 'BLACK':
                pl3_bet_black += 10000
            elif chosed_bet == 'ODD':
                pl3_bet_odd += 10000
            elif chosed_bet == '19 to 36':
                pl3_bet_19_to_36 += 10000
            elif chosed_bet == '1º':
                pl3_bet_1c += 10000
            elif chosed_bet == '2º':
                pl3_bet_2c += 10000
            elif chosed_bet == '3º':
                pl3_bet_3c += 10000
    return pl3_bet_value, pl3_bet_numbers, pl3_bet_1st_12, pl3_bet_2nd_12, pl3_bet_3rd_12, pl3_bet_1_to_18, pl3_bet_even, pl3_bet_red, pl3_bet_black, pl3_bet_odd, pl3_bet_19_to_36, pl3_bet_1c, pl3_bet_2c, pl3_bet_3c

def pl1_pay_bet(player_1_delta, last_click_right, click_right, number, mouse_x, mouse_y, player_1_score, player_turn, pl1_bet_numbers, pl1_bet_1st_12, pl1_bet_2nd_12, pl1_bet_3rd_12, pl1_bet_1_to_18, pl1_bet_even, pl1_bet_red, pl1_bet_black, pl1_bet_odd, pl1_bet_19_to_36, pl1_bet_1c, pl1_bet_2c, pl1_bet_3c):
    # Player 1 pay bet
    if click_right == True and last_click_right == False and mouse_x >= 929 and mouse_x <= 1120 and mouse_y >= 218 and mouse_y <= 317:
        if pl1_bet_numbers[number] > 0:
            player_1_score += pl1_bet_numbers[number] * 36
            player_1_delta += pl1_bet_numbers[number] * 36
        else:
            try:
                for i in range(36):
                    player_1_delta -= pl1_bet_numbers[i]
            except:
                pass
        if pl1_bet_1st_12 > 0 and number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            player_1_score += pl1_bet_1st_12 * 3
            player_1_delta += pl1_bet_1st_12 * 3
        else:
            player_1_delta -= pl1_bet_1st_12
        if pl1_bet_2nd_12 > 0 and number in [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
            player_1_score += pl1_bet_2nd_12 * 3
            player_1_delta += pl1_bet_2nd_12 * 3
        else:
            player_1_delta -= pl1_bet_2nd_12
        if pl1_bet_3rd_12 > 0 and number in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
            player_1_score += pl1_bet_3rd_12 * 3
            player_1_delta += pl1_bet_3rd_12 * 3
        else:
            player_1_delta -= pl1_bet_3rd_12
        if pl1_bet_1_to_18 > 0 and number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
            player_1_score += pl1_bet_1_to_18 * 2
            player_1_delta += pl1_bet_1_to_18 * 2
        else:
            player_1_delta -= pl1_bet_1_to_18
        if pl1_bet_19_to_36 > 0 and number in [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
            player_1_score += pl1_bet_19_to_36 * 2
            player_1_delta += pl1_bet_19_to_36 * 2
        else:
            player_1_delta -= pl1_bet_19_to_36
        if pl1_bet_even > 0 and number in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]:
            player_1_score += pl1_bet_even * 2
            player_1_delta += pl1_bet_even * 2
        else:
            player_1_delta -= pl1_bet_even
        if pl1_bet_red > 0 and number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
            player_1_score += pl1_bet_red * 2
            player_1_delta += pl1_bet_red * 2
        else:
            player_1_delta -= pl1_bet_red
        if pl1_bet_black > 0 and number in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
            player_1_score += pl1_bet_black * 2
            player_1_delta += pl1_bet_black * 2
        else:
            player_1_delta -= pl1_bet_black
        if pl1_bet_odd > 0 and number in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]:
            player_1_score += pl1_bet_odd * 2
            player_1_delta += pl1_bet_odd * 2
        else:
            player_1_delta -= pl1_bet_odd
        if pl1_bet_1c > 0 and number in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
            player_1_score += pl1_bet_1c * 3
            player_1_delta += pl1_bet_1c * 3
        else:
            player_1_delta -= pl1_bet_1c
        if pl1_bet_2c > 0 and number in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
            player_1_score += pl1_bet_2c * 3
            player_1_delta += pl1_bet_2c * 3
        else:
            player_1_delta -= pl1_bet_2c
        if pl1_bet_3c > 0 and number in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
            player_1_score += pl1_bet_3c * 3
            player_1_delta += pl1_bet_3c * 3
        else:
            player_1_delta -= pl1_bet_3c
        pl1_bet_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pl1_bet_1st_12 = 0
        pl1_bet_2nd_12 = 0
        pl1_bet_3rd_12 = 0
        pl1_bet_1_to_18 = 0
        pl1_bet_even = 0
        pl1_bet_red = 0
        pl1_bet_black = 0
        pl1_bet_odd = 0
        pl1_bet_19_to_36 = 0
        pl1_bet_1c = 0
        pl1_bet_2c = 0
        pl1_bet_3c = 0
    return player_1_delta, player_1_score, player_turn, pl1_bet_numbers, pl1_bet_1st_12, pl1_bet_2nd_12, pl1_bet_3rd_12, pl1_bet_1_to_18, pl1_bet_even, pl1_bet_red, pl1_bet_black, pl1_bet_odd, pl1_bet_19_to_36, pl1_bet_1c, pl1_bet_2c, pl1_bet_3c

def pl2_pay_bet(player_2_delta, last_click_right, click_right, number, mouse_x, mouse_y, player_2_score, player_turn, pl2_bet_numbers, pl2_bet_1st_12, pl2_bet_2nd_12, pl2_bet_3rd_12, pl2_bet_1_to_18, pl2_bet_even, pl2_bet_red, pl2_bet_black, pl2_bet_odd, pl2_bet_19_to_36, pl2_bet_1c, pl2_bet_2c, pl2_bet_3c):
    # Player 1 pay bet
    if click_right == True and last_click_right == False and mouse_x >= 929 and mouse_x <= 1120 and mouse_y >= 218 and mouse_y <= 317:
        if pl2_bet_numbers[number] > 0:
            player_2_score += pl2_bet_numbers[number] * 36
            player_2_delta += pl2_bet_numbers[number] * 36
        else:
            try:
                for i in range(36):
                    player_2_delta -= pl2_bet_numbers[i]
            except:
                pass
        if pl2_bet_1st_12 > 0 and number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            player_2_score += pl2_bet_1st_12 * 3
            player_2_delta += pl2_bet_1st_12 * 3
        else:
            player_2_delta -= pl2_bet_1st_12
        if pl2_bet_2nd_12 > 0 and number in [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
            player_2_score += pl2_bet_2nd_12 * 3
            player_2_delta += pl2_bet_2nd_12 * 3
        else:
            player_2_delta -= pl2_bet_2nd_12
        if pl2_bet_3rd_12 > 0 and number in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
            player_2_score += pl2_bet_3rd_12 * 3
            player_2_delta += pl2_bet_3rd_12 * 3
        else:
            player_2_delta -= pl2_bet_3rd_12
        if pl2_bet_1_to_18 > 0 and number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
            player_2_score += pl2_bet_1_to_18 * 2
            player_2_delta += pl2_bet_1_to_18 * 2
        else:
            player_2_delta -= pl2_bet_1_to_18
        if pl2_bet_19_to_36 > 0 and number in [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
            player_2_score += pl2_bet_19_to_36 * 2
            player_2_delta += pl2_bet_19_to_36 * 2
        else:
            player_2_delta -= pl2_bet_19_to_36
        if pl2_bet_even > 0 and number in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]:
            player_2_score += pl2_bet_even * 2
            player_2_delta += pl2_bet_even * 2
        else:
            player_2_delta -= pl2_bet_even
        if pl2_bet_red > 0 and number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
            player_2_score += pl2_bet_red * 2
            player_2_delta += pl2_bet_red * 2
        else:
            player_2_delta -= pl2_bet_red
        if pl2_bet_black > 0 and number in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
            player_2_score += pl2_bet_black * 2
            player_2_delta += pl2_bet_black * 2
        else:
            player_2_delta -= pl2_bet_black
        if pl2_bet_odd > 0 and number in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]:
            player_2_score += pl2_bet_odd * 2
            player_2_delta += pl2_bet_odd * 2
        else:
            player_2_delta -= pl2_bet_odd
        if pl2_bet_1c > 0 and number in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
            player_2_score += pl2_bet_1c * 3
            player_2_delta += pl2_bet_1c * 3
        else:
            player_2_delta -= pl2_bet_1c
        if pl2_bet_2c > 0 and number in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
            player_2_score += pl2_bet_2c * 3
            player_2_delta += pl2_bet_2c * 3
        else:
            player_2_delta -= pl2_bet_2c
        if pl2_bet_3c > 0 and number in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
            player_2_score += pl2_bet_3c * 3
            player_2_delta += pl2_bet_3c * 3
        else:
            player_2_delta -= pl2_bet_3c
        pl2_bet_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pl2_bet_1st_12 = 0
        pl2_bet_2nd_12 = 0
        pl2_bet_3rd_12 = 0
        pl2_bet_1_to_18 = 0
        pl2_bet_even = 0
        pl2_bet_red = 0
        pl2_bet_black = 0
        pl2_bet_odd = 0
        pl2_bet_19_to_36 = 0
        pl2_bet_1c = 0
        pl2_bet_2c = 0
        pl2_bet_3c = 0
    return player_2_delta, player_2_score, player_turn, pl2_bet_numbers, pl2_bet_1st_12, pl2_bet_2nd_12, pl2_bet_3rd_12, pl2_bet_1_to_18, pl2_bet_even, pl2_bet_red, pl2_bet_black, pl2_bet_odd, pl2_bet_19_to_36, pl2_bet_1c, pl2_bet_2c, pl2_bet_3c

def pl3_pay_bet(player_3_delta, last_click_right, click_right, number, mouse_x, mouse_y, player_3_score, player_turn, pl3_bet_numbers, pl3_bet_1st_12, pl3_bet_2nd_12, pl3_bet_3rd_12, pl3_bet_1_to_18, pl3_bet_even, pl3_bet_red, pl3_bet_black, pl3_bet_odd, pl3_bet_19_to_36, pl3_bet_1c, pl3_bet_2c, pl3_bet_3c):
    # Player 1 pay bet
    if click_right == True and last_click_right == False and mouse_x >= 929 and mouse_x <= 1120 and mouse_y >= 218 and mouse_y <= 317:
        if pl3_bet_numbers[number] > 0:
            player_3_score += pl3_bet_numbers[number] * 36
            player_3_delta += pl3_bet_numbers[number] * 36
        else:
            try:
                for i in range(36):
                    player_3_delta -= pl3_bet_numbers[i]
            except:
                pass
        if pl3_bet_1st_12 > 0 and number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            player_3_score += pl3_bet_1st_12 * 3
            player_3_delta += pl3_bet_1st_12 * 3
        else:
            player_3_delta -= pl3_bet_1st_12
        if pl3_bet_2nd_12 > 0 and number in [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
            player_3_score += pl3_bet_2nd_12 * 3
            player_3_delta += pl3_bet_2nd_12 * 3
        else:
            player_3_delta -= pl3_bet_2nd_12
        if pl3_bet_3rd_12 > 0 and number in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
            player_3_score += pl3_bet_3rd_12 * 3
            player_3_delta += pl3_bet_3rd_12 * 3
        else:
            player_3_delta -= pl3_bet_3rd_12
        if pl3_bet_1_to_18 > 0 and number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
            player_3_score += pl3_bet_1_to_18 * 2
            player_3_delta += pl3_bet_1_to_18 * 2
        else:
            player_3_delta -= pl3_bet_1_to_18
        if pl3_bet_19_to_36 > 0 and number in [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
            player_3_score += pl3_bet_19_to_36 * 2
            player_3_delta += pl3_bet_19_to_36 * 2
        else:
            player_3_delta -= pl3_bet_19_to_36
        if pl3_bet_even > 0 and number in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]:
            player_3_score += pl3_bet_even * 2
            player_3_delta += pl3_bet_even * 2
        else:
            player_3_delta -= pl3_bet_even
        if pl3_bet_red > 0 and number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
            player_3_score += pl3_bet_red * 2
            player_3_delta += pl3_bet_red * 2
        else:
            player_3_delta -= pl3_bet_red
        if pl3_bet_black > 0 and number in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
            player_3_score += pl3_bet_black * 2
            player_3_delta += pl3_bet_black * 2
        else:
            player_3_delta -= pl3_bet_black
        if pl3_bet_odd > 0 and number in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]:
            player_3_score += pl3_bet_odd * 2
            player_3_delta += pl3_bet_odd * 2
        else:
            player_3_delta -= pl3_bet_odd
        if pl3_bet_1c > 0 and number in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
            player_3_score += pl3_bet_1c * 3
            player_3_delta += pl3_bet_1c * 3
        else:
            player_3_delta -= pl3_bet_1c
        if pl3_bet_2c > 0 and number in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
            player_3_score += pl3_bet_2c * 3
            player_3_delta += pl3_bet_2c * 3
        else:
            player_3_delta -= pl3_bet_2c
        if pl3_bet_3c > 0 and number in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
            player_3_score += pl3_bet_3c * 3
            player_3_delta += pl3_bet_3c * 3
        else:
            player_3_delta -= pl3_bet_3c
        pl3_bet_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pl3_bet_1st_12 = 0
        pl3_bet_2nd_12 = 0
        pl3_bet_3rd_12 = 0
        pl3_bet_1_to_18 = 0
        pl3_bet_even = 0
        pl3_bet_red = 0
        pl3_bet_black = 0
        pl3_bet_odd = 0
        pl3_bet_19_to_36 = 0
        pl3_bet_1c = 0
        pl3_bet_2c = 0
        pl3_bet_3c = 0
    return player_3_delta, player_3_score, player_turn, pl3_bet_numbers, pl3_bet_1st_12, pl3_bet_2nd_12, pl3_bet_3rd_12, pl3_bet_1_to_18, pl3_bet_even, pl3_bet_red, pl3_bet_black, pl3_bet_odd, pl3_bet_19_to_36, pl3_bet_1c, pl3_bet_2c, pl3_bet_3c

# Variable
chosed_bet = None
# Variables ... for
bet = 0
bet_value = 0
# Variables for ...
number = 0
number_1 = 0
number_2 = 0
number_3 = 0
number_4 = 0
number_5 = 0
#
pl1_bet_value = 0
pl2_bet_value = 0
pl3_bet_value = 0
bet_value = 0
bet_value_str = 0
# Variables for ...
player_1_score = 1000
player_2_score = 1000
player_3_score = 1000
# Variables for ...
player_1_delta = 0
player_2_delta = 0
player_3_delta = 0
# Player Turn
player_turn = 'player_1'

# Variables for all bet data
pl1_bet_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pl2_bet_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pl3_bet_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pl1_bet_1st_12 = 0
pl2_bet_1st_12 = 0
pl3_bet_1st_12 = 0
pl1_bet_2nd_12 = 0
pl2_bet_2nd_12 = 0
pl3_bet_2nd_12 = 0
pl1_bet_3rd_12 = 0
pl2_bet_3rd_12 = 0
pl3_bet_3rd_12 = 0
pl1_bet_1_to_18 = 0
pl2_bet_1_to_18 = 0
pl3_bet_1_to_18 = 0
pl1_bet_even = 0
pl2_bet_even = 0
pl3_bet_even = 0
pl1_bet_red = 0
pl2_bet_red = 0
pl3_bet_red = 0
pl1_bet_black = 0
pl2_bet_black = 0
pl3_bet_black = 0
pl1_bet_odd = 0
pl2_bet_odd = 0
pl3_bet_odd = 0
pl1_bet_19_to_36 = 0
pl2_bet_19_to_36 = 0
pl3_bet_19_to_36 = 0
pl1_bet_1c = 0
pl2_bet_1c = 0
pl3_bet_1c = 0
pl1_bet_2c = 0
pl2_bet_2c = 0
pl3_bet_2c = 0
pl1_bet_3c = 0
pl2_bet_3c = 0
pl3_bet_3c = 0

# Variable for ...
click_right = False
# Variable for ...
last_click_right = False


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    # Declarando variavel da posição do mouse
    mouse = pg.mouse.get_pos()
    mouse_x = mouse[0]
    mouse_y = mouse[1]
    #print(str(mouse_x) + ', ' + str(mouse_y))

    click_get = pg.mouse.get_pressed()
    last_click_right = click_right
    click_right = click_get[0]

    # Player 1 All Bet Data
    pl1_bet_value, pl1_bet_numbers, pl1_bet_1st_12, pl1_bet_2nd_12, pl1_bet_3rd_12, pl1_bet_1_to_18, pl1_bet_even, pl1_bet_red, pl1_bet_black, pl1_bet_odd, pl1_bet_19_to_36, pl1_bet_1c, pl1_bet_2c, pl1_bet_3c = pl1_all_bet_data(player_1_score, player_turn, pl1_bet_value, last_click_right, click_right, chosed_bet, pl1_bet_numbers, pl1_bet_1st_12, pl1_bet_2nd_12, pl1_bet_3rd_12, pl1_bet_1_to_18, pl1_bet_even, pl1_bet_red, pl1_bet_black, pl1_bet_odd, pl1_bet_19_to_36, pl1_bet_1c, pl1_bet_2c, pl1_bet_3c)
    # Player 2 All Bet Data
    pl2_bet_value, pl2_bet_numbers, pl2_bet_1st_12, pl2_bet_2nd_12, pl2_bet_3rd_12, pl2_bet_1_to_18, pl2_bet_even, pl2_bet_red, pl2_bet_black, pl2_bet_odd, pl2_bet_19_to_36, pl2_bet_1c, pl2_bet_2c, pl2_bet_3c = pl2_all_bet_data(player_2_score, player_turn, pl2_bet_value, last_click_right, click_right, chosed_bet, pl2_bet_numbers, pl2_bet_1st_12, pl2_bet_2nd_12, pl2_bet_3rd_12, pl2_bet_1_to_18, pl2_bet_even, pl2_bet_red, pl2_bet_black, pl2_bet_odd, pl2_bet_19_to_36, pl2_bet_1c, pl2_bet_2c, pl2_bet_3c)
    # Player 3 All Bet Data
    pl3_bet_value, pl3_bet_numbers, pl3_bet_1st_12, pl3_bet_2nd_12, pl3_bet_3rd_12, pl3_bet_1_to_18, pl3_bet_even, pl3_bet_red, pl3_bet_black, pl3_bet_odd, pl3_bet_19_to_36, pl3_bet_1c, pl3_bet_2c, pl3_bet_3c = pl3_all_bet_data(player_3_score, player_turn, pl3_bet_value, last_click_right, click_right, chosed_bet, pl3_bet_numbers, pl3_bet_1st_12, pl3_bet_2nd_12, pl3_bet_3rd_12, pl3_bet_1_to_18, pl3_bet_even, pl3_bet_red, pl3_bet_black, pl3_bet_odd, pl3_bet_19_to_36, pl3_bet_1c, pl3_bet_2c, pl3_bet_3c)
    # Bet Sum
    bet_value, player_1_score, player_2_score, player_3_score = bet_calculation(bet_value, chosed_bet, last_click_right, click_right, player_1_score, player_2_score, player_3_score, player_turn)
    # Setup Money Numbers
    bet_value_str, player_1_score_str, player_2_score_str, player_3_score_str, player_1_delta_str, player_2_delta_str, player_3_delta_str = setup_money_numbers(bet_value, player_1_score, player_2_score, player_3_score, player_1_delta, player_2_delta, player_3_delta)
    # Spin
    number, number_1, number_2, number_3, number_4, number_5, player_1_delta, player_2_delta, player_3_delta = spin(last_click_right, click_right, number, mouse_x, mouse_y, number_1, number_2, number_3, number_4, number_5, player_1_delta, player_2_delta, player_3_delta)
    # Finish Bet
    chosed_bet, player_turn, bet_value = finish_bet(last_click_right, click_right, mouse_x, mouse_y, chosed_bet, player_turn, bet_value)
    # Board
    board(window, number, number_1, number_2, number_3, number_4, number_5)
    # Money Values Render
    money_values_render(bet_value_str, player_1_score_str, player_2_score_str, player_3_score_str, player_1_delta_str, player_2_delta_str, player_3_delta_str)
    # Board Hover
    board_hover(window)
    player_turn_game(window, player_turn, player_1_score_str, player_2_score_str, player_3_score_str)
    # Click Bet
    chosed_bet = click_bet(window, last_click_right, click_right, chosed_bet)
    # Player 1 Pay Bet
    player_1_delta, player_1_score, player_turn, pl1_bet_numbers, pl1_bet_1st_12, pl1_bet_2nd_12, pl1_bet_3rd_12, pl1_bet_1_to_18, pl1_bet_even, pl1_bet_red, pl1_bet_black, pl1_bet_odd, pl1_bet_19_to_36, pl1_bet_1c, pl1_bet_2c, pl1_bet_3c = pl1_pay_bet(player_1_delta, last_click_right, click_right, number, mouse_x, mouse_y, player_1_score, player_turn, pl1_bet_numbers, pl1_bet_1st_12, pl1_bet_2nd_12, pl1_bet_3rd_12, pl1_bet_1_to_18, pl1_bet_even, pl1_bet_red, pl1_bet_black, pl1_bet_odd, pl1_bet_19_to_36, pl1_bet_1c, pl1_bet_2c, pl1_bet_3c)
    # Player 2 Pay Bet
    player_2_delta, player_2_score, player_turn, pl2_bet_numbers, pl2_bet_1st_12, pl2_bet_2nd_12, pl2_bet_3rd_12, pl2_bet_1_to_18, pl2_bet_even, pl2_bet_red, pl2_bet_black, pl2_bet_odd, pl2_bet_19_to_36, pl2_bet_1c, pl2_bet_2c, pl2_bet_3c = pl2_pay_bet(player_2_delta, last_click_right, click_right, number, mouse_x, mouse_y, player_2_score, player_turn, pl2_bet_numbers, pl2_bet_1st_12, pl2_bet_2nd_12, pl2_bet_3rd_12, pl2_bet_1_to_18, pl2_bet_even, pl2_bet_red, pl2_bet_black, pl2_bet_odd, pl2_bet_19_to_36, pl2_bet_1c, pl2_bet_2c, pl2_bet_3c)
    # Player 3 Pay Bet
    player_3_delta, player_3_score, player_turn, pl3_bet_numbers, pl3_bet_1st_12, pl3_bet_2nd_12, pl3_bet_3rd_12, pl3_bet_1_to_18, pl3_bet_even, pl3_bet_red, pl3_bet_black, pl3_bet_odd, pl3_bet_19_to_36, pl3_bet_1c, pl3_bet_2c, pl3_bet_3c = pl3_pay_bet(player_3_delta, last_click_right, click_right, number, mouse_x, mouse_y, player_3_score, player_turn, pl3_bet_numbers, pl3_bet_1st_12, pl3_bet_2nd_12, pl3_bet_3rd_12, pl3_bet_1_to_18, pl3_bet_even, pl3_bet_red, pl3_bet_black, pl3_bet_odd, pl3_bet_19_to_36, pl3_bet_1c, pl3_bet_2c, pl3_bet_3c)

    pg.display.update()