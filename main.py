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

#تمرین سوم

#تمرین سوم

# دریافت عدد دو رقمی
num = int(input("یک عدد دو رقمی وارد کنید: "))

# جدا کردن رقم دهگان و یکان
tens = num // 10
ones = num % 10

# محاسبه توان‌ها
result1 = tens**ones
result2 = ones**tens
result3 = result1+result2
# نمایش نتیجه
print("رقم اول به توان رقم دوم =", result1)
print("رقم دوم به توان رقم اول =", result2)
print("حاصل جمع دو رقم =" , result3)