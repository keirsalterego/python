cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if selling_price > cost_price:
  profit = selling_price - cost_price
  print(f"The seller has made a profit of ₹{profit:.2f}.")
elif selling_price < cost_price:
  loss = cost_price - selling_price
  print(f"The seller has incurred a loss of ₹{loss:.2f}.")
else:
  print("The seller has made no profit or loss.")