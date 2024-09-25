# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar
produtos=[]
estoque=[]
for i in range(5):
    produto=(input(f"fale seus produtos {i +1}"))
    estoques=int(input("quantos produtos tem de cada"))
    produtos.append(produto)    
    estoque.append(estoques)


produtos_zerados = []

for i in range(5):
    if estoque[i] == 0:
        produtos_zerados.append(produtos[i])

if produtos_zerados:
    print(f"Produtos com estoque zerado: {', '.join(produtos_zerados)}")
else:
    print("Nenhum produto está com estoque zerado.")
    
    
       


    
