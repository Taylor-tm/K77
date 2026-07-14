import cv2

# ===================== 实验五：摄像头采集 =====================
# 1. 打开摄像头
cap = cv2.VideoCapture(0)

print("📷 实验五：摄像头已打开")
print("👉 按 S 键 保存图片")
print("👉 按 Q 键 退出")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 显示画面
    cv2.imshow("Experiment 5 - Camera Capture", frame)

    key = cv2.waitKey(1) & 0xFF

    # 按 S 保存
    if key == ord('s'):
        cv2.imwrite("camera_photo.jpg", frame)
        print("✅ 图片已保存：camera_photo.jpg")

    # 按 Q 退出
    if key == ord('q'):
        break

# 释放
cap.release()
cv2.destroyAllWindows()
print("👋 实验五结束")