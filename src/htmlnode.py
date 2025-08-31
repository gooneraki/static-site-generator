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
