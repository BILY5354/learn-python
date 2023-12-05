import cv2
import time

# 读取图片并开始计时
start_time = time.time()
img = cv2.imread(r'./02workspace/05readImage/InspH060W034B00R000C000O50L0M0.BMP', cv2.IMREAD_UNCHANGED)
elapsed_time = time.time() - start_time

# 输出读取时间和图像大小
print(f"读取用时: {elapsed_time:.2f} 秒")
print(f"图像大小: {img.shape}")