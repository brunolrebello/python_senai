
import velha_funcoes as jv
jogador = 'X'
vencedor = False

while vencedor == False:

     jv.desenhar_tabuleiro()

     jogada = int(input('Onde deseja digitar: '))
     jv.jogar(jogada,jogador)

     jv.desenhar_tabuleiro()
     jogador = jv.troca_jogador(jogador)

     jv.desenhar_tabuleiro()

     
     vencedor = jv.vitoria()

     if not vencedor:
          jogador = jv.troca_jogador(jogador)

jogador = jv.troca_jogador(jogador)
print(f'Você {jogador}venceu !!')