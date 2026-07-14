#实验一
import cv2

# 读取图片（和代码同目录，直接写文件名即可）
img = cv2.imread("test.jpg")

if img is None:
    print("❌ 图片读取失败！请检查文件名是否正确")
else:
    print("✅ 图片读取成功！")
    # 显示原图
    cv2.imshow("原图", img)
    cv2.waitKey(0)

    # 转灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("灰度图", gray)
    cv2.waitKey(0)

    # 边缘检测
    edges = cv2.Canny(gray, 50, 150)
    cv2.imshow("边缘检测", edges)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

import cv2

# ====================== 实验二：OpenCV 人脸检测 ======================
# 1. 读取图片（你已经放好 test.jpg）
image = cv2.imread("test.jpg")

if image is None:
    print("❌ 图片读取失败")
    exit()

# 2. 加载 OpenCV 自带的人脸检测模型（不用自己下 xml）
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# 3. 转灰度图（Haar 必须用灰度）
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4. 检测人脸（PPT 里的参数）
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# 5. 给每个人脸画绿色框
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 6. 显示结果
cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. 输出检测到几张脸
print(f"✅ 检测到人脸数量：{len(faces)}")