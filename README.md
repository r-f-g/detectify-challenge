# SQL injection vulnerability test

URL testing tool to identify urls vulnerable to blind SQL injections.

# Example

Terminal 1.
```bash
pipenv sync
pipenv shell
cd assignment
python app.py
```

Terminal 2.
```bash
pipenv run python blind_sql_injections.py -u "http://127.0.0.1:5000/safe/1/" -u "http://127.0.0.1:5000/vulnerable/1/" -k "id" -v 1 -n 10 -s 3
```
