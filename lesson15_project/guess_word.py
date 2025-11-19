import random

words_by_category = {
    "фрукти": {
        1: ["ківі", "мак", "лічі"],
        2: ["яблуко", "банан", "груша"],
        3: ["виноград", "апельсин", "ананас"]
    },
    "овочі": {
        1: ["кріп", "буряк", "ріпа"],
        2: ["морква", "цибуля", "гарбуз"],
        3: ["баклажан", "картопля", "кабачок"]
    },
    "природа": {
        1: ["ліс", "море", "сніг"],
        2: ["озеро", "пісок", "вітер"],
        3: ["водоспад", "джерело", "полуострів"]
    }
}

def shuffle_word(word):
    char_list = list(word.upper())
    random.shuffle(char_list)
    return " ".join(char_list)


def choice_category():
    category = input(f"Введіть категорію ({', '.join(words_by_category.keys())}): ")
    while category not in words_by_category:
        category = input(f"Введіть категорію ({', '.join(words_by_category.keys())}): ")
    return category


def choice_level():
    level = int(input("Введіть номер рівня гри (1-3): "))
    while level not in words_by_category[category]:
        level = int(input("Введіть номер рівня гри. Будь-ласка, введіть число від 1 до 3: "))
    return level

category = choice_category()
level = choice_level()
word = random.choice(words_by_category[category][level])
shuffled = shuffle_word(word)

print("Вгадай слово! Ось його перемішані літери: ", shuffled)
print(f"Підказка: перша літера - {word[0]}, остання - {word[-1]}")

attempts = 3
while attempts > 0:
    guess = input("Веди слово: ").lower()
    if guess == word:
        print("Правильно! Ти відгадав слово!")
        break
    else:
        attempts -= 1
        print(f"Неправильно! Залишилось спроб: {attempts}")
else:
    print(f"Гру закінчено. Правильне слово було: {word}")