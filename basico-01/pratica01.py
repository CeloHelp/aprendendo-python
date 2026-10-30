vendas = [120, 50, 200, 80, 150]

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


#Ex01

def totalizar_vendas_aprovadas(valores, minimo):

    vendas_filtradas = filtrar_vendas(valores, minimo)
     
    total_calculado = calcular_valores(vendas_filtradas)

    return total_calculado



#print(totalizar_vendas_aprovadas(vendas,100))

#print(totalizar_vendas_aprovadas(vendas, 200))
# Esperado: 200

#print(totalizar_vendas_aprovadas(vendas, 500))
# Esperado: 0

#print(totalizar_vendas_aprovadas([], 100))
# Esperado: 0

#print(vendas)
# Esperado: [120, 50, 200, 80, 150]


#Ex02

def aplicar_desconto(valores, percentual):

    if percentual  < 0 or percentual > 100:

          raise ValueError("Digite um percentual válido")

    lista_desconto = []
    

    for preco in valores:
        preco_com_desconto = preco - (preco * percentual / 100)
        lista_desconto.append(preco_com_desconto) 

       

    return  lista_desconto


#print(aplicar_desconto(vendas, 10))
# Esperado: [108.0, 45.0, 180.0, 72.0, 135.0]

#print(aplicar_desconto([100, 200], 0))
# Esperado: [100.0, 200.0]

#print(aplicar_desconto([100, 200], 100))
# Esperado: [0.0, 0.0]

#print(aplicar_desconto([], 10))
# Esperado: []

#print(vendas)
# Esperado: [120, 50, 200, 80, 150]

#Ex03

def calcular_total_com_desconto(valores, minimo, percentual):

    valores_filtrados = filtrar_vendas(valores, minimo)

    desconto = aplicar_desconto(valores_filtrados, percentual)

    total_final = calcular_valores(desconto)

    return total_final

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


    

 