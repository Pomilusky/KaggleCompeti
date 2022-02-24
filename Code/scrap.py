import pandas as pd
from selenium import webdriver
import numpy as np

# I am going to scrap the price of the airbnb in descember last year, in order to try and guess the price from there,
df = pd.read_csv('../Data/train.csv') # let's import the data frame
df1 = df.iloc[:1000]
df2 = df.iloc[1000:2000]
df3 = df.iloc[2000:]
# let's create the function to scrap each url,
def scrap_price(l_url):
    try:
        url = l_url+'?_set_bev_on_new_domain=1645460202_MDJlNWU5MDVhMmYw&source_impression_id=p3_1645461268_jxnf6JF4LiYEjqYh&check_in=2022-12-21&guests=1&adults=1&check_out=2022-12-22'
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("no_sandbox")
        driver = webdriver.Chrome(executable_path='/home/pomilusky/Escriptori/Ironhack/chromedriver',chrome_options=options)
        driver.get(url)
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[3]/section/div[2]/div[2]/button').click()
        a =driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/span[1]').text
        driver.quit()
        return int(a[1:])
    except: 
        driver.quit()
        return np.nan # If we can' acces the url we are going to give it a np.nan value

df1['price_now'] = df1.listing_url.apply(scrap_price)
df1.to_csv('../Data/ambPriceNow.csv',mode='w', index=False, header=True)

print('Portem 1000')
df2['price_now'] = df2.listing_url.apply(scrap_price)
df2.to_csv('../Data/ambPriceNow.csv',mode='a', index=False, header=False)

df3['price_now'] = df3.listing_url.apply(scrap_price)
df3.to_csv('../Data/ambPriceNow.csv',mode='a', index=False, header=False)
# Let's do the same with the test,

df_test = pd.read_csv('../Data/test.csv')
df_test['price_now'] = df_test.listing_url.apply(scrap_price)
df_test.to_csv('../Data/TestAmbPriceNow.csv', mode='w', index=False, header=True)