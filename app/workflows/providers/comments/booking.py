import uuid

from config.selenium import SeleniumSetup


class HotelScrapper:
    homepage = None
    provider = None

    def __init__(self, hotel_name, location):
        self.driver = SeleniumSetup().driver
        self.hotel_name = hotel_name
        self.location = location
        self.reviews = []

    def scrape(self):
        self.driver.get(self.homepage)
        self.driver.set_page_load_timeout(20)


class TrivagoScrapper(HotelScrapper):
    homepage = "https://trivago.com"
    provider = "trivago"

    # TODO: Use regex to find Reviews element ny link or partial link
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
        hotel_name_and_loc = self.driver.find_element_by_xpath('//*[@id="ss"]')
        hotel_name_and_loc.send_keys(
            "{} {}".format(self.hotel_name, self.location)
        )

        # find 'search' button
        search_button = self.driver.find_element_by_class_name(
            "sb-searchbox__button  "
        )
        search_button.click()  # click that button

        # get first match
        exact_hotel_xpath = (
            '//*[@id="hotellist_inner"]/div[1]/table/tbody/tr[1]/'
            "td[2]/h3/a/span[1]"
        )
        hotel_name = self.driver.find_element_by_xpath(exact_hotel_xpath)
        hotel_name.click()

        # switch to new window
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # find 'Guest rating button
        reviews = self.driver.find_element_by_id("show_reviews_tab")
        reviews.click()

        self._extract_comments()

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
                {"id": f"{self.provider}_{uuid.uuid4()}", "comment": comment}
            )
        return self.reviews

    def _format(self, review):
        return review.get_attribute("innerText")[2:]
