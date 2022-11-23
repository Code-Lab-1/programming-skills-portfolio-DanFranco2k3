glossary = {
    'integers': 'are whole number datas.',
    'floats': 'are numbers with decimal point.',
    'strings': 'are text enclosed in single or double quotes.',
    'boolean': 'can be represented as true or false.',
    'print': "is used to send message or output to the screen.",

    'function': 'is a group of related statements that performs a specific task.',
    'lists': "are used to store items.",
    'variable': 'stores a value by assigning it to a name.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")