from selenium import webdriver
class Test_Credence_001:
    def test_sum_001(self):
        a=3
        b=7
        sum=a+b
        print('sum of the a and b :',sum)
        if sum==10:
            print('result is correct')
            assert True

        else:
            print('result is incorrect')
            assert False


    def test_sub_002(self):
        a=20
        b=10
        sub=a-b
        print("substraction is :" ,sub)
        if sub==10:
            print("sub is correct")
            assert True

        else:
            print("sub is not correct")
            assert False

    def test_mult(self):
        p=3
        q=29
        mult=p*q
        print('multiplication is: ',mult)
        if mult==87:
            print('multiplication is correct')
            assert True

        else:
            print("multiplication is incorrect")
            assert False

    def test_CredenceUrl2(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("You are at credence.in")
            assert True
            driver.close()
        else:
            print("You are at Wrong url")
            driver.close()
            assert False