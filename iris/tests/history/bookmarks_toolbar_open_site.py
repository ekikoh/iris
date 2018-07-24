# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self, app):
        BaseTest.__init__(self, app)
        self.meta = 'Copy a website from the History sidebar and paste it to the Bookmarks toolbar, then open it.'

    def setup(self):
        """Test case setup

        This overrides the setup method in the BaseTest class, so that it can use a brand new profile.
        """
        BaseTest.setup(self)
        self.profile = Profile.BRAND_NEW
        return

    def run(self):
        search_history_box = 'search_history_box.png'
        expand_button_history_sidebar = 'expand_button_history_sidebar.png'
        view_bookmarks_toolbar = 'view_bookmarks_toolbar.png'
        toolbar_enabled = 'toolbar_is_active.png'
        bookmarks_toolbar_mozilla = 'bookmarks_toolbar_mozilla.png'

        # Open a page to create some history.
        new_tab()
        navigate(LocalWeb.MOZILLA_TEST_SITE)
        expected_1 = exists(LocalWeb.MOZILLA_LOGO, 10)
        assert_true(self, expected_1, 'Mozilla page loaded successfully.')
        close_tab()

        # Open the Bookmarks toolbar.
        access_bookmarking_tools(view_bookmarks_toolbar)
        expected_2 = exists(toolbar_enabled, 10)
        assert_true(self, expected_2, 'Bookmarks Toolbar has been activated.')

        # Open the History sidebar.
        history_sidebar()
        expected_3 = exists(search_history_box, 10)
        assert_true(self, expected_3, 'Sidebar was opened successfully.')
        expected_4 = exists(expand_button_history_sidebar, 10)
        assert_true(self, expected_4, 'Expand history button displayed properly.')
        click(expand_button_history_sidebar)

        # Copy a website from the History sidebar and paste it to the Bookmarks toolbar.
        expected_5 = exists(LocalWeb.MOZILLA_BOOKMARK_SMALL, 10)
        assert_true(self, expected_5, 'Mozilla page is displayed in the History list successfully.')

        right_click(LocalWeb.MOZILLA_BOOKMARK_SMALL)
        type(text='c')
        history_sidebar()
        right_click(toolbar_enabled)
        type(text='p')
        if Settings.is_mac():
            expected_6 = exists(bookmarks_toolbar_mozilla)
        else:
            expected_6 = exists(LocalWeb.MOZILLA_BOOKMARK_SMALL)
        assert_true(self, expected_6, 'Mozilla page was copied successfully to the Bookmarks toolbar.')

        # Open the site from the bookmarks toolbar
        if Settings.is_mac():
            click(bookmarks_toolbar_mozilla)
        else:
            click(LocalWeb.MOZILLA_BOOKMARK_SMALL)
        expected_7 = exists(LocalWeb.MOZILLA_LOGO, 10)
        assert_true(self, expected_7, 'Mozilla page loaded successfully.')