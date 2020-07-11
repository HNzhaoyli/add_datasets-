import os
from PIL import Image
from torchvision import transforms as tfs
import matplotlib.pyplot as plt
import numpy as np

random_data = r'F:\NEW_DATA\random_img'
h_filp_data = r'F:\NEW_DATA\h_filp'
v_filp_data = r'F:\NEW_DATA\v_filp'
random_img_small = r'F:\NEW_DATA\random_img_small'

def read_directory(directory_name):
    for filename in os.listdir(directory_name):
        img = Image.open(directory_name + "/" + filename)
        print(filename)
        random_img = tfs.RandomCrop((400, 900))(img)
        random_img2 = tfs.RandomCrop((400,900))(img)
        # 随机水平翻转
        h_filp = tfs.RandomHorizontalFlip(p=1)(img)
        # 随机竖直翻转
        v_flip = tfs.RandomVerticalFlip(p=1)(img)

        for i in range(1,5):
            if i == 1:
                path1 = os.path.join(random_data,'{}_{}.jpg'.format(filename,i))
                random_img.save(path1)
            if i == 2:
                path2 = os.path.join(random_data,'{}_{}.jpg'.format(filename,i))
                random_img2.save(path2)
                print(path2)
            if i == 3:
                path3 = os.path.join(h_filp_data,'{}_{}.jpg'.format(filename,i))
                h_filp.save(path3)
            if i == 4:
                path4 = os.path.join(v_filp_data,'{}_{}.jpg'.format(filename,i))
                v_flip.save(path4)


        '''        plt.figure("Transform", figsize=(20, 10))  # 图像窗口名称
        plt.suptitle('Transform')

        plt.subplot(2, 2, 1), plt.title('image')
        plt.imshow(img), plt.axis('on')

        plt.subplot(2, 2, 2), plt.title('h_flip')
        plt.imshow(h_filp), plt.axis('on')

        plt.subplot(2, 2, 3), plt.title('random_crop')
        plt.imshow(random_img), plt.axis('on')

        plt.show()'''


if  __name__ == '__main__':
    file = r'F:\原始数据集'
    for filename in os.listdir(file):
        img = Image.open(file + "/" + filename)
        random_img = tfs.RandomCrop((350, 600))(img)
        random_img2 = tfs.RandomCrop((350,600))(img)
        for i in range(1,3):
            if i == 1:
                path1 = os.path.join(random_img_small,'{}_{}.jpg'.format(filename,i))
                random_img.save(path1)
            if i == 2:
                path2 = os.path.join(random_img_small,'{}_{}.jpg'.format(filename,i))
                random_img2.save(path2)
    print('finished......')
    #read_directory(file)

