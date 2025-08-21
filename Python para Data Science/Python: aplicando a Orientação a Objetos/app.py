from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.item_cardapio import ItemCardapio


restaurante_praca = Restaurante('Praça', 'Brasileira')

bebida_suco = Bebida('Suco de laranja', 5.0, 'Grande')
prato_feijoada = Prato('Feijoada', 20.0, 'Feijoada clássica brasileira')

restaurante_praca.adicionar_item_no_cardapio(bebida_suco)
restaurante_praca.adicionar_item_no_cardapio(prato_feijoada)

bebida_suco.aplicar_desconto()
prato_feijoada.aplicar_desconto()

def main():
    restaurante_praca.exibir_cardapio



if __name__ == '__main__':
    main()
