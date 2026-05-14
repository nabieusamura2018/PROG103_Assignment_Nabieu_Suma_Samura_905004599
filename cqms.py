# CLINIC QUEUE MANAGEMENT SYSTEM (CQMS)
# PROG103 STRUCTURED PROGRAMMING ASSIGNMENT

patients = []


def register_patient():

    print("\n========== REGISTER PATIENT ==========")

    patient_name = input("Enter Patient Name: ").strip()
    patient_id = input("Enter Patient ID: ").strip()
    illness = input("Enter Illness Description: ").strip()

    while True:

        try:
            age = int(input("Enter Patient Age: "))

            if age > 0:
                break

            else:
                print("Age must be greater than 0.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    patient = {
        "name": patient_name,
        "patient_id": patient_id,
        "illness": illness,
        "age": age
    }

    patients.append(patient)

    print("\nPatient Registered Successfully!")


def view_patients():

    print("\n========== PATIENT QUEUE ==========")

    if len(patients) == 0:
        print("No patients in queue.")
        return

    for index, patient in enumerate(patients, start=1):

        print("\n-----------------------------------")
        print(f"Queue Number : {index}")
        print(f"Patient Name : {patient['name']}")
        print(f"Patient ID   : {patient['patient_id']}")
        print(f"Age          : {patient['age']}")
        print(f"Illness      : {patient['illness']}")
        print("-----------------------------------")


def search_patient():

    print("\n========== SEARCH PATIENT ==========")

    keyword = input("Enter Patient ID: ").strip()

    found = False

    for patient in patients:

        if patient['patient_id'] == keyword:

            print("\nPatient Found")
            print("-----------------------------------")
            print(f"Name      : {patient['name']}")
            print(f"Age       : {patient['age']}")
            print(f"Illness   : {patient['illness']}")
            print("-----------------------------------")

            found = True

    if not found:
        print("Patient record not found.")


def serve_patient():

    print("\n========== SERVE PATIENT ==========")

    if len(patients) == 0:
        print("No patients available.")
        return

    served_patient = patients.pop(0)

    print("\nPatient Served Successfully!")
    print(f"Served Patient : {served_patient['name']}")


def queue_summary():

    print("\n========== QUEUE SUMMARY ==========")

    print(f"Total Patients Waiting : {len(patients)}")


def main():

    while True:

        print("\n================================================")
        print("       CLINIC QUEUE MANAGEMENT SYSTEM")
        print("================================================")
        print("1. Register Patient")
        print("2. View Patient Queue")
        print("3. Search Patient")
        print("4. Serve Patient")
        print("5. Queue Summary")
        print("6. Exit System")
        print("================================================")

        choice = input("Enter Your Choice: ")

        if choice == '1':
            register_patient()

        elif choice == '2':
            view_patients()

        elif choice == '3':
            search_patient()

        elif choice == '4':
            serve_patient()

        elif choice == '5':
            queue_summary()

        elif choice == '6':

            print("\nSystem Closed Successfully.")
            print("Thank you for using CQMS.")
            break

        else:
            print("Invalid choice. Please try again.")


main()