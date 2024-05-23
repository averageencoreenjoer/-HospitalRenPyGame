define audio.musnormal = "audio/fon1.mp3"
define audio.winmus = "audio/win.mp3"
define audio.aplo = "audio/aplo.mp3"

init:
    python:
        # Переменные для отслеживания прогресса
        answered_correctly = 0

# Сцена 1: Введение
label start:
    scene cab_orig
    show orig 
    play music musnormal
    "Привет, дружок! Давай поиграем в игру? Ты вспомнишь, как правильно ухаживать за зубами, чтобы они были здоровыми и крепкими!"
    scene cab_blur
    menu:
        "Вперед!":
            jump question_1

# Сцена 2: Вопрос 1
label question_1:
    scene cab_orig
    show orig
    play music musnormal
    "Сколько раз в день нужно чистить зубы?"
    scene cab_blur
    menu:
        "Два раза в день (утром и вечером)":
            scene cab_orig
            show funny
            play music aplo
            "Молодец! "
            jump question_2
        "Почищу, если захочу!":
            scene cab_orig
            show sad
            "О, нет! Подумай еще раз."
            jump question_1


# Сцена 4: Вопрос 2
label question_2:
    scene cab_orig
    show orig
    play music musnormal
    "Утром нужно чистить зубы ..."
    scene cab_blur
    menu:
        "После завтрака":
            scene cab_orig
            show funny
            play music aplo
            "Все верно!"
            jump question_3
        "Перед едой":
            scene cab_orig
            show sad
            "Нет! Подумай еще раз."
            jump question_2


# Сцена 5: Вопрос 3
label question_3:
    scene cab_orig
    show funny
    play music musnormal
    "Вечером зубы нужно чистить:"
    scene cab_blur
    menu:
        "Перед сном, чтобы они оставались чистыми всю ночь!":
            scene cab_orig
            show funny
            play music aplo
            "Все верно!"
            jump question_4
        "Перед ужином":
            scene cab_orig
            show sad
            "Нет-Нет! После ужина на зубах останется еда. Подумай еще раз."
            jump question_3

# Сцена 6: Вопрос 4
label question_4:
    scene cab_orig
    show orig
    play music musnormal
    "Нужно ли полоскать полость рта после каждого приема пищи чистой водой?"
    scene cab_blur
    menu:
        "Да":
            scene cab_orig
            show funny
            play music aplo
            "Ты прав! Так мы помогаем зубам оставаться чистыми в течение дня"
            jump question_5
        "Нет, достаточно чистить зубы утром и вечером":
            scene cab_orig
            show sad
            "Нет! Подумай еще раз."
            jump question_4

# Сцена 7: Вопрос 5
label question_5:
    scene cab_orig
    show orig
    play music musnormal
    "Нужно ли ходить к стоматологу, если зубы не болят?"
    scene cab_blur
    menu:
        "Да, нужно два раза в год приходить к стоматологу и показывать зубки врачу":
            scene cab_orig
            show funny
            play music aplo
            "Молодец! Ты так много знаешь!"
            jump win
        "Можно не ходить, если не болят":
            scene cab_orig
            show sad
            "Плохая идея ☹, так можно пропустить начало болезни."
            jump question_5

# Сцена 8: Победа
label win:
    scene cab_orig
    show funny
    play music musnormal
    "Молодец, ты верно ответил на все 5 вопросов!"
    "А теперь, давай проверим, знаешь ли ты, как правильно чистить зубы!"
    scene cab_blur
    menu:
        "Нужно расположить зубную щётку под углом 45° к линии десен и с помощью выметающих движений почистить зубы от десны к краю зуба":
            scene cab_orig
            show 1
            play music aplo
            "Молодец, верно!"
        "Не знаю":
            scene cab_orig
            show 1
            "Хммм, похоже что ты забыл. Надо расположить зубную щётку под углом 45° к линии десен и с помощью выметающих движений почистить зубы от десны к краю зуба "       
    show orig
    play music musnormal
    "Идем дальше!"
    scene cab_blur
    menu:
        "Такими же движениями очищаем внутреннюю поверхность каждого зуба":
            scene cab_orig
            show 2
            play music aplo
            "Так точно!"
        "Не помню...":
            scene cab_orig
            show 2
            "Не забывай, что такими же движениями мы должны очистить внутреннюю поверхность каждого зуба"
    show orig
    play music musnormal
    "Продолжаем!"
    scene cab_blur
    menu:
        "Чистим жевательную поверхность каждого зуба движениями вперёд-назад":
            scene cab_orig
            show 3
            play music aplo
            "Ты молодец! Верно!"
        "Не знаю!":
            scene cab_orig
            show 3
            "Мы чистим жевательную поверхность каждого зуба движениями вперёд-назад"
    show orig
    play music musnormal
    "Следующий этап!"
    scene cab_blur
    menu:
        "С помощью кончика зубной щётки почистим верхнюю поверхность каждого переднего зуба сверху и снизу":
            scene cab_orig
            show 4
            play music aplo
            "В точку!"
        "Не помню":
            scene cab_orig
            show 4
            "Не забывай, с помощью кончика зубной щётки мы чистим верхнюю поверхность каждого переднего зуба сверху и снизу"
    show orig
    play music musnormal
    "И последний этап..."
    scene cab_blur
    menu:
        "Не забываем чистить язык!":
            scene cab_orig
            show 5
            play music aplo
            "Ты прав!"
        "Язык чистить не надо":
            scene cab_orig
            show 5
            "Язык чистить все же надо!"
    show funny
    scene cab_blur
   




# Сцена 9: Подарок
label gift:
    scene cab_orig
    show funny
    play music winmus
    "Молодец, ты показал правильные приемы чистки зубов! Возвращайся еще, если захочешь повторить нашу увлекательную игру!"
    scene cab_blur
    menu:
        "Конец":
            scene end


