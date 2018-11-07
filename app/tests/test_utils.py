import unittest
from app.utils import *


class TestUtils(unittest.TestCase):

    def test_is_ju_diphthong(self):
        self.assertTrue(is_diphthong('ju'))

    def test_is_aɪ_diphthong(self):
        self.assertTrue(is_diphthong('aɪ'))

    def test_is_æ_diphthong(self):
        self.assertFalse(is_diphthong('æ'))

    def test_is_ɪ_diphthong(self):
        self.assertFalse(is_diphthong('ɪ'))

    def test_get_possible_diphthongs_for_ɪ(self):
        self.assertEqual(set(['ɔɪ', 'eɪ', 'aɪ']), set(get_possible_diphthongs('ɪ')))

    def test_get_possible_diphthongs_for_ʊ(self):
        self.assertEqual(set(['aʊ', 'oʊ']), set(get_possible_diphthongs('ʊ')))

    def test_get_possible_diphthongs_for_ʌ(self):
        self.assertEqual(set([]), set(get_possible_diphthongs('ʌ')))

    def test_find_occurrences_for_ɪ(self):
        self.assertEqual([2, 6], get_occurrences("/bɪˈhaɪnd/", 'ɪ'))

    def test_find_occurrences_for_ʌ(self):
        self.assertEqual([], get_occurrences("/bɪˈhaɪnd/", 'ʌ'))

    def test_get_diphthong_for_behind(self):
        self.assertEqual('bɪ', get_diphthong('/bɪˈhaɪnd/', 'ɪ', 2))

    def test_get_diphthong_for_behind_second_occurrence(self):
        self.assertEqual('aɪ', get_diphthong('/bɪˈhaɪnd/', 'ɪ', 6))

    def test_has_diphthong_for_behind(self):
        self.assertTrue(has_diphthong('ɪ', '/bɪˈhaɪnd/'))

    def test_has_diphthong_for_famous(self):
        self.assertTrue(has_diphthong('ɪ', '/ˈfeɪ.məs/'))

    def test_has_diphthong_for_brown(self):
        self.assertTrue(has_diphthong('a', '/braʊn/'))

    def test_has_diphthong_for_brown_with_ipa_ʊ(self):
        self.assertTrue(has_diphthong('ʊ', '/braʊn/'))

    def test_has_diphthong_for_which(self):
        self.assertFalse(has_diphthong('ɪ', '/wɪtʃ/'))
