from pathlib import Path
import os

print (''' ========== CLI FILE MANAGER ==========

        1. List Files
        2. Create File
        3. Read File
        4. Write to File
        5. Rename File
        6. Delete File
        7. Create Folder
        8. Rename Folder
        9. Delete Folder
        0. Exit
                            ''')

choice = int(input(" Enter your choice : "))




#-------- Ask for directory --------


def ask_for_directory():
    print ('''
    1. Current Directory
    2. Another Directory
    ''')
    
    directory_choice = int(input(" Enter your choice 1 or 2 : "))
    if directory_choice==1:
        print("You have selected Current Directory  ")
        selected_directory = Path.cwd()
        return selected_directory
    

    elif directory_choice==2:
        print("You have selected Another Directory  ")
    else:
        print("Invalid choice. Please select 1 or 2.")
        ask_for_directory()    
    

#----------------------------------------------------
if choice==1:
    ask_for_directory()
    
        
# if user 