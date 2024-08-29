from PIL import Image
import numpy as np

image_path = 'caminho/para/sua/imagem.jpg' 
image = Image.open(image_path)

# Converter a imagem para um array numpy
image_np = np.array(image)

# Analisar as cores na imagem
# Considerando áreas verdes como aquelas com valores mais altos no canal verde
green_channel = image_np[:, :, 1]
red_channel = image_np[:, :, 0]
blue_channel = image_np[:, :, 2]

# Definir uma máscara para as áreas verdes
green_mask = (green_channel > red_channel) & (green_channel > blue_channel)

# Calcular a porcentagem de áreas verdes
green_area_percentage = np.sum(green_mask) / green_mask.size * 100

# Exibir o resultado
print(f'A área verde corresponde a aproximadamente {green_area_percentage:.2f}% da área total.')
