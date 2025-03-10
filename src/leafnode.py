from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError('leaf nodes must have a value')
        if self.tag == None:
            return self.value
        output_string = f'<{self.tag}'
        if self.props:
            output_string += ' '
            for k, v in self.props.items():
                output_string += '%s="%s"' % (k, v)
        output_string += f'>{self.value}</{self.tag}>'
        return output_string
