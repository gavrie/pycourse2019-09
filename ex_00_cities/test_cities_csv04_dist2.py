from .cities import City, distance

"""
Implement a `distance` function in the `cities` module.
It should return the distance between two cities using the `haversine` package.
"""

def test_distance():
    haifa = City(name='Haifa', lat=32.8204, lng=34.98, country='Israel')
    jerusalem = City(name='Jerusalem', lat=31.7784, lng=35.2066, country='Israel')

    dist = distance(haifa, jerusalem)
    assert 110 < dist < 120
