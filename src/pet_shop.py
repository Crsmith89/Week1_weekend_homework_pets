# WRITE YOUR FUNCTIONS HERE
# 1 - Get pet shop name
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# 2 - Get total cash
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# 3 - Add or remove cash +10, += operator performs an addition operator and then assigns the result of the operation to a variable.
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    




