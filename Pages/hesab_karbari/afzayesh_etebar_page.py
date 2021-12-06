import time
from Base.basepage import BasePage


class afzayeshEtebarPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # locators
    _avatar_ =              "//img[@alt='rom']"
    _hesab_karbari_man =    "//a[@href='/a/account']"
    _afzayesh_etebar =      "//a[contains(text(),'افزایش اعتبار')]"
    _dropdown_price =       "//select[@name='sku']"
    _dropdown_250HT =       "//select[@name='sku']/option[4]"      #dropdown = _dropdown_250HT.selectByIndex(2);
    _edame_price =          "//button[@type='submit']"
    _edame_adreshayeshoma = "//button[@type='submit']"
    _codtakhfif_textfield = "//input[@placeholder='کد تخفیف را وارد کنید']"
    _baresi_emal_codtakhfif ="//a[contains(text(),'بررسی')]"
    _cod_takhfif_errorMessage = "//span[contains(text(),'کد تخفیف نامعتبر است.')]"


    # actions
    def clickOnAvatar(self):
        self.elementClick(self._avatar_,locatorType="xpath")
    def clickOnHesabKarbari(self):
        self.elementClick(self._hesab_karbari_man,locatorType="xpath")
    def clickOnAfzayeshEtebar(self):
        self.elementClick(self._afzayesh_etebar,locatorType="xpath")
    def clickOnPriceDropdown(self):
        self.elementClick(self._dropdown_price,locatorType="xpath")
    def choosePriceFromDropdown(self):
        self.elementClick(self._dropdown_250HT,locatorType="xpath")
    def confirmChosenPrice_edame(self):
        self.elementClick(self._edame_price,locatorType="xpath")
    def confirmChosenAddress_edame(self):
        self.elementClick(self._edame_adreshayeshoma,locatorType="xpath")
    def enterCodTakhrif(self, cod):
        self.sendKeys(cod ,self._codtakhfif_textfield,locatorType="xpath")
    def clickOnEmalCodTakhfif(self):
        self.elementClick(self._baresi_emal_codtakhfif, locatorType="xpath")



    def afzayeshEtebar_with_codtakhfif(self, cod=""):
        self.clickOnAvatar()
        self.clickOnHesabKarbari()
        self.clickOnAfzayeshEtebar()

        parentHandel = self.driver.current_window_handle
        allhandles = self.driver.window_handles
        for handle in allhandles:
            print(handle)
            if handle not in parentHandel:
                self.driver.switch_to.window(handle)

                self.clickOnPriceDropdown()
                self.choosePriceFromDropdown()
                self.confirmChosenPrice_edame()
                self.confirmChosenAddress_edame()
                self.enterCodTakhrif(cod)
                self.clickOnEmalCodTakhfif()

                self.driver.close()
                break

        self.driver.switch_to.window(parentHandel)






    #def verify_faile_afzayeshetebar(self):
