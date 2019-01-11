import struct
import random

class Raiz(object):
    
    def __init__(self, f):
        self.f = f
        
    def __repr__(self):
        return str(self.f)
    
    def getReprGenetica(self):
        packed = bytearray(struct.pack('f', self.f))
        intRepr = 0
        for i in range(len(packed)):
            intRepr |= packed[i]
            intRepr = intRepr << 8 if i != (len(packed) - 1) else intRepr
        return intRepr
    
    @staticmethod
    def getTamanhoGenoma():
        return struct.calcsize('f')
    
    @staticmethod
    def getRaizFromReprGenetica(rep):
        intList = []
        for i in range(struct.calcsize('f')):
            intByte = rep & 0xFF
            intList.insert(0, intByte)
            rep >>= 8
        b = bytes(intList)
        return Raiz(struct.unpack('f', b)[0])
    
    @staticmethod
    def geraRaizAleatoria():
        byteList = []
        for i in range(struct.calcsize('f')):
            b = random.getrandbits(8)
            byteList.append(b)
        b = bytes(byteList)
        return Raiz(struct.unpack('f', b)[0])

    @staticmethod
    def geraRaizesAleatorias(n):
        raizes = []
        for i in range(n):
            raizes.append(Raiz.geraRaizAleatoria())
        return raizes

def main():
    r = Raiz.geraRaizAleatoria()
    print(r)
    re = r.getReprGenetica()
    print(re)
    r2 = Raiz.getRaizFromReprGenetica(re)
    print(r2)

if __name__ == '__main__':
    main()