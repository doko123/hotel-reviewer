from selenium import webdriver
import time


def hotel_scrapper(hotel_name, location):
    negatives = []  # container for negative comments
    positives = []  # container for possitive comments
    execute_time = time.time()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(20)
    driver.get("https://booking.com")

    write_hotel_name_and_loc = driver.find_element_by_xpath(
        '//*[@id="ss"]'
    )  # find field to type data
    write_hotel_name_and_loc.send_keys(
        "{} {}".format(hotel_name, location)
    )  # type data

    search_button = driver.find_element_by_class_name(
        "sb-searchbox__button  "
    )  # find 'search' button
    search_button.click()  # click that button

    hotel_name_path = driver.find_element_by_xpath(
        '//*[@id="hotellist_inner"]/div[1]/div[2]/div[1]/div[1]/h3/a '
    )
    # get first match
    hotel_name_path.click()

    time.sleep(3)  # wait for open and load new windowecho "" > .gitignore
    driver.switch_to.window(driver.window_handles[-1])  # switch to new window

    element = driver.find_element_by_id(
        "show_reviews_tab"
    )  # find 'Guest rating button
    element.click()

    time.sleep(3)
    negs = driver.find_elements_by_class_name(
        "review_neg "
    )  # find all negative comments
    time.sleep(5)
    negatives = [
        each_neg.get_attribute("innerText")[4:] for each_neg in negs
    ]  # get negatives

    pos = driver.find_elements_by_class_name(
        "review_pos "
    )  # find all positive comments
    positives = [
        each_pos.get_attribute("innerText")[4:] for each_pos in pos
    ]  # get positives

    full_comment = [
        {"comment": "{}{}".format(pos, neg)}
        for pos, neg in zip(positives, negatives)
    ]  # create json
    driver.quit()
    print(full_comment)  # zamień na return! \/ usuń.
    print("--- %s seconds ---" % (time.time() - execute_time))
