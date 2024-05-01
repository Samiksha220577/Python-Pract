# input_str = input("Enter a list of lists of integers separated by commas, where each list is separated by spaces: ")
# list_str = input_str.split(',')
# print(list_str)
# lists = [list(map(int, sublist.split())) for sublist in list_str]
# print(lists)
# sublist_sum = [sum(sublist) for sublist in lists]
# print(sublist_sum)
# print('coustomer',sublist_sum.index(max(sublist_sum))+1,'hax maximum money',max(sublist_sum))
#
#
#
# # li=list(map(str,input().split(",")))
# # m=[]
# # for i in li:
# #     x=list(map(int,i.split()))
# #     y=sum(x)
# #     m.append(y)
# # print(max(m))
# ---------------------------------------------
# mat=input()
# rows=mat.split(',')
# weal=0
# for r in rows:
#     ele=r.split()
#     rem=max(map(int,ele))
#     if rem>weal:
#         weal=rem
# print(weal)
# ---------------------------------------------
# reinprep
def maximumWealth(accounts):
    max_wealth = 0
    for customer in accounts:
        wealth = sum(customer)
        if wealth > max_wealth:
            max_wealth = wealth
    return max_wealth
# customers = 2
# accounts = [[1,2,3], [3,2,1]]
# Get the number of customers
customers = int(input("Enter the number of customers: "))

# Initialize the accounts list
accounts = []

# Get the bank accounts for each customer
for i in range(customers):
    # Get the account balances for each customer as a list
    account_balances = list(map(int, input(f"Enter the account balances for customer {i+1} separated by spaces: ").split()))
    # Add the account balances list to the accounts list
    accounts.append(account_balances)

# Print the accounts list for verification
print("Accounts: ", accounts)

print(maximumWealth(accounts))