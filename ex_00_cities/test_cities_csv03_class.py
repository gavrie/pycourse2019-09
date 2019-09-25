# from .cities_csv03_class_00 import City
# from .cities_csv03_class_11_eq import City
# from .cities_csv03_class_12_hash import City
from .cities_csv04_dataclass import City
# from .cities_csv05_attrs import City


def test_equals():
    c1 = City(name='Haifa', lat=32.8204, lng=34.98, country='Israel')
    c2 = City(name='Haifa', lat=32.8204, lng=34.98, country='Israel')

    assert c1 == c2


def test_set():
    c1 = City(name='Jerusalem', lat=31.7784, lng=35.2066, country='Israel')
    c2 = City(name='Jerusalem', lat=31.7784, lng=35.2066, country='Israel')

    cities = set()
    cities.add(c1)
    cities.add(c2)

    print(cities)
    assert cities == {c1}
    assert cities == {c2}
