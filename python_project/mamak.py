from selenium import webdriver

def birinci_durum():
    browser = webdriver.Chrome("chromedriver.exe")
    browser.minimize_window()
    browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=100&a20=38470&a24_min=50")

    i = 1
    ortalama = 0

    while (i <= 14):
        try:
            if(i!=4 and i!=5):
                browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=100&a20=38470&a24_min=50")

                button = browser.find_element_by_xpath("//*[@id='searchResultsTable']/tbody/tr[" + str(i) + "]")
                button.click()

                fiyat = browser.find_element_by_xpath("//*[@id='classifiedDetail']/div/div[2]/div[2]/h3").text
                fiyat = str(fiyat)
                fiyat = fiyat.replace(" TL", "")
                fiyat = fiyat.replace(".", "")
                ortalama += int(fiyat)
                #print(ortalama)
                i += 1

            else:
                i+=1

        except:
            pass

    browser.quit()
    return int(ortalama/13)

def ikinci_durum():
    browser = webdriver.Chrome("chromedriver.exe")
    browser.minimize_window()
    browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=150&a20=38470&a24_min=100")

    i = 1
    ortalama = 0

    while (i <= 14):
        try:
            if(i!=3 and i!=5):
                browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=150&a20=38470&a24_min=100")

                button = browser.find_element_by_xpath("//*[@id='searchResultsTable']/tbody/tr[" + str(i) + "]")
                button.click()

                fiyat = browser.find_element_by_xpath("//*[@id='classifiedDetail']/div/div[2]/div[2]/h3").text
                fiyat = str(fiyat)
                fiyat = fiyat.replace(" TL", "")
                fiyat = fiyat.replace(".", "")
                ortalama += int(fiyat)
                #print(ortalama)
                i += 1

            else:
                i+=1

        except:
            pass

    browser.quit()
    return int(ortalama/13)

def ucuncu_durum():
    browser = webdriver.Chrome("chromedriver.exe")
    browser.minimize_window()
    browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=200&a20=38470&a24_min=150")

    i = 1
    ortalama = 0

    while (i <= 6):
        try:
            if(i!=4):
                browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=200&a20=38470&a24_min=150")

                button = browser.find_element_by_xpath("//*[@id='searchResultsTable']/tbody/tr[" + str(i) + "]")
                button.click()

                fiyat = browser.find_element_by_xpath("//*[@id='classifiedDetail']/div/div[2]/div[2]/h3").text
                fiyat = str(fiyat)
                fiyat = fiyat.replace(" TL", "")
                fiyat = fiyat.replace(".", "")
                ortalama += int(fiyat)
                #print(ortalama)
                i += 1

        except:
            pass

    browser.quit()
    return int(ortalama/5)

def dorduncu_durum():
    browser = webdriver.Chrome("chromedriver.exe")
    browser.minimize_window()
    browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=100&a20=38474&a24_min=50")

    i = 1
    ortalama = 0

    while (i <= 14):
        try:
            if(i!=4):
                browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=100&a20=38474&a24_min=50")

                button = browser.find_element_by_xpath("//*[@id='searchResultsTable']/tbody/tr[" + str(i) + "]")
                button.click()

                fiyat = browser.find_element_by_xpath("//*[@id='classifiedDetail']/div/div[2]/div[2]/h3").text
                fiyat = str(fiyat)
                fiyat = fiyat.replace(" TL", "")
                fiyat = fiyat.replace(".", "")
                ortalama += int(fiyat)
                #print(ortalama)
                i += 1

            else:
                i+=1

        except:
            pass

    browser.quit()
    return int(ortalama/13)

def besinci_durum():
    browser = webdriver.Chrome("chromedriver.exe")
    browser.minimize_window()
    browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=150&a20=38474&a24_min=100")

    i = 1
    ortalama = 0

    while (i <= 14):
        try:
            if(i!=4 and i!=12):
                browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=150&a20=38474&a24_min=100")

                button = browser.find_element_by_xpath("//*[@id='searchResultsTable']/tbody/tr[" + str(i) + "]")
                button.click()

                fiyat = browser.find_element_by_xpath("//*[@id='classifiedDetail']/div/div[2]/div[2]/h3").text
                fiyat = str(fiyat)
                fiyat = fiyat.replace(" TL", "")
                fiyat = fiyat.replace(".", "")
                ortalama += int(fiyat)
                #print(ortalama)
                i += 1

            else:
                i+=1

        except:
            pass

    browser.quit()
    return int(ortalama/13)

def altinci_durum():
    browser = webdriver.Chrome("chromedriver.exe")
    browser.minimize_window()
    browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=200&a20=38474&a24_min=150")

    i = 1
    ortalama = 0

    while (i <= 14):
        try:
            if(i!=2 and i!=5):
                browser.get("https://www.sahibinden.com/satilik-daire/ankara-mamak?a24_max=200&a20=38474&a24_min=150")

                button = browser.find_element_by_xpath("//*[@id='searchResultsTable']/tbody/tr[" + str(i) + "]")
                button.click()

                fiyat = browser.find_element_by_xpath("//*[@id='classifiedDetail']/div/div[2]/div[2]/h3").text
                fiyat = str(fiyat)
                fiyat = fiyat.replace(" TL", "")
                fiyat = fiyat.replace(".", "")
                ortalama += int(fiyat)
                #print(ortalama)
                i += 1

            else:
                i+=1

        except:
            pass

    browser.quit()
    return int(ortalama/13)