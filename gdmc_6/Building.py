class Building:
    def __init__(self, size):
        self.size = size
        self.area = size[0]*size[2]
        self.clearable=True
        self.name='building'

    def build(self,editor,leftBackBottomPoint) -> None:
        raise NotImplementedError()

