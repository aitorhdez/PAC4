import unittest
import utils.utils as utils


class TestOrfMatchPattern(unittest.TestCase):

    def test_orf_match_pattern(self):

        orf_desc = "this is my orf description my13charsWord"
        self.assertTrue(utils.orf_match_pattern(orf_desc, "", -1))
        self.assertTrue(utils.orf_match_pattern(orf_desc, "orf", -1))
        self.assertTrue(utils.orf_match_pattern(orf_desc, "chars", 13))
        self.assertTrue(utils.orf_match_pattern(orf_desc, "descr", 11))

        self.assertFalse(utils.orf_match_pattern(orf_desc, "", 1))
        self.assertFalse(utils.orf_match_pattern(orf_desc, "orfs", -1))
        self.assertFalse(utils.orf_match_pattern(orf_desc, "chars", 12))
        self.assertFalse(utils.orf_match_pattern(orf_desc, "chars", 14))


class TestGet_matching_dimension(unittest.TestCase):

    def test_get_matching_dimension(self):
        classes = [("2,1,1,2", ""), ("1,2,1,1", ""), ("2,1,1,1", ""),
                   ("1,3,1,1", ""), ("0,1,1,1", "")]
        self.assertEqual(utils.get_matching_dimension(classes, 1), 5)
        self.assertEqual(utils.get_matching_dimension(classes, 2), 3)
        self.assertEqual(utils.get_matching_dimension(classes, 3), 1)