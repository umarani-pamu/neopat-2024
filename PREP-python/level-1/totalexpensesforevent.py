brand_expenses=float(input())
travel_expenses=float(input())
food_expenses=float(input())
logistic_expenses=float(input())
total_expenses=brand_expenses+travel_expenses+food_expenses+logistic_expenses
brand_percentage=(brand_expenses/total_expenses)*100
travel_percentage=(travel_expenses/total_expenses)*100
food_percentage=(food_expenses/total_expenses)*100
logistic_percentage=(logistic_expenses/total_expenses)*100
print(f"{total_expenses:.2f}")
print(f"{brand_percentage:.2f}"+"%")
print(f"{travel_percentage:.2f}"+"%")
print(f"{food_percentage:.2f}"+"%")
print(f"{logistic_percentage:.2f}"+"%")