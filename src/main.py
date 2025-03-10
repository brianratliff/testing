from textnode import TextType, TextNode
from htmlnode import HTMLNode


def main():
    # tn = TextNode('This is a text node', TextType.BOLD, 'https://www.boot.dev')
    # print(tn)
    hnb = HTMLNode('b', 'bold this text')
    print(hnb)

    # tag, value, children, props
    hn = HTMLNode('a', 'click here to search', props={'href': 'https://www.google.com', 'target': '_blank'})
    print(hn)

if __name__ == '__main__':
    main()

