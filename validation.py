import os
from datetime import datetime, timedelta


def create_date_range(start_date, end_date, delta=timedelta(hours=1)):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += delta


def check_missing_files(start_date, end_date, directory):
    missing_files = []
    # 遍历指定日期范围内的每一个小时
    for dt in create_date_range(start_date, end_date):
        # 构造文件名
        file_name = dt.strftime("BTCUSDT-1h-%Y-%m-%d.csv")
        # 检查文件是否存在于指定目录
        if not os.path.exists(os.path.join(directory, file_name)):
            missing_files.append(file_name)

    return missing_files


# 设置开始日期和结束日期
start_date = datetime(2017, 8, 17)
end_date = datetime(2023, 11, 7)

# 检查data目录下是否有缺失的文件
missing_files = check_missing_files(start_date, end_date, 'data_unzip')

# 打印结果
if missing_files:
    print("以下文件缺失:")
    for file_name in missing_files:
        print(file_name)
else:
    print("没有文件缺失。")

