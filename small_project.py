# print("Please select your first order frome our list...")
# print("1. simple tea : 10rs/-")
# print("2. khulhad tea : 20rs/-")
# print("3. normal petiz : 30rs/-")
# print("4. chees petiz : 40rs/-")
# print("5. masala petiz : 50rs/-")
# print("6. cold coffee : 50rs/-.")

# num=int(input("please enter the serial number of product frome list..."))

# print("your order is confirmed")
# num2=input("place anather order ?, if no simply press 'NO'")
# if(num2==1):
#     print("you select 1 and your order  is confirmed")
# elif(num2==2):
#     print("you select 2 and your order  is confirmed")
# elif(num2==3):
#     print("you select 3 and your order  is confirmed")
# elif(num2==4):
#     print("you select 4 and your order  is confirmed")
# elif(num2==5):
#     print("you select 5 and your order  is confirmed")
# elif(num2==6):
#     print("you select 6 and your order  is confirmed")
# else:
#     print("thank you for visiting here")



# def show_menu():
#     print("\n--- Welcome to Our Café ---")
#     print("Please select your order from the list below:")
#     print("1. Simple Tea      : ₹10")
#     print("2. Kulhad Tea      : ₹20")
#     print("3. Normal Patties  : ₹30")
#     print("4. Cheese Patties  : ₹40")
#     print("5. Masala Patties  : ₹50")
#     print("6. Cold Coffee     : ₹50")

# def get_item_name(num):
#     menu = {
#         1: "Simple Tea",
#         2: "Kulhad Tea",
#         3: "Normal Patties",
#         4: "Cheese Patties",
#         5: "Masala Patties",
#         6: "Cold Coffee"
#     }
#     return menu.get(num, "Invalid item")

# def main():
#     while True:
#         show_menu()
#         try:
#             choice = int(input("Enter the serial number of the product you want to order: "))
#             item = get_item_name(choice)
#             if item == "Invalid item":
#                 print("Invalid selection. Please try again.")
#             else:
#                 print(f"You selected: {item}")
#                 print("Your order is confirmed! ✅")
#         except ValueError:
#             print("Please enter a valid number.")

#         again = input("\nDo you want to place another order? (yes/no): ").strip().lower()
#         if again == "no":
#             print("Thank you for visiting! 😊")
#             break

# # Run the program
# main()
# 6



# Show menu to the user
print("Welcome to Our Café!")
print("Please select your order from the list below:")
print("1. Simple Tea      : ₹10")
print("2. Kulhad Tea      : ₹20")
print("3. Normal Patties  : ₹30")
print("4. Cheese Patties  : ₹40")
print("5. Masala Patties  : ₹50")
print("6. Cold Coffee     : ₹50")

# Start a loop to allow multiple orders
while True:
    num = int(input("\nEnter the number of the item you want to order: "))

    # Check which item was selected
    if num == 1:
        print("You selected Simple Tea. Your order is confirmed ")
    elif num == 2:
        print("You selected Kulhad Tea. Your order is confirmed ")
    elif num == 3:
        print("You selected Normal Patties. Your order is confirmed ")
    elif num == 4:
        print("You selected Cheese Patties. Your order is confirmed ")
    elif num == 5:
        print("You selected Masala Patties. Your order is confirmed ")
    elif num == 6:
        print("You selected Cold Coffee. Your order is confirmed ")
    else:
        print("Invalid choice. Please try again.")

    # Ask if the user wants to place another order
    another = input("Do you want to place another order? (yes/no): ")

    if another.lower() == "no":
        print("Thank you for visiting our café! ")
        break
