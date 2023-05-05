import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


def poem_generator(user_strings):
    driver = webdriver.Chrome()

    driver.get("http://neogranka.ru/generator_stihov.html")

    title = driver.title
    assert title == "Генератор стихов"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="text")
    print(text_box.text)
    submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    text_box.send_keys(f"""{user_strings} 
    """)
    submit_button.click()

    try:
        while True:
            ud = driver.find_element(By.NAME, 'ud')
            ud.is_selected()
            select_button = driver.find_element(By.CSS_SELECTOR, 'button.mod-udareniye-submit.link1')
            select_button.click()
    except selenium.common.exceptions.NoSuchElementException:
        pass

    message = driver.find_element(By.CSS_SELECTOR, 'div.error')
    value = message.text
    print(value)
    result = driver.find_element(By.CSS_SELECTOR, 'div.result')
    print(result.text)
    return result.text
    # assert value == "Введите текст...!"

    driver.quit()


if __name__ == '__main__':
    poem_generator("С рифмой у меня плохо чувак Не придумаваются никак")


