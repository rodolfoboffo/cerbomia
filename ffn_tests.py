from ffn import FFNBuilder, FeedForwardNet, CAMADA_SOFTMAX, CAMADA_RELU
import unittest
import math

class FeedForwardNetTest(unittest.TestCase):

    def setUp(self):
        tipos = [
            CAMADA_RELU,
            CAMADA_SOFTMAX
        ]
        pesos = [
            [
                [2.0, 1.0],
                [3.0, 2.0],
                [1.0, 1.0]
            ],
            [
                [1.0, 1.0, 1.0],
                [2.0, 1.0, 0.0]
            ]
        ]

        desvios = [
            [1.0, 0.0, 0.0],
            [0.0, 0.0]
        ]

        self.ffn = FeedForwardNet(tipos, pesos, desvios)

    def test_avaliaSaida(self):
        entrada = [1.0, 2.0]
        saida = self.ffn.alimenta(entrada)
        #[5.0, 7.0, 3.0]
        #[15.0, 17.0]
        saidaEsperada = [
            math.exp(15.0) / (math.exp(15.0) + math.exp(17.0)),
            math.exp(17.0) / (math.exp(15.0) + math.exp(17.0))
        ]
        self.assertEqual(saida, saidaEsperada, 'Saida diferente do esperado')

class FFNBuilderTest(unittest.TestCase):

    def setUp(self):
        self.builder = FFNBuilder()
        self.builder.adicionaCamadaEntrada(2)
        self.builder.adicionaCamada(3, CAMADA_RELU)
        self.builder.adicionaCamada(2, CAMADA_SOFTMAX)

    def test_randomNet(self):
        net = self.builder.geraAleatorio()
        print(net.alimenta([1.0, 2.0]))


class FFNBuilderTest2(unittest.TestCase):

    def setUp(self):
        self.builder = FFNBuilder()
        self.builder.adicionaCamadaEntrada(2)
        self.builder.adicionaCamada(3, CAMADA_RELU)
        self.builder.adicionaCamada(2, CAMADA_SOFTMAX)

        tipos = [
            CAMADA_RELU,
            CAMADA_SOFTMAX
        ]
        pesos = [
            [
                [2.0, 1.0],
                [3.0, 2.0],
                [1.0, 1.0]
            ],
            [
                [1.0, 1.0, 1.0],
                [2.0, 1.0, 0.0]
            ]
        ]

        desvios = [
            [1.0, 0.0, 0.0],
            [0.0, 0.0]
        ]

        self.ffn = FeedForwardNet(tipos, pesos, desvios)

    def test_packUnpack(self):
        rep = self.ffn.getReprGenetica()
        newFfn = self.builder.getFromReprGenetica(rep)
        self.assertEqual(self.ffn, newFfn, 'Redes são diferentes')

class FuncoesAtivacao(unittest.TestCase):

    def test_relu(self):
        self.assertEqual(FeedForwardNet.relu([6.0, -2.0]), [6.0, 0.0], 'ReLu nao está correto.')
        self.assertEqual(FeedForwardNet.relu([-1.0]), [0.0], 'ReLu nao está correto.')

if __name__ == '__main__':
    unittest.main()