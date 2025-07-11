import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def word_translation(word):
    translator = Translator()
    result = translator.translate(word, src="en", dest="ru")
    return result.text


def get_english_words():
    url = "https://randomword.com/"

    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        english_word_element = soup.find("div", id="random_word")
        if english_word_element is not None:
            english_word = english_word_element.text.strip()
        else:
            english_word = ""  # или некоторое значение по умолчанию

        word_definition_element = soup.find("div", id="random_word_definition")
        if word_definition_element is not None:
            word_definition = word_definition_element.text.strip()
        else:
            word_definition = ""  # или некоторое значение по умолчанию

        return {"english_word": english_word, "word_definition": word_definition}

    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None


def word_game():
    print('Добро пожаловать в игру "Угадай слово"!')

    while True:
        word_dict = get_english_words()

        if (
            not word_dict
            or "english_word" not in word_dict
            or "word_definition" not in word_dict
        ):
            break

        word = word_dict["english_word"]
        definition = word_dict["word_definition"]

        word_rus = word_translation(word)
        definition_rus = word_translation(definition)

        print(f"Значение слова: {definition_rus}")

        user_input = input("Введите слово на русском языке: ")

        if user_input == word_rus:
            print("Поздравляем! Вы угадали слово!")
        else:
            print(f"Неправильно. Было загадано слово: {word_rus}.")

        play_again = input("Хотите сыграть ещё? (y/n): ")
        if play_again.lower() != "y":
            break

    print("Спасибо за игру!")


if __name__ == "__main__":
    word_game()
