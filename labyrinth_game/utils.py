from labyrinth_game.constants import ROOMS

def describe_current_room(game_state):
    room_name = game_state['current_room']
    room = ROOMS[room_name]

    print(f"== {room_name.upper()} ==")
    print(room['description'])

    if room['items']:
        print("Заметные предметы:", ", ".join(room['items']))

    print("Выходы:", ", ".join(room['exits'].keys()))

    if room['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")

def solve_puzzle(game_state):
    """Попытка решить загадку в текущей комнате"""
    current_room = game_state['current_room']
    room = ROOMS[current_room]

    if room['puzzle'] is None:
        print("Загадок здесь нет.")
        return

    question, answer = room['puzzle']
    print(question)
    user_answer = input("Ваш ответ: ").strip().lower()

    if user_answer == answer.lower():
        print("Верно! Вы успешно решили загадку.")
        # Убираем загадку, чтобы нельзя было решить дважды
        room['puzzle'] = None
        # Если это комната с сокровищем — победа
        if current_room == "treasure_room":
            print("Сундук открыт! Вы нашли сокровище. Поздравляем, вы победили!")
            game_state['game_over'] = True
    else:
        print("Неверно. Попробуйте снова.")

def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")
