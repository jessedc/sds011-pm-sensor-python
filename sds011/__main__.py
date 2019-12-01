"""
CLI Entry point
"""
import argparse
from influxdb import InfluxDBClient

from sds011.sds011 import SDS011
from sds011.influx import measurements_from_data

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

    sensor = SDS011(args.port)
    # sensor.read_data_callback(on_data_callback)
    sensor.debug_data_callback(lambda b: print("{}".format(b.hex())))


def on_data_callback(data):

    points = measurements_from_data(data)
    influx_client.write_points(points, database=influx_db)


if __name__ == "__main__":
    main()
