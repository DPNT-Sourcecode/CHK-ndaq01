from solutions.CHK.checkout_solution import checkout


class TestCheckout():
    def test_illegal_input(self):
        assert checkout('-') == -1

    def test_checkout_r2_basic_deals(self):
        assert checkout('AAA') == 130
        assert checkout('AAAA') == 180
        assert checkout('AAAAA') == 200
        assert checkout('AAAAAA') == 250
        assert checkout('AAAAAAAA') == 330
        assert checkout('AAAAAAAAA') == 380
        assert checkout('AAAAAAAAAA') == 400

    def test_checkout_r2_free_B(self):
        assert checkout('EE') == 80
        assert checkout('EEB') == 80
        assert checkout('EEBB') == 110
        assert checkout('EEBBB') == 125

    def test_checkout_r2_combined(self):
        assert checkout('AAAAAEEBAAABB') == 455





