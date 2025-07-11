import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def main():
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

    # Поиск статьи
    search_word = input("Введите слово для поиска: ")
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(search_word)
    search_box.send_keys(Keys.RETURN)

    # Переход на статью
    article_link = browser.find_element(By.LINK_TEXT, search_word)
    article_link.click()

    # Основной цикл
    while True:
        choice = input(
            "Выберите действие:\n"
            "1. Листать параграфы текущей статьи\n"
            "2. Перейти на одну из связанных страниц\n"
            "3. Выйти из программы\n"
            "> "
        )

        if choice == "1":
            browse_paragraphs(browser)
        elif choice == "2":
            navigate_to_random_related_page(browser)
        elif choice == "3":
            print("Программа завершена.")
            break
        else:
            print("Неправильное действие. Попробуйте снова.")

    browser.quit()


def browse_paragraphs(browser):
    """Прокручивает параграфы статьи."""
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        user_input = input("Нажмите 1 для следующего параграфа или 0 для выхода: ")
        if user_input == "0":
            break


def navigate_to_random_related_page(browser):
    """Переходит на случайную связанную страницу."""
    hatnotes = [
        element
        for element in browser.find_elements(By.TAG_NAME, "div")
        if element.get_attribute("class") == "hatnote navigation-not-searchable ts-main"
    ]

    if not hatnotes:
        print("Нет связанных страниц.")
        return

    random_hatnote = random.choice(hatnotes)
    link = random_hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    print(f"Переход по ссылке: {link}")
    browser.get(link)
    input("Нажмите Enter для выхода в главное меню")


if __name__ == "__main__":
    main()
