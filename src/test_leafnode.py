import unittest
from leafnode import LeafNode
from htmlnode import HTMLNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_value(self):
        node = LeafNode('span', 'Hello, World!', props={'class': 'greeting'})
        expected_output = '<span class="greeting">Hello, World!</span>'
        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_no_tag(self):
        node = LeafNode(value='No Tag')
        expected_output = 'No Tag'
        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_without_value(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode('span', props={'class': 'greeting'})
            node.to_html()

if __name__ == "__main__":
    unittest.main()