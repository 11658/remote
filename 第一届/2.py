# # 定义初始的 JSON 数据
# json_data = [
#     {'石志刚': ['打卡', 3, '迟到', '一次']},
#     {'石刚': ['打卡', 3, '迟到', '一次']}
# ]
#
# #添加
#
# # 增加数据
# def add_data(name, key, value):
#     for item in json_data:
#         if name in item:
#             item[name].append(key)
#             item[name].append(value)
#             break
#     else:
#         json_data.append({name: [key, value]})
#
# # 删除数据
# def delete_data(name, key):
#     for item in json_data:
#         if name in item:
#             item[name].remove(key)
#             break
#
# # 修改数据
# def update_data(name, key, new_value):
#     for item in json_data:
#         if name in item:
#             index = item[name].index(key)
#             item[name][index + 1] = new_value
#             break
#
# # 查询数据
# def query_data(name, key):
#     for item in json_data:
#         if name in item:
#             index = item[name].index(key)
#             return item[name][index + 1]
#     return None
#
# # 测试代码
# add_data('石志刚', '请假', '一天')
# print(json_data)  # 输出：[{'石志刚': ['打卡', 3, '迟到', '一次', '请假', '一天']}, {'石刚': ['打卡', 3, '迟到', '一次']}]
#
# delete_data('石志刚', '迟到')
# print(json_data)  # 输出：[{'石志刚': ['打卡', 3, '请假', '一天']}, {'石刚': ['打卡', 3, '迟到', '一次']}]
#
# update_data('石刚', '打卡', 4)
# print(json_data)  # 输出：[{'石志刚': ['打卡', 3, '请假', '一天']}, {'石刚': ['打卡', 4, '迟到', '一次']}]
#
# result = query_data('石刚', '打卡')
# print(result)  # 输出：4
# import datetime
#
# date_string = "24-02-20 星期二"
# # 首先，去除字符串中的中文星期部分，以便正确解析日期
# date_only = date_string.split(' ')[0]
#
# # 然后，根据格式化字符串将字符串转换成datetime对象
# # 注意这里的格式应当对应字符串的实际格式，"%d-%m-%y" 表示日-月-年两位数形式
# date_object = datetime.datetime.strptime(date_only, "%y-%m-%d")
#
# # 从datetime对象中提取日
# day_of_month = date_object.day
# print(day_of_month)

from datetime import datetime

# 定义字符串

# def time_difference(text):
#     # 提取时间部分
#     start_time_str = text[8:13]
#     end_time_str = text[20:25]
#     # print(start_time_str, end_time_str)
#     # 将时间字符串转换为datetime对象
#     date_format = "%H:%M"
#     start_time = datetime.strptime(start_time_str, date_format)
#     end_time = datetime.strptime(end_time_str, date_format)
#     print(start_time, end_time)
#     # 计算时间差的秒数
#     time_diff_seconds = (end_time - start_time).total_seconds()
#
#     # 将秒数转换为小时数
#     hours = time_diff_seconds / 3600
#     return hours
#
# text = '调休02-23 13:30到02-23 17:30 0.5天'
# print(time_difference(text))


# leave_date = ["7", "8", "9"]
# if '7' in leave_date:
#     print('7' in leave_date)

#
# from openpyxl import load_workbook
#
# # 读取 Excel 文件
# file_name = "2024年2月考勤明细20241.xlsx"
#
# # 加载工作簿
# wb1 = load_workbook(filename=file_name)
#
# # 获取工作表
# sheet = wb1.worksheets[1]
#
# for row in sheet.rows:
#     # 遍历每一列
#     list_data1 = []
#     for cell in row:
#         # 打印单元格的值
#         list_data1.append(cell.value)
#     print(list_data1)
# # 修改指定位置的数据
# sheet.cell(row=13, column=13).value = '123'
#
# # 保存工作簿
# wb1.save(filename=file_name)

# from PIL import Image
#
# def concatenate_images_vertically(image1_path, image2_path, output_path):
#     # Open images
#     image1 = Image.open(image1_path)
#     image2 = Image.open(image2_path)
#
#     # Ensure both images have the same width
#     width = max(image1.width, image2.width)
#     image1 = image1.resize((width, image1.height))
#     image2 = image2.resize((width, image2.height))
#
#     # Create a new blank image with combined height
#     new_image = Image.new('RGB', (width, image1.height + image2.height))
#
#     # Paste images onto the new blank image
#     new_image.paste(image1, (0, 0))
#     new_image.paste(image2, (0, image1.height))
#
#     # Save the new image
#     new_image.save(output_path)
#
# if __name__ == "__main__":
#     image1_path = "微信截图_20240301164122.png"
#     image2_path = "微信截图_20240301164159.png"
#     output_path = "3597750.png"
#
#     concatenate_images_vertically(image1_path, image2_path, output_path)
def time_difference_tiao(text,text1):

    start_time_str = text
    end_time_str = text1
    # print(start_time_str, end_time_str)
    # 将时间字符串转换为datetime对象
    date_format = "%H:%M"
    start_time = datetime.strptime(start_time_str, date_format)
    end_time = datetime.strptime(end_time_str, date_format)
    # print(start_time, end_time)
    # 计算时间差的秒数
    time_diff_seconds = (end_time - start_time).total_seconds()

    # 将秒数转换为小时数
    hours = time_diff_seconds / 3600
    if hours >= 7:
        return 1
    else:
        return 0.5


print(time_difference_tiao("20:00","22:00"))