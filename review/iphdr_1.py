import struct
import binascii

class Udphdr():
    def __init__(self, song_port, su_port, udp_len, checksum):
        self.song_port = song_port
        self.su_port = su_port
        self.udp_len = udp_len
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!4H', self.song_port, self.su_port, self.udp_len, self.checksum)
        return packed

    def unpack_Udphdr(buffer):
        unpacked = struct.unpack('!4H', buffer[:20])
        return unpacked

    def getSrcPort(unpacked):
        return unpacked[0]

    def getDstPort(unpacked):
        return unpacked[1]

    def getLength(unpacked):
        return unpacked[2]

    def getChecksum(unpacked):
        return unpacked[3]

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpack_udphdr = Udphdr.unpack_Udphdr(packed_udphdr)
print(unpack_udphdr)

print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'.format(Udphdr.getSrcPort(unpack_udphdr), Udphdr.getDstPort(unpack_udphdr), Udphdr.getLength(unpack_udphdr), Udphdr.getChecksum(unpack_udphdr)))
