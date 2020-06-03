# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 1
extra_payment = 1000
extra_payment_start_month = 60
extra_payment_end_month = 108

while principal > 0 and principal > payment:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if(months >= extra_payment_start_month and months <= extra_payment_end_month):
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(f'{months}, {total_paid:0.2f}, {principal:0.2f}')
    months += 1

payment = principal
principal = principal - payment
total_paid = total_paid + payment
print(f'{months}, {total_paid:0.2f}, {principal:0.2f}')
