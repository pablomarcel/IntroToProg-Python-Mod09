# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Pablo Montijo, 3.15.2021,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
from DataClasses import Employee as Emp
from ProcessingClasses import FileProcessor as Fp
from IOClasses import EmployeeIO as Eio

strFile = 'EmployeeData.txt'
lstTable = []

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts

# Show user a menu of options

while(True):

    try:
        lstFileData = Fp.read_data_from_file(strFile) # Loads data from file into list
    except Exception as e:
        print('There was a non-specific error')
        print(e, e.__doc__, type(e), sep='\n')

    Eio.print_menu_items() # prints menu options

# Get user's menu option choice

    strChoice = Eio.input_menu_options() # gets user's Choice

    # Show user current data in the list of employee objects

    if strChoice.strip() == '1':

        lstTable.clear()
        for line in lstFileData:
            lstTable.append(Emp(line[0], line[1], line[2].strip())) # adds objects to a list table

        for row in lstTable:    # prints current list
            print(row.to_string())

    # Let user add data to the list of employee objects

    elif strChoice.strip() == '2':

        lstTable.append(Eio.input_employee_data())  # adds an employee object to a list table
        for row in lstTable:    # prints current list
            print(row.to_string())


    # let user save current data to file

    elif strChoice.strip() == '3':

        Fp.save_data_to_file(strFile, lstTable) # saves a list table to the text file

    # Let user exit program

    elif strChoice.strip() == '4':  #Exits
        print("Goodbye!")
        break  # and Exit

# Main Body of Script  ---------------------------------------------------- #
