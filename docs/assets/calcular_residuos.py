
import hashlib

def peso_hash(i, M):
    h = hashlib.sha256(str(i).encode()).hexdigest()
    return int(h, 16) % M

def calcular_residuos(formula, pesos, M):
    return sum(p * r for p, r in zip(pesos, formula)) % M

# Exemplo simplificado
formula = [1, 0, 1]
pesos = [1, 2, 3]
M = 1000003
print("S(φ) mod M =", calcular_residuos(formula, pesos, M))
