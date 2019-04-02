import requests
import httpretty
import unittest

from loremipsum import generate_paragraph

from utils import source


class SourceTest(unittest.TestCase):
    @httpretty.activate
    def test_get_source(self):
        end = generate_paragraph()[2]

        httpretty.register_uri(
            httpretty.GET,
            "https://word-search-engine.jorgechato.com",
            body=end
        )

        result = source.get_source("https://word-search-engine.jorgechato.com")

        self.assertEqual(end, result, msg="Objects should be equals")

    def test_strict_search_one(self):
        text = "this is a text with only one -word word."

        self.assertEqual(
            1,
            source.strict_search("word", text),
            msg="Objects should be equals"
        )

    def test_strict_search_multiple(self):
        text = "this is word text is a text with multiple word words."

        self.assertEqual(
            2,
            source.strict_search("word", text),
            msg="Objects should be equals"
        )

    def test_flex_search_one(self):
        text = "this is a text with only one text -word."

        self.assertEqual(
            1,
            source.flex_search("word", ["-", "<"], text),
            msg="Objects should be equals"
        )

    def test_flex_search_multiple(self):
        text = "this is text word- text is a text with multiple text words. <word"

        self.assertEqual(
            2,
            source.flex_search("word", ["-", "<"], text),
            msg="Objects should be equals"
        )


if __name__ == '__main__':
    unittest.main()
