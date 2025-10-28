# دریافت سن از کاربر
age = int(input("سن خود را به سال وارد کنید: "))

# محاسبه بر اساس سال
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# نمایش نتایج
print("سن شما به ساعت:", hours)
print("سن شما به دقیقه:", minutes)
print("سن شما به ثانیه:", seconds)

#تمرین دوم

# دریافت عدد دو رقمی از کاربر
num = int(input("یک عدد دو رقمی وارد کنید: "))

# جدا کردن دهگان و یکان
tens = num // 10
ones = num % 10

# ساخت عدد معکوس
reverse_num = ones * 10 + tens

# نمایش نتیجه
print("مقلوب عدد =", reverse_num)