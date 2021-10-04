# Проверка наличия кнопки добавления в корзину на странице товара
def test_presence_add_cart_button_diff_languages(browser):
    url = 'http://selenium1py.pythonanywhere.com//catalogue/coders-at-work_207/'
    browser.get(url)
    add_to_cart_button_elements = browser.find_elements_by_css_selector('.btn-add-to-basket')
    count_add_to_cart_button_elements = len(add_to_cart_button_elements)
    assert count_add_to_cart_button_elements == 1
