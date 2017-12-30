from io import StringIO

# 初始化后写入内容
buffer = StringIO()
buffer.write("第一次我说爱你的时候，第一次我牵起你的双手\n")
buffer.write("第一次看着我，还没有开口已被你猜透\n")
print(buffer.getvalue())


# 初始化的时候写入内容
f = StringIO('If the night is not forever\nat least we are still together')
while True:
    line = f.readline()
    if line == '':
        break
    print(line.strip())