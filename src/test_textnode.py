import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url(self):
        url = 'https://www.boot.dev'
        node = TextNode('This is a text node', TextType.IMAGE, url)
        self.assertEqual(url, node.url)

    def test_url_none(self):
        node = TextNode('This is a text node', TextType.BOLD)
        self.assertEqual(node.url, None)








if __name__ == "__main__":
    unittest.main()
