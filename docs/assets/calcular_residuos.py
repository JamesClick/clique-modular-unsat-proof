import hashlib

def peso_hash(i, M):
    """Gera um peso baseado no hash SHA-256 do índice i, reduzido mod M."""
    h = hashlib.sha256(str(i).encode()).hexdigest()
    return int(h, 16) % M

def carregar_formula_cnf(caminho_arquivo):
    """
    Lê um arquivo .cnf no formato DIMACS e retorna a lista de cláusulas.
    Cada cláusula é uma lista de literais inteiros (positivos ou negativos).
    """
    clausulas = []
    with open(caminho_arquivo, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if linha == '' or linha.startswith(('c', 'p')):
                continue
            literais = list(map(int, linha.split()))
            if literais[-1] == 0:
                literais = literais[:-1]
            clausulas.append(literais)
    return clausulas

def calcular_residuos_modulares(clausulas, M, esquema='hash'):
    """
    Calcula o vetor de resíduos e a soma total modular S(φ;w,M).
    Cada literal é associado a um peso baseado no esquema ('hash', 'seq', etc).
    """
    residuos = []
    pesos = {}

    for idx, clausula in enumerate(clausulas):
        soma = 0
        for lit in clausula:
            var = abs(lit)
            if var not in pesos:
                if esquema == 'hash':
                    pesos[var] = peso_hash(var, M)
                elif esquema == 'seq':
                    pesos[var] = var
                elif esquema == 'exp':
                    pesos[var] = pow(2, var, M)
            peso = pesos[var]
            soma += peso if lit > 0 else -peso
        residuos.append(soma % M)

    soma_total = sum(residuos) % M
    return residuos, soma_total

# Exemplo de uso
if __name__ == "__main__":
    caminho_cnf = "exemplo.cnf"  # Substitua pelo nome do seu arquivo
    M = 101
    esquema = 'hash'  # Pode trocar para 'seq' ou 'exp'

    clausulas = carregar_formula_cnf(caminho_cnf)
    residuos, soma_total = calcular_residuos_modulares(clausulas, M, esquema)

    print("Resíduos por cláusula:", residuos)
    print("S(φ;w,M) =", soma_total)
