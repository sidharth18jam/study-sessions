print('Project Title: BMI Insights: Visualizing Health Data with Python')
print('=================================================================')
print('Developed by Dhairya Arya')

USER_ID = "guest"
PASSWORD = "password"

def my_login():
    while True: 
        id = input('Enter Guest Login ID: ')
        pwd = input('Enter your Password: ')
        if id == USER_ID and pwd == PASSWORD:
            print('Login Successful')
            return True
        else:
            print('Oops, wrong password or ID! Try Again')
            retry = input("Do you want to try again? (Y/N): ")
            if retry.lower() != 'y':
                print("Exiting login attempt.")
                return False  


def welcome_message():
    print("===================================")
    print("  Visualizing Health Data with Python     ")
    print("===================================")
    print("🌟 Explore your Body Mass Index 🌟")
    print("🚀 Let's embark on a journey to better health together!")
    print("===================================")

welcome_message()

import csv
import os
import matplotlib.pyplot as plt

def calculate_bmi(weight, height):
    """Calculate BMI using weight and height."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Return the BMI category based on the calculated BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def save_to_csv(data):
    """Save BMI data to a CSV file."""
    file_exists = os.path.isfile('Bmi.csv')
    
    with open("Bmi.csv", "a", newline="") as fw:
        writer = csv.writer(fw)
        if not file_exists:
            writer.writerow(["Name", "Age", "Blood Group", "Gender", "Weight", "Height", "BMI", "Bmi Category"])  # Write header if file is new
        writer.writerow(data)

def plot_bmi_data():
    """Plot BMI data from the CSV file, gender-wise."""
    male_bmis = []
    female_bmis = []
    names_male = []
    names_female = []

    if os.path.isfile('Bmi.csv'):
        with open('Bmi.csv', 'r') as fr:
            reader = csv.reader(fr)
            next(reader)  # Skip header
            for row in reader:
                name = row[0]  # Name
                bmi = float(row[6])  # BMI
                gender = row[3]  # Gender

                if gender.lower() == 'male':
                    names_male.append(name)
                    male_bmis.append(bmi)
                elif gender.lower() == 'female':
                    names_female.append(name)
                    female_bmis.append(bmi)

    # Plotting for Males
    plt.figure(figsize=(12, 6))
    
    # Males
    plt.subplot(1, 2, 1)
    plt.bar(names_male, male_bmis, color='lightblue')
    plt.xlabel('Names')
    plt.ylabel('BMI')
    plt.title('BMI of Male Individuals')
    plt.xticks(rotation=45)

    # Females
    plt.subplot(1, 2, 2)
    plt.bar(names_female, female_bmis, color='lightpink')
    plt.xlabel('Names')
    plt.ylabel('BMI')
    plt.title('BMI of Female Individuals')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

def main():
    if my_login():
        print("Welcome to the BMI Calculator!")
        
        continue_choice = 'Y'
        
        while continue_choice in ['Y', 'y']:
            name = input("Enter Your Name: ")
            age = int(input("Enter Your Age: "))
            bg = input("Enter Your Blood Group: ")
            gender = input("Enter your Gender (Male/Female): ")
            weight = float(input("Enter your weight (kg): "))
            height = float(input("Enter your height (m): "))  
            bmi = calculate_bmi(weight, height)
            category = get_bmi_category(bmi)

            print(f"Your BMI is: {bmi:.2f}")
            print(f"You are categorized as: {category}")

            # Save data to CSV
            save_to_csv([name, age, bg, gender, weight, height, bmi, category])

            continue_choice = input("Do you want to continue? (Y/N): ")
        
        # Call the plot function after exiting the loop
        plot_bmi_data()
        print("Exiting the program.")

if __name__ == "__main__":
    main()

