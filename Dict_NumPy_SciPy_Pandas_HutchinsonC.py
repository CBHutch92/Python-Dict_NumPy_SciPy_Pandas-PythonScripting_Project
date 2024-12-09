# Assignment 4
# Casey Hutchinson
# ITEC 3100
# Due by 10/20/2024



# Part A
# Write a Python program that creates and uses the dictionary below, which maps country name to internet top-level domains(TLDs)
def internetDomain_Dictionary():
    # Dictionary with country name as key and TLD as value
    tlds = {'Canada':'ca', 'United States':'us', 'Mexico':'mx'}

    # Brief explanation of what the program will do when the user opens it
    print("This program has initialized with an existing dictionary which maps country name to internet top-level domains (TLDs).")
    print("We will run a series of checks on this dictionary.")

    # Step A - checks whether the dictionary contains the key 'Canada' displayed to the user in a T/F format
    print("\n")
    print("True or False: the dictionary contains the key 'Canada'")
    Dictionary_Canada = 'Canada' in tlds.keys()
    print(Dictionary_Canada)

    # Step B - checks whether the dictionary contains the key 'France' displayed to the user in a T/F format
    print("\n")
    print("True or False: the dictionary contains the key 'France'")
    Dictionary_France = 'France' in tlds.keys()
    print(Dictionary_France)

    # Step C - iterates through the key-value pairs and displays them to the user in a two-column format
    print("\n")
    print("Now I'm going to display the Countries and their TLD in the current version of the dictionary.")
    print("Column 1 is the Country, and column 2 is the TLD.")
    print("_________________")
    for Country, TLD in tlds.items():
        print(f"{Country}, {TLD}")

    # Step D - adds the key-value pair of 'Sweden' and 'sw'
    print("\n")
    print("Now I'd like to add the Country 'Sweden' and it's TLD 'sw' to the dictionary.")
    tlds['Sweden'] = 'sw'
    print(tlds)

    # Step E - updates the value for the key 'Sweden' to 'se' because 'sw' was incorrect
    print("\n")
    print("Looks like we've successfully added Sweden to the dictionary! However, I made a mistake.")
    print("I entered the TLD as 'sw' but that is incorrect. I'm going to update it to the correct TLD (se).")
    tlds['Sweden'] = 'se'
    print(tlds)

    # Step F - use a dictionary comprehension to reverse the keys and values
    print("\n")
    print("Now I'm going to swap the keys and values for the dictionary (TLDs become the Key and Country's become the value).")
    swap_map = {Country: TLD for TLD, Country in tlds.items()}
    tlds = swap_map
    print(tlds)

    # Step G - use a dictionary comprehension to convert the country name to all uppercase letters
    print("\n")
    print("Now that I've reversed the keys and values, I'd like the capitlize the entirety of the Country names in the dictionary.")
    Capitlize_Country = {TLD: Country.upper() for TLD, Country in tlds.items()}
    tlds = Capitlize_Country
    print(tlds)

    print("\n")
    print("Thanks for looking at this dictionary with me!")

    

# Part B
# Write a python program that uses NumPy and SciPy to perform a series of tasks
def NumPy_SciPy_tasks():
    import numpy as np
    import scipy as sp
    from scipy import stats
    
    print("\n")
    print("________________________________________________________________________________________________")
    print("Now I would like to ask you to enter some values that we can use to create an array.")
    print("All values in the final array will be rounded to 3 decimal places.")
    # Step A - create a NumPy array of random numbers using minimum and maxium values input by the user along with desired number of values in the array
    while True:
        try:
            minimum = float(input("Please enter the minimum value you would like to set for the array: "))
            if minimum > 0:
                maximum = float(input("Please enter the maximum value you would like to set for the array: "))
                if maximum > minimum:
                    total_values = int(input("Please enter a whole number for the total number of values you would like to produce for the array (we need *AT LEAST* 2 to run our tests in the next stage): "))
                    if total_values >= 2:
                        random_numbers = np.random.uniform(minimum, maximum, total_values)
                        new_array = np.array(random_numbers)

                        # Step B - displays the array in a neat and orderly manner
                        print(np.round(new_array, 3))
                        print("\n")
                        break
                    else:
                        print("Your total number of values must be at least 2. Try again.")
                else:
                    print("Invalid input. Please enter a maximum value that is greater than the value entered for the minimum. Try again")
            else:
                print("Invalid input. Please enter a number value that is greater than 0. Try again.")
        except:
            print("Invalid input. Please enter a a valid number.")

    while True:
        # Step C - I couldn't find a basic way to use SciPy to find the mean, median, and variance of the array. I read about things like tmean online but it didn't seem appropriate so I used NumPy. Apologies if I misunderstood the assignment.
        print("Now that we have our array, we can run some statistical analysis on the values.")
        # Mean
        print("First, we'll determine the mean of the values in the array (rounded to 3 decimal places).")
        mean = np.mean(new_array)
        mean = round(mean, 3)
        print(f"The mean of the values in the array is {mean}")                                                             # Step D - displays the statistical property for the array with descriptive label
        print("\n")
        # Median
        print("Next we will find the median value of the array (rounded to 3 decimal places).")
        median = np.median(new_array)
        median = round(median, 3)
        print(f"The median value of the array is {median}")                                                                 # Step D - displays the statistical property for the array with descriptive label
        print("\n")
        # Variance
        print("Lastly we will find the variance of all the values in the array (rounded to 3 decimal places).")
        variance = np.var(new_array)
        variance = round(variance, 3)
        print(f"The variance of all the values in the array is {variance}")                                                 # Step D - displays the statistical property for the array with descriptive label
        break
 


# Part C
def Temp_DataFrame():
    import pandas as pd
    print("\n")
    print("_________________________________________________")

    # Step A - create a DataFrame named temperatures from a dictionary of three temperature readings each for Maxine, James, and Amanda
    print("Now we will look at some temperature readings.")
    names_temps = {'Maxine': [98.4, 97.9, 98.6], 
                   'James': [94.9, 96.0, 95.5], 
                   'Amanda': [99.0, 98.5, 100.0]}
    temperatures = pd.DataFrame(names_temps)
    print("\n")
    print("This is our current table of people and their temperature readings. I'd like to make it more specific by adding 'Morning', 'Afternoon', and 'Evening' labels.")
    print(temperatures)

    # Step B - recreate the DataFrame from part A with custom indices using the index keyword argument and a list containing Morning, Afternoon, and Evening
    print("\n")
    new_labels = ['Morning', 'Afternoon', 'Evening']
    temperatures = pd.DataFrame(names_temps, index=new_labels)
    print("Here is our new table with updated labels. It looks a little neater!")
    print(temperatures)

    # Step C - select from temperatures the column of temperature readings for Maxine
    print("\n")
    print("Lets take a closer look at Maxine's temperature readings.")
    Maxine = temperatures['Maxine']
    print(Maxine)

    # Step D - select from temperatures the row for Morning temperaute readings
    print("\n")
    print("Now let's look at just the morning temperature readings for everyone.")
    Morning = temperatures.iloc[0]
    print(Morning)

    # Step E - select from temperatures the row for Morning and Evening temperature readings
    print("\n")
    print("Let's look at morning and evening temperatures now.")
    morn_eve = temperatures.loc[['Morning', 'Evening']]
    print(morn_eve)

    # Step F - select from temperatures the columns for temperature readings for Amanda and Maxine
    print("\n")
    print("This time we will look at Amanda and Maxine's temperature readings.")
    Amanda_Maxine = temperatures[['Amanda', 'Maxine']]
    print(Amanda_Maxine)

    # Step G - select from temperatures the elements for Amanda and Maxine in the Morning and Afternoon
    print("\n")
    print("That's exactly what we were looking for, but this time I'm going to remove the 'Evening' row from the table.")
    no_evening = temperatures.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']]
    print(no_evening)

    # Step H - use the describe method to produce temperatures' descriptive statistics
    print("\n")
    print("Since we've taken several looks at the data, we should take a deeper look at the descriptive statistics for each persons readings.")
    print(temperatures.describe())

    # Step I - transpose temperatures
    print("\n")
    print("Since we've been looking at the table the same way throughout, let's transpose the data.")
    transpose_temps = temperatures.transpose()
    temperatures = transpose_temps
    print(temperatures)

    # Step J - sort temperatures so that its column names are in alphabetical order
    print("\n")
    print("Lastly, we're going to sort the temperature columns so that they are listed in alphabetical order.")
    alphabetical = temperatures[['Afternoon', 'Evening', 'Morning']]
    temperatures = alphabetical
    print(temperatures)
    print("\n")
    print("Thanks for looking at these temperatures with me. Have a great day!")

def main():
    internetDomain_Dictionary()
    NumPy_SciPy_tasks()
    Temp_DataFrame()

if __name__ == "__main__":
    main()