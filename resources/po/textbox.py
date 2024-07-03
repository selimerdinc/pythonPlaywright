from resources.po.utils import Utils


class Textbox:
    def __init__(self, utils: Utils):
        self.utils = utils
        self.usernameSelector = "input[id='userName']"
        self.userEmailSelector = "input[id='userEmail']"
        self.currentAddressSelector = "textarea[id='currentAddress']"
        self.permanentAddressSelector = "textarea[id='permanentAddress']"
        self.username = "p[id='name']"
        self.email = "p[id='email']"
        self.currentAddress = "p[id='currentAddress']"
        self.permanentAddress = "p[id='permanentAddress']"

    def fill_the_username(self, text):
        self.utils.fill_the_input(self.usernameSelector, text)

    def fill_the_email(self, text):
        self.utils.fill_the_input(self.userEmailSelector, text)

    def fill_current_address(self, text):
        self.utils.fill_the_input(self.currentAddressSelector, text)

    def fill_permanent_address(self, text):
        self.utils.fill_the_input(self.permanentAddressSelector, text)

    def verify_output(self,):
        username = self.utils.get_text_for_locator(self.username)
        email = self.utils.get_text_for_locator(self.email)
        currentAddress = self.utils.get_text_for_locator(self.currentAddress)
        permanentAddress = self.utils.get_text_for_locator(self.permanentAddress)
        return username,email,currentAddress,permanentAddress
