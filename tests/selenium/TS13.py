from BaseTest import BaseTest
from selenium.webdriver.common.by import By
import logging

class TS13(BaseTest):
    def test_edit_passwords(self):
        logging.info("=============================================")
        logging.info("Test TS13: Edit password")
        logging.info("=============================================")
        self.openurl("http://localhost/spravce/public/login.php")
        self.fill_text("user_name","DonS")
        self.fill_text("password","P.lb.45_?1!")
        self.click_button("input[type='submit']", "none")
        self.check_url("http://localhost/spravce/public/dashboard.php")
        self.click_menu_link("Show all password")
        self.check_url("http://localhost/spravce/public/view_services.php")
        self.edit("edit")
        self.check_url_contains("edit_service.php")
        self.fill_text("updated_service_name","spartapraha")
        self.fill_text("updated_service_user_name","DonSalieri")
        self.fill_text("updated_service_user_password","mistrligy")
        self.click_button("input[type='submit']", "none")
        self.check_url("http://localhost/spravce/public/view_services.php")
        self.verify_changes("spartapraha","DonSalieri","mistrligy")
       
 


        
        
if __name__ == "__main__":
    import unittest
    unittest.main()