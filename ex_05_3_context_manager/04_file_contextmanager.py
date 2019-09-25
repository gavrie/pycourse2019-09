from contextlib import contextmanager
import logging

logger = logging.getLogger()


@contextmanager
def open_context(filename):
    logger.info("File opened")
    f = open(filename)
    try:
        yield f
    finally:
        f.close()
        logger.info("File closed")


def process_file():
    with open_context('/etc/hosts') as f:

        for line in f:
            print(line.rstrip())
            if line.startswith("#"):
                return


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    process_file()
