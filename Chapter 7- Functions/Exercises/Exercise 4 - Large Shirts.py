def make_shirt(shirt_size='large', message_in_the_shirt='I love Python!'):
    print()
    print("I'm going to make a " + (shirt_size) + " t-shirt.")
    print("It will say, " + (message_in_the_shirt))
make_shirt()
make_shirt(shirt_size='medium')
print()
make_shirt('extra extra large', 'Programmers < gamers.')