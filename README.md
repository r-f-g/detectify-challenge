# SQL injection vulnerability test

## Problem summary

We need to determine if the average response time from a normal request is the same as the request contain the SQL SLEEP command.
The result, if the page is vulnerable, returns less than one false positive result in ten thousand.

## Tool

URL testing tool to identify urls vulnerable to blind SQL injections.

### Description of the result

I decided to use the Student's T-test because it is a good statistical method to see if two fields with the same variance have different average values. To achieve one positive result in ten thousand, we must select p_value 5 * 10 ^ 5 and the number of requests at least 8 when we use 3s as SQL sleep time.

#### log file
In the log file, you will find information about the URL tested, the test time, and the page vulnerability result.

#### csv
The csv file contains two columns for each URL tested. The first (start with [SAFE]) contains response times for a normal request and the second (start with [INJECT]) contains response times for a request with SQL injection.
All "np.nan`" represent ConnectionError. 

### Example how to use

Terminal 1. We need to run a test server.
```bash
pipenv sync
pipenv shell
cd assignment
python app.py
```

Terminal 2. Execute our tool.
```bash
pipenv run python blind_sql_injections.py -u "http://127.0.0.1:5000/safe/1/" -u "http://127.0.0.1:5000/vulnerable/1/" -k "id" -v 1 -n 10 -s 3
```

### How run test
```bash
pipenv run pytest -sv
```

