# quark.py

class Quark(object):
    def flip(self): # this is a method that alters flavor of quark via weak
    #interaction while retaining symmetry; check example_quark.py
        if self.flavor == "up":
            self.flavor = "down"
        elif self.flavor == "down":
            self.flavor = "up"
        elif self.flavor == "top":
            self.flavor = "bottom"
        elif self.flavor == "bottom":
            self.flavor = "top"
        elif self.flavor == "strange":
            self.flavor = "charm"
        elif self.flavor == "charm":
            self.flavor = "strange"
        else :
            raise AttributeError("The quark cannot be flipped, because the "
                             "flavor is not valid.")