# WRITE YOUR FUNCTIONS HERE
# 1 - Get pet shop name
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# 2 - Get total cash
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# 3 - Add or remove cash +10, += operator performs an addition operator and then assigns the result of the operation to a variable.
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash 
    
# 4 - add_or_remove_cash -10 - Review these why not working, did have it working but changed something. 
def add_or_remove_cash(pet_shop, total):
    pet_shop["admin"]["total_cash"] = total

# 5 - Get pets sold, searches admin dict returns pets sold
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# 6 - Increase pets sold, using +=operator as per question 3 assigning result of the operation to a variable then return increase. 
def increase_pets_sold(pet_shop, total):
    pet_shop["admin"]["pets_sold"] += total
    return pet_shop["admin"]["pets_sold"]

# 7 - Get stock count, using len pets list
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# 8 - Get pets breed found matching breed, blank list to loop pet hsop list. 
def get_pets_by_breed(pet_shop,breed):
    pets_of_breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_of_breed_list.append(pet)
    return pets_of_breed_list

# 9 - pets by breed not found, thought do else if return, need to review. 
def get_pets_by_breed(pet_shop, breed):
    pets_of_breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_of_breed_list.append(pet)
    
  
# 10 - return pets name, pets shop -- pets -- name = pet
def find_pet_by_name(pet_shop,name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return (pet)

# 11 - Find pet by name not on list
def find_pet_by_name(pet_shop,name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
        

#  12 - remove pet by name, did have look using index method but need explination, think it could be done too. 
def remove_pet_by_name(pet_shop,name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
         pet_shop["pets"].remove(pet)


# 13 - Add new pet to stock, add new pet dictionary append new_pet
def add_pet_to_stock(pet_shop,new_pet):
    pet_shop["pets"].append(new_pet)

# 14 - Get customer cash, access customers then return cash value
def get_customer_cash(customer):
    cash=customer["cash"]
    return cash

# 15 - Remove customer cash, access customer remove cash from thier dictionary -=  
def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

# 16 - Get customer pet count
def get_customer_pet_count(customers):
    return len(customers["pets"])


# 17 - Add pet to customer
def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)

            
#  Review further details tomorrow, head like a sive at the moment!!