from PIL import Image

def rotate_image(image_path, degrees):
    image = Image.open(image_path)
    rotated_image = image.rotate(degrees)
    rotated_image.save("rotated_image.jpg")
    print("Image rotated and saved as rotated_image.jpg")

rotate_image("C:\\Users\\junti\\OneDrive\\Desktop\\2025-Lamborghini-Hypercar.jpg", 90)
