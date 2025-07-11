import random
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get(
    "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
)

search_word = input("Введите слово для поиска: ")

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(search_word)
search_box.send_keys(Keys.RETURN)

a = browser.find_element(By.LINK_TEXT, search_word)
a.click()


while True:
    choise = input(
        "Выберите действие:\n"
        "1. Листать параграфы текущей статьи\n"
        "2. Перейти на одну из связанных страниц\n"
        "3. Выйти из программы\n"
    )

    if choise == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(paragraph.text)
            # нажмите 1 для следующего параграфа или 0 для выхода
            choice = input(
                "Нажмите 1 для следующего параграфа или 0 для выхода в главное меню: "
            )
            if choice == "0":
                break

    elif choise == "2":
        hatnotes = []
        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable ts-main":
                hatnotes.append(element)

        hatnote = random.choice(hatnotes)

        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        print(link)
        browser.get(link)
        input("Нажмите Enter для выхода в главное меню")
        continue

    elif choise == "3":
        print("Программа завершена.")
        break

    else:
        print("Неправильное действие.")
