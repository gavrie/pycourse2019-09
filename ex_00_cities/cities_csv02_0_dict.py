import csv


def main():
    with open("../data/worldcities.csv") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if row['country'] != "Israel":
                continue

            print("{}, {}, {}, {}".format(
                row['city_ascii'],
                row['lat'],
                row['lng'],
                row['country'],
            ))


if __name__ == '__main__':
    main()
