# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Load an example image
# image_path = r"D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\fishhealth-main\fishhealth-main\img\data\input.png"
# image = cv2.imread(image_path)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# # Data augmentation functions
# def rotate_image(image, angle):
#     height, width = image.shape[:2]
#     rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
#     rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
#     return rotated_image

# def flip_image(image, flip_code):
#     flipped_image = cv2.flip(image, flip_code)
#     return flipped_image

# def scale_image(image, scale_factor):
#     scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
#     return scaled_image

# # Data augmentation parameters
# rotation_angle = 30  # Rotation angle in degrees
# flip_code = 1  # Flip horizontally (0), vertically (1), or both (-1)
# scale_factor = 1.2  # Scale factor

# # Apply data augmentation
# augmented_images = []
# augmented_images.append(rotate_image(image, rotation_angle))
# augmented_images.append(flip_image(image, flip_code))
# augmented_images.append(scale_image(image, scale_factor))

# # Plot original and augmented images
# plt.figure(figsize=(10, 5))
# plt.subplot(2, 3, 1)
# plt.imshow(image)
# plt.title("Original")
# plt.axis('off')

# # Plot augmented images
# titles = ["Rotated", "Flipped", "Scaled"]
# for i in range(len(augmented_images)):
#     plt.subplot(2, 3, i + 2)
#     plt.imshow(augmented_images[i])
#     plt.title(titles[i])
#     plt.axis('off')

# plt.tight_layout()
# plt.show()


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an example image
# image_path = "example_image.jpg"
image_path = r"D:\New Volume(D old)\PhD Course\Courses\Second semester\AI project\Fig - AI project code\fishhealth-main\fishhealth-main\img\data\input.png"
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Load an example image
# image_path = "example_image.jpg"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# Data augmentation functions
def flip_image(image, flip_code):
    flipped_image = cv2.flip(image, flip_code)
    return flipped_image

def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def blur_image(image, kernel_size):
    blurred_image = cv2.blur(image, (kernel_size, kernel_size))
    return blurred_image

def increase_hue(image, factor):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    hsv_image[:, :, 0] = np.clip(hsv_image[:, :, 0].astype(int) + factor, 0, 179)
    return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)

# Data augmentation parameters
flip_codes = [0, 1, -1]  # Flip horizontally (0), vertically (1), or both (-1)
rotation_angle = 30  # Rotation angle in degrees
kernel_size = 13  # Kernel size for blurring
hue_factor = 20  # Increase in hue

# Apply data augmentation
augmented_images = []
for flip_code in flip_codes:
    augmented_images.append(flip_image(image, flip_code))
augmented_images.append(rotate_image(image, rotation_angle))
augmented_images.append(blur_image(image, kernel_size))
augmented_images.append(increase_hue(image, hue_factor))

# Plot augmented images
plt.figure(figsize=(10, 8))
titles = ["Horizontal Flip", "Vertical Flip", "Horizontal and Vertical Flip", 
          "Rotated", "Blurred", "Increased Hue"]
for i in range(len(augmented_images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(augmented_images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
