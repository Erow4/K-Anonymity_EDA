
# Age (v1): A function to generalize age into ranges
def generalize_age(age):
    if 18 <= age < 25:
        return "18-25"
    elif 25 <= age < 35:
        return "25-35"
    elif 35 <= age < 45:
        return "35-45"
    elif 45 <= age < 55:
        return "45-55"
    elif 55 <= age < 65:
        return "55-65"
    elif 65 <= age:
        return "65+"
    else:
        return "Under 18"

# Age (v2): A (broader) function to generalize age into ranges
def generalize_age_2(age):
    if 35 <= age < 55:
        return "35-55"
    elif 55 <= age < 85:
        return "55-85"
    elif 85 <= age:
        return "85+"
    else:
        return "Under 35"

# BMI: A function to generalize BMI into categories 
# Note, I googled the standard health classifications per BMI
def generalize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
    
# Charges: A function to generalize charges into categories
def generalize_charges(charges):
    if charges < 1000:
        return "less than 1000"
    elif 1000 <= charges < 2000:
        return "1000-2000"
    elif 2000 <= charges < 3000:
        return "2000-3000"
    elif 3000 <= charges < 4000:
        return "3000-4000"
    elif 4000 <= charges < 5000:
        return "4000-5000"
    else:
        return "5000+"