
# 📘 Assignment: Hangman Game

## 🎯 Objective

Construa um jogo da Forca em Python para praticar manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória. O jogador deverá revelar uma palavra oculta antes de esgotar as tentativas disponíveis.

## 📝 Tasks

### 🛠️ Preparar a palavra e o progresso do jogo

#### Descrição
Use a lista de palavras fornecida no código inicial para selecionar uma palavra secreta aleatoriamente e prepare a exibição do progresso para que o jogador possa acompanhar as letras reveladas.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida.
- Mostrar cada letra ainda não adivinhada como um espaço em branco, por exemplo, `_ _ _ _`.
- Atualizar o progresso para revelar todas as ocorrências de uma letra correta.

### 🛠️ Implementar os palpites e o fim da partida

#### Descrição
Crie o loop principal que recebe palpites de letras, atualiza o estado do jogo e encerra a partida quando o jogador adivinhar a palavra ou não tiver mais tentativas.

#### Requisitos
O programa concluído deve:

- Solicitar palpites de letras ao jogador.
- Rastrear e exibir quantas tentativas incorretas ainda restam.
- Encerrar a partida quando a palavra for adivinhada ou as tentativas incorretas se esgotarem.
- Exibir uma mensagem de vitória ou derrota ao final da partida.

Exemplo de progresso para uma palavra de quatro letras:

```text
_ _ _ _
p _ t _
```