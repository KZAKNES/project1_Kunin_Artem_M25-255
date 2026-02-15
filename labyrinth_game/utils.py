import math

from .constants import ROOMS


def pseudo_random(seed, modulo):
    """Простейший псевдослучайный генератор на основе синуса"""
    x = math.sin(seed * 12.9898) * 43758.5453
    frac = x - math.floor(x)
    return int(frac * modulo)

def trigger_trap(game_state):
    """Срабатывание ловушки"""
    print("Ловушка активирована! Пол стал дрожать...")
    inventory = game_state['player_inventory']
    if inventory:
        idx = pseudo_random(game_state['steps_taken'], len(inventory))
        lost_item = inventory.pop(idx)
        print(f"Вы потеряли предмет: {lost_item}")
    else:
        chance = pseudo_random(game_state['steps_taken'], 10)
        if chance < 3:
            print("Вы попали в смертельную ловушку. Игра окончена.")
            game_state['game_over'] = True
        else:
            print("Вы чудом избежали опасности.")

def describe_current_room(game_state):
    """Печать описания текущей комнаты"""
    room_name = game_state['current_room']
    room = ROOMS[room_name]
    print(f"\n== {room_name.upper()} ==")
    print(room['description'])
    if room.get('items'):
        print("Заметные предметы:", ", ".join(room['items']))
    print("Выходы:", ", ".join(room['exits']))
    if room.get('puzzle'):
        print("Кажется, здесь есть загадка (используйте команду solve).")

def random_event(game_state):
    """Случайные события при перемещении"""
    chance = pseudo_random(game_state['steps_taken'], 10)
    if chance != 0:
        return  # событие не произошло

    event_type = pseudo_random(game_state['steps_taken'], 3)
    inventory = game_state['player_inventory']
    current_room = game_state['current_room']

    if event_type == 0:
        print("Вы нашли на полу монетку.")
        ROOMS[current_room]['items'].append('coin')
    elif event_type == 1:
        print("Вы услышали странный шорох.")
        if 'sword' in inventory:
            print("Вы отпугнули существо своим мечом.")
    elif event_type == 2:
        if current_room == 'trap_room' and 'torch' not in inventory:
            print("Вы попали в опасное место!")
            trigger_trap(game_state)

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

def attempt_open_treasure(game_state):
   """Попытка открыть сундук с сокровищами"""
   room_name = game_state['current_room']
   if room_name != 'treasure_room':
       print("Здесь нет сундука с сокровищами.")
       return
   
   # Проверка наличия ключа
   if 'treasure_key' in game_state['player_inventory']:
       print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
       # Удаляем сундук из комнаты
       if 'treasure_chest' in ROOMS[room_name]['items']:
           ROOMS[room_name]['items'].remove('treasure_chest')
       print("В сундуке сокровище! Вы победили!")
       game_state['game_over'] = True
       return
   
   # Предложение ввести код
   print("Сундук заперт. Нужен ключ или код.")
   choice = input("Ввести код? (да/нет): ").strip().lower()
   
   if choice == 'да':
       # Получаем правильный код из загадки
       puzzle = ROOMS[room_name].get('puzzle')
       if puzzle:
           correct_code = puzzle[1]
           code = input("Введите код: ").strip()
           if code == correct_code:
               print("Замок щёлкает! Сундук открыт!")
               if 'treasure_chest' in ROOMS[room_name]['items']:
                   ROOMS[room_name]['items'].remove('treasure_chest')
               print("В сундуке сокровище! Вы победили!")
               game_state['game_over'] = True
           else:
               print("Неверный код.")
       else:
           print("Не удалось получить код.")
   else:
       print("Вы отступаете от сундука.")

def solve_puzzle(game_state):
    """Решение загадки в текущей комнате"""
    room_name = game_state['current_room']
    
    # Если игрок в комнате с сокровищами, вызываем специальную функцию
    if room_name == 'treasure_room':
        from .utils import attempt_open_treasure
        attempt_open_treasure(game_state)
        return
    
    room = ROOMS[room_name]
    puzzle = room.get('puzzle')

    if not puzzle:
        print("Загадок здесь нет.")
        return

    question_text, correct_answer = puzzle
    print(question_text)
    answer = input("Ваш ответ: ").strip().lower()

    # Дополнительно можно принимать альтернативный ответ, например 'десять' для '10'
    alt_answers = []
    if room_name == 'hall':
        alt_answers = ['десять']
    elif room_name == 'alchemist_lab':
        alt_answers = ['двенадцать']
    elif room_name == 'armored_vault':
        alt_answers = ['двенадцать']

    valid_answers = [str(correct_answer).lower()] + [a.lower() for a in alt_answers]

    if answer in valid_answers:
        print("Верно! Вы успешно решили загадку.")
        # Можно добавить награду за решение, если нужно
        # Например, добавим ключ в качестве награды за решение загадки в armored_vault
        if room_name == 'armored_vault':
            if 'treasure_key' not in game_state['player_inventory']:
                game_state['player_inventory'].append('treasure_key')
                print("Вы нашли ключ от сундука с сокровищами!")
    else:
        print("Неверно.")
        if room_name == 'trap_room':
            trigger_trap(game_state)

