import random

class Element:
    def __init__(self, eid="", name="") -> None:
        self._eid = eid
        self.name = name

    @property
    def eid(self):
        return self._eid if random.random() > 0.5 else None

    def click(self):
        print(f"{self} Clicked")

    def input(self, text):
        print(f"{self} Input {text=}")


class App:
    def __init__(self, *e):
        self.page = [*e]

    def find(self, eid="", name=""):
        # Your code goes here
        return Element(eid=eid, name=name)
        # pass


def te_find_element():
    app = App(
        Element(eid="tv_phone"),
        Element(name="btn_login"),
    )
    phone = app.find(eid="tv_phone")
    phone.input("13912345678")

    login = app.find(name="btn_login")
    login.click()
    print("done")

te_find_element()