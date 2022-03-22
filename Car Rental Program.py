#import a module to allow us print our dictionary in a form that is easier to read.
import pprint
#making a nested dictionary for the first 5 cars in the business and all their attributes
all_cars = {"Toyota":{"car_model": "Camry", "year_released": "2018", "year_bought": "2021", "plate_number": "NIG501", "money_made": "$100", "times_rented": "5"},
            "Honda":{"car_model": "Odyssey", "year_released": "2020", "year_bought": "2021", "plate_number": "NIG601", "money_made": "$200", "times_rented": "10"},
            "Ford":{"car_model": "Explorer", "year_released": "2019", "year_bought": "2021", "plate_number": "NIG701", "money_made": "$300", "times_rented": "15"},
            "Mercedes Benz":{"car_model": "AMG GT Roadster Convertible", "year_released": "2017", "year_bought": "2021", "plate_number": "NIG801", "money_made": "$400", "times_rented": "20"},
            "Chevrolet":{"car_model": "Suburban", "year_released": "2016", "year_bought": "2021", "plate_number": "NIG901", "money_made": "$500", "times_rented": "25"}
            }
print("Welcome Omondi, these are the cars in your current collection")
pprint.pprint(all_cars, sort_dicts=False)
#list of all operation Omondi can perform in his business
print("These are the operations you can perform in your business:\n1. Add a new car\n2. Update the attributes of a car\n3. Remove a car from your collection\n4. Rent a car")
#Use functions to perform any of the operations Omondi chooses
def operations():
    omondi_input = int(input("Please enter the number of the operation you want to perform: "))
    if omondi_input == 1:
        add_car()     #This calls the function for adding a new car
    elif omondi_input == 2:
        update_car()    #Calls the function for updating the attributes of a car
    elif omondi_input == 3:
        remove_car()     #Calls he function for removing a car from the collection
    elif omondi_input == 4:
        rent_car()      #Calls the function for renting a car
    else:
        print("Please enter either 1,2,3,or 4")
    operations()    #Repeats the function whenever the option is wrong
#function to add a new car to the collection
def add_car():
    response = ["y","yes","yeah"]
    adding = input("Are you ready to add a new car to your collection?")
    if adding in response:
        car_brand = input("Please enter the brand of the new car:\n ")
        car_model = input("Please enter the model of the new car:\n ")
        year_released = input("Please enter the year the car was released:\n ")
        year_bought = input ("Please enter the year you bought the car:\n ")
        plate_number = input("Please enter the plate number of the car:\n ")
        money_made = input("How much have you made from this car?\n ")
        times_rented = input("How many times have you rented-out this car?\n ")
#Code to add the car to the collection using inputed attributes
        all_cars[car_brand]= {"car_model":car_model, "year_released":year_released, "year_bought":year_bought,
                              "plate_number":plate_number, "money_made":money_made, "times_rented":times_rented}
        pprint.pprint(all_cars, sort_dicts=False)    #prints updated car collection
        another_operation = input("Would you like to perform another operation?")
        if another_operation in response:
            operations()
        else:
            exit()    #ends the operations if Omondi does not want to perform another operation
    else:
        operations()   #Gives Omondi another chance to pick another operation to perform

#function to update the attribute of a car
def update_car():
    response = ["y", "yes", "yeah"]
    updating = input("Are you ready to update your car?")
    if updating in response():
        update_response = input("Which car would you like to update?\n")
        if update_response in all_cars:
            update_key= input("Which attribute do you want to change?\n")
            update_value= input("What do you want to change it to?\n")
# code to add the update to the car collection
            all_cars[update_response][update_key]=update_value    #updates the car collection
            pprint.pprint(all_cars, sort_dict=False)        #prints the updated collection
            print("\n This is your updated car collection")
            another_operation = input("Would you like to perform another operation?")
            if another_operation in response:
                operations()
            else:
                exit()
        else:
            print("You entered an invalid car")
    else:
        operations()  # Asks Omondi to pick another operation to perform

#function to remove a car from Omondi's collection
def remove_car():
    response = ["y", "yes", "yeah"]
    remove = input("Would you like to remove a car from your collection?\n")
    if remove in response:
        remove_car = input("Which car would you like to delete?\n")
        if remove_car in all_cars:
            del all_cars[remove_car]
            print("You have successfully deleted this car. This is your new collection \n")
            pprint.pprint(all_cars, sort_dicts=False)
            another_operation = input("Would you like to perform another operation?")
            if another_operation in response:
                operations()
            else:
                exit()
        else:
            print("You entered an invalid car")
    else:
        operations()
#function to rent a car
def rent_car(g):
#counting how many times each car has been rented
    rent_Toyota = 0
    rent_Honda = 0
    rent_Ford = 0
    rent_Mercedes_Benz = 0
    rent_Chevrolet = 0
#counting the amount of money made from each car
    price_Toyota = 0
    price_Honda = 0
    price_Ford = 0
    price_Mercedes_Benz = 0
    price_Chevrolet = 0
    while True:
        pprint.pprint(all_cars, sort_dicts=False)   # This shows Omondi the cars that he currently has in his collection
        omondi_rent = input("What car would you like to rent?\n")
        if omondi_rent in all_cars and omondi_rent == "Toyota":
            rent_Toyota += 1
            price_Toyota += 100     #100 is the price of renting a Toyota car, in dollars
        elif omondi_rent in all_cars and omondi_rent == "Honda":
            rent_Honda += 1
            price_Honda += 200  # 200 is the price of renting a Honda car, in dollars
        elif omondi_rent in all_cars and omondi_rent == "Ford":
            rent_Ford += 1
            price_Ford += 400  # 400 is the price of renting a Ford car, in dollars
        elif omondi_rent in all_cars and omondi_rent == "Mercedes_Benz":
            rent_Mercedes_Benz += 1
            price_Mercedes_Benz += 500  # 500 is the price of renting a Mercedes Benz, in dollars
        elif omondi_rent in all_cars and omondi_rent == "Chevrolet":
            rent_Chevrolet += 1
            price_Chevrolet += 450  # 450 is the price of renting a Chevrolet car, in dollars
        else:
            print("Sorry, your input is not in our collection")
            response = ["y", "yes", "yeah"]
            reply = input("Do you want to rent another car?\n")
            if reply in response:
                rent_car()
            elif reply not in response:
                print("Toyota was rented out ", rent_Toyota, "times and", price_Toyota, " dollars was gained.\n"
                      "Honda was rented out ", rent_Honda, "times and", price_Honda, "dollars was realised. \n"
                      "Ford was rented out ",rent_Ford, "times and", price_Ford, "dollars was realised. \n"
                      "Mercedes Benz was rented out ", rent_Mercedes_Benz, "times and", price_Mercedes_Benz, "dollars was realised. \n"
                      "Chevrolet was rented out ",rent_Chevrolet, "times and", price_Ford, "dollars was realised. \n")
                another_operation = input("Would you like to perform another operation?\n")
                if another_operation in response:
                    operations()
                else:
                    exit()
                if name == "_main_":
                    operations()