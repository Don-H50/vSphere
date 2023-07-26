import re
import json

# 用于存储结果的列表
result = []

# 文件路径和名称
file_path = r"D:\save_url.txt"
i = 0
# 打开文件
with open(file_path, 'r') as file:
    for line in file:
        # 检查当前行是否包含[INFO]且URL包含"https://192.168.8.99"
        if '[INFO]' in line and "https://192.168.8.99" in line and 'GET' in line:
            i = i + 1
            # 提取请求方法
            method = re.search(r'processing (.*?) ', line).group(1)
            # 提取URL
            url = re.search(r'https://192.168.8.99[^\s]*', line).group()
            # 将结果添加到字典中
            # result.append({"method": method, "url": url})
            result.append(json.dumps({"method": method, "url": url}))

for item in result:
    print(item)
print(i)

# 将结果转为集合进行去重
result = list(set(result))

# 将字符串再转回字典
result = [json.loads(item) for item in result]

output_file_path = r"./save2.json"
with open(output_file_path, 'w') as output_file:
    for item in result:
        #output_file.write(json.dumps(item, indent = 4) + '\n')
        output_file.write(json.dumps(item) + '\n')
