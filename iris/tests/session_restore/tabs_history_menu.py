# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self):
        BaseTest.__init__(self)
        self.meta = 'All recently closed tabs can be reopened from the history menu'
        self.test_case_id = '117178'
        self.test_suite_id = '68'
        self.locales = ['en-US']

    def run(self):
        local_url = [LocalWeb.FIREFOX_TEST_SITE, LocalWeb.FIREFOX_TEST_SITE_2, LocalWeb.FOCUS_TEST_SITE,
                     LocalWeb.FOCUS_TEST_SITE_2, LocalWeb.MOZILLA_TEST_SITE, LocalWeb.POCKET_TEST_SITE]
        website_image_pattern = [LocalWeb.FIREFOX_LOGO, LocalWeb.FIREFOX_LOGO, LocalWeb.FOCUS_LOGO,
                                   LocalWeb.FOCUS_LOGO, LocalWeb.MOZILLA_LOGO, LocalWeb.POCKET_LOGO]
        history_menu_bar_pattern = Pattern('history_menu_bar.png')
        recently_closed_pattern = Pattern('recently_closed_tabs.png')
        tabs_list_pattern = Pattern('tabs_list.png')
        restore_tabs_pattern = Pattern('restore_all_tabs_button.png')

        for _ in range(6):
            new_tab()
            navigate(local_url[_])
            website_loaded = exists(website_image_pattern[_], 20)
            assert_true(self, website_loaded,
                        'Website {0} loaded'
                        .format(_+1))
        [close_tab() for _ in range(5)]
        one_tab_exists = exists(website_image_pattern[0], 20)
        assert_true(self, one_tab_exists,
                    'One opened tab left. All 5 tabs were successfully closed.')
        type(Key.ALT)
        history_menu_bar_exists = exists(history_menu_bar_pattern, 20)
        assert_true(self, history_menu_bar_exists,
                    'History menu bar is visible.')
        click(history_menu_bar_pattern, 0.2)
        recently_closed_menu = exists(recently_closed_pattern, 20)
        assert_true(self, recently_closed_menu,
                    'Recently Closed Tabs option exists.')
        hover(recently_closed_pattern, 0.2)  # hover doesn't open popup list
        click(recently_closed_pattern)
        tabs_list_exists = exists(tabs_list_pattern, 20)
        assert_true(self, tabs_list_exists,
                    'Previously Opened Tabs list exists.')
        click(restore_tabs_pattern, 0.2)
        #  check if all tabs reopened correctly
        tabs_count = len(website_image_pattern)
        for _ in range(6):
            if len(website_image_pattern) == 1:
                one_tab_left = exists(website_image_pattern[0], 20)
                assert_true(self, one_tab_left,
                            'All {0} tabs were successfully reopened.'
                            .format(tabs_count - 1))
            else:
                tab_exists = exists(website_image_pattern.pop())
                assert_true(self, tab_exists,
                            'Tab {0} successfully reopened.'
                            .format(tabs_count - _))
                previous_tab()
