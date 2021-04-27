import struct
import binascii


class UdpHeader:

    def __init__(self, Source_Port, Destination_Port, Length, Checksum):
        self.Source_Port = Source_Port
        self.Destination_Port = Destination_Port
        self.Length = Length
        self.Checksum = Checksum

    def pack_Udpheader(self):
        packed = b''
        packed += struct.pack('!4H', self.Source_Port, self.Destination_Port, self.Length, self.Checksum)
        return packed


def unpack_Upheader(buffer):
    unpacked = struct.unpack('!4H', buffer[:8])
    return unpacked


udp = UdpHeader(5555, 80, 1000, 0xFFFF)
packed_Upheader = udp.pack_Udpheader()
print(binascii.b2a_hex(packed_Upheader))

unpacked_Upheader = unpack_Upheader(packed_Upheader)
print(unpacked_Upheader)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'.format(unpacked_Upheader[0], unpacked_Upheader[1],unpacked_Upheader[2], unpacked_Upheader[3]))