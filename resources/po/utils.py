from playwright.sync_api import sync_playwright


class Utils:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
        self.submitButton = "button[id='submit']"
        self.url = "https://demoqa.com/text-box"

    def initialize_playwright(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def go_to_site(self):
        self.page.goto(self.url)

    def fill_the_input(self, selector, value):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    def close_browser(self):
        self.browser.close()

    def click_value(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def get_text_for_locator(self, selector):
        self.page.wait_for_selector(selector)
        element_text = self.page.locator(selector).first.text_content()
        return element_text

    def click_submit_button(self):
        self.page.wait_for_selector(self.submitButton)
        self.click_value(self.submitButton)