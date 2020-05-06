import matplotlib.pyplot as plt
import numpy as np
import itertools


class examples:
    def __init__(self):
        self.img = plt.imread('flowers.jpg')

    def show_img(self):
        plt.imshow(self.img)
        plt.show()
        plt.close()

    def ex1(self):
        img2 = self.img.copy()
        for i in range(1, img2.shape[0]):
            for j in range(1, img2.shape[1]):
                if np.random.rand() <= 0.1:
                    img2[i, j, :] = 255

        plt.imshow(img2)
        plt.show()
        plt.close()

    def ex2(self):
        img3 = self.img.copy()
        for i in range(1, img3.shape[0]):
            for j in range(1, img3.shape[1]):
                if np.random.rand() <= 0.3:
                    img3[i, j, 0] = np.random.randint(0, 256)
                    img3[i, j, 1] = np.random.randint(0, 256)
                    img3[i, j, 2] = np.random.randint(0, 256)

        plt.imshow(img3)
        plt.show()
        plt.close()


class exercise1:
    def __init__(self, mask_size, mask_coeff):
        self.img = plt.imread('flowers.jpg')
        self.mask_size = mask_size
        self.mask = mask_coeff * np.ones((mask_size, mask_size))

    def print_mask(self):
        """
        Debug
        :return:
        """
        print(self.mask)

    def print_img(self):
        """
        Debug
        :return:
        """
        print(self.img)

    def show_img(self):
        """
        Debug
        :return:
        """
        plt.imshow(self.img)
        plt.show()
        plt.close()

    def filter_image(self):
        filtered = self.img.copy()

        for (x,y) in itertools.product(range(self.mask_size // 2, filtered.shape[0] - self.mask_size // 2),range(self.mask_size // 2, filtered.shape[0] - self.mask_size // 2)):
            # print(f"X: {x}, Y: {y}")
            # print(f"OLD VALUE: {filtered[x,y,:]}")

            new_value = 0

            for (i,j) in itertools.product(range(-(self.mask_size // 2), (self.mask_size // 2) + 1, 1),range(-(self.mask_size // 2), (self.mask_size // 2) + 1, 1)):
                    # print(f"I: {i}, J: {j}")
                    new_value += self.mask[i, j] * filtered[x + i, y + j, :]

            filtered[x, y, :] = new_value
            # print(f"NEW VALUE: {filtered[x, y, :]}")

        self.img = filtered

class exercise2:
    def __init__(self, window_size):
        self.img = plt.imread('flowers.jpg')
        self.window_size = window_size

    def print_img(self):
        """
        Debug
        :return:
        """
        print(self.img)

    def show_img(self):
        """
        Debug
        :return:
        """
        plt.imshow(self.img)
        plt.show()
        plt.close()

    def filter_image(self):
        filtered = self.img.copy()

        for (x,y) in itertools.product(range(self.window_size // 2, filtered.shape[0] - self.window_size // 2),
                                       range(self.window_size // 2, filtered.shape[0] - self.window_size // 2)):
            # print(f"BEFORE: {filtered[x,y,:]}")
            window = []
            for i in range(-(self.window_size // 2), (self.window_size // 2) + 1, 1):
                for j in range(-(self.window_size // 2), (self.window_size // 2) + 1, 1):
                    window.append(filtered[x + i, y + j, :])
            filtered[x, y, :] = np.median(window)
            # print(f"WINDOW: {window}")
            # print(f"AFTER: {filtered[x,y,:]}")

        self.img = filtered

class exercise3:
    def __init__(self):
        self.img = plt.imread('flowers.jpg')

    def show_img(self):
        """
        Debug
        :return:
        """
        plt.imshow(self.img)
        plt.show()
        plt.close()

    def filter_image(self):
        filtered = self.img.copy()
        for (x, y) in itertools.product(range(1, filtered.shape[0]), range(1, filtered.shape[0])):
            if x > (x + (x%10) - 4) and y > (y + (y%10) - 4):
                filtered[x,y,:] = filtered[x + (x%10) - 4, y + (y%10) - 4, :]

        self.img = filtered

class exercise4:
    def __init__(self):
        self.img = plt.imread('flowers.jpg')

    def show_img(self):
        """
        Debug
        :return:
        """
        plt.imshow(self.img)
        plt.show()
        plt.close()

    def filter_image(self):
        filtered = self.img.copy()
        for (x, y) in itertools.product(range(1, filtered.shape[0]), range(1, filtered.shape[0])):
            if (x > 0 and y > 0) and (x % 2 == 0 or y % 2 == 0):
                filtered[x, y, :] = filtered[x - 1, y - 1, :]

        self.img = filtered



if __name__ == '__main__':
    ex1 = exercise1(3, (1 / 9))
    ex1.show_img()
    ex1.filter_image()
    ex1.show_img()

    ex2 = exercise2(3)
    ex2.show_img()
    ex2.print_img()
    ex2.filter_image()
    ex2.show_img()

    ex3 = exercise3()
    ex3.show_img()
    ex3.filter_image()
    ex3.show_img()

    ex4 = exercise4()
    ex4.show_img()
    ex4.filter_image()
    ex4.show_img()