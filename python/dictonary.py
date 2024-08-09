stocks = {"TCS":3000,"infosys":4000,"SBI":1700,"HDFC":400}
stocks["IDFC"]:7000
print("dic",type(stocks),stocks)
print("keys",stocks.keys())
print("values",stocks.values())
for i in stocks:
    print("stocks",stocks,stocks[i])
for key,value in stocks.items():
    print("key", key,"value",value)

stocks.pop("TCS")
print("poped item",stocks)
stocks.popitem()#delets last element
print(stocks)
#swapping key value
swapped ={}
for key,value in stocks.items():
    swapped[value]=key
print("swapped",swapped)


