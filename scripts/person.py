class Person:

    def __init__(self, first, last, weight, height):
        "init method runs everytime we create a new instance"
        self.first = first
        self.last = last
        self.weight = weight
        self.height = height

    @property
    def email(self):
        return "{}.{}@st.hanze.nl".format(self.first[0], self.last).lower()

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @property
    def bmi(self):
        return (self.weight / ((self.height / 100) ** 2))
