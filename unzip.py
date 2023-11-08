import os
import zipfile

# 创建一个目录来存放解压后的文件
unzip_dir = 'data_unzip'
if not os.path.exists(unzip_dir):
    os.makedirs(unzip_dir)

# 遍历data目录中的所有文件
data_dir = 'data'
for item in os.listdir(data_dir):
    if item.endswith('.zip'):  # 检查文件扩展名
        file_path = os.path.join(data_dir, item)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # 解压文件到指定目录
            zip_ref.extractall(unzip_dir)
            print(f"解压完成: {item}")

print("所有文件解压完成。")
