import zipfile
# sample.xlsx와 index.html 파일을 sample.zip으로 압축

zf = zipfile.ZipFile('sample.zip', 'w')
zf.write('sample.xlsx')
zf.write('index.html')
zf.close()

# sample.zip 파일을 c:\Users\dhkim 아래에 압축풀기
uzf = zipfile.ZipFile('sample.zip', 'r')
uzf.extractall(path='c:\\Users\\dhkim')