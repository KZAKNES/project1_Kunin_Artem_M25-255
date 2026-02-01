#!/usr/bin/env python3

from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, solve_puzzle, show_help
from labyrinth_game.player_actions import get_input, show_inventory, move_player, take_item, use_item

def process_command(game_state, command_line):
    """Обрабатывает команды игрока"""
    parts = command_line.split()
    if not parts:
        return

    command = parts[0].lower()
    arg = " ".join(parts[1:]) if len(parts) > 1 else ""

    if command == "go":
        if arg:
            move_player(game_state, arg)
        else:
            print("Укажите направление: go <north/south/east/west>")
    elif command == "take":
        if arg:
            take_item(game_state, arg)
        else:
            print("Укажите предмет: take <item>")
    elif command == "inventory":
        show_inventory(game_state)
    elif command == "use":
        if arg:
            use_item(game_state, arg)
        else:
            print("Укажите предмет: use <item>")
    elif command == "look":
        describe_current_room(game_state)
    elif command == "solve":
        solve_puzzle(game_state)
    elif command == "help":
        show_help()
    elif command in ["quit", "exit"]:
        game_state['game_over'] = True
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
