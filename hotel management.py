
def review_service():
    print("Please review your experience with us!!")
    review_guest = input()

def update_details():
    print("Are you extending your stay (yes/no):")
    update_profile = input()
    if update_profile.lower() == "yes":
        print("How many more days would you like to stay?")
        extended_stay = int(input())
        return extended_stay
    else:
        return 0

feed = "yes"

while feed.lower() == "yes":
    print("----------------Welcome to Hotel Management System----------------")
    print("Choose Service to Access:\n")
    print("1. Room Booking\n2. Check out\n3. Update Booking\n4. Exit\n")
    inp = input()

    match inp:
        case '1':
            family = int(input("Enter the number of guests: "))
            guest_details = []
            for i in range(family):
                print(f"Enter Details of Guest {i+1}")
                guest_name = input("Enter your Full Name: ")
                guest_age = input("Enter age: ")
                guest_details.append({'name': guest_name, 'age': guest_age})
            total_stay = int(input("Days of Stay: "))
            print(f"Booking confirmed for {total_stay} days.")
            
        case '2':
            print("Thank You For your visit:")
            review_service()
        case '3':
            extended_stay = update_details()
            if extended_stay:
                total_stay += extended_stay
                print(f"Your stay has been extended by {extended_stay} days. Total stay is now {total_stay} days.")
            else:
                print("No extension made to your stay.")
        case '4':
            print("Thank You!!")
            break
        case _:
            print("Invalid input. Please choose a valid option.")

    print("Do you want to continue (yes/no) ?")
    feed = input()
