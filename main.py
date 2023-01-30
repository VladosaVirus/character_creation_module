from random import randint


DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:

    CHAR_CLASS = 'отважный любитель приключений'
    ATTACK = (1, 3)
    DEFENCE = (1, 5)
    BUFF = 15
    SPECIAL_SKILL = 'Удача'

    def __init__(self, name):
        self.name = name


    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.ATTACK)
        return f'{self.name} нанес противку урон равный {value_attack}'


    def defence(self):
        value_defence = DEFAULT_DEFENCE + randit(*self.DEFENCE)
        return f'{self.name} блокировал {value_defence}'


    def SPECIAL(self):
        return (f'{self.name} применил специальное умение'
                f'{self.SPECIAL_SKILL} {self.BUFF}')


    def __str__(self) -> str:
        return f'{self.__class__.__name__} - {self.CHAR_CLASS}'


class Warrior(Character):
    CHAR_CLASS = ('дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
    ATTACK = (3, 5)
    DEFENCE = (5, 10)
    BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    CHAR_CLASS = ('находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
    ATTACK = (5 + 10)
    DEFENCE = (-2, 2)
    BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    CHAR_CLASS = ('могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
    ATTACK = (-3, -1)
    DEFENCE = (2, 5)
    BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def start_training(Character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    commands = {'attack': character.attack,
                'defence': character.defence,
                'special': character.special}
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands:
            print((selected_class(char_name)))
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    
    approve_choice: str = None

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()