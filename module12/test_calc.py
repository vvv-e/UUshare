import calc

def test_add():
    if calc.add(1,2) == 3:
        print("Test add(a,b) is OK")
    else:
        print("Test add(a,b) is fail")

def test_sub():
    if calc.sub(1,2) == -1:
        print("Test sub(a,b) is OK")
    else:
        print("Test sub(a,b) is fail")

def test_mul():
    if calc.mul(1,2) == 2:
        print("Test mul(a,b) is OK")
    else:
        print("Test mul(a,b) is fail")

def test_div():
    if calc.div(2,1) == 2:
        print("Test div(a,b) is OK")
    else:
        print("Test div(a,b) is fail")

if __name__ == "__main__":
    test_add()
    test_sub()
    test_mul()
    test_div()
