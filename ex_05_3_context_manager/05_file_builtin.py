import logging

logger = logging.getLogger()


def process_file():
    with open('/etc/hosts') as f:
        for line in f:
            print(line.rstrip())
            if line.startswith("#"):
                return


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    process_file()
