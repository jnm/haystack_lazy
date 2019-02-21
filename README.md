1. `pip install -r requirements.txt`
1. `./manage.py migrate`
1. `./manage.py loaddata data.json`
1. `./manage.py runserver`
1. Go to http://localhost:8000/admin/ and log in as user `testy` with password `testy`
1. In the same browser session, go to http://localhost:8000/favorite_word/banana/
1. Observe
    ```
    Exception Type: TypeError at /favorite_word/banana
    Exception Value: 'User' object is not iterable
    ```
