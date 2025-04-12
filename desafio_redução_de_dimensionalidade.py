# Função para converter uma imagem colorida (matriz 3D) para níveis de cinza
def converter_para_cinza(imagem_colorida):
    altura = len(imagem_colorida)
    largura = len(imagem_colorida[0])
    imagem_cinza = [[0 for _ in range(largura)] for _ in range(altura)]

    for i in range(altura):
        for j in range(largura):
            # Calcula o valor de cinza usando a média dos canais RGB
            r, g, b = imagem_colorida[i][j]
            cinza = int(0.3 * r + 0.59 * g + 0.11 * b)  # Fórmula ponderada para tons de cinza
            imagem_cinza[i][j] = cinza

    return imagem_cinza

# Função para binarizar uma imagem em tons de cinza
def binarizar_imagem(imagem_cinza, limiar=128):
    altura = len(imagem_cinza)
    largura = len(imagem_cinza[0])
    imagem_binarizada = [[0 for _ in range(largura)] for _ in range(altura)]

    for i in range(altura):
        for j in range(largura):
            # Aplica o limiar para binarização
            imagem_binarizada[i][j] = 255 if imagem_cinza[i][j] > limiar else 0

    return imagem_binarizada

# Exemplo de uso
# Matriz representando uma imagem colorida (3x3 pixels, com valores RGB)
imagem_colorida = [
    [(255, 0, 0), (0, 255, 0), (0, 0, 255)],  # Linha 1
    [(128, 128, 128), (255, 255, 0), (0, 255, 255)],  # Linha 2
    [(0, 0, 0), (255, 255, 255), (100, 100, 100)]  # Linha 3
]

# Converte para tons de cinza
imagem_cinza = converter_para_cinza(imagem_colorida)
print("Imagem em tons de cinza:")
for linha in imagem_cinza:
    print(linha)

# Converte para imagem binarizada
imagem_binarizada = binarizar_imagem(imagem_cinza)
print("\nImagem binarizada:")
for linha in imagem_binarizada:
    print(linha)