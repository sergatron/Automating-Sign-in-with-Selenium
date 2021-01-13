
from time import sleep
from selenium import webdriver
import datetime as dt


def convert_date(date_str):
    """
    Takes date string in format mm/dd/yyyy and outputs date string
    in the format mm/dd/yyyy
    """

    dt_format = dt.datetime.strptime(date_str, '%m-%d-%Y')

    return dt_format.strftime('%m/%d/%Y')


# username_input = sys.argv[1]
# password_input = sys.argv[2]


# Get user inputs
print(' --- Please Enter Credentials --- ')
username_input = input("Enter username:")
password_input = input('Enter password:')

start_date_input = convert_date(input("Enter start date (mm-dd-yyyy):"))
end_date_input = convert_date(input("Enter end date (mm-dd-yyyy):"))


# insert path to the chromedriver
# OR; add Chromdriver to same directory as Python script
driver = webdriver.Chrome()


print('Navigating to URL...')
url = "https://www.e-zpassny.com/vector/account/home/accountLogin.do?locale=en_US&from=Home"
# open URL
driver.get(url)

sleep(2)

# find username and password on the form
user_xpath = '//*[@id="templatecontent"]/div/form/span/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[4]/input'
username = driver.find_element_by_xpath(user_xpath)

pswd_xpath = '//*[@id="templatecontent"]/div/form/span/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td[4]/input'
password = driver.find_element_by_xpath(pswd_xpath)


username.send_keys(username_input)
sleep(1)
password.send_keys(password_input)
sleep(1)

# Logon Button
print('Logging in...')
logon_xpath = '//*[@id="btnLogin"]'
logon_button = driver.find_element_by_xpath(logon_xpath)
logon_button.click()

sleep(3)

# navigate to
# --> transactions
# --> transaction view
driver.find_element_by_xpath('//*[@id="menu"]/ul/li[10]/a').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="menu"]/ul/li[12]/a').click()
sleep(1)


# start/end date Xpath
start_date = driver.find_element_by_name('startDateAll')
end_date = driver.find_element_by_name('endDateAll')

# clear form inputs
start_date.clear()
end_date.clear()
# find and send dates into form
start_date.send_keys(start_date_input)
end_date.send_keys(end_date_input)
sleep(1)

# click button to get transactions
print('Getting transactions for specified dates...')
search_button = driver.find_element_by_xpath('//*[@id="btnSearch"]')
search_button.click()
sleep(2)

# Select file type for download (PDF)
driver.find_element_by_xpath(
    '//*[@id="templatecontent"]/div/form/span/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]/table/tbody/tr/td[1]/select/option[1]'
).click()
sleep(1)

# Download
print('Downloading PDF...')
download_button = driver.find_element_by_xpath(
    '//*[@id="templatecontent"]/div/form/span/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]/table/tbody/tr/td[2]/a/img'
)
download_button.click()
print('Download complete! Exiting browser ...')
sleep(5)

driver.quit()
