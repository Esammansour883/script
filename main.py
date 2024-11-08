# برنامج بسيط لطباعة رسالة ترحيبية وحساب مجموع رقمين
def main():
    print("مرحباً بك في أول مشروع لك على GitHub Codespaces!")
    # إدخال رقمين من المستخدم
    num1 = float(input("Enter The Number one: "))
    num2 = float(input("Enter The Number Tow: "))
    
    # حساب المجموع
    total = num1 + num2
    
    # طباعة النتيجة
    print("مجموع الرقمين هو:", total)

# استدعاء الدالة الرئيسية
if __name__ == "__main__":
    main()
