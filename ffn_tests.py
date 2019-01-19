from ffn import FeedForwardNet, CAMADA_SOFTMAX, CAMADA_RELU
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



if __name__ == '__main__':
    unittest.main()