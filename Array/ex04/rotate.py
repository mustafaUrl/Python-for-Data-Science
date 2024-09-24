import numpy as np
from load_image import ft_load
from PIL import Image


def main():
    
    img = ft_load("../animal.jpeg")
    start_y = 100
    start_x = 450
    end_y = 500
    end_x = 850

    cropped_img = img[start_y:end_y, start_x:end_x]


    gray_img = 0.2989 * cropped_img[:, :, 0] + 0.5870 * cropped_img[:, :, 1] + 0.1140 * cropped_img[:, :, 2]

    gray_img = gray_img.astype(np.uint8)

    image = Image.fromarray(gray_img)
    
    transpose = np.array(image)
    rez = [[transpose[j][i] for j in range(len(transpose))] for i in range(len(transpose[0]))]
    
    rez = np.array(rez)
    print("New shape after Transpose: ", rez.shape, "\n", rez)
    image = Image.fromarray(rez)
    image.save("output_image_gray_numpy.jpg")

if __name__ == "__main__":
    main()