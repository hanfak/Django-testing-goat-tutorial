from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Han has heard about a cool new online to-do app. He goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He types "Buy peacock feathers" into a text box (Han's hobby
        # is tying fly-fishing lures)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # There is still a text box inviting him to add another item. He
        # enters "Use peacock feathers to make a fly" (Han is very methodical)
        # The page updates again, and now shows both items on his list
        self.fail('Finish the test!')


        # Han wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for his -- there is some
        # explanatory text to that effect.

        # He visits that URL - his to-do list is still there.

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
