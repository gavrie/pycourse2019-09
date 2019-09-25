from contextlib import contextmanager
import logging

logger = logging.getLogger()

level = 0

def output(s):
    print("  " * level, s)


@contextmanager
def tag(name):
    output("<%s>" % name)
    global level
    level += 1

    yield

    level -= 1
    output("</%s>" % name)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    with tag("body"):
        with tag("div"):
            with tag("p"):
                output("Hello world")
