from nose import SkipTest

from tests.gsuite_tests import get_driver, check_recover_objects

driver = get_driver('spreadsheet')


# noinspection PyClassHasNoInit
class TestSheetsParser:
    def test___init__(self):
        # sheets_parser = SheetsHandler(client, KumoObj, delimiter)
        raise SkipTest  # TODO: implement your test here

    def test_get_comments(self):
        # sheets_parser = SheetsHandler(client, KumoObj, delimiter)
        # assert_equal(expected, sheets_parser.get_comments(file_choice))
        raise SkipTest  # TODO: implement your test here

    def test_get_log(self):
        # sheets_parser = SheetsHandler(client, KumoObj, delimiter)
        # assert_equal(expected, sheets_parser.get_log(start, end, choice))
        raise SkipTest  # TODO: implement your test here

    def test_parse_log(self):
        # sheets_parser = SheetsHandler(client, KumoObj, delimiter)
        # assert_equal(expected, sheets_parser.parse_log(c_log))
        raise SkipTest  # TODO: implement your test here

    def test_parse_snapshot(self):
        # sheets_parser = SheetsHandler(client, KumoObj, delimiter)
        # assert_equal(expected, sheets_parser.parse_snapshot(snapshot))
        raise SkipTest  # TODO: implement your test here

    def test_recover_objects(self):
        check_recover_objects(driver)
