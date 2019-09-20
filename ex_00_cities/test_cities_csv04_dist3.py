from .cities import City, distance

"""
Convert the `distance` function that you implemented into a method of the City class.
"""

def test_distance():
    haifa = City(name='Haifa', lat=32.8204, lng=34.98, country='Israel')
    jerusalem = City(name='Jerusalem', lat=31.7784, lng=35.2066, country='Israel')

    dist = haifa.distance(jerusalem)
    assert 110 < dist < 120
