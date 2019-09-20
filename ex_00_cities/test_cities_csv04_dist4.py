from . import cities

"""
Instead of creating City instances manually, implement a `lookup` method that will
return cities defined in the CSV file.

Hint: maintain a dict of cities with the name as a key.
"""

def test_distance():
    haifa = cities.lookup('Haifa')
    jerusalem = cities.lookup('Jerusalem')

    dist = haifa.distance(jerusalem)
    assert 110 < dist < 120
