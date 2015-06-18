### Othello - Agente Minimax 

#### Conceito do algoritmo

O algoritmo minimax é usado para determinar quais movimentos um agente computacional pode executar em jogos como jogo-da-velha, xadrez ou othello. Tais jogos são chamados **Jogos de informação perfeita**. Eles recebem esse nome, pois, baseados na atual configuração do jogo, é possível prever todos os movimentos possíveis do oponente. Jogos como o *buraco*, por exemplo, não são considerados de informação perfeita pois não é possível prever com 100% de certeza a mão do adversário.

O algoritmo tenta se assemelhar ao pensamento humano no momento do jogo. Esse seria um raciocínio como *"Se eu jogar nessa casa, meu adversário ficará sem movimentos"*.

#### Representando o tabuleiro como árvore

Caso desejássemos representar o tabuleiro do othello como árvore, a raíz seria a configuração inicial do tabuleiro, no primeiro nível, teríamos todas as jogadas que o jogador

![Árvore do Othello](http://yavar.naddaf.name/ai_othello_fullsize.gif)

Representando os estados do jogo como árvore permite ao computador avaliar quais dos movimentos vão ocasionar em uma vitória, empate ou derrota.

Para representar o tabuleiro como árvore, alguns pontos são importantes, dentre eles:

1. O estado atual do jogo, ou seja, como as peças estão posicionadas no tabuleiro
2. O jogador que tem a vez
3. Todos os movimentos possíveis daquela rodada

Todos esses pontos acima listados são chamados de **estado de jogo**. Uma **árvore**, portanto, seria formada por *todos os possíveis estados de jogo válidos.*

#### Rankeando os estados de jogo

Vamos rankear os estados do jogo usando uma heuristica. Para o caso do jogador preto, por exemplo, vamos indicar o maior ranking como o estado com maior chance de vitória. No caso do jogador branco, portanto, o menor ranking passa a ser o de maior chance de vitória.

#### Referências

> http://www.flyingmachinestudios.com/programming/minimax/