#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# TMcFarland, 2021-Mar-07, never faltered to create CD Class,
# TMcFarland, 2021-Mar-07, gonna start over on IO
# TMcFarland, 2021-Mar-08, give signficant attempt at general code flow
# TMcFarland, 2021-Mar-09, you dealt with old sample code, got functionality with objects
# TMcFarland, 2021-Mar-09, up to date comments and doc strings
#------------------------------------------#

import os.path

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []


class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # -- Constructor -- #
    def __init__(self, cid, cttl, cartst):
        # -- Attributes -- #
        self.__cd_id = None
        self.__cd_title = None
        self.__cd_artist = None
        self.cd_id = cid
        self.cd_title = cttl
        self.cd_artist = cartst

    # -- Properties -- #
    @property  #getter
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        if type(value) == int:
            self.__cd_id = value
        else:
            raise Exception('This entry requires an interger (whole positive number)')

    @property  #getter
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        if type(value) == str:
            self.__cd_title = value
        else:
            raise Exception('This entry requires a Stirng (just type in the title of the CD!')

    @property #getter
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        if type(value) == str:
            self.__cd_artist = value
        else:
            raise Exception('This entry requires a String (Just type in the name of the artist!)')

    # -- Methods -- #
    def defaultResponse(self):
        return self.cd_id, self.cd_title, self.cd_artist

    def __str__(self):
        return self.defaultResponse()


class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
            Takes list of CD Objects
            Converts to text, CSV formatted
            Saves that to text file
        load_inventory(file_name): -> (a list of CD objects)
            Loads CSV formated .txt file
            When read is converted to multiple cd OBJECTS
    """

    @staticmethod
    def load_inventory(textFile, cdClass, cdTable):
        """Function to manage data ingestion from file to a list of objects

        Reads the data from file identified by textFile into a 2D table
        (list of objects). One line in the file represents one object in table.

        Args:
            textFile (string): name of file used to read the data from
            cdClass (Class): Uses as template to create objects
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            None
        """
        cdTable.clear()  # this clears existing data and allows to load data from file
        #check to see if database file already exists. If not, create blank one.
        fileCreated = False
        if os.path.exists(textFile):
            try:
                objFile = open(textFile, 'r')
                for row in objFile:
                    cdObjInfo = row.strip().split(',')
                    cdObj = cdClass(int(cdObjInfo[0]), cdObjInfo[1], cdObjInfo[2])
                    cdTable.append(cdObj)
                objFile.close()
            except EOFError as e:
                print('Your CDInventory.dat file is blank!')
                print('Here\'s what the computer has to say about this:')
                print(type(e), e, e.__doc__, sep = '\n') #syntax from FDN_Py_module_07, pg 20, listing 12
        else:
            #create blank database in same folder as script
            objFile = open(textFile, 'w')
            objFile.close()
            fileCreated = True
        return fileCreated, cdTable

    @staticmethod
    def save_inventory(textFile, cdTable):
        """Writes List of Dicitonaries lstTbl from memory into a text file.
        Ensures proper comma seperated formatting for best storage and retrieval
        Args:
            testFile: references a text file, with comma three seperated values.
            cdTable: list of objects, each object holding three pieces of cd information

        Returns:
            None
        """
        objFile = open(textFile, 'w')
        for row in cdTable:
            objFile.write('{},{},{}\n'.format (row.cd_id, row.cd_title, row.cd_artist))
        objFile.close()



# -- PRESENTATION (Input/Output) -- #
class IO:

    """""Handling Input / Output. Takes input from user and adds to database. Loads database.

    properties:

    methods:
        print_menu:  Displays menu to user
        menu_choice:  Gets user input for menu selection
        show_inventory:  Displays current inventory table
        user_cd_input:  Receives user input for CD ID number, Album Title, and Artist Name
    """

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('\n\n-  ---------------+= CD INVENTORY 2000 =+---------------  -')
        print('\nMenu')
        print('\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of objects: 2D data structure that holds the data during runtime.

        Returns:
            None.
        """

        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by: {})'.format (row.cd_id, row.cd_title, row.cd_artist))
        print('======================================')

    @staticmethod
    def user_cd_input():
        """ Receives user input for CD ID number, Album Title, and Artist Name
        Args:
            None
        Returns:
            CD ID number, CD Title, CD Artist Name
        """

        # Ask user for new ID, CD Title and Artist
        while True:
            try:
                intID = int(input('Enter ID: ').strip())
                break
            except ValueError as e:
                print('That does not appear to be an integer. Try again.')
                print('Here\'s what the computer has to say about this:')
                print(type(e), e, e.__doc__, sep = '\n') #syntax from FDN_Py_module_07, pg 20, listing 12
            except Exception as e:
                print('There was some sort of general error, please try again')
                print('Here\'s what the computer has to say about this:')
                print(type(e), e, e.__doc__, sep = '\n')
        while True:
            strTitle = input('What is the CD\'s title? ').strip()
            if strTitle == '':
                print('For the love of God, please enter *something*')
                continue
            else:
                break
        while True:
            strArtist = input('What is the Artist\'s name? ').strip()
            if strArtist == '':
                print('For the love of God, please enter *something*')
                continue
            else:
                break
        return intID, strTitle, strArtist


# -- SCRIPT MAIN BODY -- #

# Load text file & convert into List of Objects on Launch
try:
    noDatFilePresent, lstOfCDObjects = FileIO.load_inventory(strFileName, CD, lstOfCDObjects)
    #check to see if  FileProcessor.load_inventory returned a Bool of True. if so, DB file didn't exist
    if noDatFilePresent:
        print('\nCDInventory.txt didn\'t exist in folder. A blank version has been created\n')
except:
    print('Error during file load, starting with empty database')

while True:
    #Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # MENU SELECTIONS
    # EXIT
    if strChoice == 'x':
        break

    # LOAD process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...\n')
            fileCreated, lstOfCDObjects = FileIO.load_inventory(strFileName, CD, lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.\n')
        IO.show_inventory(lstOfCDObjects)
        continue

    # ADD CD: process add a CD
    elif strChoice == 'a':
        #assign received data from user variables from return of IO.user_cd_input
        recIntId, recStrTitle, recStrArtist = IO.user_cd_input()
        #create CD object
        cd = CD(recIntId, recStrTitle, recStrArtist)
        #append list
        lstOfCDObjects.append(cd)
        #show updated inventory
        IO.show_inventory(lstOfCDObjects)
        continue

    # DISPLAY INVENTORY: process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue

    # SAVE: process save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        #Process choice
        if strYesNo == 'y' or 'yes':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            print('Saved to file\n')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue

    # CATCH ALL
    else:
        print('General Error')




