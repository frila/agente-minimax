### Othello - Agente Minmax 

#### Conceito do algoritmo

O algoritmo minmax é usado para determinar quais movimentos um agente computacional pode executar em jogos como jogo-da-velha, xadrez ou othello. Tais jogos são chamados **Jogos de informação perfeita**. Eles recebem esse nome, pois, baseados na atual configuração do jogo, é possível prever todos os movimentos possíveis do oponente. Jogos como o *buraco*, por exemplo, não são considerados de informação perfeita pois não é possível prever com 100% de certeza a mão do adversário.

O algoritmo tenta se assemelhar ao pensamento humano no momento do jogo. Esse seria um raciocínio como *"Se eu jogar nessa casa, meu adversário ficará sem movimentos"*.

#### Representando o tabuleiro como árvore

Caso desejássemos representar o tabuleiro do othello como árvore, a raíz seria a configuração inicial do tabuleiro, no primeiro nível, teríamos todas as jogadas que o jogador

![Árvore do Othello](http://yavar.naddaf.name/ai_othello_fullsize.gif)

#### Referências

> http://www.flyingmachinestudios.com/programming/minimax/