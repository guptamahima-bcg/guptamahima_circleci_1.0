import random

#===============main=====================
class Bill_App:
    def __init__(self):
    # ================variables=======================
        self.sanitizer = int(0)
        self.mask = int(0)
        self.hand_gloves = int(0)
        self.syrup = int(0)
        self.cream = int(0)
        self.thermal_gun = int(0)
    # ============grocery==============================
        self.rice = int(0)
        self.food_oil = int(0)
        self.wheat = int(0)
        self.spices = int(0)
        self.flour = int(0)
        self.maggi = int(0)
        #=============coldDrinks=============================
        self.sprite = int(0)
        self.mineral = int(0)
        self.juice = int(0)
        self.coke = int(0)
        self.lassi = int(0)
        self.mountain_duo = int(0)
    # ==============Total product price================
        self.medical_price = str('')
        self.grocery_price = str('')
        self.cold_drinks_price = str('')
    # ==============Customer==========================
        self.c_name = str('')
        self.c_phone = str('')
        self.bill_no = str('')
        x = random.randint(1000, 9999)
        self.bill_no = str(x)
        self.search_bill = str('')
    # ===============Tax================================
        self.medical_tax = str('')
        self.grocery_tax = str('')
        self.cold_drinks_tax = str('')

    def total(self):
        self.m_h_g_p = self.hand_gloves*12
        self.m_s_t = self.sanitizer*2
        self.m_m_p = self.mask*5
        self.m_s_p = self.syrup*30
        self.m_c_p = self.cream*5
        self.m_t_g_p = self.thermal_gun*15
        self.total_medical_price = float(self.m_m_p+self.m_h_g_p+self.m_s_t+self.m_c_p+self.m_t_g_p+self.m_s_p)

        self.medical_price = "Rs. "+str(self.total_medical_price)
        self.c_tax = round((self.total_medical_price*0.05), 2)
        self.medical_tax= "Rs. "+str(self.c_tax)

        self.g_r_p = self.rice*10
        self.g_f_o_p = self.food_oil*10
        self.g_w_p = self.wheat*10
        self.g_s_p = self.spices*6
        self.g_f_p = self.flour*8
        self.g_m_p = self.maggi*5
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_s_p+self.g_f_p+self.g_m_p)

        self.grocery_price = "Rs. " + str(self.total_grocery_price)
        self.g_tax = round((self.total_grocery_price*5), 2)
        self.grocery_tax = "Rs. " + str(self.g_tax)

        self.c_d_s_p = self.sprite*10
        self.c_d_w_p = self.mineral*10
        self.c_d_j_p = self.juice*10
        self.c_d_c_p = self.coke*10
        self.c_d_l_p = self.lassi*10
        self.c_m_d = self.mountain_duo*10
        self.total_cold_drinks_price = float(self.c_d_s_p+self.c_d_w_p+self.c_d_j_p+self.c_d_c_p+self.c_d_l_p+self.c_m_d)

        self.cold_drinks_price = "Rs. "+str(self.total_cold_drinks_price)
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax = "Rs. "+str(self.c_d_tax)

        self.total_bill = float(self.total_medical_price+self.total_grocery_price+self.total_cold_drinks_price+self.c_tax+self.g_tax+self.c_d_tax)

    def clear_data(self):
        op = 1
        if op > 0:
            self.sanitizer = 0
            self.mask = 0
            self.hand_gloves = 0
            self.syrup = 0
            self.cream = 0
            self.thermal_gun = 0
    # ============grocery==============================
            self.rice = 0
            self.food_oil = 0
            self.wheat = 0
            self.spices = 0
            self.flour = 0
            self.maggi = 0
    # =============coldDrinks=============================
            self.sprite = 0
            self.mineral = 0
            self.juice = 0
            self.coke = 0
            self.lassi = 0
            self.mountain_duo = 0
    # ====================taxes================================
            self.medical_price = ''
            self.grocery_price = ''
            self.cold_drinks_price = ''

            self.medical_tax = ''
            self.grocery_tax = ''
            self.cold_drinks_tax = ''

            self.c_name = ''
            self.c_phone = ''

            self.bill_no = ''
            x = random.randint(1000, 9999)
            self.bill_no = str(x)

            self.search_bill = ''

obj = Bill_App()
obj.clear_data()
print("Welcome to Star Supermarket!!")
