from typing import cast
from mypy_extensions import TypedDict

import csv


City = TypedDict('City', {
    'city_ascii': str,
    'lat': float,
    'lng': float,
    'country': str,
})


def main() -> None:
    with open("../data/worldcities.csv") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            city = cast(City, row)

            if city['country'] != "Israel":
                continue

            print("{}, {}, {}, {}".format(
                city['city_ascii'],
                city['lat'],
                city['lng'],
                city['county'],
            ))


if __name__ == '__main__':
    main()
