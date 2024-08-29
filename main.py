from PIL import Image
import numpy as np

image_path = 'diretorio'
image = Image.open(image_path)

image_np = np.array(image)
green_channel = image_np[:, :, 1]
red_channel = image_np[:, :, 0]
blue_channel = image_np[:, :, 2]
green_mask = (green_channel > red_channel) & (green_channel > blue_channel)

area = np.sum(green_mask) / green_mask.size * 100

print(f'Aproximadamente {area:.2f}% da área total.')
