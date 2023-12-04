from smbus2 import SMBus
from pm25 import PM25


class PM25_I2C(PM25):
    """
    A module for using the PM2.5 Air quality sensor over I2C

    :param i2c_bus: The I2C SMBus instance to use.
    :param int address: The I2C address of the device. Defaults to :const:`0x12`
    """

    def __init__(
        self, i2c_bus: SMBus, address: int = 0x12
    ) -> None:
        self.i2c_bus = i2c_bus
        self.address = address
        super().__init__()

    def _read_data(self) -> None:
        with SMBus(self.i2c_bus) as bus:
            return bus.read_block_data(self.address, 0)

