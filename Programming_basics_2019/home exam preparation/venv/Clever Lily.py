age = int(input())
mashine_price = float(input())
toy_price = int(input())

toys_count=0
money=10
savings=0
for years in range(1, age+1):
    if years % 2 !=0 :
      toys_count+=1
    else:
        savings+=money
        money+=10
        savings-=1
savings+=(toy_price*toys_count)

if savings>= mashine_price:
    print(f'Yes! {abs(mashine_price-savings):.2f}')
else:
    print(f'No! {abs(mashine_price-savings):.2f}')