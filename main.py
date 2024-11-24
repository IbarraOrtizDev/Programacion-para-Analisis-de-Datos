from queue import Full
from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=option)
    driver.get("https://listado.mercadolibre.com.co/194252707166")
    time.sleep(5)
    ## document.querySelector(".product__list").getElementsByClassName("product__item")
    products = driver.find_elements(By.CSS_SELECTOR, ".shops__layout-item")
    print(f"Products: {len(products)}")
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
        print(f"Title: {title} - Price: {price} - Marca: {marca} - Imagen: {imagenProducto}, Link: {linkProduct}, Rating: {rating}")

    driver.quit()

def queryData(prod, selector, name):
    try:
        return prod.find_element(selector, name)
    except:
        return None

if __name__ == "__main__":
    main()
