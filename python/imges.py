import numpy as np

image = np.array([
    [100, 150, 200, 50],
    [50,  100, 150, 200],
    [200, 50,  100, 150],
    [150, 200, 50,  100]
], dtype=np.uint8)

print("Original Image Matrix (4x4):")
print(image)
print("-" * 45)

reshaped_image = image.reshape(2, 8)
print("Reshaped Image (2x8):")
print(reshaped_image)
print("-" * 45)

cropped_region = image[0:2, 0:2]
print("Sliced Region (Top-Left 2x2 Crop):")
print(cropped_region)
print("-" * 45)

bright_image = np.clip(image.astype(np.float32) + 50, 0, 255).astype(np.uint8)
print("Brightness-Adjusted Image (+50):")
print(bright_image)
print("-" * 45)

transformation_matrix = np.array([
    [1.1, 0,   0,   0],
    [0,   1.1, 0,   0],
    [0,   0,   1.1, 0],
    [0,   0,   0,   1.1]
])

transformed_image = np.dot(image.astype(np.float32), transformation_matrix)
transformed_image = np.clip(transformed_image, 0, 255).astype(np.uint8)
print("Transformed Image (Matrix Multiplication):")
print(transformed_image)
