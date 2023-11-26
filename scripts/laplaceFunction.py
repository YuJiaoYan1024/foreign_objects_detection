import cv2

def get_picture_sharpness(image_path):
    image = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image_var = str(int(cv2.Laplacian(image_gray, cv2.CV_64F).var()))
    # image_var = str(int(cv2.Laplacian(image_gray, cv2.CV_16U).var()))

    font_face = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    thickness = 1
    baseline = 0

    var_size = cv2.getTextSize(image_var, font_face, font_scale, thickness)
    # 清晰度值的绘制位置
    draw_start_point = (20, var_size[0][1] + 10)
    cv2.putText(image, image_var, draw_start_point, font_face, font_scale, (0, 0, 255), thickness)

    cv2.imshow('frame', image)
    cv2.waitKey(0)

    return image_var

print(get_picture_sharpness("./images1/1.jpg"))
print(get_picture_sharpness("./images2/1.png"))