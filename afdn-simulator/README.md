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

Certifique-se de seguir a estrutura e os nomes das seções corretamente ao configurar o autômato usando o formato YAML.

## Utilização

Para utilizar o simulador de autômatos finitos, siga as etapas descritas no README principal.
