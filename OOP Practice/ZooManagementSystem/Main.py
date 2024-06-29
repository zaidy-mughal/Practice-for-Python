from Zoo import Zoo


safariZoo = Zoo()
print("\n====== Zoo Management System ======\n")

while True:
    print("1. Add Animal to Zoo")
    print("2. Remove Animal from Zoo")
    print("3. Listen the Sound of Animal")
    print("4. See what the Animal Eating")
    print("5. Check Animal Health Status")
    print("6. See All the Animals in the Zoo")
    
    print("7. Press Other than 1-7 to Close.")

    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
        safariZoo.addAnimal()
    
    elif choice == 2:
        safariZoo.removeAnimal()

    elif choice == 3:
        safariZoo.makeSound()

    elif choice == 4:
        safariZoo.feedAnimal()

    elif choice == 5:
        safariZoo.checkHealth()

    elif choice == 6:
        safariZoo.viewAllAnimals()

    else:
        print("Thanks for Using\n")
        break

