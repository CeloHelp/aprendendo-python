# Python — Parâmetros com valores padrão e argumentos nomeados

## Objetivo

Entender como fornecer argumentos por posição ou pelo nome e como definir valores usados quando um argumento é omitido.

## 1. Parâmetros e argumentos

**Parâmetros** são os nomes declarados na definição da função. **Argumentos** são os valores fornecidos na chamada.

```python
def calcular_desconto(valores, percentual):  # Parâmetros.
    ...

calcular_desconto(vendas, 10)  # Argumentos.
```

Os exemplos com `...` mostram apenas a assinatura da função; não implementam seu processamento.

## 2. Argumentos posicionais

Quando fornecemos argumentos sem nome, a posição determina qual parâmetro recebe cada valor:

```python
calcular_desconto(vendas, 10)
# valores recebe vendas.
# percentual recebe 10.
```

## 3. Argumentos nomeados

Na chamada, podemos indicar explicitamente o parâmetro de destino:

```python
calcular_desconto(valores=vendas, percentual=10)
```

Os argumentos nomeados podem aparecer em outra ordem:

```python
calcular_desconto(percentual=10, valores=vendas)
```

Essa escrita não cria variáveis externas chamadas `valores` ou `percentual`: fornece argumentos para a função.

## 4. Combinando as formas

Nas chamadas simples que estamos estudando, os argumentos posicionais vêm antes dos nomeados:

```python
calcular_desconto(vendas, percentual=10)
```

`vendas` ocupa o primeiro parâmetro, `valores`. Não podemos fornecer um segundo argumento para o mesmo parâmetro:

```python
# Inválido: valores recebe dois argumentos.
calcular_desconto(vendas, valores=[200], percentual=10)
```

## 5. Parâmetros com valores padrão

O padrão é definido na declaração da função. Os parâmetros continuam separados por vírgulas:

```python
def calcular_total_com_desconto(valores, minimo=0, percentual=10):
    ...
```

- `valores` é obrigatório.
- `minimo` usa `0` se seu argumento for omitido.
- `percentual` usa `10` se seu argumento for omitido.

Nas definições simples que estamos usando, os parâmetros obrigatórios vêm antes dos parâmetros com padrão. Uma função também pode ter apenas um parâmetro com padrão; não é necessário ter vários parâmetros.

## 6. Omitir, substituir e combinar padrões

Considerando a definição anterior:

| Chamada | `minimo` utilizado | `percentual` utilizado |
|---|---:|---:|
| `calcular_total_com_desconto(vendas)` | 0 (padrão) | 10 (padrão) |
| `calcular_total_com_desconto(vendas, 5, 20)` | 5 | 20 |
| `calcular_total_com_desconto(vendas, minimo=5, percentual=20)` | 5 | 20 |
| `calcular_total_com_desconto(vendas, percentual=20, minimo=5)` | 5 | 20 |
| `calcular_total_com_desconto(vendas, percentual=20)` | 0 (padrão) | 20 |
| `calcular_total_com_desconto(vendas, 20)` | 20 | 10 (padrão) |

Para manter o segundo parâmetro no padrão e fornecer um valor para o terceiro, omitimos o argumento do segundo e nomeamos o terceiro:

```python
calcular_total_com_desconto(vendas, percentual=20)
```

Não existe uma posição vazia na chamada: `calcular_total_com_desconto(vendas, , 20)` é inválido.

**O parâmetro omitido usa o padrão; o parâmetro informado usa o valor recebido, seja por posição ou pelo nome.**

## 7. Valor padrão e argumento nomeado são recursos diferentes

```python
# Na definição: estabelece o padrão.
def calcular_desconto(valores, percentual=10):
    ...

# Na chamada: fornece um argumento pelo nome.
calcular_desconto(valores=vendas, percentual=20)
```

Um parâmetro não precisa ter padrão para receber um argumento nomeado. No exemplo, `valores` é obrigatório e pode ser informado como `valores=vendas`.

## 8. Cuidados essenciais

- **O padrão não memoriza o último argumento.** Depois de uma chamada com `percentual=20`, uma nova chamada que omita esse argumento continuará usando o padrão `10`.
- **Padrão não é validação.** Definir `percentual=10` não impede que alguém forneça `-5`. A validação com `if` e `raise ValueError` continua necessária quando a regra exige isso.
- **Omitir um argumento obrigatório causa `TypeError`.** Nesta função, não podemos omitir `valores`.
- **Listas e dicionários como padrão exigem cuidado.** Os padrões são avaliados quando a função é definida; um objeto mutável usado como padrão pode ser compartilhado entre chamadas. Por enquanto, a prática usará padrões numéricos, textos e booleanos.

## Próxima etapa

A teoria acima é suficiente para começar os próximos exercícios sobre este tema. A prática será escolher quando usar posição, nome e omissão, mantendo a lógica da solução por minha conta.

## Consulta opcional

- [Documentação oficial — Valores padrão](https://docs.python.org/pt-br/3/tutorial/controlflow.html#default-argument-values)
- [Documentação oficial — Argumentos nomeados](https://docs.python.org/pt-br/3/tutorial/controlflow.html#keyword-arguments)
