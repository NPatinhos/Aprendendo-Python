# copy, sorted, produtos.sort
import copy
# Exercícios
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]



# 1 Aumente os preços dos produtos a seguir em 10%

#for produto in produtos:
 #   produto['preco'] *= 1.1

# 2 Gere novos_produtos por deep copy (cópia profunda)
#novos_produtos = copy.deepcopy(produtos)

#faz um deepcopy do original e modifica so o conteudo da copia
novos_produtos = [
    {**produto, 'preco': produto['preco']*1.1 }
    for produto in copy.deepcopy(produtos)
]

# 3 Ordene os produtos por nome decrescente (do maior para menor)
novos_produtos = sorted(novos_produtos, key=lambda k : k['nome'], reverse=True)

# 4 Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenador_por_nomes = copy.deepcopy(novos_produtos)
# 5 Ordene os produtos por preco crescente (do menor para maior)
novos_produtos = sorted(novos_produtos, key=lambda k : k['preco'])
# 6 Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)

print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')