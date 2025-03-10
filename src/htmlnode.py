
class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('this code has not been implemented yet')

    def props_to_html(self):
        output_list = []
        for k, v in self.props.items():
            output = '%s="%s"' % (k, v)
            output_list.append(output)
        return ' '.join(output_list)

    def __repr__(self):
        output_string = 'HTMLNode:'
        # tag
        if self.tag:
            output_string += '\n\t' + self.tag
        # value
        if self.value:
            output_string += '\n\t' + self.value
        # children
        if self.children:
            output_string += '\n\tChildren:'
            for child in self.children:
                output_string += '\n\t\t%r' % str(child)
        # props
        if self.props:
            output_string += '\n\tProperties:'
            for k, v in self.props.items():
                output_string += '\n\t\t"%s" = "%s"' % (k, v)
        return output_string
