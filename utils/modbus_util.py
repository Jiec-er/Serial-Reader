# 封装版Serial
# @author GJ
from binascii import *
import crcmod
import serial.tools.list_ports

# 生成CRC16-MODBUS校验码
def crc16Add(read):
    crc16 = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    data = read.replace(" ", "")
    readcrcout = hex(crc16(unhexlify(data))).upper()
    str_list = list(readcrcout)
    if len(str_list) == 5:
        str_list.insert(2, '0')
    crc_data = "".join(str_list)
    read = read.strip() + ' ' + crc_data[4:] + ' ' + crc_data[2:4]
    return read


# SELECT USB PORT FROM ALL PORTS
def getUSB():
    port_list = list(serial.tools.list_ports.comports())
    for i in port_list:
        if "USB" in str(i):
            return str(i)[0:4]
    return 0
