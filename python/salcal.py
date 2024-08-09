s_allowance = {"HRA":0.4,"DA":0.3,"TA":0.15}
s_deduction = {"PF":0.5,"Insurance":5000}

def calAllowance(basic):
    total_allowance =0;
    for key in s_allowance:
        total_allowance+=s_allowance[key]*basic;
    return total_allowance;
def calDeduction(basic):
    total_deduction=0
    for key in s_deduction:
        if type(s_deduction[key]) is not int:
            total_deduction+=s_deduction[key]*basic
        else:
            total_deduction+=s_deduction[key]
    return total_deduction
def pTax(mSal):
    prof_tax=0
    if mSal >=8500 and mSal<=10000:
        prof_tax=200
    elif mSal>10000 and mSal<=30000:
        prof_tax=300
    elif mSal > 30000:
        prof_tax=500
    return prof_tax

def sal():
    bsal = int(input("enrter the salary",))
    gsal=bsal+calAllowance(bsal)
    p_tax = pTax(gsal)
    nsal=gsal-calDeduction(bsal)-p_tax
    print("basic allowance",bsal)
    print("Allowance",calAllowance(bsal))
    print("deduction",calDeduction(bsal))
    print("profTax",p_tax)
    print("gross sal",gsal)
    print("net salary",nsal)
sal()

