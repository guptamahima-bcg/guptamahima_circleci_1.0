from billing_system import Bill_App

def main():
    bill_app = Bill_App()
    bill_app.hand_gloves = 10
    bill_app.syrup = 10
    bill_app.rice = 20
    bill_app.flour = 20
    bill_app.mineral = 10
    bill_app.juice = 10

    bill_app.total()

    assert bill_app.total_bill == 2821.0, "Error with Test 2"
    print("Test 2 passed")

if __name__ == "__main__":
    main()
