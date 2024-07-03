import pytest
from resources.po.utils import Utils
from resources.po.textbox import Textbox

@pytest.fixture(scope="module")
def utils():
    utils_instance = Utils()
    utils_instance.initialize_playwright()
    yield utils_instance
    utils_instance.close_browser()

@pytest.fixture
def textbox(utils):
    return Textbox(utils)

def test_verify_textbox(textbox, utils):
    utils.go_to_site()

    textbox.fill_the_username("selimerdinc")
    textbox.fill_the_email("selimerdinc@selimerdinc.com")
    textbox.fill_current_address("Selim Erdinç")
    textbox.fill_permanent_address("Selim Erdinç")

    utils.click_submit_button()

    text = textbox.verify_output()
    print(text)

    assert "Name:selimerdinc" in text
    assert "Email:selimerdinc@selimerdinc.com" in text
    assert "Current Address :Selim Erdinç " in text
    assert "Permananet Address :Selim Erdinç" in text