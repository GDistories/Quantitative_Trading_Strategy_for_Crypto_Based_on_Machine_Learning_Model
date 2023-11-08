import os
from datetime import datetime, timedelta
import pandas as pd

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
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 11, 7)

# 检查data目录下是否有缺失的文件
missing_files = check_missing_files(start_date, end_date, 'data_unzip_2023')

# 打印结果
if missing_files:
    print("以下文件缺失:")
    for file_name in missing_files:
        print(file_name)
else:
    print("没有文件缺失，开始合并文件。")

    # 确定合并后文件的名称
    output_file = "merged_data_2023.csv"

    # 获取data_unzip目录下所有的csv文件
    csv_files = [file for file in os.listdir('data_unzip_2023') if file.endswith('.csv')]

    # 按文件名排序，确保数据顺序正确
    csv_files.sort()

    # 创建一个空的DataFrame来追加数据
    merged_df = pd.DataFrame()

    # 遍历并追加数据
    for file in csv_files:
        file_path = os.path.join('data_unzip_2023', file)
        print(f"正在读取文件 {file_path}...")
        # 读取CSV文件
        df = pd.read_csv(file_path)
        # 追加到合并的DataFrame
        merged_df = pd.concat([merged_df, df])

    # 保存到新的CSV文件
    merged_df.to_csv(output_file, index=False)
    print(f"所有数据已合并到文件 {output_file}。")


