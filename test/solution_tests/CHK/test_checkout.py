from unittest import TestCase

from accelerate_runner.lib.solutions.CHK.checkout_solution import checkout


class TestCheckout(TestCase):
    def test_checkout_r2_basic_deals(self):
        assert checkout('AAA') == 130
        assert checkout('AAAA') == 180
        assert checkout('AAAAA') == 200
        assert checkout('AAAAAA') == 250
        assert checkout('AAAAAAAAAA') == 400
