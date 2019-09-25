import logging

logger = logging.getLogger()


def process_file():
    f = open('/etc/hosts')
    logger.info("File opened")

    for line in f:
        print(line.rstrip())

    f.close()
    logger.info("File closed")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    process_file()
