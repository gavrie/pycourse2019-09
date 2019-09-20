import csv


def main():
    with open("../data/worldcities.csv") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            country = row[4]
            if country != "Israel":
                continue

            print("{}, {}, {}, {}".format(
                row[1],
                row[2],
                row[3],
                row[4],
            ))


if __name__ == '__main__':
    main()
