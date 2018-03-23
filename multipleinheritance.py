class Father():
    def skill(self):
        print("gardening")


class Mother():
    def skill(self):
        print("cooking")


class Child(Father, Mother):
    def skill(self):
        Father.skill(self)
        Mother.skill(self)
        print("sports")

c=Child()
c.skill()