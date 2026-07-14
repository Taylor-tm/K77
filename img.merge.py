import cv2
import numpy as np

# ===================== 实验四：图像拼接 =====================
# 1. 读取两张图片（自己放 test1.jpg 和 test2.jpg）
img1 = cv2.imread("test1.jpg")
img2 = cv2.imread("test2.jpg")

if img1 is None or img2 is None:
    print("❌ 请放入 test1.jpg 和 test2.jpg 到项目里！")
    exit()

# 2. 统一高度（自动适配）
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]

if h1 != h2:
    img2 = cv2.resize(img2, (int(w2 * h1 / h2), h1))

# 3. 水平拼接
result = np.hstack((img1, img2))

# 4. 显示并保存
cv2.imshow("实验四：图像拼接", result)
cv2.imwrite("merge_result.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
print("✅ 拼接完成！已保存为 merge_result.jpg")