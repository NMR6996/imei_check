from core.models import Phones
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Command(BaseCommand):
    help = 'Send Mail to Users'

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome()

    def handle(self, *args, **kwargs):
        self.refresh_property()

    def check_status_func(self, imei):
        self.driver.get("https://portal.rinn.az/az/imei-check-service")
        assert "Portalı" in self.driver.title
        elem = self.driver.find_element(By.ID, "imeiCheck")
        elem.clear()
        elem.send_keys(imei)
        elem.send_keys(Keys.RETURN)
        wait = WebDriverWait(self.driver, 10)
        popup_element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "imei-check-service__modal-description")))
        information = popup_element.text
        return information

    @staticmethod
    def check_status(status):
        if "keçib" in status:
            return "Qeydiyyatdan keçib!"
        elif "keçirilməyib" in status:
            return "Qedyiyyatdan keçirilməyib!"
        return status

    def refresh_property(self):
        for phone in Phones.objects.filter(status="Qedyiyyatdan keçirilməyib!"):
            status = self.check_status_func(imei=phone.imei)
            phone.status = self.check_status(status=status)
            phone.save()
