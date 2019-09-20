from .cities import City

# Don't forget to `pip install haversine` first
import haversine

# Similar to Redis GEODIST

def test_distance():
    haifa = City(name='Haifa', lat=32.8204, lng=34.98, country='Israel')
    jerusalem = City(name='Jerusalem', lat=31.7784, lng=35.2066, country='Israel')

    dist = haversine.haversine((haifa.lat, haifa.lng), (jerusalem.lat, jerusalem.lng))
    assert 110 < dist < 120
