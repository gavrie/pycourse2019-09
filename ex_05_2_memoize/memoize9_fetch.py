from typing import Dict, Tuple, Any

import time
import logging

import requests

logger = logging.getLogger()


def memoize(func):
    cache: Dict[Tuple[Any, ...], int] = {}

    def cached(*args):
        if args not in cache:
            cache[args] = func(*args)

        return cache[args]

    return cached


@memoize
def fetch_stars(repo: str) -> int:
    url = f"https://api.github.com/repos/{repo}"
    logger.info("Fetching result from %s", url)
    return requests.get(url).json()['stargazers_count']


def print_stars(repo: str):
    start_time = time.time()
    stars = fetch_stars(repo)
    duration = time.time() - start_time

    logger.info("Stars for %s: %s (took %.3fs)", repo, stars, duration)


def main() -> None:
    log_format = "%(asctime)s %(levelname)s [%(name)s] %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)

    print_stars("antirez/redis")
    print_stars("aerospike/aerospike-server")

    print_stars("antirez/redis")
    print_stars("hazelcast/hazelcast")

    print_stars("antirez/redis")


if __name__ == '__main__':
    main()
