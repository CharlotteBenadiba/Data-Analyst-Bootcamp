import os
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

# Function to display images
def show_images(original, augmented, title):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(augmented)
    plt.title(title)
    plt.axis('off')

    plt.show()

# Load a sample image - replace 'path_to_dataset' with the actual path
!pip install kaggle
#import kaggle
from google.colab import files
files.upload()
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download olgabelitskaya/flower-color-images
!unzip flower-color-images.zip

# Load a sample image from the unzipped dataset
path_to_dataset = '/content'  # Path to the unzipped dataset folder
image_path = os.path.join(path_to_dataset, '0001.png')  # Sample image
original_image = Image.open(image_path)

# Rotation
rotated_image = original_image.rotate(90)
show_images(original_image, rotated_image, 'Rotated Image')

# Horizontal Flip
hflipped_image = ImageOps.mirror(original_image)
show_images(original_image, hflipped_image, 'Horizontally Flipped Image')

# Vertical Flip
vflipped_image = ImageOps.flip(original_image)
show_images(original_image, vflipped_image, 'Vertically Flipped Image')

# Scaling (Zoom In)
width, height = original_image.size
scaled_image = original_image.resize((int(width * 1.2), int(height * 1.2)), Image.ANTIALIAS)
show_images(original_image, scaled_image, 'Scaled Image')

# Optionally, save the augmented images
save_path = 'augmented_images'  # Create this directory if it doesn't exist
rotated_image.save(os.path.join(save_path, 'rotated_image.png'))
hflipped_image.save(os.path.join(save_path, 'hflipped_image.png'))
vflipped_image.save(os.path.join(save_path, 'vflipped_image.png'))
scaled_image.save(os.path.join(save_path, 'scaled_image.png'))
