import time
import board
import busio

MCP23017_ADDRESS = 0x20

i2c = busio.I2C(board.GP13, board.GP12)
i2c.try_lock()
i2c.scan()

result = bytearray(1)
i2c.writeto(MCP23017_ADDRESS, bytes(0x05));
i2c.readfrom_into(MCP23017_ADDRESS, result); print(result)
i2c.writeto(MCP23017_ADDRESS, bytes(0x0A));
i2c.readfrom_into(MCP23017_ADDRESS, result); print(result)

i2c.writeto(MCP23017_ADDRESS, bytes([0x00, 0xff]));
i2c.writeto(MCP23017_ADDRESS, bytes([0x01, 0x00]));

i2c.writeto(MCP23017_ADDRESS, bytes([0x00]));
i2c.readfrom_into(MCP23017_ADDRESS, result); print(result)
i2c.writeto(MCP23017_ADDRESS, bytes([0x01]));
i2c.readfrom_into(MCP23017_ADDRESS, result); print(result)

i2c.writeto(MCP23017_ADDRESS, bytes([0x00]));
i2c.readfrom_into(MCP23017_ADDRESS, result); print(result)
i2c.writeto(MCP23017_ADDRESS, bytes([0x01]));
i2c.readfrom_into(MCP23017_ADDRESS, result); print(result)

i2c.writeto(MCP23017_ADDRESS, bytes([0x13, 0x04]));

while True:
    i2c.writeto(MCP23017_ADDRESS, bytes([0x12]));
    i2c.readfrom_into(MCP23017_ADDRESS, result); print(result)
    time.sleep(0.5)

i2c.writeto
