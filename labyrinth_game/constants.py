ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый факел.',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'alchemist_lab'},
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.', '10')
    },
    'trap_room': {
        'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
        'exits': {'west': 'entrance'},
        'items': ['rusty_key'],
        'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг')
    },
    'library': {
        'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
        'exits': {'east': 'hall', 'north': 'armored_vault'},
        'items': ['ancient_book'],
        'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 'резонанс')
    },
    'alchemist_lab': {
        'description': 'Мрачная лаборатория с колбами и склянками. Воздух пахнет серой и травами.',
        'exits': {'south': 'hall', 'east': 'armored_vault'},
        'items': ['potion', 'scroll'],
        'puzzle': ('На столе записка: "Сложите числа 7 и 5 и скажите результат."', '12')
    },
    'armored_vault': {
        'description': 'Массивная комната с металлическими стенами. В центре стоит большой бронзовый сундук.',
        'exits': {'west': 'alchemist_lab', 'east': 'kitchen'},
        'items': ['bronze_chest'],
        'puzzle': ('На сундуке надпись: "Введите код, который равен сумме чисел 3, 4 и 5."', '12')
    },
    'kitchen': {
        'description': 'Старая кухня с затхлым запахом. На столе остатки еды.',
        'exits': {'west': 'armored_vault', 'north': 'treasure_room'},
        'items': ['knife', 'apple'],
        'puzzle': None
    },
    'treasure_room': {
        'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый код.',
        'exits': {'south': 'kitchen'},
        'items': ['treasure_chest'],
        'puzzle': ('Сундук защищен кодом. Введите число, которое равно сумме 5 + 5', '10')
    }
}
