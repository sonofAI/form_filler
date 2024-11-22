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
        time.sleep(2)

        driver.find_element(By.NAME, "name").send_keys(name)
        driver.find_element(By.NAME, "surname").send_keys(surname)
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "phone").send_keys(phone)
        driver.find_element(By.NAME, "birth_date").send_keys(birth_date)
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        screenshot_path = f"./screenshots/{timestamp}_{name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Скриншот сохранён: {screenshot_path}")

        update_user_status(user_id, "filled")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()
