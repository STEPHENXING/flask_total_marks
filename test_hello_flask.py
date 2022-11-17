from unittest import TestCase

import hello_flask


class Test(TestCase):
    def test_get_total_calc(self):
        # self.fail()
        ret = hello_flask.get_total_calc(["0", "1", "2"])
        assert ret == 3
        ret = hello_flask.get_total_calc([])
        assert ret == 0
        ret = hello_flask.get_total_calc(["0", "1", "a"])
        assert ret == 1





