import random

# gerar uma string de referência aleatória
def referencias(n=20):
    return [random.randint(0, 9) for _ in range(n)]

# algoritmo FIFO
def fifo_memoria(paginas, quadros):
    falhas = 0
    memoria = []

    for i in paginas:
        if i not in memoria:
            falhas += 1
            if len(memoria) >= quadros:
                memoria.pop(0)
            memoria.append(i)
    return falhas

# algoritmo LRU
def lru_memoria(paginas, quadros):
    falhas = 0
    memoria = []

    for i in paginas:
        if i not in memoria:
            falhas += 1
            if len(memoria) >= quadros:
                memoria.pop(0)
            memoria.append(i)
        else:
            memoria.remove(i)
            memoria.append(i)
    
    return falhas

# simular os algoritmos com diferentes números de quadros
def simular_algoritmos(quadros, num_referencias=20):
    paginas = referencias(num_referencias)
    print(f"\nReferências de página: {paginas}")
    print(f"Quadros de memória: {quadros}")
    
    # Simulação FIFO
    falhas_fifo = fifo_memoria(paginas, quadros)
    print(f"Falhas de página (FIFO): {falhas_fifo}")

    # Simulação LRU
    falhas_lru = lru_memoria(paginas, quadros)
    print(f"Falhas de página (LRU): {falhas_lru}")

    return falhas_fifo, falhas_lru

# rodar simulações com diferentes quadros de memória
def main():
    for quadros in [3, 4, 5]:
        falhas_fifo, falhas_lru = simular_algoritmos(quadros)
        
        # Comparando os resultados dos algoritmos
        if falhas_fifo < falhas_lru:
            print(f"\nPara {quadros} quadros, FIFO teve menos falhas.")
        elif falhas_lru < falhas_fifo:
            print(f"\nPara {quadros} quadros, LRU teve menos falhas.")
        else:
            print(f"\nPara {quadros} quadros, FIFO e LRU tiveram o mesmo número de falhas.")

if __name__ == "__main__":
    main()