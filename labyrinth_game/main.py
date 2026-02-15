#!/usr/bin/env python3

from .constants import COMMANDS
from .player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from .utils import (
    describe_current_room,
    random_event,
    solve_puzzle,
)


def show_help():
    print("\nДоступные команды:")
    for cmd, desc in COMMANDS.items():
        print(f"  {cmd.ljust(16)} - {desc}")

def process_command(game_state, command_line):
    """Обрабатывает команды игрока"""
    parts = command_line.split()
    if not parts:
        return
    
    command = parts[0].lower()
    arg = " ".join(parts[1:]) if len(parts) > 1 else ""

    # Односложные команды направления превращаем в go
    if command in ["north", "south", "east", "west"]:
        command = "go"
        arg = command_line.lower()

    if command == "go":
        if arg:
            move_player(game_state, arg)
            random_event(game_state)  # Случайные события после перемещения
        else:
            print("Укажите направление: go <north/south/east/west>")
    elif command == "take":
        if arg:
            take_item(game_state, arg)
        else:
            print("Укажите предмет: take <item>")
    elif command == "inventory":
        show_inventory(game_state)
    elif command in ["quit", "exit"]:
        game_state['game_over'] = True
    elif command == "help":
        show_help()
    elif command == "use":
        if arg:
            use_item(game_state, arg)
        else:
            print("Укажите предмет: use <item>")
    elif command == "solve":
        # Если игрок в treasure_room, вызов особой функции
        if game_state['current_room'] == "treasure_room":
            from .utils import attempt_open_treasure
            attempt_open_treasure(game_state)
        else:
            solve_puzzle(game_state)
    elif command == "look":
        describe_current_room(game_state)
    else:
        print("Неизвестная команда. Используйте help.")

def main():
    """Главная функция игры"""
    print("Добро пожаловать в Лабиринт сокровищ!")

    game_state = {
        'player_inventory': [],
        'current_room': 'entrance',
        'game_over': False,
        'steps_taken': 0
    }

    # Показываем описание стартовой комнаты
    describe_current_room(game_state)

    # Основной игровой цикл
    while not game_state['game_over']:
        command = get_input("Введите команду: ")
        process_command(game_state, command)

    print("Игра завершена. Спасибо за игру!")

if __name__ == "__main__":
    main()
