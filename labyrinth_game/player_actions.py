from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room

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
        game_state['current_room'] = next_room
        game_state['steps_taken'] += 1
        print(f"Вы идете {direction}...\n")
        describe_current_room(game_state)
    else:
        print("Нельзя пойти в этом направлении.")

def take_item(game_state, item_name):
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]

    if item_name in room_data['items']:
        game_state['player_inventory'].append(item_name)
        room_data['items'].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")

def use_item(game_state, item_name):
    inventory = game_state['player_inventory']
    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return

    if item_name == "torch":
        print("Вы зажгли факел. Стало светлее, и вы видите все вокруг.")
    elif item_name == "sword":
        print("Вы держите меч уверенно. Чувствуете силу.")
    elif item_name == "bronze_chest":
        print("Вы открыли бронзовую шкатулку и нашли внутри rusty_key.")
        if "rusty_key" not in inventory:
            inventory.append("rusty_key")
    else:
        print("Вы не знаете, как использовать этот предмет.")
