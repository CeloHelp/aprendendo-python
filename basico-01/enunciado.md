# Prática de Python — Funções e manipulação de dados

## Objetivo

Praticar:
- Parâmetros e argumentos.
- Retorno de valores.
- Uma função chamando outra.
- Filtro, transformação e acumulação.
- Preservação da lista original.
- Validação de entradas.

Faça um exercício por vez. Você pode consultar sintaxe e métodos,
mas tente construir a lógica antes de procurar exemplos prontos.

## Dados utilizados

Os valores representam vendas em reais:

```python
vendas = [120, 50, 200, 80, 150]
```

## Código de partida

Estas são as funções que já construímos. Você pode reutilizá-las:

```python
def filtrar_vendas(valores, minimo):
    lista_filtrada = []

    for valor in valores:
        if valor >= minimo:
            lista_filtrada.append(valor)

    return lista_filtrada


def calcular_valores(valores):
    valores_somados = 0

    for valor in valores:
        valores_somados += valor

    return valores_somados
```

---

## Exercício 1 — Conectar funções

Crie:

```python
def totalizar_vendas_aprovadas(valores, minimo):
    # Sua implementação.
```

### Comportamento esperado

A função deve:
1. Chamar `filtrar_vendas` com os argumentos recebidos.
2. Guardar a lista devolvida.
3. Passar essa lista para `calcular_valores`.
4. Devolver o total calculado.

### Regras

- Reutilize as duas funções existentes.
- Não escreva um novo `for` dentro desta função.
- Não use `print` dentro dela.
- Preserve a lista original.

### Chamadas para conferir

```python
print(totalizar_vendas_aprovadas(vendas, 100))
# Esperado: 470

print(totalizar_vendas_aprovadas(vendas, 200))
# Esperado: 200

print(totalizar_vendas_aprovadas(vendas, 500))
# Esperado: 0

print(totalizar_vendas_aprovadas([], 100))
# Esperado: 0

print(vendas)
# Esperado: [120, 50, 200, 80, 150]
```

### Explique ao terminar

Qual variável recebe o retorno do filtro e como esse resultado
chega à função de soma?

---

## Exercício 2 — Transformar valores

Crie:

```python
def aplicar_desconto(valores, percentual):
    # Sua implementação.
```

### Comportamento esperado

A função deve receber uma lista de preços e devolver uma nova lista
com o desconto aplicado a cada preço.

O percentual será informado na escala de 0 a 100:
- `10` significa 10%.
- `0` significa nenhum desconto.
- `100` significa desconto integral.

Fórmula:

preço com desconto = preço - (preço × percentual / 100)

### Regras

- Crie uma lista nova.
- Use `for` e `append`.
- Preserve a lista original.
- Devolva a lista depois de terminar o laço.
- Não use `print` dentro da função.
- Se o percentual for menor que 0 ou maior que 100, lance
  `ValueError` com uma mensagem explicativa.

Sintaxe de referência para lançar uma exceção:

```python
raise ValueError("Sua mensagem")
```

### Chamadas para conferir

```python
print(aplicar_desconto(vendas, 10))
# Esperado: [108.0, 45.0, 180.0, 72.0, 135.0]

print(aplicar_desconto([100, 200], 0))
# Esperado: [100.0, 200.0]

print(aplicar_desconto([100, 200], 100))
# Esperado: [0.0, 0.0]

print(aplicar_desconto([], 10))
# Esperado: []

print(vendas)
# Esperado: [120, 50, 200, 80, 150]
```

Execute separadamente as chamadas inválidas abaixo:
uma exceção sem tratamento interrompe a execução do programa.

```python
aplicar_desconto(vendas, -5)
# Esperado: ValueError
```

```python
aplicar_desconto(vendas, 110)
# Esperado: ValueError
```

### Explique ao terminar

Por que os `append`s dessa função não alteram a lista original?

---

## Exercício 3 — Organizar um processamento completo

Crie:

```python
def calcular_total_com_desconto(valores, minimo, percentual):
    # Sua implementação.
```

### Comportamento esperado

A função deve realizar estas etapas, nesta ordem:

1. Filtrar os valores maiores ou iguais ao mínimo.
2. Aplicar o desconto aos valores aprovados.
3. Somar os valores com desconto.
4. Devolver o total final.

A aprovação considera o preço original, antes do desconto.

### Regras

- Reutilize `filtrar_vendas`, `aplicar_desconto`
  e `calcular_valores`.
- Não repita as implementações dessas funções.
- Não escreva um novo `for` nesta função.
- Use variáveis intermediárias com nomes claros.
- Não use `print` dentro dela.
- Preserve a lista original.
- Deixe `aplicar_desconto` realizar a validação do percentual.

### Chamadas para conferir

```python
print(calcular_total_com_desconto(vendas, 100, 10))
# Esperado: 423.0

print(calcular_total_com_desconto(vendas, 200, 10))
# Esperado: 180.0

print(calcular_total_com_desconto(vendas, 500, 10))
# Esperado: 0

print(calcular_total_com_desconto([], 100, 10))
# Esperado: 0

print(vendas)
# Esperado: [120, 50, 200, 80, 150]
```

Observação: em comparações visuais, `0` e `0.0` representam
o mesmo resultado numérico nestes exercícios.

### Explique ao terminar

Descreva o caminho dos dados na primeira chamada:
- Qual lista sai do filtro?
- Qual lista sai da aplicação do desconto?
- Qual valor sai da soma?

---

## Como enviar para revisão

Envie um exercício por vez, contendo:
1. Seu código.
2. O resultado da execução.
3. Sua explicação ou o ponto em que ficou em dúvida.

Se travar, envie a tentativa incompleta e descreva o que pretendia fazer.
Não é necessário resolver os três antes de pedir ajuda.