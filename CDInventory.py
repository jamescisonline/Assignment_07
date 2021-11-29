#--------------------------------------------------------------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# James Crockett, 2021-Nov-27, Add Exception handling to IO, and Processing
# James Crockett, 2021-Nov-28, Convert file access to binary, fix logic errors with loading 2D 
#                              dictionary and passing content to display inventory function.
#--------------------------------------------------------------------------------------------------#

# Objectives:
#----------------
# Add structured error handling: where there is user interaction.
# A. [Done] Add structured error handling: type casting (string to int).
# B. [Done] Add structured error handling:  file access operations.
# C. [Done] Modify the permanent data store to use binary data.
# D. [Done] Update docstrings and add your involvement to the header.

import pickle

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileDat = 'CDOutput.dat' # binary ouptput file
objFile = None  # file object
intIDDel = None # delete input value


# -- PROCESSING -- #
class DataProcessor:
    # DONE add functions for processing here
        
    # save data to memory
    @staticmethod
    def add_cd(val1, val2, val3):        
        """Add CD
                Accepts 3 arguments that are recorded into a dictionary row
                and saved into memory, a 2D table.
                Includes Exception handling for keys, sequence issues, and general errors.

        Args:
                val1: used for ID value.
                val2: used for Title.
                val3: used for Artist.

        Returns: 
            None.

        """
        try:
            intID = int(val1)
            dicRow = {'ID': intID, 'Title': val2, 'Artist': val3}
            lstTbl.append(dicRow)
        except LookupError as e: #flags issues with dictionary, tuple, list index, or sequence issues.
            print('\n----Key, index mapping, or squence is invalid----\n')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()
        except Exception as e:
            print('That is a general error.')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()    
            
    # delete data from memory
    @staticmethod
    def del_cd():        
        """Prompt user for which ID value to delete from memory, a 2D table.

        Args:
            None.

        Returns: 
            None. 
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

class FileProcessor:
    """Processing the data to and from text file"""
    
    #load data file, objFile
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.
        
        Includes Exception handling for file open, close, processing issues,
        keys, sequence issues, and general errors.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        # DONE add error handling for file access
        objFile = open(strFileDat, 'ab+') #binary access, creates text file if it doesn't exist
        objFile.close()

        table.clear()  # this clears existing data and allows to load data from file
        try:
            fileObj = open(file_name, 'rb') #binary format, file read
            tbl2d = pickle.load(fileObj)
        except OSError as e:
            print('\n----Issue with opening file----\n')
            print('Error Details:')
            print(type(e), e.filename, e.__doc__, sep='\n\n') #filename method flags issues with processing file
            print()
        except FileNotFoundError as e:
            print('\n----That file does not exist----\n')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n\n')
            print()
        except LookupError as e: #flags issues with dictionary, tuple, list index, or sequence issues.
            print('\n----Key, index mapping, or squence is invalid----\n')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()
        except Exception as e:
            print('That is a general error.')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()
        return tbl2d
    
    @staticmethod
    def write_file(file_name, table):
        """Saves CD list table from memory to text file.
        
        Includes Exception handling for file open, close, processing issues,
        and general errors.
        
        Args:
            file_name: contains file name value where data is to written.
            
            table: contains value of list table name to save data from.

        Returns: 
            None. 
        """
        # TODO B2. add error handling for file access
        try:
            with open(file_name, 'wb+') as fileObj:#binary format, create if file doesn't exist, overwrite file to avoid duplicates
                pickle.dump(table, fileObj)
        except OSError as e:
            print('\n----Issue with opening file.----\n')
            print('Error Details:')
            # TODO add this in knowledge doc 
            print(type(e), e.filename, e.__doc__, sep='\n\n') #filename method flags issues with processing file
            print()
        except FileNotFoundError as e:
            print('\n----That file does not exist----\n')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n\n')
            print()
        except Exception as e:
            print('That is a general error.')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Includes Exception handling for general errors from user input choice.

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            # TODO A1. add error handling for user interaction, general exception handling only, no type validation here
            try:
                choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
                print() # add extra line for formatting
            except Exception as e:
                print('That is a general error.')
                print('Error Details:')
                print(type(e), e, e.__doc__, sep='\n')
                print()   
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def get_cd_input():        
        """Prompt user for three input values for new CD: ID, Title, Artist.
        
        Includes Exception handling for user input value, and general errors.
        
        Args:
            None.

        Returns: 
            Returns a tuple containing ID, Title, and Artist from user inputs.

        """       
        # TODO A2. add error handling for user interaction
        strID = 0
        strTitle = None
        strArtist = None
        try:
            strID = (int(input('Enter ID: ').strip()))
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
        except ValueError as e:
            print('That is not an integer.')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()
        except Exception as e:
            print('That is a general error.')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()    
        return strID, strTitle, strArtist



# 1. When program starts, read in the currently saved Inventory
lstTbl = FileProcessor.read_file(strFileDat, lstTbl) # unpack 2D dictionary from read function into lstTbl variable
# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        # DONE add error handling for user interaction, general exception handling only, no type validation here
        try:
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ').lower().strip()
        except Exception as e:
            print('That is a general error.')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstTbl = FileProcessor.read_file(strFileDat, lstTbl) # unpack 2D dictionary from read function into lstTbl variable
            
            IO.show_inventory(lstTbl)
        else:
            input('cancelling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # unpack tuple, varibles to be accessed by add_cd method
        # DONE IO called here, add error handling
        try:
            strID, strTitle, strArtist = IO.get_cd_input()  
        except LookupError as e:
            print('\n----Key, index mapping, or squence is invalid----\n')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()
        except Exception as e:
            print('That is a general error.')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()
        else:    
            # 3.3.2 Add item to the table
            DataProcessor.add_cd(strID, strTitle, strArtist)     
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        # 3.5.1.2 ask user which ID to remove
        
        try:
            IO.show_inventory(lstTbl)
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        # DONE add error handling for user interaction
        except ValueError as e:
            print('\n----That is not an integer----\n')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()
        except Exception as e:
            print('That is a general error.')
            print('Error Details:')
            print(type(e), e, e.__doc__, sep='\n')
            print()    
        # 3.5.2 search thru table and delete CD
        else:
            DataProcessor.del_cd()
            IO.show_inventory(lstTbl)
        finally:
            print('---Select "d" from menu to delete another CD---')
            print()
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(strFileDat, lstTbl) #output binary dat file used
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




