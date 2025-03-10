import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    # tag, value, children, props
    def test_eq(self):
        node = HTMLNode('a')
        with self.assertRaises(NotImplementedError) as context:
            node.to_html()

    def test_not_eq(self):
        node = HTMLNode('a', value='none')
        node2 = HTMLNode('a', value='different value')
        self.assertNotEqual(node, node2)

    def test_url(self):
        url = 'https://www.boot.dev'
        node = HTMLNode('a', props={'href': url})
        self.assertEqual(url, node.props['href'])








if __name__ == "__main__":
    unittest.main()
