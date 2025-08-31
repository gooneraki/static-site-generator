class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return (
            " "
            + " ".join(list(map(lambda x: f'{x[0]}="{x[1]}"', self.props.items())))
            + " "
            if self.props is not None
            else ""
        )

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Missing value for LeafNode")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag for ParentNode")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Missing children for ParentNode")
        return f"<{self.tag}{self.props_to_html()}>{
            ('\n').join(list(map(lambda x: x.to_html()  ,self.children)))
        }</{self.tag}>"
