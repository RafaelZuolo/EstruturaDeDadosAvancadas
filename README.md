# MAC6957 - Estruturas de Dados Avançadas
Repositório com diversos códigos que eu fiz para a aula de estrutura de dados avançadas no IME USP em 2019

Estão inclusos pilhas e filas persistentes, isto é, podemos dar "roll-back" nas
operações push, pop, enqueue e dequeue e recuperar o estado da pilha/fila exatamente
como no passado.

Temos também Árvore Splay, Árvore de busca binária persistente, árvore de segmentos e Trie.

A estrutura de dados mais complexa (em termos de desafio técnico de implementação)
é a Fila de Prioridade retroativa. Essa estrutura funciona exatamente como uma Fila de
Prioridade, mas as inserções e as operações DelMin têm um time-stamp. Assim é
possível realizar ou remover operações "no passado" e eficientemente recuperar
o estado atual da Fila de Prioridade com a nova operação. Recomendo a leitura do
artigo Retroactive Data Structures, de ERIK D. DEMAINE, JOHN IACONO, e STEFAN LANGERMAN.
