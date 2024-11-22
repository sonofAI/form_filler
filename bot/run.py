import time
from form_filler import check_and_fill_form
from db import init_db

if __name__ == "__main__":
    init_db()
    while True:
        check_and_fill_form()
        time.sleep(60)  # 10 минут
