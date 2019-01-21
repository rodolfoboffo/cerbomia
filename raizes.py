import struct
import random

class RaizBuilder(object):

    def getTamanhoGenoma(self):
        return struct.calcsize(self.getFormatoStruct())

    def getFormatoStruct(self):
        return 'f'

    def getFromReprGenetica(self, rep):
        intList = []
        for i in range(struct.calcsize('f')):
            intByte = rep & 0xFF
            intList.insert(0, intByte)
            rep >>= 8
        b = bytes(intList)
        return Raiz(struct.unpack(Raiz.getFormatoStruct(), b)[0])

    def geraAleatorio(self):
        byteList = []
        for i in range(struct.calcsize('f')):
            b = random.getrandbits(8)
            byteList.append(b)
        b = bytes(byteList)
        return Raiz(struct.unpack('f', b)[0])

    def geraAleatorios(self, n):
        raizes = []
        for i in range(n):
            raizes.append(self.geraAleatorio())
        return raizes

class Raiz(object):
    
    def __init__(self, f):
        self.f = f
        
    def __repr__(self):
        return str(self.f)

    def getValor(self):
        return self.f

    def getReprGenetica(self):
        packed = bytearray(struct.pack('f', self.f))
        intRepr = 0
        for i in range(len(packed)):
            intRepr |= packed[i]
            intRepr = intRepr << 8 if i != (len(packed) - 1) else intRepr
        return intRepr
    
def main():
    r = Raiz.geraRaizAleatoria()
    print(r)
    re = r.getReprGenetica()
    print(re)
    r2 = Raiz.getRaizFromReprGenetica(re)
    print(r2)

if __name__ == '__main__':
    main()