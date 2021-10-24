import random
def cards():
    blue = [str(x)+'_blue' for x in range(1,10)]+[str(x)+'_blue' for x in range(10)]
    for i in range(2):
        blue.append('reverse_blue')
        blue.append('+2_blue')
        blue.append('skip_blue')
    blue.append('change_color')
    blue.append('+4')

    red = [str(x)+'_red' for x in range(1,10)]+[str(y)+'_red' for y in range(10)]
    for i in range(2):
        red.append('reverse_red')
        red.append('+2_red')
        red.append('skip_red')
    red.append('change_color')
    red.append('+4')

    green = [str(x)+'_green' for x in range(1,10)]+[str(z)+'_green' for z in range(10)]
    for i in range(2):
        green.append('reverse_green')
        green.append('+2_green')
        green.append('skip_green')
    green.append('change_color')
    green.append('+4')

    yellow = [str(x)+'_yellow' for x in range(1,10)]+[str(u)+'_yellow' for u in range(10)]
    for i in range(2):
        yellow.append('reverse_yellow')
        yellow.append('+2_yellow')
        yellow.append('skip_yellow')
    yellow.append('change_color')
    yellow.append('+4')

    cards = blue + red + green + yellow
    return cards

def decks():
    numPlayers = input('How many players are gonna play? ')
    count = 1
    nicknames = []
    while count <= int(numPlayers):
        nickname = input('Type your nickname: ')
        nicknames.append(nickname)
        count += 1
    decks = []
    for i in range(int(numPlayers)):
        decks.append(random.choices(cards(), k = 6))

    return decks

print(decks())
    
    