from time import sleep

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_open_base_page(page, base_url):
    base_page = BasePage(page, base_url)
    base_page.goto()
    sleep(1)


def test_add_to_cart(page, base_url):
    home_page = HomePage(page, base_url)
    home_page.open()
    home_page.go_to_products()

    product_page = ProductPage(page, base_url)
    product_page.wait_loaded()
    product_page.add_to_cart_by_id(3)

    sleep(3)
