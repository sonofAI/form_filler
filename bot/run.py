import time
from form_filler import check_and_fill_form
from db import init_db

if __name__ == "__main__":
    init_db()
    # run the form filler every 10 minutes
    while True:
        check_and_fill_form()
        time.sleep(600)
