from typing import List
import requests


def fetch(urls: List[str]) -> List[int]:
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
