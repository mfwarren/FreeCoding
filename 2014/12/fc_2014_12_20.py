import unittest
import string


class PythonTest(unittest.TestCase):

    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEARDOWN")

    def test_first(self):
        print("TESTING")


class Default(dict):
    def __missing__(self, key):
        return key


class StringTests(unittest.TestCase):

    def test_two(self):
        print("TEST TWO")

    def test_digits(self):
        assert(string.digits == '0123456789')

    def test_positional_format(self):
        self.assertEqual('{} - {}'.format('a', 'b'), 'a - b')

    def test_capwords(self):
        self.assertEqual(string.capwords('matt warren is cool'), 'Matt Warren Is Cool')
        self.assertEqual(string.capwords('matt,warren,is cool', ','), 'Matt,Warren,Is cool')

    def test_capitalization(self):
        self.assertEqual('title'.capitalize(), 'Title')
        self.assertEqual('Title'.casefold(), 'title')
        self.assertEqual('Title'.lower(), 'title')
        self.assertEqual('ß'.casefold(), 'ss')
        self.assertEqual('a'.center(9), '    a    ')
        self.assertEqual('matt warren is cool'.title(), 'Matt Warren Is Cool')

    def test_formatting(self):
        self.assertEqual('aaaba'.count('a'), 4)
        self.assertEqual('abc\n'.encode('utf-8'), b'abc\n')
        self.assertEqual('\t\tasdf'.expandtabs(tabsize=2), '    asdf')
        self.assertEqual(' \t asdf \t'.strip(), 'asdf')

        class Default(dict):
            def __missing__(self, key):
                return key

        self.assertEqual('{name} lives in {country}'.format_map(Default(name="Matt")), 'Matt lives in country')

    def test_checks(self):
        self.assertTrue('asdf'.isalpha())
        self.assertTrue('1234'.isnumeric())
        self.assertTrue('1234asdf'.isalnum())

    def test_join(self):
        self.assertEqual(' '.join(['1', '2', '3']), '1 2 3')

    def test_split(self):
        self.assertEqual('asdf asdf'.split(' '), ['asdf', 'asdf'])
        self.assertEqual('asdf'.partition('d'), ('as', 'd', 'f'))

    def test_find(self):
        self.assertEqual('asdfasdf'.find('f'), 3)
        self.assertEqual('asdfasdf'.rfind('a'), 4)
        self.assertTrue('asdf'.endswith('df'))
        self.assertTrue('asdf'.startswith('as'))

if __name__ == '__main__':
    unittest.main()
