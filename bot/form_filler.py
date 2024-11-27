from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from db import get_next_user, update_user_status
from datetime import datetime
import time

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  # чтобы сохранить скрины

FORM_URL = "https://b24-iu5stq.bitrix24.site/backend_test/"

def check_and_fill_form():
    user = get_next_user()
    if not user:
        print("Нет пользователей для обработки.")
        return

    user_id, name, surname, email, phone, birth_date, status = user

    options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")  # browser wont be shown
    driver = webdriver.Firefox(options=options)

    try:
        driver.get(FORM_URL)
        time.sleep(3)

        driver.find_element(By.NAME, "name").send_keys(name)
        driver.find_element(By.NAME, "lastname").send_keys(surname)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "b24-form-btn").click()  # это кнопа далее
        time.sleep(2)

        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "phone").send_keys(phone)
        time.sleep(2)
        buttons = driver.find_elements(By.CLASS_NAME, "b24-form-btn")
        buttons[1].click()  # тута были две кнопки с одинакывыми классами(назад и далее) поэтому находим обе и выбираем вторую
        time.sleep(2)

        birth_date_input = driver.find_element(By.XPATH, "//input[@class='b24-form-control'][@readonly='readonly']")
        driver.execute_script("arguments[0].value = arguments[1];", birth_date_input, birth_date)  # просто делаем валуе = валуе чтобы вставить др а то по другому туда писать не получается кроме что все детали в ручную нажимать
        time.sleep(3)
        buttons = driver.find_elements(By.CLASS_NAME, "b24-form-btn")
        buttons[1].click()


        # SAVINGGGG
        time.sleep(3)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        screenshot_path = f"{BASE_DIR}/screenshots/{timestamp}_{name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Скриншот сохранён: {screenshot_path}")

        update_user_status(user_id, "filled")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()
    