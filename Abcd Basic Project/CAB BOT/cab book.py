
import random

booking_id = 1001
history = []

while True:
    print("\n===== CAB BOOKING CHATBOT =====")
    print("1. Book Ride")
    print("2. Ride History")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n===== SELECT CAB =====")
        print("1. Auto - Rs.12/km")
        print("2. Sedan - Rs.18/km")
        print("3. SUV - Rs.25/km")

        cab = input("Choose cab: ")

        if cab == "1":
            cab_name = "Auto"
            rate = 12
        elif cab == "2":
            cab_name = "Sedan"
            rate = 18
        elif cab == "3":
            cab_name = "SUV"
            rate = 25
        else:
            print("Invalid cab choice!")
            continue

        print("\n===== PICKUP LOCATION =====")
        print("1. Pune Station")
        print("2. Swargate")
        print("3. Hinjawadi")

        pickup = input("Choose pickup: ")

        if pickup == "1":
            source = "Pune Station"
        elif pickup == "2":
            source = "Swargate"
        elif pickup == "3":
            source = "Hinjawadi"
        else:
            print("Invalid pickup location!")
            continue

        print("\n===== DROP LOCATION =====")
        print("1. Shivajinagar - 5 km")
        print("2. Kothrud - 8 km")
        print("3. Wakad - 10 km")

        drop = input("Choose drop: ")

        if drop == "1":
            destination = "Shivajinagar"
            distance = 5
        elif drop == "2":
            destination = "Kothrud"
            distance = 8
        elif drop == "3":
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid drop location!")
            continue

        fare = rate * distance

        print("\n===== FARE DETAILS =====")
        print("Cab Type:", cab_name)
        print("Pickup:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "per km")
        print("Total Fare: Rs.", fare)

        otp = random.randint(1000, 9999)

        print("\n===== WARNING =====")
        print("Your OTP is:", otp)
        print("Warning: Once the OTP has been shared, the ride Cannot be cancelled.")

        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm = input("Enter your choice: ")

        if confirm == "1":
            entered_otp = input("Enter OTP: ")

            if entered_otp == str(otp):
                print("\n===== BOOKING CONFIRMED =====")
                print("OTP verified successfully!")
                print("Your ride is booked successfully!")

                print("\n===== FARE RECEIPT =====")
                print("Booking ID: CAB" + str(booking_id))
                print("Cab Type:", cab_name)
                print("Pickup:", source)
                print("Destination:", destination)
                print("Distance:", distance, "km")
                print("Rate: Rs.", rate, "per km")
                print("Total Fare: Rs.", fare)
                print("Booking Status: Confirmed")

                history.append([
                    "CAB" + str(booking_id),
                    cab_name,
                    source,
                    destination,
                    distance,
                    fare,
                    "Confirmed"
                ])

                booking_id += 1

            else:
                print("\nWrong OTP!")
                print("Booking failed. You cannot try again.")

        elif confirm == "2":
            print("\nRide cancelled successfully!")
            print("Booking not confirmed.")

        else:
            print("\nInvalid choice. Booking not confirmed.")

    elif choice == "2":
        print("\n===== RIDE HISTORY =====")

        if len(history) == 0:
            print("No confirmed rides found.")
        else:
            for ride in history:
                print("\nBooking ID:", ride[0])
                print("Cab Type:", ride[1])
                print("Pickup:", ride[2])
                print("Destination:", ride[3])
                print("Distance:", ride[4], "km")
                print("Total Fare: Rs.", ride[5])
                print("Status:", ride[6])

    elif choice == "3":
        print("\nThank you for using Cab Booking Chatbot!")
        break

    else:
        print("Invalid choice. Please try again.")
