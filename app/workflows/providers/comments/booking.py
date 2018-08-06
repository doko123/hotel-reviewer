import uuid

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from config.selenium import SeleniumSetup


class HotelScrapper:
    homepage = None
    provider = None
    reviews = []
    hotel_title = None
    hotel_location_title = None
    delay = 4  # timeout in seconds

    def __init__(self, hotel_name, location):
        self.selenium_setup = SeleniumSetup()
        self.driver = self.selenium_setup.driver
        self.hotel_name = hotel_name
        self.location = location

    def scrape(self):
        self.driver.get(self.homepage)
        self.driver.set_page_load_timeout(20)


class TrivagoScrapper(HotelScrapper):
    homepage = "https://trivago.com"
    provider = "trivago"

    # TODO: Use regex to find Reviews element by link or partial link
    def scrape(self):

        write_hotel_and_name_loc = self.driver.find_element_by_xpath(
            '//*[@id="horus-querytext"]'
        )
        write_hotel_and_name_loc.send_keys(
            "{} {}".format(self.hotel_name, self.location)
        )

        search_button = self.driver.find_element_by_xpath(
            '//*[@id="js-fullscreen-hero"]/div/form/div/div[1]'
            "/div/div/div[2]/button"
        )
        search_button.click()

        hotel_path = self.driver.find_element_by_xpath(
            "//*[@class = 'name__copytext m-0 item__slideout-toggle']"
        )
        self.driver.execute_script("arguments[0].click();", hotel_path)

        hotel_reviews_path = self.driver.find_element_by_name("Reviews")
        self.driver.execute_script("arguments[0].click();", hotel_reviews_path)

        comments = self.driver.find_elements_by_xpath(
            '//*[@class="sl-review__summary  sl-review__'
            'summary--ltr m-0 w-100 fl-leading"]'
        )

        for comment in comments:
            comment = {
                "id": self.provider,
                "comment": comment.get_attribute("innerText"),
            }
            self.comments.append(comment)


class BookingScrapper(HotelScrapper):
    homepage = "https://booking.com"
    provider = "booking"

    def scrape(self):
        super().scrape()
        # enter search data

        try:
            hotel_name_and_loc = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="ss"]'))
            )
        except TimeoutException:
            self.selenium_setup.tear_down()
            return

        hotel_name_and_loc.send_keys(
            "{} {}".format(self.hotel_name, self.location)
        )

        # find 'search' button
        try:
            search_button = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="frm"]/div[1]/div[4]/div[2]/button')
                )
            )
        except TimeoutException:
            self.selenium_setup.tear_down()
            return
        self.driver.execute_script("arguments[0].click();", search_button)

        # get first match
        exact_hotel_xpath = (
            '//*[@id="hotellist_inner"]/div[1]/table/tbody/tr[1]/'
            "td[2]/h3/a/span[1]"
        )
        self.hotel_location_title = self.driver.find_element_by_xpath(
            '//*[@id="ss"]'
        ).get_attribute("value")
        try:
            hotel_name = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.XPATH, exact_hotel_xpath))
            )
        except TimeoutException:
            self.selenium_setup.tear_down()
            return
        self.driver.execute_script("arguments[0].click();", hotel_name)

        # switch to new window
        self.driver.switch_to.window(self.driver.window_handles[-1])

        self.hotel_title = self.driver.find_element_by_xpath(
            '//*[@id="hp_hotel_name"]'
        ).get_attribute("innerText")

        # find 'Guest rating button
        try:
            reviews = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.ID, "show_reviews_tab"))
            )
        except TimeoutException:
            self.selenium_setup.tear_down()
            return
        self.driver.execute_script("arguments[0].click();", reviews)

        sort_by_date = Select(self.driver.find_element_by_xpath(
            '//*[@id="review_sort"]'
        ))
        sort_by_date.select_by_value("f_recent_desc")

        self._extract_comments()

        self.selenium_setup.tear_down()

    def _extract_comments(self):

        positive_reviews = self.driver.find_elements_by_class_name(
            "review_pos "
        )
        negative_reviews = self.driver.find_elements_by_class_name(
            "review_neg "
        )

        for p_review, n_review in zip(positive_reviews, negative_reviews):

            comment = f"{self._format(p_review)} {self._format(n_review)}"
            self.reviews.append(
                {"id": f"{self.provider}_{uuid.uuid4()}", "text": comment}
            )
        return self.reviews

    def _format(self, review):
        return (
            review.get_attribute("innerText")
            .replace("\n", "")
            .replace("눉", "")
            .replace("눇", "")
        )
