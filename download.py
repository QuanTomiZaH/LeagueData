import selenium
import selenium.webdriver
import time


def download():
    root_url = 'https://www.rotowire.com/esports/stats-lol.php'

    print('Opening web browser')
    driver = selenium.webdriver.Chrome()
    print('\tDone')

    print('Retrieving initial web page')
    driver.get(root_url)
    print('sleeping')
    time.sleep(3)
    driver.find_element_by_xpath("//button[id ='value']")
    <button class="export-button is-csv"><img alt="CSV" src="https://content.rotowire.com/images/export-csv.png">CSV</button>
    driver.find_element_by_link_text("CSV").click()
    print('\tDone')


# the main sequence to enact
def main():
    download()


# excecute the program
if __name__ == '__main__':
    main()