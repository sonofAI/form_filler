from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from db import get_next_user, update_user_status
from datetime import datetime
import time

def check_and_fill_form():
    user = get_next_user()
    if not user:
        print("Нет пользователей для обработки.")
        return

    user_id, name, surname, email, phone, birth_date, status = user

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.binary_location = "/usr/bin/chromium"
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://b24-iu5stq.bitrix24.site/backend_test/")
        time.sleep(3)

        # Шаг 1: Ввод имени и фамилии
        driver.find_element(By.NAME, "name").send_keys(name)  # Введите имя
        driver.find_element(By.NAME, "lastname").send_keys(surname)  # Введите фамилию
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "b24-form-btn").click()  # Нажмите «Далее» для перехода к следующему шагу
        time.sleep(2)  # Дождитесь загрузки следующего шага

        # Шаг 2: Ввод email и телефона
        driver.find_element(By.NAME, "email").send_keys(email)  # Введите email
        driver.find_element(By.NAME, "phone").send_keys(phone)  # Введите номер телефона
        time.sleep(2)
        # driver.find_element(By.CLASS_NAME, "b24-form-btn").click()  # Нажмите «Далее» для перехода к следующему шагу
        # submit_button = driver.find_element(By.XPATH, "//button[text()='Далее']")
        # submit_button.click()
        buttons = driver.find_elements(By.CLASS_NAME, "b24-form-btn")
        buttons[1].click()
        time.sleep(2)  # Дождитесь загрузки следующего шага

        # Шаг 3: Ввод даты рождения и отправка формы
        # driver.find_element(By.NAME, "birth_date").send_keys(birth_date)  # Введите дату рождения
        # driver.find_element(By.ID, "submit_button").click()  # Нажмите кнопку «Отправить»
        birth_date_input = driver.find_element(By.XPATH, "//input[@class='b24-form-control'][@readonly='readonly']")
        driver.execute_script("arguments[0].value = arguments[1];", birth_date_input, birth_date)
        # birth_date_input.click()  # Открываем календарь, если поле кликабельно
        # birth_date_input.send_keys(birth_date)  # Вводим дату
        time.sleep(10)  # Дождитесь завершения отправки
        # driver.find_element(By.CLASS_NAME, "b24-form-btn").click()  # Нажмите «Далее» для перехода к следующему шагу
        # submit_button = driver.find_element(By.XPATH, "//button[text()='Отправить']")
        # submit_button.click()
        buttons = driver.find_elements(By.CLASS_NAME, "b24-form-btn")
        buttons[1].click()


        time.sleep(3)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        screenshot_path = f"./screenshots/{timestamp}_{name}.png"
        screenshot_path = f"C:/Users/ME/Desktop/form_filler-main/form_filler-main/bot/screenshots/{timestamp}_{name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Скриншот сохранён: {screenshot_path}")

        update_user_status(user_id, "filled")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()
    