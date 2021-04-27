class Mycomplex:
    def __init__(self,a,b):
        self.one = '3-4i'
        self.two = '-5+2i'

    def multi(self,one, two):
        self.one = '3-4i'
        self.two = '-5+2i'
        if "-" in self.one:
            new_one = one.split("-")
            a = int(new_one[0])
            b = int(new_one[1][0])
        if "+" in self.two:
            new_two = two.split("+")
            c = int(new_two[0])
            d = int(new_two[1][0])
        cal_result1 = (a*c) + abs(b*d)
        cal_result2 = (a*d) + (-b*c)
        result = str(cal_result1) +"+" + str(cal_result2) + "i"
        return result



obj = Mycomplex( '3-4i','-5+2i')
print(obj.multi( '3-4i','-5+2i' ))