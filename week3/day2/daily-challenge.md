# Daily challenge: 
---
### What you will learn 

- Data Augmentation
- Data visualization using MatPlotLib or PIL libraries.
  
---
### Your Task

- Load and Visualize Images using the [Flower Color Images dataset](https://www.kaggle.com/datasets/olgabelitskaya/flower-color-images)
- Rotate an image by 90 degrees
- Flip an image horizontally and then vertically.
- Zoom in on an image (scale by 1.2x) using `.resize(...)`
- Display the original and augmented images side by side for comparison using this function :
  ```python
  import matplotlib.pyplot as plt
  from PIL import Image, ImageOps
  
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
  ```

---

### Duration & Difficulty
| Duration (approx)    | Difficulty |
|----------------------|------------|
| 20 minutes           |     ⭐     |

---
### Submit your Daily Challenge 

Don’t forget to push to Github!
