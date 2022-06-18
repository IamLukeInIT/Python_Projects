from selenium import webdriver

#enter the website
browser = webdriver.Edge()
browser.get('webiste')
def create():
        #login, xpath from devtools
        python_button = browser.find_elements_by_xpath("//*[@id='username']")[0]
        python_button.send_keys('*********')
        python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
        python_button.send_keys('*********')
        python_button = browser.find_elements_by_xpath("//*[@id='loginHasloForm']/div[2]/input[4]")[0]
        python_button.click() #login button
        
        #downloads files
        python_button = browser.find_elements_by_xpath("//*[@id='portlet_announcementportlet_WAR_nnkportlet']/div[2]/div/div/div/div/div[3]/a")[0]
        python_button.click()
        
if __name__ == "__main__":
    create()
