from typing import Iterable
import requests


def fetch(urls: Iterable[str]) -> Iterable[int]:
    statuses = []

    for url in urls:
        status = requests.head(url).status_code
        statuses.append(status)

    return statuses


def main():
    for status in fetch(["http://google.com/", "http://example.com/"]):
        print(status)


if __name__ == '__main__':
    main()
