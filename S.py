def count_errors(dictionary, exercise):
    dictionary_set = set(dictionary)
    errors = 0
    exercise_words = exercise.split()

    for word in exercise_words:
        word = word.lower()  # Переводимо слово у нижній регістр для порівняння зі словником
        if word not in dictionary_set:  # Якщо слова немає в словнику, рахуємо його правильним
            continue
        elif word.capitalize() in dictionary_set:  # Якщо слово великими літерами є в словнику, рахуємо його правильним
            continue
        else:
            errors += 1  # В іншому випадку враховуємо помилку

    return errors

# Зчитуємо кількість слів у словнику
n = int(input())

# Читаємо словник
dictionary = [input() for _ in range(n)]

# Читаємо перший рядок вправи
exercise = input()

# Виводимо кількість помилок у вправі
print(count_errors(dictionary, exercise))

# Читаємо наступні рядки вправи та виводимо кількість помилок
while True:
    try:
        exercise = input()
        print(count_errors(dictionary, exercise))
    except EOFError:
        break
