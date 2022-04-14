import random

def split():
    try:
        people = int(input("Enter the number of friends joining (including you):\n"))
    except (TypeError, ValueError):
        print("No one is joining for the party")
        return
    share = {}
    if (not people > 0):
        print("No one is joining for the party")
        return
    print()
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(people):
        name = input()
        share[name] = 0
    print()
    print("Enter the total bill value:")
    bill = int(input())
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    print()
    if answer == "Yes":
        rand = random.randint(0, people - 1)
        lucky = list(share)[rand]
        print(f"{lucky} is the lucky one!")
        print()
        share_per_person = round((bill/(people - 1)), 2)
        for i in share:
            share[i] = share_per_person
        share[lucky] = 0
        print(share)
        return
    print("No one is going to be lucky")
    print()
    share_per_person = round((bill/people), 2)
    for i in share:
        share[i] = share_per_person
    print()
    print(share)
    

split()