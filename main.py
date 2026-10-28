emprestimos = [
    {"id": 101, "livro": "Clean Code", "status": "emprestado"},
    {"id": 102, "livro": "Effective Java", "status": "disponivel"},
    {"id": 103, "livro": "Refactoring", "status": "emprestado"}
]

novalista = []



for i in emprestimos:
    novalista.append(i["livro"])


print(novalista)


