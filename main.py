from selenium import webdriver
from selenium.webdriver.common.by import By

from mongo import MongoConnection


db_client = MongoConnection().client
db = db_client.get_database('alibaba')
col = db.get_collection('products')

driver = webdriver.Chrome()
driver.get("https://sale.alibaba.com/category/1tab_searoom_productlist/index.html?spm=a27aq.cp_15.1209139070.2.3c734e30hP3YVf&wx_navbar_transparent=true&path=/p/dv8r5d9qf/index.html&ncms_spm=a27aq.28390436&prefetchKey=met&wx_xpage=true&deliveryId=4426004_904380808_STOCK_25_87208537&topOfferIds=1600764379248&categoryIds=&cardId=&tracelog=fy23_all_categories_home_lp")
items = driver.find_elements(By.CLASS_NAME, "hugo4-pc-grid-item")
for i in items:

    product_name = i.find_element(by=By.CLASS_NAME, value="subject-pc").text
    price_range = i.find_element(by=By.CLASS_NAME, value="hugo3-fz-medium").text
    moq = i.find_element(by=By.CLASS_NAME, value="moq-number").text

    document = {
        "product_name": product_name,
        "product_price": price_range,
        "moq": moq
    }

    col.insert_one(document=document)

    print("Nombre del producto:", product_name)
    print("Precio del producto:", price_range)
    print("MOQ:", moq)
    print('=' * 40)

driver.quit()
driver.close()