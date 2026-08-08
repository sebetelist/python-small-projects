# RPG Character Creator 

full_dot = '●'
empty_dot = '○'
MAX_STAT = 10


def create_character(name, strength, intelligence, charizma):

    if not isinstance(name, str):
        return 'The character name should be a string'
    elif name == '':
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif ' ' in name:
        return 'The character name should not contain spaces'

    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charizma, int):
        return 'All stats should be integers'
    elif strength < 1 or intelligence < 1 or charizma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or intelligence > 4 or charizma > 4:
        return 'All stats should be no more than 4'
    elif sum([strength, intelligence, charizma]) != 7:
        return 'The character should start with 7 points'
    character_stats = stats(strength, intelligence, charizma)
    hero_class, hero_description = choose_class(strength, intelligence, charizma)

    return f"{name}\n{hero_class}: {hero_description}\n{character_stats}"


def stats(strength, intelligence, charizma):
    stat_string = empty_dot * MAX_STAT
    strn = stat_string.replace(empty_dot,full_dot, strength)
    intl = stat_string.replace(empty_dot,full_dot, intelligence)
    char = stat_string.replace(empty_dot, full_dot, charizma)

    return f'STR {strn}\nINT {intl}\nCHA {char}'

def choose_class(strength, intelligence, charizma):
    class_descriptions = {
    'Warrior': 'A fearless fighter, strong in battle.',
    'Mage': 'A master of arcane knowledge.',
    'Bard': 'A charismatic storyteller and performer.'
}
    if strength >= intelligence and strength >= charizma:
        char_class = 'Warrior'
    elif intelligence >= charizma:
        char_class = 'Mage'
    else:
        char_class = 'Bard'
    return char_class, class_descriptions.get(char_class)



try:
    print(create_character(input('Hero name: '), int(input('STR: ')), int(input('INT: ')), int(input('CHA: '))))
except KeyboardInterrupt:
    print('\nExit')
except ValueError:
    print('\nAll stats shoul be numbers')


