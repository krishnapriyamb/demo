fixed_amount=100000
withdraw=int(input('amount to withdraw'))
if withdraw<=fixed_amount:
    print('amount in the account=',fixed_amount-withdraw)
else:
    print('invalid')
