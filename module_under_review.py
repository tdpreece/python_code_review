class C:
    @property
    def y(self):
        0/0

hasattr(C(), "y")
