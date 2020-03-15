import logging
import time
from typing import List

import click
from tqdm import tqdm

from utils.logger import set_up_logger

logger = logging.getLogger(__name__)


@click.command()
@click.option("--urls", "-u", multiple=True, type=click.STRING, required=True, help="list of urls to be tested")
@click.option("--number", "-n", default=100, type=click.INT, help="number of requests")
@click.option("--debug", is_flag=True, default=False, help="logging debug mode")
def main(urls: List[str], number: int, debug: bool):
    """run SQL injection vulnerability test"""
    set_up_logger("SQL_injections", debug)
    logger.info(f"SQL injection vulnerability test [{number:d}x] for urls {urls}.")

    start = time.monotonic()
    for url in tqdm(urls, desc="urls"):
        logger.info(f"start test of url {url}")
        for _ in tqdm(range(number), desc="test"):
            pass
        logger.info(f"finished test of {url}")

    logger.info(f"test was finished at time {time.monotonic()-start:.3f}")


if __name__ == "__main__":
    main()
