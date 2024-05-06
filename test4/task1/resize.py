import cv2

path = 'E:/20212333Python\demo09_AnalisisData/test4\pic'

for i in range(0, 40):
    # 读取分割后的图像
    image = cv2.imread(path + '/cut/' + f'{i}' + '.png', cv2.IMREAD_GRAYSCALE)

    # 调整大小为30x30
    resized_image = cv2.resize(image, (30, 30))

    cv2.imwrite(path + '/resize/' + f'{i}' + '.png', resized_image)


