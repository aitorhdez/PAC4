import unittest
import parser.parseClasses as parser


class TestParseFunction(unittest.TestCase):

    def test_parse_function(self):

        # Comprovem que parsegem correctament cada paràmetre de la linia
        line = "function(tb501,[1,1,1,0],'galE1',\"UDP-glucose 4-epimerase\")."
        self.assertEqual(parser.parse_function(line)[0], "tb501")
        self.assertEqual(parser.parse_function(line)[1], "1,1,1,0")
        self.assertEqual(parser.parse_function(line)[2], "galE1")
        self.assertEqual(parser.parse_function(line)[3], "UDP-glucose 4-epimerase")


class TestParseClass(unittest.TestCase):

    def test_parse_class(self):
        # Comprovem que parsegem correctament cada paràmetre de la linia
        line = "class([1,0,0,0],\"Small-molecule metabolism \")"
        self.assertEqual(parser.parse_class(line)[0], "1,0,0,0")
        self.assertEqual(parser.parse_class(line)[1], "Small-molecule metabolism")
