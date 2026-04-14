# 📘 Assignment: Jogo da Forca

## 🎯 Objective

Desenvolver um jogo da Forca em Python para praticar manipulação de strings, loops, condicionais e entrada de dados do usuário. Ao final, o programa deve permitir que o jogador tente adivinhar uma palavra oculta antes de acabar o número de tentativas.

## 📝 Tasks

### 🛠️ Criar a lógica principal do jogo

#### Description
Crie um programa em Python que selecione uma palavra aleatória de uma lista predefinida e conduza uma partida simples de Forca no terminal. O jogador deve digitar letras para tentar descobrir a palavra, enquanto o programa mostra o progresso atual e controla a quantidade de erros.

#### Requirements
Completed program should:

- Selecionar uma palavra aleatória de uma lista predefinida.
- Exibir a palavra oculta usando underscores para as letras ainda nao descobertas.
- Solicitar ao jogador um palpite de uma letra por vez.
- Atualizar o progresso da palavra quando uma letra correta for informada.
- Reduzir o numero de tentativas restantes quando o palpite estiver incorreto.
- Encerrar o jogo com mensagem de vitoria quando a palavra for descoberta.
- Encerrar o jogo com mensagem de derrota quando as tentativas acabarem.


### 🛠️ Melhorar a experiencia do jogador

#### Description
Refine o jogo para deixá-lo mais claro e facil de acompanhar durante a execucao. Mostre informacoes uteis a cada rodada, como letras ja tentadas e quantidade de tentativas restantes, para que o jogador possa tomar decisoes melhores.

#### Requirements
Completed program should:

- Exibir o estado atual da palavra a cada rodada.
- Informar quantas tentativas restantes o jogador ainda possui.
- Mostrar as letras que ja foram tentadas.
- Evitar que a mesma letra seja processada repetidamente sem aviso.
- Exibir mensagens claras para entradas invalidas ou repetidas.