from selenium import webdriver

class infow():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path="")


    def get_info(self,query):
        self.query=query
        self.driver.get(url("https://www.youtube.com"))
        search=self.driver.find_element_by_xpath(" ")
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element_by_xpath(" ")
        enter.click()

assit=infow()
assit.get.info("hello")        