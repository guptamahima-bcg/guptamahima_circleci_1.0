from billing_system import Bill_App

def main():
    bill_app = Bill_App()
    bill_app.sanitizer = 3
    bill_app.thermal_gun = 2
    bill_app.wheat = 20
    bill_app.maggi = 3
    bill_app.sprite = 2
    bill_app.lassi = 5

    bill_app.total()

    assert bill_app.total_bill == 1404.8, "Error with Test 1"
    print("Test 1 passed")

if __name__ == "__main__":
    main()
