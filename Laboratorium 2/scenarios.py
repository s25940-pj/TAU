from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class XKomSearchTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.x-kom.pl")
        self.driver.maximize_window()

    def test_accept_cookies_and_search(self):
        driver = self.driver
        

        try:
            cookies_banner = driver.find_element(By.XPATH, "//*[@role='dialog']")
            self.assertTrue(cookies_banner.is_displayed(), "Cookies consent banner is not displayed.")
            accept_button = cookies_banner.find_element(By.XPATH, ".//button[@data-name='AcceptPermissionButton']")
            self.assertTrue(accept_button.is_displayed(), "Accept button on the cookies banner is not displayed.")
            accept_button.click()
            time.sleep(2)
        except:
            print("Cookies consent banner is not available or was already accepted.")


        search_box = driver.find_element(By.CLASS_NAME, "parts__Input-sc-60750d44-0")
        self.assertTrue(search_box.is_displayed(), "Search box is not visible.")
        self.assertTrue(search_box.is_enabled(), "Search box is not enabled.")


        search_query = "laptop"
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        

        time.sleep(4)
        

        search_results_section = driver.find_element(By.ID, "listing-container")
        self.assertTrue(search_results_section.is_displayed(), "Search results section is not displayed.")


        search_results = driver.find_elements(By.CLASS_NAME, "parts__ProductListCol-sc-a93b49f9-1")
        self.assertGreater(len(search_results), 0, "No search results were found.")
        

        for i, result in enumerate(search_results[:5]):
            description = result.text
            self.assertIn("zł", description.lower(), f"Price tag is not present in search result description {i}.")


        for i, result in enumerate(search_results[:5]):
            description = result.text
            self.assertTrue(description != None, f"Description is not displayed for result {i + 1}.")


        pagination_next_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div/a")
        pages_total_number = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div/span[2]").text.split(' ')[1])
        self.assertTrue(pagination_next_button.is_enabled() and pages_total_number > 1, "Pagination is not available for multiple pages of results.")

    def tearDown(self):

        self.driver.quit()


class AmazonSearchTest(unittest.TestCase):
    
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.amazon.com")
        self.driver.maximize_window()

    def test_search_functionality(self):
        driver = self.driver
        

        search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
        self.assertTrue(search_bar.is_displayed(), "Search bar is not displayed.")
        self.assertTrue(search_bar.is_enabled(), "Search bar is not enabled.")
        

        search_query = "laptop"
        search_bar.send_keys(search_query)
        search_bar.send_keys(Keys.RETURN)


        time.sleep(2)


        results_section = driver.find_element(By.ID, "search")
        self.assertTrue(results_section.is_displayed(), "Results page is not displayed.")
        

        search_results = driver.find_elements(By.XPATH, "//div[contains(@class, 's-result-item') and @data-component-type='s-search-result']")
        self.assertGreater(len(search_results), 0, "No search results were found.")
        

        for i, result in enumerate(search_results[:5]):
            title = result.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
            self.assertTrue(title.is_displayed(), f"Result {i+1} does not have a title.")
            self.assertGreater(len(title.text), 0, f"Result {i+1} has an empty title.")
        

        for i, result in enumerate(search_results[:5]):
            try:
                price = result.find_element(By.XPATH, ".//span[@class='a-price']")
                self.assertTrue(price.is_displayed(), f"Result {i+1} does not display a price.")
            except:
                print(f"Result {i+1} does not have a price.")


        sort_dropdown = driver.find_element(By.ID, "s-result-sort-select")
        self.assertTrue(sort_dropdown.is_displayed(), "Sort by dropdown is not displayed.")
        self.assertTrue(sort_dropdown.is_enabled(), "Sort by dropdown is not enabled.")

    def tearDown(self):
        self.driver.quit()
        

class YouTubeSearchTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.youtube.com")
        self.driver.maximize_window()

    def test_search_and_filters(self):
        driver = self.driver
        

        try:
            cookie_banner = driver.find_element(By.XPATH, "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button")
            self.assertTrue(cookie_banner.is_displayed(), "Cookie consent banner is not displayed.")
            cookie_banner.click()
            time.sleep(2) 
        except:
            print("Cookie consent banner is not available or was already accepted.")
            

        search_bar = driver.find_element(By.NAME, "search_query")
        self.assertTrue(search_bar.is_displayed(), "Search bar is not displayed.")
        self.assertTrue(search_bar.is_enabled(), "Search bar is not enabled.")
        

        search_query = "Python tutorials"
        search_bar.send_keys(search_query)
        search_bar.send_keys(Keys.RETURN)
        

        time.sleep(4)
        

        results_section = driver.find_element(By.CLASS_NAME, "ytd-two-column-search-results-renderer")
        self.assertTrue(results_section.is_displayed(), "Search results page is not displayed.")
        

        search_results = driver.find_elements(By.ID, "video-title")
        self.assertGreater(len(search_results), 0, "No search results were found.")
        

        first_result_title = search_results[0].get_attribute("title")
        self.assertIn("Python", first_result_title, "Search query is not found in the first result title.")
        

        filter_button = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/div/ytd-search-header-renderer/div[3]/ytd-button-renderer/yt-button-shape/button")
        self.assertTrue(filter_button.is_displayed(), "Filter button is not displayed.")
        self.assertTrue(filter_button.is_enabled(), "Filter button is not enabled.")
        

        filter_button.click()
        time.sleep(2)
        upload_date_filter = driver.find_element(By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer[1]/a")
        self.assertTrue(upload_date_filter.is_displayed(), "Upload date filter is not displayed.")
        upload_date_filter.click()
        time.sleep(4)
        
        updated_results = driver.find_elements(By.ID, "video-title")
        self.assertGreater(len(updated_results), 0, "No results found after applying filter.")

    def tearDown(self):
        self.driver.quit()


class EbaySearchTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.ebay.com")
        self.driver.maximize_window()

    def test_filters_and_sorting(self):
        driver = self.driver
    
        search_bar = driver.find_element(By.ID, "gh-ac")
        self.assertTrue(search_bar.is_displayed(), "Search bar is not displayed.")
        self.assertTrue(search_bar.is_enabled(), "Search bar is not enabled.")
        
        search_query = "laptop"
        search_bar.send_keys(search_query)
        search_bar.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        results_section = driver.find_element(By.ID, "srp-river-results")
        self.assertTrue(results_section.is_displayed(), "Search results page is not displayed.")
        
        search_results = driver.find_elements(By.CLASS_NAME, "s-item")
        self.assertGreater(len(search_results), 0, "No search results were found.")
        
        brand_filter = driver.find_elements(By.CLASS_NAME, "x-refine__item__title-container")[7]
        self.assertTrue(brand_filter.is_displayed(), "Brand filter is not displayed.")
        brand_filter.click()
        time.sleep(1)
        
        dell_filter = driver.find_element(By.XPATH, "//span[text()='Dell']")
        self.assertTrue(dell_filter.is_displayed(), "Dell filter is not displayed.")
        dell_filter.click()
        time.sleep(2)
        
        updated_results = driver.find_elements(By.CLASS_NAME, "s-item")
        self.assertGreater(len(updated_results), 0, "No results found after applying filter.")
        
        sort_dropdown = driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div[1]/div[2]/div[2]/div[3]/div[1]/div/span/button")
        self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown is not displayed.")
        sort_dropdown.click()
        lowest_price_option = driver.find_element(By.XPATH, "//span[text()='Price + Shipping: lowest first']")
        self.assertTrue(lowest_price_option.is_displayed(), "Sort option is not displayed.")
        lowest_price_option.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
