# Autômato Finito Determinístico (AFD)

Este arquivo README descreve a configuração de um autômato finito determinístico (AFD) representado por meio de um arquivo de definição. O AFD é definido pelos estados, símbolos do alfabeto, conjunto de estados de início, conjunto de estados de aceitação e as regras de transição.

## Estrutura do Arquivo

O arquivo de definição do autômato segue um formato YAML simples, com as seguintes seções:

- `start`: Define o estado inicial do autômato.
- `ends`: Lista de estados de aceitação do autômato.
- `rules`: Conjunto de regras de transição para cada estado e símbolo do alfabeto.

## Exemplo

Aqui está um exemplo de um arquivo de definição de autômato:

```yaml
start: q0
ends:
  - qf
rules:
  q0:
    a:
      - q0
    b:
      - q1
      - q0
  q1:
    b:
      - qf
  qf:
    b:
      - qf
```

Neste exemplo, o autômato possui três estados: `q0`, `q1` e `qf`. O estado inicial é `q0`, e o estado de aceitação é `qf`. As regras de transição são definidas da seguinte maneira:

- De `q0` para `q0` quando o símbolo de entrada é `a`.
- De `q0` para `q1` e `q0` quando o símbolo de entrada é `b`.
- De `q1` para `qf` quando o símbolo de entrada é `b`.
- De `qf` para `qf` quando o símbolo de entrada é `b`.

## Utilização

Para utilizar esse arquivo de definição do autômato em um programa ou implementação, você pode carregar o conteúdo do arquivo e processá-lo de acordo com a linguagem de programação ou biblioteca específica que esteja utilizando.

Certifique-se de que sua implementação respeite as definições de estados iniciais, estados de aceitação e as regras de transição fornecidas pelo arquivo de definição.

Espero que este arquivo README tenha ajudado a entender a configuração e utilização do autômato definido. Se você tiver mais dúvidas, sinta-se à vontade para perguntar.
