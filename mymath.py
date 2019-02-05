from decimal import Decimal

EPSILON = Decimal('0.00000001')

class VetorUtil(object):
    
    @staticmethod
    def soma(v1, v2):
        return VetorUtil.aplica(v1, v2, lambda v1, v2: v1 + v2)
    
    @staticmethod
    def subtrai(v1, v2):
        return VetorUtil.aplica(v1, v2, lambda v1, v2: v1 - v2)
    
    @staticmethod
    def produtoHadamard(v1, v2):
        return VetorUtil.aplica(v1, v2, lambda v1, v2: v1 * v2)
    
    @staticmethod
    def divisaoHadamard(v1, v2):
        return VetorUtil.aplica(v1, v2, lambda v1, v2: v1 / v2)
    
    @staticmethod
    def aplica(v1, v2, f):
        if len(v1) != len(v2):
            raise Exception('Vetores de tamanhos diferentes')
        return [f(v1[i], v2[i]) for i in range(len(v1))]

class FuncaoVetorial(object):
    
    def __init__(self, f):
        self.f = f
        
    def avalia(self, v):
        return self.f(v)

    def derivadaParcial(self, v, i):
        eps = [Decimal(0) if vi != i else EPSILON for vi in range(len(v))]
        h2 = self.avalia(v)
        h1 = self.avalia(VetorUtil.subtrai(v, eps))
        delta = VetorUtil.subtrai(h2, h1)
        derivada = VetorUtil.divisaoHadamard(delta, eps)
        return derivada

def main():
    f = lambda v: list(map(lambda x: Decimal(2)*x + Decimal(4) if x > 0 else Decimal(0), v))
    fv = FuncaoVetorial(f)
    print(fv.derivadaParcial([Decimal(-1)], 0))

if __name__ == '__main__':
    main()