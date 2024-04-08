# Banco de Dados 2

## Aula 1 - 31/08/2022 - Quarta

Hierarquia de Memória

      / \      / \ + custo
     /   \      |  + velocidade
    /  R  \     |
   /   C   \    |
  /    MP   \   |
 /     MS    \  |
/             \ |  + capacidade

Métodos de armazenamento

- Como funciona o armazenamento no HD
- Como funciona o armazenamento no SSD

- Sequencial, Heap, Hash, árvore -> Vantagens e desvantagens
- Estrutura de índices (parte mais importante)
  - Ex.: armazena os endereços de uma query já feita meio que na memória cache para fácil acesso depois

Clusters: tempo de processamento X Espaço de armazenamento

## Aula 2 - 09/09/2022 - Sexta - 16h16

1. SELECT cod_cliente, cliente FROM Cliente
2. SELECT cliente FROM Cliente WHERE localidade = 'Braga'
3. SELECT cod_cliente FROM Conta WHERE cod_agencia = '123'
4. SELECT cliente FROM Cleinte, Agencia WHERE Cliente.localidade = Agencia.local
5. SELECT cliente FROM Cliente, Agencia, Conta WHERE -> Cliente.cod_cliente = Conta.cod_cliente AND Conta.cod_agencia = Agencia.cod_agencia AND Agencia.localidade = Cliente.localidade
6. SELECT cliente FROM Emprestimo,Cliente WHERE valor > 2500 AND Emprestimo.cod_cliente = Cliente.cod_cliente
7. SELECT

## Aula X - 21/09/2022 - Quarta

Projeto Lógico/físico/conceitual ... // 23
ACID//Leitura fantasma, nonrepeatable read, dirty read

Estudar: gerenciamento de transações

- Níveis de isolamento
  - Read uncommited
  - Read commited
  - Repeatable read: recortar arquivo Word aberto
  - Serializable: abrir arquivos via usb de celular passando arquivos
