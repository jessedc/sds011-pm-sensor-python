"""
CLI Entry point
"""
import argparse
import time

from influxdb import InfluxDBClient

from sds011.sds011 import SDS011
from sds011.influx import measurement_from_data

influx_client = None
influx_db = None


def main():
    """
    Invoke the parser
    """
    parser = argparse.ArgumentParser(description='Parse sds011 serial data')
    parser.add_argument('-i', '--influx', help='Influx DB host')
    parser.add_argument('-d', '--database', help='InfluxDB database', default='airquality')
    parser.add_argument('-p', '--port', help='Serial port', default='/dev/ttyUSB0')
    args = parser.parse_args()

    global influx_db, influx_client
    influx_client = InfluxDBClient(host=args.influx, port=8086)
    influx_db = args.database

    sensor = SDS011(args.port, use_query_mode=True)

    # Designed to roughly model a minute cycle
    while True:
        sensor.sleep(sleep=False)  # Wake up the sensor
        # "The data is stable when the sensor works after 30 seconds;"
        time.sleep(30)

        # read 5, sleep 1s each time
        results = []
        for i in range(6):
            result = sensor.query()
            if result is not None:
                pm25, pm100 = result
                measurement = measurement_from_data(pm25, pm100, "r1r0guexu75g")
                results.append(measurement)

                print("PM2.5 {}; PM10 {}".format(pm25, pm100))
            else:
                print("No response from sensor")

            time.sleep(1)

        sensor.sleep()

        influx_client.write_points(results, database=influx_db)

        # Put the sensor to sleep for 24 seconds
        time.sleep(24)


if __name__ == "__main__":
    main()
