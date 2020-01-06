from datetime import datetime, timezone


def measurement_from_data(pm25, pm100, geohash):
    """
    Turn the SDS011 object into a set of influx-db compatible measurement object
    :param geohash: Geohash of the location
    :param pm25:
    :param pm100
    :return: dictionary
    """

    timestamp = datetime.now(timezone.utc).astimezone().isoformat()

    return {
        "measurement": "pm",
        "tags": {
            "sensor": "sds011",
            "location": "outdoors",
            "geohash": geohash,
        },
        "time": timestamp,
        "fields": {
            "pm25": float(pm25),
            "pm100": float(pm100)
        }
    }

