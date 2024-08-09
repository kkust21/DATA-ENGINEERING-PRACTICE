class Salary:
    #s_allowance = {"HRA": 0.4, "DA": 0.3, "TA": 0.15}
    #s_deduction = {"PF": 0.5, "Insurance": 5000}
    def __init__(self, basic):
        self.basic = basic
    def getbasic(self):
        print("basic", self.basic)



class Allowance(Salary):
    s_allowance = {"HRA": 0.4, "DA": 0.3, "TA": 0.15}

    def getallowance(self):
        total_allowance = 0
        for key in self.s_allowance:
            total_allowance += self.s_allowance[key] * self.basic
        return total_allowance;


class Deduction(Salary):
    def getDeduction(basic):
        s_deduction = {"PF": 0.5, "Insurance": 5000}
        total_deduction = 0
        for key in s_deduction:
            if type(s_deduction[key]) is not int:
                total_deduction += s_deduction[key] * basic
            else:
                total_deduction += s_deduction[key]
        return total_deduction


class Calsalary(Allowance, Deduction):
    def sal(self):
        super().getbasic()
        print("basic sal:",self.basic)

        super().getDeduction()

        gsal =  super().getbasic() + super().getallowance()
        p_tax = self.pTax(gsal)
        nsal = gsal - super().getDeduction(self.basic) - p_tax

        print("basic allowance", self.basic)
        print("Allowance", super().getallowance())
        print("deduction", super().getDeduction(self.basic))
        print("profTax", p_tax)
        print("gross sal", gsal)
        print("net salary", nsal)

        def pTax(mSal):
            prof_tax = 0
            if mSal >= 8500 and mSal <= 10000:
                prof_tax = 200
            elif mSal > 10000 and mSal <= 30000:
                prof_tax = 300
            elif mSal > 30000:
                prof_tax = 500
            return prof_tax



    """"
    def pTax(mSal):
        prof_tax = 0
        if mSal >= 8500 and mSal <= 10000:
            prof_tax = 200
        elif mSal > 10000 and mSal <= 30000:
            prof_tax = 300
        elif mSal > 30000:
            prof_tax = 500
        return prof_tax

    def sal():
        bsal = int(input("enrter the salary", ))
        gsal = bsal + calAllowance()
        p_tax = pTax(gsal)
        nsal = gsal - calDeduction(bsal) - p_tax
        print("basic allowance", bsal)
        print("Allowance", calAllowance())
        print("deduction", calDeduction(bsal))
        print("profTax", p_tax)
        print("gross sal", gsal)
        print("net salary", nsal)

    sal()"""


s1 = Calsalary(2000)
s1.sal()
