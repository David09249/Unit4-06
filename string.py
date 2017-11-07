# Created by: David Wang
# Created on: 10-Nov-2017
# Created for: ICS3U
# Daily Assignment - Unit4-06
# This program displays

def compare_strings(first_input_string, second_input_string):
    first_input_string = first_input_string.upper()
    second_input_string = second_input_string.upper()
    
    if first_input_string == second_input_string:
        return True
    else:
        return False

first_string = raw_input('Input the first string: ')
first_string = str(first_string)
second_string = raw_input('Input the second string: ')
second_string = str(second_string)
equal = compare_strings(first_string, second_string)
if equal == True:
    print("The string '" + first_string + "' and the string '" + second_string + "' " + " are the same.")
elif equal == False:
    print("The string '" + first_string + "' and the string '" + second_string + "' " + " are not the same.")
