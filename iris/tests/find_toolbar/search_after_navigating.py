# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self):
        BaseTest.__init__(self)
        self.meta = 'Search again after navigating to another page'
        self.test_case_id = 'C127264'
        self.test_suite_id = '2085'
        self.locales = ['en-US']

    def run(self):

        find_toolbar_pattern = Pattern('find_toolbar_text.png')

        page_title_pattern = Pattern('page_title_search_navigate.png')

        word_browser_green_pattern = Pattern('word_browser_green.png')

        link_load_listener_pattern = Pattern('link_load_listener.png')
        navigate_load_listener_page_title_pattern = Pattern('navigate_page_title.png')
        word_browser_in_find_bar_pattern = Pattern('word_browser_in_find_bar.png')

        phrase_not_found_label_pattern = Pattern('phrase_not_found_label.png')

        tabbed_browser_page_local = self.get_asset_path('page_1.htm')

        navigate(tabbed_browser_page_local)
        page_title_pattern_exists = exists(page_title_pattern, 5)

        assert_true(self, page_title_pattern_exists, 'The page is successfully loaded.')

        open_find()

        # Remove all text from the Find Toolbar
        edit_select_all()
        edit_delete()

        find_toolbar_is_opened = wait(find_toolbar_pattern, 5)

        assert_true(self, find_toolbar_is_opened, 'The Find Toolbar is successfully displayed '
                                                  'by pressing CTRL + F / Cmd + F.')

        type('browser')
        type(Key.ENTER)

        word_browser_green_exists = exists(word_browser_green_pattern, 5)

        assert_true(self, word_browser_green_exists, 'The items corresponding to "browser" are found.')

        exists(link_load_listener_pattern, 10)
        click(link_load_listener_pattern, 1)

        navigate_to_page_loaded = exists(navigate_load_listener_page_title_pattern, 10)

        assert_true(self, navigate_to_page_loaded, 'The browser navigated to the clicked link.')

        click(word_browser_in_find_bar_pattern, 1)
        type(Key.ENTER)

        # Linux needs extra Key.ENTER to pass a test
        if Settings.get_os() == Platform.LINUX:
            type(Key.ENTER)

        phrase_not_found_label_exists = exists(phrase_not_found_label_pattern, 2)

        assert_true(self, phrase_not_found_label_exists, 'No visible issue of the highlighted items are present.')
