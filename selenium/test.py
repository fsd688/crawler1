from selenium import webdriver
from selenium.webdriver.common.by import By
import xlsxwriter

import string
wd = webdriver.Chrome("chromedriver.exe")
wd.implicitly_wait(20)
# 创建工作簿
workbook = xlsxwriter.Workbook('测试文件.xlsx')  # 创建一个excel文件
# 创建工作表
worksheet = workbook.add_worksheet()  # 在文件中创建一个名为这是sheet1的sheet,不加名字默认为sheet1
row = 0
col = 0
# =============
# element = wd.find_element(By.ID,"inputVarTcm")
# element.send_keys('陈皮')
# element = wd.find_element(By.ID,"searchBtTcm")
# element.click()
# =============

for i in range(3,100):
    wd.get('https://old.tcmsp-e.com/molecule.php?qn='+str(i+1))
    # element = wd.find_element(By.ID, "kendo_adme")
    # a = element.find_elements(By.TAG_NAME,'th')
    # print(a[4].text)

    try:
        molName = wd.find_element(By.CLASS_NAME,"tableRst2").find_element(By.TAG_NAME,"td").text
        # 下载mol2文件
        element_mol2 = wd.find_element(By.CLASS_NAME, "stct")
        # TODO element_mol2.click()
        # print(element_mol2)
        # 获取OB值和DL值
        Pharmacological_and_molecular_properties_data = wd.find_element(By.ID, "kendo_adme")
        element = Pharmacological_and_molecular_properties_data.find_elements(By.TAG_NAME, 'td')
        ob = element[4].text
        dl = element[7].text
        ob = float(ob)
        dl = float(dl)
        if (ob >= 30 and dl >= 0.18):
            # TODO print(ob,dl)
            # 将关联target写入excel
            related_target = wd.find_element(By.ID, "kendo_target")
            isNA = related_target.get_attribute("innerHTML")
            if (isNA != 'N/A'):
                # target页数
                pageNum = related_target.find_elements(By.CSS_SELECTOR, ".k-pager-wrap.k-grid-pager.k-widget")[0] \
                    .find_elements(By.CSS_SELECTOR, ".k-pager-numbers.k-reset")[0] \
                    .find_elements(By.TAG_NAME, "li").__len__()





                if(pageNum == 1):
                    first_page_target = related_target.find_element(By.CLASS_NAME, "k-grid-content").find_elements(By.TAG_NAME, "tr")

                    for content in first_page_target:
                        content = content.find_elements(By.TAG_NAME, "td")[0].text
                        worksheet.write(row, 0, molName)
                        worksheet.write(row, 1, content)
                        row+=1









                elif(pageNum>1):
                    first_page_target = related_target.find_element(By.CLASS_NAME, "k-grid-content").find_elements(By.TAG_NAME, "tr")
                    for content in first_page_target:
                        content = content.find_elements(By.TAG_NAME, "td")[0].text

                        worksheet.write(row, 0, molName)
                        worksheet.write(row, 1, content)
                        row += 1
                    for k in range(pageNum-1):
                        tag_a = related_target.find_elements(By.CSS_SELECTOR, ".k-pager-wrap.k-grid-pager.k-widget")[0] \
                                                .find_elements(By.CLASS_NAME, "k-link")
                        idx3 = 0
                        for tag in tag_a:
                            if (tag.text == 'Go to the next page'):
                                tag.click()
                                content = related_target.find_element(By.CLASS_NAME,"k-grid-content").find_elements(By.TAG_NAME,"tr")
                                for c in content:
                                    content = c.find_elements(By.TAG_NAME, "td")[0].text
                                    worksheet.write(row, 0, molName)
                                    worksheet.write(row, 1, content)
                                    row += 1





                print(str(i + 1), pageNum)
    except:
        print(str(i + 1),'发生异常')



workbook.close()

