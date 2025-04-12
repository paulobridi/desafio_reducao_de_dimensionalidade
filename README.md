# desafio_reducao_de_dimensionalidade

O código implementa duas funções principais para manipulação de imagens representadas como matrizes:

1. **`converter_para_cinza(imagem_colorida)`**: 
   - Converte uma imagem colorida (matriz 3D com valores RGB) para níveis de cinza (matriz 2D).
   - Usa uma fórmula ponderada para calcular o tom de cinza: `0.3 * R + 0.59 * G + 0.11 * B`.

2. **`binarizar_imagem(imagem_cinza, limiar=128)`**:
   - Converte uma imagem em tons de cinza (matriz 2D) para uma imagem binarizada (preto e branco).
   - Aplica um limiar (128 por padrão) para definir se o pixel será preto (0) ou branco (255).

No exemplo, uma matriz 3x3 representando uma imagem colorida é convertida para tons de cinza e, em seguida, binarizada. Os resultados são exibidos no console.
