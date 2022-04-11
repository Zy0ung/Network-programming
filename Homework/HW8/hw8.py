import struct
import binascii

#udphdr 클래스 정의
class Udphdr:
    def __init__(self, sou_port, des_port, udp_len, checksum):
        self.sou_port = sou_port
        self.des_port = des_port
        self.udp_len = udp_len
        self.checksum = checksum
    
    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!4H', self.sou_port, self.des_port, self.udp_len, self.checksum)
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

unpacked_udphdr = Udphdr.unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)

print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'.format(Udphdr.getSrcPort(unpacked_udphdr), Udphdr.getDstPort(unpacked_udphdr), Udphdr.getLength(unpacked_udphdr), Udphdr.getChecksum(unpacked_udphdr)))
