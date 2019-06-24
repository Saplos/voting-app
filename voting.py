"""This simple voting app is used in the 2019 presidential elections"""

Atiku = 0
Buhari = 0
status = False


def vote():
    global Atiku, Buhari, status
    entry = int(input("Welcome to the voting app \n \
        \nFor Atiku Abubakar: 1 \n \
        \nFor Muhammadu Buhari: 2\n \
        \nTo exit: 3 \n"))
    if entry == 1:
        Atiku += 1
    elif entry == 2:
        Buhari += 1
    elif entry == 3:
        status = True


while status is False:
    vote()

print('The summary of the results are as follows: \n \
    \nAtiku Abubakar: {0} \n \
    \nMuhammadu Buhari: {1}'.format(Atiku, Buhari))
