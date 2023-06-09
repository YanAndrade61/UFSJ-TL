# Simulador de Autômatos Finitos

Este repositório contém um programa simulador de autômatos finitos (AFDs) e autômatos finitos não determinísticos (AFNs). O programa permite que o usuário especifique os autômatos e submeta strings (palavras) para verificar se são aceitas pelos autômatos em questão.

## Funcionalidades

O programa simulador possui as seguintes funcionalidades:

- Especificação de AFDs: O usuário pode definir os estados, símbolos do alfabeto, conjunto de estados de início, conjunto de estados de aceitação e as regras de transição para um AFD.

- Especificação de AFNs: O usuário pode definir os estados, símbolos do alfabeto, conjunto de estados de início, conjunto de estados de aceitação e as transições não determinísticas para um AFN.

- Verificação de palavras: O usuário pode submeter palavras ao programa para verificar se elas são aceitas pelos AFDs ou AFNs especificados. O programa informará se a palavra é aceita ou rejeitada.

## Formato de Configuração do Autômato

O programa aceita a especificação dos autômatos usando o formato YAML (YAML Ain't Markup Language). O formato YAML é uma linguagem de serialização de dados legível por humanos e fácil de entender.

Aqui está um exemplo de como o autômato pode ser configurado usando o formato YAML:

### AFDs e AFNs

```yaml
type: AFD
states:
  - q0
  - q1
  - qf
alphabet:
  - a
  - b
start: q0
ends:
  - qf
rules:
  q0:
    a: 
      - q0
    b: 
      - q1
  q1:
    a: 
      - qf
  qf:
    b: 
      - qf
```

Neste exemplo, o autômato é um AFD, e as seções especificadas são:

- `type`: Indica o tipo de autômato. Pode ser "AFD" ou "AFN".
- `states`: Lista de estados do autômato.
- `alphabet`: Lista de símbolos do alfabeto.
- `start`: Estado inicial do autômato.
- `ends`: Lista de estados de aceitação do autômato.
- `rules`: Conjunto de regras de transição para cada estado e símbolo do alfabeto.

### Autômatos de Pilha

```yaml
  type: PILHA
  states:
    - q0
    - q1
    - qf
  alphabet:
    - a
    - b
  start: q0
  ends:
    - qf
  rules:
    q0:
      - [a, vz, A, [q0]]
      - [b, vz, B, [q0]]
      - [vz, vz, vz, [q1]]
    q1:
      - [a, A, vz, [q1]]
      - [b, B, vz, [q1]]
      - ['?', '?', vz, [qf]]
```  

Neste exemplo, o autômato é um autômato de pilha, e as seções especificadas são:

- `type`: Deva ser igual a "PILHA".
- `states`: Lista de estados do autômato.
- `alphabet`: Lista de símbolos do alfabeto.
- `start`: Estado inicial do autômato.
- `ends`: Lista de estados de aceitação do autômato.
- `rules`: Conjunto de regras de transição para cada estado e símbolo do alfabeto. Cada estado tem uma quadrupla onde o primeiro elemento representa o símbolo para o qual a regra é válida, o segundo elemento é o valor a ser desempilhado, o terceiro elemento é o valor a ser empilhado e o quarto elemento é uma lista contendo todos os estados finais.

Certifique-se de seguir a estrutura e os nomes das seções corretamente ao configurar o autômato usando o formato YAML.

## Utilização

Os automatos para utilização devem estar na pasta config_files.
Para simbolizar o vazio, utilize o simbolo 'vz'. Para simbolizar a ? use '?'
