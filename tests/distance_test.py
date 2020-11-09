from mlproject.distance import haversine

def test_haversine():
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 38.736946, -9.142685
    distance = haversine(lon1, lat1, lon2, lat2)
    assert distance == 1453.861242976993
