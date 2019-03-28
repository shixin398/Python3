from selenium import webdriver
import pandas as pd

# driver = "D:/python/"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# browser = webdriver.Chrome(driver, chrome_options=chrome_options)
# browser = webdriver.PhantomJS()
# browser.maximize_window()

# browser = webdriver.Chrome()
# browser.get("http://data.eastmoney.com/bbsj/201806/lrb.html")
# element = browser.find_element_by_css_selector("#dt_1")

# test
# td_content = element.find_elements_by_tag_name("td")
#tdList = []
# for td in td_content:
#     tdList.append(td.text)
# print(tdList)

# chang to DataFrame
# col = len(element.find_elements_by_css_selector('tr:nth-child(1) td'))
# tdList = [tdList[i:i + col] for i in range(0, len(tdList), col)]
# tdList_detail = []
# links = element.find_elements_by_css_selector('#dt_1 a.red')
# for link in links:
#     url = link.get_attribute("href")
#     tdList_detail.append(url)
# tdList_detail = pd.Series(tdList_detail)
# df_table = pd.DataFrame(tdList)
# df_table["url"] = tdList_detail
# print(df_table)
# print(df_table.head())

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()
browser.maximize_window()  # 最大化窗口,可以选择设置
wait = WebDriverWait(browser, 1)


def go():
    element = browser.find_element_by_css_selector("#dt_1")
    tdlist = []
    td_content = element.find_elements_by_tag_name("td")
    for td in td_content:
        tdlist.append(td.text)
    # chang to DataFrame
    col = len(element.find_elements_by_css_selector('tr:nth-child(1) td'))
    tdlist = [tdlist[i:i + col] for i in range(0, len(tdlist), col)]
    tdlistdetail = []
    links = element.find_elements_by_css_selector('#dt_1 a.red')
    for link in links:
        url = link.get_attribute("href")
        tdlistdetail.append(url)
    tdlistdetail = pd.Series(tdlistdetail)
    df_table = pd.DataFrame(tdlist)
    print(df_table)
    df_table["url"] = tdlistdetail
    print(df_table.head())
    df_table.to_csv('D:\\a.csv', sep=',', header=True, index=True,encoding="utf_8_sig")


def index_page(page):
    try:
        browser.get('http://data.eastmoney.com/bbsj/201806/lrb.html')
        print('正在爬取第： %s 页' % page)
        wait.until(
            EC.presence_of_element_located((By.ID, "dt_1")))
        # 判断是否是第1页，如果大于1就输入跳转，否则等待加载完成。
        if page > 1:
            # 确定页数输入框
            input = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="PageContgopage"]')))
            input.click()
            input.clear()
            input.send_keys(page)
            submit = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#PageCont > a.btn_link')))
            submit.click()
            time.sleep(2)
        # 确认成功跳转到输入框中的指定页
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#PageCont > span.at'), str(page)))
        go()
    except Exception:
        return None

def init():
    # 重构url
    # 1 设置财务报表获取时期
    year = int(float(input('请输入要查询的年份(四位数2007-2018)：  ')))
    # int表示取整，里面加float是因为输入的是str，直接int会报错，float则不会
    while (year < 2007 or year > 2018):
        year = int(float(input('年份数值输入错误，请重新输入：')))
    quarter = int(float(input('请输入小写数字季度(1:1季报，2-年中报，3：3季报，4-年报)：  ')))
    while (quarter < 1 or quarter > 4):
        quarter = int(float(input('季度数值输入错误，请重新输入：  ')))
    # 转换为所需的quarter 两种方法,2表示两位数，0表示不满2位用0补充
    quarter = '{:02d}'.format(quarter * 3)
    # quarter = '%02d' %(int(month)*3)
    date = '{}{}' .format(year, quarter)

    # 2 设置财务报表种类
    tables = int(
        input('请输入查询的报表种类对应的数字(1-业绩报表；2-业绩快报表：3-业绩预告表；4-预约披露时间表；5-资产负债表；6-利润表；7-现金流量表):  '))
    dict_tables = {1: '业绩报表', 2: '业绩快报表', 3: '业绩预告表',
                   4: '预约披露时间表', 5: '资产负债表', 6: '利润表', 7: '现金流量表'}
    dict = {1: 'yjbb', 2: 'yjkb/13', 3: 'yjyg',
            4: 'yysj', 5: 'zcfz', 6: 'lrb', 7: 'xjll'}
    category = dict[tables]

    # 3 设置url
    url = 'http://data.eastmoney.com/{}/{}/{}.html' .format('bbsj', date, category)
    print(url)  # 测试输出的url

    # 4 选择爬取页数范围
    start_page = int(input('请输入下载起始页数：\n'))
    nums = input('请输入要下载的页数，（若需下载全部则按回车）：\n')
    # 确定网页中的最后一页
    browser.get(url)
    # 确定最后一页页数不直接用数字而是采用定位，因为不同时间段的页码会不一样
    try:
        page = browser.find_element_by_css_selector('.next + a')  # next节点后面的a节点
    except:
        page = browser.find_element_by_css_selector('.at + a')
    else:
        print('没有找到该节点')
    # 上面用try.except是因为绝大多数页码定位可用'.next+ a'，但是业绩快报表有的只有2页，无'.next+ a'节点
    end_page = int(page.text)

    if nums.isdigit():
        end_page = start_page + int(nums)
    elif nums == '':
        end_page = end_page
    else:
        print('页数输入错误')
    # 输入准备下载表格类型
    print('准备下载:{}-{}' .format(date, dict_tables[tables]))
    for page in range(start_page,end_page):  # 测试翻4页
        index_page(page)


def main():
    init()


if __name__ == '__main__':
    main()
