class calculator:
    def __init__(self,symb ,num1 ,num2 ):
        self.num1 = num1
        self.num2 = num2
        self.symb = symb
    def calcult(self):
        if self.symb == "+":
            return self.num1 + self.num2
        elif self.symb == "-":
            return self.num1 - self.num2
        elif self.symb == "*":
            return self.num1 * self.num2
        elif self.symb == "/":
            return self.num1 / self.num2



while True :
    calcul = calculator(str(input("select opration + for addition - for substraction * for multiplication / for division : ")), int(input("enter first number: ")), int(input("enter enter second number: ")))

    print("doing: %d %s %d " % (calcul.num1, calcul.symb, calcul.num2))
    if calcul.symb == "/":
        print("operation ans is: %d and the remainder is: %d " % (calcul.calcult(), calcul.num1 % calcul.num2))
    else:
        print("operation ans is: ", calcul.calcult())