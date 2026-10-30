# Aprendendo Python 🐍

Este repositório registra meu aprendizado em Python, com foco em construir uma base sólida para trabalhar com **Análise de Dados**.

Já tenho experiência com programação em Java e estou praticando a sintaxe e os comportamentos do Python por meio de pequenos problemas. Também aproveito este espaço para exercitar Git e GitHub e acompanhar minha evolução pelas alterações no código.

## Objetivo

Receber um pequeno conjunto de dados e conseguir construir, com autonomia, um programa que consulte, filtre, transforme, agregue e apresente informações, organizando a solução em funções.

A ideia é consultar a documentação para dúvidas de sintaxe e métodos específicos, desenvolvendo meu próprio raciocínio para estruturar as soluções.

## Como estou estudando

- Converso sobre os conceitos e comparo comportamentos com o que já conheço de Java.
- Resolvo exercícios a partir de objetivos, regras e resultados esperados, construindo a lógica por conta própria.
- Executo diferentes entradas, incluindo listas vazias e valores inválidos.
- Explico o caminho dos dados e reviso os pontos que ainda não ficaram claros.
- Uso o ChatGPT como apoio para discussão, elaboração de exercícios e revisão das tentativas.

O código registra etapas reais do aprendizado e pode ser revisitado conforme eu avanço.

## Práticas atuais

### Funções e processamento de vendas

Em [`pratica01.py`](pratica01.py), trabalho com uma lista de vendas para praticar:

- Filtro por valor mínimo.
- Soma com acumulador.
- Aplicação de descontos em uma nova lista.
- Validação de percentuais com `ValueError`.
- Conexão entre funções usando parâmetros e retornos.
- Preservação dos dados originais.

Exemplo de processamento implementado:

```python
vendas = [120, 50, 200, 80, 150]

total = calcular_total_com_desconto(vendas, 100, 10)
print(total)  # 423.0
```

Nesse exemplo, as vendas de pelo menos R$ 100 recebem 10% de desconto e seus valores finais são somados.

### Listas de dicionários

Em [`main.py`](main.py), exploro o acesso a dados de livros em uma lista de dicionários, extraindo seus títulos para uma nova lista.

## Arquivos

| Arquivo | Conteúdo |
| --- | --- |
| [`enunciado.md`](enunciado.md) | Enunciados, regras e chamadas de conferência dos exercícios. |
| [`pratica01.py`](pratica01.py) | Funções e exercícios de processamento de vendas. |
| [`main.py`](main.py) | Exploração de listas de dicionários com dados de livros. |

## Como executar

Com Python 3 instalado, abra o terminal na pasta do repositório e execute:

```bash
python pratica01.py
```

Para executar a exploração de livros:

```bash
python main.py
```

Dependendo da instalação, o comando pode ser `python3` ou, no Windows, `py`.

Os arquivos atuais utilizam apenas recursos nativos do Python, sem dependências externas. Algumas chamadas de conferência em `pratica01.py` estão comentadas e podem ser habilitadas para experimentar outros cenários.

## Próximos temas

- Parâmetros com valores padrão e argumentos nomeados.
- Retorno de múltiplos resultados e uso de tuplas.
- Manipulação de listas, dicionários e sets.
- Busca, contagem e agrupamento de informações.
- Pequenos problemas de análise de dados com funções.

Os próximos exercícios serão adicionados gradualmente, conforme a consolidação dos fundamentos.
