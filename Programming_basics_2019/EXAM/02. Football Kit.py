shirt_price=float(input())
sum_needed=float(input())


shorts_price=0.75*shirt_price
socks_price=0.2*shorts_price
buttons_price=(shorts_price+shirt_price)*2

total_sum=(shirt_price+shorts_price+socks_price+buttons_price)*0.85

if total_sum>=sum_needed:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {(sum_needed-total_sum):.2f} lv. more.")