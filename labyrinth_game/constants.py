COMMANDS = {
    "go <direction>": "перейти в направлении (north/south/east/west)",
    "take <item>": "поднять предмет",
    "use <item>": "использовать предмет",
    "inventory": "показать инвентарь",
    "solve": "решить загадку в комнате",
    "quit / exit": "выйти из игры",
    "help": "показать это сообщение"
}


ROOMS = {
    'entrance': {
        'description': (
            'Вы в темном входе лабиринта. Стены покрыты мхом. '
            'На полу лежит старый факел.'
        ),
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': (
            'Большой зал с эхом. По центру стоит пьедестал с '
            'запечатанным сундуком.'
        ),
        'exits': {
            'south': 'entrance',
            'west': 'armored_vault',
            'north': 'alchemist_lab'
        },
        'items': [],
        'puzzle': (
            'Назовите число, которое идет после девяти.',
            '10'
        )
    },
    'trap_room': {
        'description': (
            'Комната с подозрительным полом. Кажется, '
            'здесь много ловушек.'
        ),
        'exits': {
            'west': 'entrance',
            'north': 'library',
            'east': 'kitchen'
        },
        'items': [],
        'puzzle': None
    },
    'alchemist_lab': {
        'description': (
            'Мрачная лаборатория с колбами и склянками. '
            'Воздух пахнет серой и травами.'
        ),
        'exits': {
            'south': 'hall',
            'east': 'armored_vault'
        },
        'items': ['potion', 'scroll'],
        'puzzle': (
            'Сложите числа 7 и 5 и скажите результат.',
            '12'
        )
    },
    'armored_vault': {
        'description': (
            'Массивная комната с металлическими стенами. '
            'В центре стоит большой бронзовый сундук.'
        ),
        'exits': {
            'west': 'alchemist_lab',
            'east': 'treasure_room'
        },
        'items': ['bronze_chest'],
        'puzzle': (
            'Введите код, который равен сумме чисел 3, 4 и 5.',
            '12'
        )
    },
    'library': {
        'description': (
            'Старая библиотека с пыльными книгами. '
            'Здесь тихо и прохладно.'
        ),
        'exits': {'south': 'trap_room'},
        'items': ['ancient_book'],
        'puzzle': None
    },
    'kitchen': {
        'description': (
            'Кухня с разбросанной посудой. Запахи давно ушли.'
        ),
        'exits': {'west': 'trap_room'},
        'items': ['knife'],
        'puzzle': None
    },
    'treasure_room': {
        'description': (
            'Комната, на столе большой сундук с сокровищами.'
        ),
        'exits': {'west': 'armored_vault'},
        'items': ['treasure_chest'],
        'puzzle': (
            'Поздравляем! Вы нашли сокровища. '
            'Введите любое число, чтобы открыть сундук.',
            '0'
        )
    }
}
