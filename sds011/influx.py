from datetime import datetime, timezone
from copy import deepcopy


def measurements_from_data(data):
    """
    Turn the SDS011 object into a set of influx-db compatible measurements
    :param data:
    :return:
    """

    timestamp = datetime.now(timezone.utc).astimezone().isoformat()

    measure_base = {
        "measurement": "pm",
        "tags": {
            "sensor": "sds011",
            "location": "outdoors"
        },
        "time": timestamp,
        "fields": {}
    }

    measurements = []

    measurement = deepcopy(measure_base)

    pass
