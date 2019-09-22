from typing import Iterable
import requests

# Implement `Iterable` implicitly with a generator

def fetch(urls: Iterable[str]) -> Iterable[int]:
    for url in urls:
        status = requests.head(url).status_code
        yield status


def main():
    for status in fetch({"http://google.com/", "http://example.com/"}):
        print(status)


if __name__ == '__main__':
    main()
