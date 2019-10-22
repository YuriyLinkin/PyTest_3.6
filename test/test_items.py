import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_add_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    print("\nfinding AddToBasket button..")
    assert True, browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
