# Проверка наличия кнопки добавления в корзину на странице товара
def test_presence_add_cart_button_diff_languages(browser):
    url = 'http://selenium1py.pythonanywhere.com//catalogue/coders-at-work_206/'
    browser.get(url)
    add_to_cart_button_elements = browser.find_elements_by_css_selector('.btn-add-to-basket')
    count_add_to_cart_button_elements = len(add_to_cart_button_elements)
    # для assert выбрано сравнение на равенство с единицей, а не > 0, т.к. если элементов будет больше, чем один,
    # то с тестом что-то не так, он должен упасть
    assert count_add_to_cart_button_elements == 1, 'Кнопка добавления в корзину отсутстует на странице товара (либо ' \
                                                   'кнопок больше, чем 1) '
