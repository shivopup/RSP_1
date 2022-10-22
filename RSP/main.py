import random
# 1-rock, 2-scissors, 3-paper

mcount = 0
pcount = 0

variation = ['rock', 'scissors', 'paper']

while mcount < 2 and pcount < 2:

    def Start():

        global mcount

        button = str.lower(input('If you wanna play-print "play". \nIf you wanna stop playing-print"stop"\n'))

        if button == 'play':
            Choosing()
        elif button == 'stop':
            print('Thanks for playing!')
            mcount = 4
        else:
            print('I do not understand, try again\n ')
            Start()

    def Choosing():

        global mcount, pcount

        while mcount < 2 and pcount < 2:

        machine = random.choice(variation)

            players_choice = input('Make your choice!\n 1-Rock\n 2-Scissors\n 3-paper\n 4-Come back to the main menu\n')

            def Battle():

                global pcount, mcount

                if machine == players_choice:
                    print(pcount, mcount)
                    Choosing()

                elif machine == 'rock' and players_choice == 'scissors':
                    mcount += 1
                    print(pcount, mcount)
                    Choosing()

                elif machine == 'rock' and players_choice == 'paper':
                    pcount += 1
                    print(pcount, mcount)
                    Choosing()

                elif machine == 'scissors' and players_choice == 'rock':
                    pcount += 1
                    print(pcount, mcount)
                    Choosing()

                elif machine == 'scissors' and players_choice == 'paper':
                    mcount += 1
                    print(pcount, mcount)
                    Choosing()

                elif machine == 'paper' and players_choice == 'scissors':
                    pcount += 1
                    print(pcount, mcount)
                    Choosing()

                elif machine == 'paper' and players_choice == 'rock':
                    mcount += 1
                    print(pcount, mcount)
                    Choosing()

            if players_choice == '1':
                players_choice = 'rock'
                print(players_choice)
                print(machine)
            elif players_choice == '2':
                players_choice = 'scissors'
                print(players_choice)
                print(machine)
            elif players_choice == '3':
                players_choice = 'paper'
                print(players_choice)
                print(machine)
            elif players_choice == '4':
                print('Returning to the main menu')
                Start()
            else:
                print('You can choose only 1, 2, 3 or 4. Try again!')
                Choosing()

            Battle()

    Start()

if mcount == 2:
    print(f'You lost, Game over\nThe final score is {pcount} {mcount}\n')
elif pcount == 2:
    print(f'You are a winner. Congratulations!\nThe final score is {pcount} {mcount}\n')

x = input('Enter every key to close the app\n')