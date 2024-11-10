from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class XKomSearchTest(unittest.TestCase):
    
    def setUp(self):
        # Initialize the driver and open x-kom.pl
        self.driver = webdriver.Chrome()  # Can use Firefox or Edge
        self.driver.get("https://www.x-kom.pl")
        self.driver.maximize_window()

    def test_accept_cookies_and_search(self):
        driver = self.driver
        
        # Check if the cookie consent banner is displayed and accept it if present
        try:
            cookies_banner = driver.find_element(By.XPATH, "//*[@role='dialog']")
            self.assertTrue(cookies_banner.is_displayed(), "Cookies consent banner is not displayed.")
            accept_button = cookies_banner.find_element(By.XPATH, ".//button[@data-name='AcceptPermissionButton']")
            self.assertTrue(accept_button.is_displayed(), "Accept button on the cookies banner is not displayed.")
            accept_button.click()
            time.sleep(1)  # Give time for the banner to close
        except:
            print("Cookies consent banner is not available or was already accepted.")

        # Verify that the search box is displayed and enabled
        search_box = driver.find_element(By.CLASS_NAME, "parts__Input-sc-60750d44-0")
        self.assertTrue(search_box.is_displayed(), "Search box is not visible.")
        self.assertTrue(search_box.is_enabled(), "Search box is not enabled.")

        # Perform a search query
        search_query = "laptop"
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for search results to load
        time.sleep(2)
        
        # Verify that the search results section is displayed
        search_results_section = driver.find_element(By.ID, "listing-container")
        self.assertTrue(search_results_section.is_displayed(), "Search results section is not displayed.")

        # Check that there are results for the search query
        search_results = driver.find_elements(By.CLASS_NAME, "parts__ProductListCol-sc-a93b49f9-1")
        self.assertGreater(len(search_results), 0, "No search results were found.")
        
        # Verify that the first 5 results contain the search query in the product title
        for i, result in enumerate(search_results[:5]):
            product_name = result.text.split('\n')[0]
            self.assertIn(search_query.lower(), product_name.lower(), f"Search query '{search_query}' not found in result {i + 1}: '{product_name}'.")

        # Verify the presence of a price label in the search results
        for i, result in enumerate(search_results[:5]):
            price_label = result.find_element(By.XPATH, '//*[@id="listing-container"]/div[1]/div/div[2]/div[3]/div[1]/div[2]/span')
            self.assertTrue(price_label.is_displayed(), f"Price label not displayed for result {i + 1}.")

        # Verify that pagination is available if there are more than one page of results
        pagination = driver.find_elements(By.CLASS_NAME, "pagination-item")
        self.assertTrue(len(pagination) > 0, "Pagination is not available for multiple pages of results.")

    def tearDown(self):
        # Close the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
