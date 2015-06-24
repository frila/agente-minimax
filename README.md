## Othello - Agente Minimax 

### Conceito do algoritmo

O algoritmo minimax é usado para determinar quais movimentos um agente computacional pode executar em jogos como jogo-da-velha, xadrez ou othello. Tais jogos são chamados **Jogos de informação perfeita**. Eles recebem esse nome, pois, baseados na atual configuração do jogo, é possível prever todos os movimentos possíveis do oponente. Jogos como o *buraco*, por exemplo, não são considerados de informação perfeita pois não é possível prever com 100% de certeza a mão do adversário.

O algoritmo tenta se assemelhar ao pensamento humano no momento do jogo. Esse seria um raciocínio como *"Se eu jogar nessa casa, meu adversário ficará sem movimentos"*.

### Representando o tabuleiro como árvore

Caso desejássemos representar o tabuleiro do othello como árvore, a raíz seria a configuração inicial do tabuleiro, no primeiro nível, teríamos todas as jogadas que o jogador

![Árvore do Othello](http://yavar.naddaf.name/ai_othello_fullsize.gif)

Representando os estados do jogo como árvore permite ao computador avaliar quais dos movimentos vão ocasionar em uma vitória, empate ou derrota.

Para representar o tabuleiro como árvore, alguns pontos são importantes, dentre eles:

1. O estado atual do jogo, ou seja, como as peças estão posicionadas no tabuleiro
2. O jogador que tem a vez
3. Todos os movimentos possíveis daquela rodada

Todos esses pontos acima listados são chamados de **estado de jogo**. Uma **árvore**, portanto, seria formada por *todos os possíveis estados de jogo válidos.*

### Rankeando os estados de jogo

Vamos rankear os estados do jogo usando uma heuristica. Para o caso do jogador preto, por exemplo, vamos indicar o maior ranking como o estado com maior chance de vitória. No caso do jogador branco, portanto, o menor ranking passa a ser o de maior chance de vitória.

### Players

#### Player 1: Heman, O príncipe de Eternian

##### Estratégia

A Estratégia do player consiste em tentar minimizar o número de jogadas possíveis do adversário. Ele faz uso de uma estratégia defensiva, impedindo que o adversário progrida no tabuleiro. Caso duas jogadas sejam avaliadas como boas, Heman fará uso daquela que renderá o maior score.

##### Resultados

Heman foi posto a prova contra o agente Corner, que procura sempre os cantos, gerando o seguinte resultado:

![Massacre do Heman](http://img.ctrlv.in/img/15/06/24/558a001ad7a96.png)

O príncipe de Eternian batalhou contra outros players feitos pelo grupo, vencendo todos os oponentes.

É importante ressaltar que esse agente **não** faz uso do algoritmo de minimax. Apenas a jogada seguinte é observada.

#### Player 2: MunHá, o de vida (quase) eterna

##### Estratégia

Com base na seguinte tabela:

![Tabela de heurísticas](http://img.ctrlv.in/img/15/06/24/558a02afc34ae.png)

O algoritmo do player MunHa utiliza-se do algoritmo Minimax para maximizar a heuristica. A função heuristica soma o ponto de cada bracket no tabuleiro de sua respectiva cor e subtrai pela soma dos pontos do seu adversário ( tal ponto eh dado pela tabela ).

#### Referências

> http://www.flyingmachinestudios.com/programming/minimax/