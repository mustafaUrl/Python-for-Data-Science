import numpy as np
from load_image import ft_load
from PIL import Image


def main():
    ''' This function will crop the image and convert it to grayscale using numpy '''
    img = ft_load("../animal.jpeg")

    # height, width = img.shape[:2]

    # center_x = width // 2
    # center_y = height // 2

    # start_x = center_x - 200 
    # start_y = center_y - 200
    # end_x = center_x + 200
    # end_y = center_y + 200

    start_y = 100
    start_x = 450
    end_y = 500
    end_x = 850

    cropped_img = img[start_y:end_y, start_x:end_x]


    gray_img = 0.2989 * cropped_img[:, :, 0] + 0.5870 * cropped_img[:, :, 1] + 0.1140 * cropped_img[:, :, 2]

    gray_img = gray_img.astype(np.uint8)

    image = Image.fromarray(gray_img)

    image.save("output_image_gray_numpy.jpg")
    
    print(f"New shape after slicing: {gray_img.shape}\n {gray_img}")

    return gray_img



if __name__ == "__main__":
    main()