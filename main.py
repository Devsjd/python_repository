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