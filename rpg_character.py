# RPG Character Creator

full_dot = "●"
empty_dot = "○"
MAX_STAT = 10


class Character:
    def __init__(self, name, strength, intelligence, charizma):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.charizma = charizma

    def choose_class(self):
        class_descriptions = {
            "Warrior": "A fearless fighter, strong in battle.",
            "Mage": "A master of arcane knowledge.",
            "Bard": "A charismatic storyteller and performer.",
        }
        if self.strength >= self.intelligence and self.strength >= self.charizma:
            char_class = "Warrior"
        elif self.intelligence >= self.charizma:
            char_class = "Mage"
        else:
            char_class = "Bard"
        return char_class, class_descriptions.get(char_class)

    def stats(self):
        stat_string = empty_dot * MAX_STAT
        strn = stat_string.replace(empty_dot, full_dot, self.strength)
        intl = stat_string.replace(empty_dot, full_dot, self.intelligence)
        char = stat_string.replace(empty_dot, full_dot, self.charizma)

        return f"STR {strn}\nINT {intl}\nCHA {char}"

    def validate_character(self):

        if not isinstance(self.name, str):
            return "The character name should be a string"
        elif self.name == "":
            return "The character should have a name"
        elif len(self.name) > 10:
            return "The character name is too long"
        elif " " in self.name:
            return "The character name should not contain spaces"

        if (
            not isinstance(self.strength, int)
            or not isinstance(self.intelligence, int)
            or not isinstance(self.charizma, int)
        ):
            return "All stats should be integers"
        elif self.strength < 1 or self.intelligence < 1 or self.charizma < 1:
            return "All stats should be no less than 1"
        elif self.strength > 4 or self.intelligence > 4 or self.charizma > 4:
            return "All stats should be no more than 4"
        elif sum([self.strength, self.intelligence, self.charizma]) != 7:
            return "The character should start with 7 points"
        character_stats = self.stats()
        hero_class, hero_description = self.choose_class()

        return f"{self.name}\n{hero_class}: {hero_description}\n{character_stats}"


try:
    hero = Character(
        input("Hero name: "),
        int(input("STR: ")),
        int(input("INT: ")),
        int(input("CHA: ")),
    )
    print(hero.validate_character())
except KeyboardInterrupt:
    print("\nExit")
except ValueError:
    print("\nAll stats shoul be numbers")
