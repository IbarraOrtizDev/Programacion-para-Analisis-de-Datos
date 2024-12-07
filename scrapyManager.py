from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def queryData(prod, selector, name):
    try:
        element = prod.find_element(selector, name)
        return element
    except:
        return None

def queryEanAlkomprar(codEan):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(f"https://www.alkosto.com/search?text={codEan}")
    time.sleep(5)
    products = driver.find_elements(By.CSS_SELECTOR, ".product__list .product__item")
    datos = []
    print("Productos encontrados: ", len(products))
    for product in products:
        title_element = queryData(product, By.CSS_SELECTOR, ".product__item__top__title")
        title = title_element.text if title_element else None
        price_element = queryData(product, By.CSS_SELECTOR, ".price")
        price = price_element.text if price_element else None
        marca_element = queryData(product, By.CSS_SELECTOR, ".product__item__top__brand")
        marca = marca_element.text if marca_element else None
        imagenProducto_element = queryData(product, By.TAG_NAME, "img")
        imagenProducto = imagenProducto_element.get_attribute("src") if imagenProducto_element else None
        rating_element = queryData(product, By.CSS_SELECTOR, ".averageNumber")
        rating = rating_element.text if rating_element else None
        linkProduct_element = queryData(product, By.CSS_SELECTOR, ".product__item__top__link")
        linkProduct = linkProduct_element.get_attribute("href") if linkProduct_element else None
        
        datos.append({
            "title": title,
            "price": price,
            "marca": marca,
            "imagenProducto": imagenProducto,
            "rating": rating,
            "linkProduct": linkProduct,
            "store": "Alkomprar",
            "ean": codEan
        })

    driver.quit()
    return datos


def queryEanMercadoLibre(codEan):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(f"https://listado.mercadolibre.com.co/{codEan}")
    time.sleep(5)
    products = driver.find_elements(By.CSS_SELECTOR, ".shops__layout-item")
    datos = []
    print("Productos encontrados: ", len(products))
    for product in products:
        title_element = queryData(prod=product, selector= By.CSS_SELECTOR, name=".poly-component__title")
        title = title_element if title_element is None else title_element.text
        price_element = queryData(prod= queryData(prod=product, selector= By.CSS_SELECTOR, name=".poly-price__current"), selector= By.CSS_SELECTOR, name=".andes-money-amount__fraction")
        price = price_element if price_element is None else price_element.text
        marca = ""
        linkProduct_element = queryData(prod=product, selector= By.TAG_NAME, name="a")
        linkProduct = linkProduct_element if linkProduct_element is None else linkProduct_element.get_attribute("href")
        imagenProducto_element= queryData(prod=product, selector= By.TAG_NAME, name="img")
        imagenProducto = imagenProducto_element if imagenProducto_element is None else imagenProducto_element.get_attribute("src")
        rating_element = queryData(prod=product, selector= By.CSS_SELECTOR, name=".poly-reviews__rating")
        rating = rating_element if rating_element is None else rating_element.text
        
        datos.append({
            "title": title,
            "price": price,
            "marca": marca,
            "imagenProducto": imagenProducto,
            "rating": rating,
            "linkProduct": linkProduct,
            "store": "MercadoLibre",
            "ean": codEan
        })

    driver.quit()
    return datos