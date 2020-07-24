# mortgage.py
#

# Exercise 1.7


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0


extra_payment_start_month = int(input('start month: '))
extra_payment_end_month = int(input('end month: '))
extra_payment = int(input('extra payment: '))

while principal > 0:
    if month > extra_payment_start_month and month < extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    principal = principal * (1+rate/12) - payment
    if principal < 0:
        payment = payment + principal
        principal = 0
    total_paid = total_paid + payment
    month += 1
    print(month, total_paid, principal)

print('Total paid', total_paid,'\n', 'over', month, 'months')
