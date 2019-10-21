from unittest import TestCase

from polish import reverse_polish


class TestReverse_polish(TestCase):
    def test_reverse_polish_0(self):
        res = reverse_polish(-1, [2, 3, '+'])
        print(res)
        assert res == 5

    def test_reverse_polish_1(self):
        res = reverse_polish(-1, [2, 2, 2, '+', '*'])
        print(res)
        assert res == 8

    def test_reverse_polish_2(self):
        res = reverse_polish(-1, [3, 2, 1, '+', '*'])
        print(res)
        assert res == 9

    def test_reverse_polish_3(self):
        res = reverse_polish(-1, [3, 2, '+', 1, 3, '+', '*'])
        print(res)
        assert res == 20

    def test_reverse_polish_4(self):
        res = reverse_polish(-1, [10, 5, '<', 5, 14, '?'])
        print(res)
        assert res == 14

    def test_reverse_polish_5(self):
        res = reverse_polish(-1, [5, 10, '<', 5, 14, '?'])
        print(res)
        assert res == 5

    def test_reverse_polish_6(self):
        res = reverse_polish(-1, [5, 14, '-'])
        print(res)
        assert res == -9
