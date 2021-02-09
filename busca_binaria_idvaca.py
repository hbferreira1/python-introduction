def busca_binaria(v, p, r, x):
    if p <= r:
        q = (p + r) // 2
        if x > v[q]:
            return busca_binaria(v, q+1, r, x)
        elif x < v[q]:    
            return busca_binaria(v, q-1, r, x)
        else:
            return q  
    return -1

vetor = list(range(0, 10))
idvaca = 8
posicao = busca_binaria(vetor, 0, len(vetor)-1, idvaca)

if posicao >= 0:
    print(" A vaca de ID %d foi encontrada e está na posição %d" % (idvaca, posicao))
else:
    print(" O ID %d não está registrado" % idvaca)    

print(vetor)   
