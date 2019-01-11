class Terreno(object):
    
    def __init__(self):
        pass

class Terra(Terreno):
    
    @classmethod
    def getId(clss):
        return 0
    
    def __repr__(self):
        return ' '

class Nascedouro(Terreno):

    @classmethod
    def getId(clss):
        return 1

    def __repr__(self):
        return '*'

class Altar(Terreno):

    @classmethod
    def getId(clss):
        return 2

    def __repr__(self):
        return '+'

MAPA_DE_TERRENOS = {
    Terra.getId(): Terra,
    Altar.getId(): Altar,
    Nascedouro.getId(): Nascedouro,
}