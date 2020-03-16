import logging
import time
from datetime import datetime
from typing import List

import click
from tqdm import tqdm

from utils.logger import set_up_logger
from utils.save import save_results
from vulnerability.sql_injections import url_vulnerability

logger = logging.getLogger(__name__)


@click.command()
@click.option("--urls", "-u", multiple=True, type=click.STRING, required=True, help="list of urls to be tested")
@click.option("--key", "-k", type=click.STRING, default="id", help="name of argument")
@click.option("--value", "-v", type=click.STRING, default="1", help="value of argument")
@click.option("--number", "-n", default=100, type=click.INT, help="number of requests")
@click.option("--sleep", "-s", default=3, type=click.INT, help="sleep injection time")
@click.option("--min_p_value", "-p", default=5 * 10e-5, type=click.FLOAT, help="sleep injection time")
@click.option("--debug", is_flag=True, default=False, help="logging debug mode")
def main(urls: List[str], key: str, value: str, number: int, sleep: int, min_p_value: float, debug: bool):
    """run SQL injection vulnerability test"""
    set_up_logger("SQL_injections", debug)
    logger.info(f"SQL injection vulnerability test [{number:d}x] for urls {urls}.")

    test_results, results_file = {}, f"SQL_injections__{datetime.now():%Y%m%d-%H%M}.csv"

    start = time.monotonic()
    for url in tqdm(urls, desc="urls"):
        vulnerable, save_times, inject_times = url_vulnerability(url, number, key, value, sleep, min_p_value)

        # save times
        test_results[f"[SAFE]{url}[vulnerable=={vulnerable}]"] = save_times
        test_results[f"[INJECT]{url}[vulnerable=={vulnerable}]"] = inject_times

    save_results(results_file, test_results)

    logger.info(f"test was finished at time {time.monotonic()-start:.3f}")


if __name__ == "__main__":
    main()
