import os
currentPath = os.path.abspath('.')
filePath = currentPath + "/../config.txt"


# 读取文件
with open(filePath, 'r') as file:
    currentLine = 1
    for line in file.readlines():
        print("currentLine : %d, content : %s" % (currentLine, line))
        currentLine = currentLine + 1

# 追加内容
with open(filePath, 'a') as file:
    file.write("\nNobody, 20, Male, America")

# 写文件
newFilePath = currentPath + "/../newFile.txt"
with open(newFilePath, 'w') as file:
    file.write("If the night is not forever\nat least we are still together")

# 创建目录
currentPath = os.path.abspath('.')
newDir = os.path.join(currentPath, 'steven')
os.makedirs(newDir, exist_ok=True)

# 拆分目录
newFilePath = currentPath + "/../newFile.txt"
fileName = os.path.split(newFilePath)[1]
print(fileName)
