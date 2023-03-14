from rdkit import Chem
import os
import re
# files = os.listdir("./mol2")
# a = Chem.MolFromMol2File("./mol2/MOL000330.mol2")
# smile = Chem.MolToSmiles(a)
# print(smile)
# # for file in files:
#     a = Chem.MolFromMol2File("./mol2/"+file)
#     smile = Chem.MolToSmiles(a)
#     # print(file[0:9],smile)
#     print(smile)

import xlsxwriter

# 创建工作簿
workbook = xlsxwriter.Workbook('测试文件.xlsx')  # 创建一个excel文件

# 创建工作表
worksheet = workbook.add_worksheet('这是sheet1')  # 在文件中创建一个名为这是sheet1的sheet,不加名字默认为sheet1

# 写入数据
worksheet.write(0, 0, '写点什么好')  # 第1行第1列（即A1）写入

workbook.close()

print()
print("hotfix")
print("hotfix")
