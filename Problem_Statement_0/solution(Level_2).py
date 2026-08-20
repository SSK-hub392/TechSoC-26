def ship_details():

    print("----NEW SHIP DETAILS----")
    storage_capacity = int(input("\nEnter maximum storage capacity: "))
    no_of_containers = int(input("Enter number of containers: "))
    print()

    i = 1
    total_weight = 0
    weights = []

    while i <= no_of_containers:
        weight = float(input(f"Enter weight of container {i}: "))
        i += 1
        total_weight += weight
        weights.append(weight)

    avg_weight = total_weight / no_of_containers

    heaviest = max(weights)
    lightest = min(weights)

    def classification():
        if total_weight >= 200:
            return "Heavy"
        else:
            return "Light"

    def status():
        if total_weight <= storage_capacity:
            return "Shipment can be unloaded"
        else:
            return "Shipment exceeds port capacity"

    # Ship Details

    print()
    print("=" * 55)
    print("Ship Details")
    print("=" * 55)

    print(
        f"Total Shipment Weight: {total_weight}\n"
        f"Average Container Weight: {avg_weight}\n"
        f"Heaviest Container: {heaviest}\n"
        f"Lightest Container: {lightest}\n"
        f"Classification: {classification()}\n"
        f"Port Capacity: {storage_capacity}\n"
        f"Status: {status()}"
    )


    # Feature-8: Current Ship Menu
    
    
    while True:

        print()
        print("=" * 55)
        print("Current Ship Menu")
        print("=" * 55)

        print("1. Sorted Display (Feature 1)")
        print("2. Bar Chart (Feature 3)")
        print("3. Save Report (Feature 4)")
        print("4. Search Container (Feature 6)")
        print("5. Kth Heaviest (Feature 7)")
        print("Q. Exit Current Ship")

        print("-" * 55)

        choice = input("Enter your choice: ")

        # Feature-1: Sorted Display

        if choice == "1":

            sorted_weights = weights.copy()

            for i in range(no_of_containers - 1):

               for j in range(no_of_containers - 1 - i):

                    if sorted_weights[j] > sorted_weights[j + 1]:

                        sorted_weights[j], sorted_weights[j + 1] = (sorted_weights[j + 1], sorted_weights[j])
                            
                        
            print()
            print("Containers in sorted order:")
            print()

            k = 1

            for weight in sorted_weights:
                print(f"{k}. {weight}")
                k += 1

        # Feature-3: Bar Chart

        elif choice == "2":

            print()
            print("Container Weight Bar Chart:")
            print()

            for i in range(no_of_containers):

                no_of_stars = int(weights[i] / 5)

                stars = ""

                for m in range(no_of_stars):
                    stars += "*"

                print(
                    f"Container {i + 1} ({weights[i]})  : {stars}"
                )

            print()
            print("(Each * represents 5 units)")



        # Feature-4: Save Report

        elif choice == "3":
        
            print()
            print("-" * 55)
        
            file_name1 = input("Enter the file name: ")
        
            with open(file_name1, "w") as file:
        
             file.write(
                        f"Total Shipment Weight: {total_weight}\n"
                        f"Average Container Weight: {avg_weight}\n"
                        f"Heaviest Container: {heaviest}\n"
                        f"Lightest Container: {lightest}\n"
                        f"Classification: {classification()}\n"
                       ) 
        
            print(f"Report saved to {file_name1}")




        # Feature-6: Search

        elif choice == "4":

            weight_choice = float( input("Enter the weight of container: "))
            
            weight_found = False

            for i in range(len(weights)):

                weight = weights[i]

                if weight_choice == weight:

                    print("Container found!")
                    print(f"Container {i + 1} has weight {weight}")
                    
                    weight_found = True
                    break

            if weight_found == False:

                print(f"No container found with weight {weight_choice}.")
                    




        # Feature-7: Kth Heaviest

        elif choice == "5":

            sorted_weights = weights.copy()

            for i in range(no_of_containers - 1):

                for j in range(no_of_containers - 1 - i):

                    if sorted_weights[j] > sorted_weights[j + 1]:

                        sorted_weights[j], sorted_weights[j + 1] = sorted_weights[j + 1], sorted_weights[j]
                        

            k = int(input("Enter K (position of the heaviest container): "))
              
            if k == 1:
                position = "1st"

            elif k == 2:
                position = "2nd"

            elif k == 3:
                position = "3rd"

            else:
                position = f"{k}th"


            if k in range(1, no_of_containers + 1):

                print(f"The {position} heaviest container has weight: {sorted_weights[no_of_containers - k]} ")
                
            elif k <= 0:

                print("Invalid input: N must be at least 1.")

            else:

                print(f"Invalid input: Only {no_of_containers} containers exist.")
                



        # Quit

        elif choice.lower() == "q":

            print()
            print("Finished with current ship.")
            break

        else:

            print("Invalid choice. Please try again.")




def read_container_file():


     file_name3 = input("\nEnter the container data file name: ")
          
     with open(file_name3, "r") as file:
    
                wts = []
                containers_no = int(file.readline().strip())
                printing_wts = ""
                total_shipment_weight = 0
    
                for i in range(containers_no):
    
                    wt = int(file.readline().strip())
                    wts.append(wt)
                    printing_wts += str(wt) + ", "
                    total_shipment_weight += wt
    
                printing_wts = printing_wts.rstrip(", ")
    
                average_container_weight = (total_shipment_weight / containers_no)
                
                heaviest_container = max(wts)
                lightest_container = min(wts)
    
                if total_shipment_weight >= 200:
                    classification = "Heavy"
                else:
                    classification = "Light"
    
                print()
                print("=" * 55)
                print("Shipment Loaded From File")
                print("=" * 55)
    
                print(
                    f"Loaded {containers_no} containers "
                    f"from {file_name3}\n"
                    f"Weights: {printing_wts}\n"
                )
    
                print(
                    f"Total Shipment Weight: "
                    f"{total_shipment_weight}\n"
                    f"Average Container Weight: "
                    f"{average_container_weight}\n"
                    f"Heaviest Container: "
                    f"{heaviest_container}\n"
                    f"Lightest Container: "
                    f"{lightest_container}\n"
                    f"Classification: {classification}"
                )



# Feature-8: Main Terminal Menu(own feature)
 
while True:

    
    print()
    print("----SMART CARGO TERMINAL----")
    print()
    

    print("1. New Ship Details")
    print("2. Read Container Data File")
    print("Q. Exit")

    print("-" * 55)

    choice = input("Enter your choice: ")

    # Option 1: New Ship Details

    if choice == "1":

      no_of_ships = 0

      while True:

        ship_details()

        no_of_ships += 1

        print()
        print("-" * 55)

        while True:

            continue_choice = input(
                "Do you want to process another ship? (yes/no): "
            )

            if continue_choice.lower() == "yes":
                break

            elif continue_choice.lower() == "no":
                print()
                print(f"Total ships processed: {no_of_ships}")
                print("Returning to main menu...")
                break

            else:
                print("Enter either 'yes' or 'no'.")

        if continue_choice.lower() == "no":
            break




    # Option 2: Read Container Data File
    # Feature-5: Read from File

    elif choice == "2":


         read_container_file()
       



    # Exit

    elif choice.lower() == "q":

        print()
        print("=" * 55)
        print("Thank you for using Smart Cargo Terminal!")
        print("=" * 55)

        break

    else:

        print()
        print("Invalid choice. Please try again.")

          
       
       
          



