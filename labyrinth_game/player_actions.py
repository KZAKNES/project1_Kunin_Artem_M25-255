from .constants import ROOMS
from .utils import describe_current_room, random_event


def get_input(prompt="> "):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"

def show_inventory(game_state):
    inventory = game_state['player_inventory']
    if inventory:
        print("Ваш инвентарь:", ", ".join(inventory))
    else:
        print("Ваш инвентарь пуст.")

def move_player(game_state, direction):
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]

    if direction in room_data['exits']:
        next_room = room_data['exits'][direction]

        # Проверка на treasure_room
        if next_room == 'treasure_room':
            # Проверяем наличие ключа в инвентаре
            if 'rusty_key' in game_state['player_inventory']:
                print("Вы используете найденный ключ, чтобы открыть путь в "
                      "комнату сокровищ.")
                game_state['current_room'] = next_room
                describe_current_room(game_state)
                random_event(game_state)
                return
            else:
                print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
                return

        # Перемещение в обычную комнату
        game_state['current_room'] = next_room
        game_state['steps_taken'] += 1
        print(f"Вы идете {direction}...\n")
        describe_current_room(game_state)
        random_event(game_state)
    else:
        print("Нельзя пойти в этом направлении.")


def take_item(game_state, item_name):
    """Поднятие предмета"""
    # Проверка на попытку поднять сундук с сокровищами
    if item_name == 'treasure_chest' and game_state['current_room'] == 'treasure_room':
        print("Вы не можете поднять сундук, он слишком тяжелый.")
        return
    
    room = ROOMS[game_state['current_room']]
    items = room.get('items', [])
    if item_name in items:
        game_state['player_inventory'].append(item_name)
        items.remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")

def use_item(game_state, item_name):
    """Использование предмета"""
    if item_name not in game_state['player_inventory']:
        print("У вас нет такого предмета.")
        return

    if item_name == 'torch':
        print("Вы зажгли факел. Стало светлее, и вы видите все вокруг.")
    elif item_name == 'potion':
        print("Вы выпили зелье. Чувствуете прилив сил!")
    elif item_name == 'scroll':
        print("Вы прочитали свиток. Он содержит магическую информацию.")
    elif item_name == 'bronze_chest':
        if 'treasure_key' not in game_state['player_inventory']:
            print("Вам нужен ключ, чтобы открыть шкатулку.")
        else:
            print("Вы открыли бронзовую шкатулку и нашли внутри ржавый ключ!")
            if 'rusty_key' not in game_state['player_inventory']:
                game_state['player_inventory'].append('rusty_key')
            # Remove the used treasure_key
            if 'treasure_key' in game_state['player_inventory']:
                game_state['player_inventory'].remove('treasure_key')
    elif item_name == 'sword':
        print("Вы держите меч. Чувствуете уверенность в себе.")
    else:
        print(f"Вы не знаете, как использовать {item_name}.")
