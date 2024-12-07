from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from . import sqlAdmin as sql
from . import sqlString as ut
from . import helpers as hp

def queryData(prod, selector, name):
    try:
        element = prod.find_element(selector, name)
        return element.text if element else None
    except:
        return None

def queryData2(prod, selector, name):
    try:
        element = prod.find_element(selector, name)
        return element
    except:
        return None
    
def upDefaultWebdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def queryDataAttr(prod, selector, name, attr):
    try:
        element = prod.find_element(selector, name)
        return element.get_attribute(attr) if element else None
    except:
        return None

def queryEanAlkomprar(codEan):
    sqlManager = dataQuery()
    dataAlkomprar = sqlManager.query_data(ut.selectDataLastOneDayByStore, (codEan, "Alkomprar"))

    if (len(dataAlkomprar) != 0) :
        return hp.arrayJsonResponse(dataAlkomprar)

    driver = upDefaultWebdriver()
    driver.get(f"https://www.alkosto.com/search?text={codEan}")
    time.sleep(5)
    products = driver.find_elements(By.CSS_SELECTOR, ".product__list .product__item")
    datos = []
    print("Productos encontrados: ", len(products))
    for product in products:
        title = queryData(product, By.CSS_SELECTOR, ".product__item__top__title")
        price = queryData(product, By.CSS_SELECTOR, ".price")
        marca = queryData(product, By.CSS_SELECTOR, ".product__item__top__brand")
        imagenProducto = queryDataAttr(product, By.TAG_NAME, "img", "src")
        rating = queryData(product, By.CSS_SELECTOR, ".averageNumber")
        linkProduct = queryDataAttr(product, By.CSS_SELECTOR, ".product__item__top__link", "href")

        datos.append(hp.jsonResponse([None,title, price.replace("$", ""), marca, imagenProducto, rating, linkProduct, "Alkomprar", codEan]))

    driver.quit()
    saveData(datos)
    return datos


def queryEanMercadoLibre(codEan):
    sqlManager = dataQuery()
    dataMerCadoLibre = sqlManager.query_data(ut.selectDataLastOneDayByStore, (codEan, "MercadoLibre"))

    if (len(dataMerCadoLibre) != 0) :
        return hp.arrayJsonResponse(dataMerCadoLibre)
    
    driver = upDefaultWebdriver()
    driver.get(f"https://listado.mercadolibre.com.co/{codEan}")
    time.sleep(5)
    products = driver.find_elements(By.CSS_SELECTOR, ".shops__layout-item")
    datos = []
    print("Productos encontrados: ", len(products))
    for product in products:
        title =  queryData(prod=product, selector= By.CSS_SELECTOR, name=".poly-component__title")
        price = queryData(prod= queryData(prod=product, selector= By.CSS_SELECTOR, name=".poly-price__current"), selector= By.CSS_SELECTOR, name=".andes-money-amount__fraction")
        marca = ""
        rating = queryData(prod=product, selector= By.CSS_SELECTOR, name=".poly-reviews__rating")


        linkProduct_element = queryData2(prod=product, selector= By.TAG_NAME, name="a")
        linkProduct = linkProduct_element if linkProduct_element is None else linkProduct_element.get_attribute("href")
        imagenProducto_element= queryData2(prod=product, selector= By.TAG_NAME, name="img")
        imagenProducto = imagenProducto_element if imagenProducto_element is None else imagenProducto_element.get_attribute("src")
        
        datos.append(hp.jsonResponse([None,title, price, marca, imagenProducto, rating, linkProduct, "MercadoLibre", codEan]))

    driver.quit()
    saveData(datos)
    return datos


def queryEan(codEan):
    queryEanMercadoLibre(codEan)
    queryEanAlkomprar(codEan)
    sqlManager = dataQuery()

    data = sqlManager.query_data(ut.selectDataString, (codEan,))
    sqlManager.close()
    resp = hp.arrayJsonResponse(data)
    return resp

def dataQuery():
    sqlManager = sql.SqlManager("dataQuery.db")
    sqlManager.connect()
    sqlManager.create_table(ut.createTableString)
    return sqlManager

def saveData(arrayDic):
    sqlManager = dataQuery()
    for item in arrayDic:
        sqlManager.insert_data(ut.insertDataString, (item["title"], item["price"], item["marca"], item["imagenProducto"], item["rating"], item["linkProduct"], item["store"], item["ean"]))
    sqlManager.close()
    return "Data saved"