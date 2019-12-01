import serial


class SDS011:

    # in_data, in_checksum, wait_header = range(4)

    def __init__(self, port='/dev/ttyAMA0', timeout=5):
        self.header = 0xAA
        self.command = 0xC0
        self.tail = 0xAB

        self.value = bytearray()
        self.bytes_sum = 0
        # self.state = self.wait_header
        # self.dict = {}

        self.ser = serial.Serial(port, 9600, timeout=timeout)

    def input(self, byte):
        """
        Parse byte
        :param byte:
        :return:
        """
        # if byte == self.tail:
        #     self.state = self.wait_header
        #     return self.value

        # if self.state == self.wait_header:

        return None

    def debug_data_callback(self, callback):
        while True:
            byte = self.ser.read(1)
            if byte:
                callback(byte)

    def read_data_callback(self, callback):
        while True:
            byte = self.ser.read(1)
            if byte:
                packet = self.input(byte)
                if packet is not None:
                    callback(packet)
            else:
                break