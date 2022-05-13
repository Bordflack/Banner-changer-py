#!/usr/bin/python3
# Made by Bordflack

from os import path
from subprocess import run
from random import randint
import time
from datetime import datetime
import json

Try = 0
ren = False
strtupopt = True

############################### Path to the Banner file

path_banner = '/etc/ssh/Banner'

###############################

try:
    with open('settings.file', 'r') as load:
        loadedset = json.load(load)  # opening the settings file
        sel = loadedset['0']  # which setting to be loaded of the 3
        selopt = loadedset[str(sel)]  # Loading selected file 1,2 or 3
        Fhig = selopt['Fhig']  # Highest file number
        Flow = selopt['Flow']  # Lowest file number 0 or 1 depending on how they are managed
        Lowtim = selopt['Lowtim']  # Shortest delay time
        Htim = selopt['Htim']  # Highest delay time
        ren = selopt['Rneed']  # Restart of the ssh daemon if needed
        Verb = selopt['Verb']  # Verbal mode
        ASCII = selopt['ASCII']  # Path to the ASCII art folder
        strtup = selopt['Auto']  # Auto start script without human interaction
    print("\n\n================================================")
    print("Loaded settings")
    print("================================================\n")

except FileNotFoundError as err:
    try:
        # Creating a new Setting file if the old one is not found at the locations
        # and also loading the standard settings
        print("\n\n================================================")
        print('Settings not found\nMaking new File')
        print("================================================\n")
        loadedset = {'0': 1,
                     '1': {'Fhig': 2, 'Flow': 0, 'Lowtim': 30, 'Htim': 60, 'Rneed': False, 'Verb': True,
                           'ASCII': './Examples/', 'Auto': False},
                     '2': {'Fhig': 2, 'Flow': 0, 'Lowtim': 30, 'Htim': 60, 'Rneed': False, 'Verb': True,
                           'ASCII': './Examples/', 'Auto': False},
                     '3': {'Fhig': 2, 'Flow': 0, 'Lowtim': 30, 'Htim': 60, 'Rneed': False, 'Verb': True,
                           'ASCII': './Examples/', 'Auto': False}}
        sel = 1
        selopt = loadedset['1']
        Fhig = selopt['Fhig']
        Flow = selopt['Flow']
        Lowtim = selopt['Lowtim']
        Htim = selopt['Htim']
        ren = selopt['Rneed']
        Verb = selopt['Verb']
        ASCII = selopt['ASCII']
        strtup = selopt['Auto']
        with open('settings.file', 'w') as f:
            json.dump(loadedset, f, indent=2)
        print("\n\n================================================")
        print("Created new settings file")
        print("\n\n================================================\n")
    except Exception as err:
        print("\n\n================================================")
        print("ERROR")
        print(err)
        print("================================================\n")
        exit()

if strtup == True:
    strtupopt = False
while strtupopt == True:
    print("\n\n================================================")
    print('1.Help \n2.Options  \n3.Run  \n0.Quit')
    print("================================================\n")
    try:
        select = int(input('\n: '))
    except:
        print('Use numbers only please.')

    if select == 1:
        print("\n\n================================================")
        print('This script is used for changing the SSH Banner or other banner files if wanted (Make sure to enable '
              'the Banner in the SSH-config file and that the file location is pointed at the correct file.)in a '
              'randomised Time in seconds.')
        print('It selects from the correctly named files and uses the content to overwrite the Banner File')
        print('\nUse this Script at your own Risk. Or read through it for assurance what your running')
        print("================================================\n")
        select = input(':')
        continue
    elif select == 2:  # Reading saved options and if wanted saves them
        inset = True
        while inset == True:
            print("\n\n================================================")
            print('1.Load \n2.Edit \n0.Back')
            print("================================================\n")
            try:
                selset = int(input('Selection: '))
                if selset == 1:
                    try:
                        while True:
                            selset = int(input('Which to load 1-3, back with 0:'))
                            if 1 <= selset <= 3:
                                selopt = loadedset[str(selset)]
                                Fhig = selopt['Fhig']
                                Flow = selopt['Flow']
                                Lowtim = selopt['Lowtim']
                                Htim = selopt['Htim']
                                ren = selopt['Rneed']
                                Verb = selopt['Verb']
                                ASCII = selopt['ASCII']
                                strtup = selopt['Auto']

                                with open('settings.file', 'w') as f:
                                    loadedset['0'] = selset
                                    json.dump(loadedset, f, indent=2)
                                inset = False
                                print("\n\n================================================")
                                print("Loaded setting:", selset)
                                print("================================================\n")
                                break
                            elif selset == 0:
                                break
                            else:
                                print('Enter a valid number 0-3/n')
                                continue
                    except Exception as err:
                        print("\n================================================")
                        print('Failed loading settings file.')
                        print(err)
                        print("================================================")
                        continue
                elif selset == 2:
                    while True:
                        try:
                            print("\n\n================================================")
                            print('Edit which Setting 1-3?\n0 for back')
                            print("================================================\n")
                            selset = int(input('Selection: '))
                        except:
                            print("\n================================================")
                            print('Numbers from 0-3 please')
                            print("================================================")
                        if selset == 0:
                            break
                        elif 1 <= selset <= 3:
                            try:
                                tselopt = loadedset[str(selset)]
                                tFhig = tselopt['Fhig']
                                tFlow = tselopt['Flow']
                                tLowtim = tselopt['Lowtim']
                                tHtim = tselopt['Htim']
                                tren = tselopt['Rneed']
                                tVerb = tselopt['Verb']
                                tASCII = tselopt['ASCII']
                                tstrtup = tselopt['Auto']
                                print('\n\n================================================')
                                print('Selected Option:', selset)
                                print('================================================\n')
                                # Changing temporary settings
                                while True:
                                    print("\n\n================================================")
                                    print('\n1.Highest file number:', tFhig, '\n2.Lowest file number:', tFlow,
                                          '\n3.Highest delay in s:', tHtim, '\n4.Lowest delay in s:', tLowtim,
                                          '\n5.Restart of ssh enabled:', tren, '\n6.Verbal mode:', tVerb,
                                          '\n7.Path to Files:', tASCII, '\n8.No interaction mode:', tstrtup)
                                    print("================================================\n")
                                    try:
                                        num = int(input('\n0 for back or save\nSelect 1-8:'))
                                    except Exception as err:
                                        print(err)
                                        continue
                                    if num == 0:
                                        print("\n\n================================================")
                                        num = int(input('\n0.back\n1.save\n2.exit \noptions:'))
                                        print("================================================\n")
                                        if num == 0:
                                            continue
                                            # Saving temporary settings
                                        elif num == 1:
                                            with open('settings.file', 'w') as f:
                                                loadedset[str(selset)] = {'Fhig': tFhig, 'Flow': tFlow,
                                                                          'Lowtim': tLowtim, 'Htim': tHtim,
                                                                          'Rneed': tren, 'Verb': tVerb, 'ASCII': tASCII,
                                                                          'Auto': tstrtup}
                                                json.dump(loadedset, f, indent=2)
                                            print("\n\n================================================")
                                            print("Settings saved")
                                            print("================================================\n")
                                            break
                                        elif num == 2:
                                            break
                                    elif num == 1:
                                        tFhig = int(input('\n:'))
                                        continue
                                    elif num == 2:
                                        tFlow = int(input('\n:'))
                                        continue
                                    elif num == 3:
                                        tHtim = int(input('\n:'))
                                        continue
                                    elif num == 4:
                                        tLowtim = int(input('\n:'))
                                        continue
                                    elif num == 5:
                                        num = int(input('\n1 to enable 0 to disable:'))
                                        if num == 1:
                                            tren = True
                                        elif num == 0:
                                            tren = False
                                        continue
                                    elif num == 6:
                                        num = int(input('\n1 to enable 0 to disable:'))
                                        if num == 1:
                                            tVerb = True
                                        elif num == 0:
                                            tVerb = False
                                        continue
                                    elif num == 7:
                                        print('\nuse of "./" may not work\n')
                                        print('Give the absolute path to the Folder.\n')
                                        ttASCII = input('Path:')
                                        print(ttASCII)
                                        if path.isdir(ttASCII) == False:
                                            print("\n\nPlease enter a valid path to which you have access.\n\n")
                                            time.sleep(1)
                                        elif path.isdir(ttASCII) == True:
                                            tASCII = ttASCII
                                        continue
                                    elif num == 8:
                                        num = int(input('\n1 to enable 0 to disable:'))
                                        if num == 1:
                                            print("\n\n================================================")
                                            tmp = input(
                                                "Are you sure?\nThis setting will when loaded skip the user input "
                                                "section\nand start the script directly.\nY or N:")
                                            print("================================================\n")
                                            if tmp == 'Y':
                                                tstrtup = True
                                            else:
                                                continue
                                        elif num == 0:
                                            tstrtup = False
                                        continue
                                    elif num == 0:
                                        break
                            # continue
                            except Exception as err:
                                print("···ERROR···")
                                print(err)
                        else:
                            print("Enter a number 1-3\n0 for back")
                elif selset == 0:
                    inset = False
                    continue
                else:
                    print('Enter a number from 1 to 3\n')
            except FileNotFoundError as err:
                print("\n\n================================================")
                print(err)
                print("================================================\n")
            except Exception as err:
                print("\n\n================================================")
                print('···ERROR···')
                print(err)
                print("================================================\n")
            continue
    elif select == 3:
        strtupopt = False
        continue
    elif select == 0:
        print("\n\n================================================")
        print("Bye bye see you soon")
        print("================================================")
        exit()

#
#
#
# Main script part that changes the File content
print("\n\n================================================")
print("Program running")
print("================================================\n")

while True:
    try:
        sell = randint(Flow, Fhig)  # Filenum (min, max)
        tim = randint(Lowtim, Htim)  # Randomised time for delay in seconds (min, max)
        time.sleep(tim)

        fp = open(ASCII + str(sell), 'rt')  # '/usr/share/banner/'
        fp1 = open(path_banner, 'wt')
        re = fp.read()
        fp1.write(re)
        timestamp = datetime.now()

        # Closing files so the changes are Readable by sshd
        if 'fp' in locals() and fp:
            fp.close()
        if 'fp1' in locals() and fp1:
            fp1.close()
            # Restarting the sshd server to apply the changes
        if Try == 0 and ren == True:
            try:
                subprocess.run('/etc/init.d/ssh restart')
            except:
                Try = 1
        if Try == 1 and ren == True:
            try:
                subprocess.run('/etc/rc.d/ssh restart')
            except:
                Try = 2
        if Try == 2 and ren == True:
            try:
                subprocess.run('systemctl restart ssh')
            except:
                Try = 3
        if Try == 3 and ren == True:
            print("\n\n================================================")
            print("subprocess.run Error")
            print("Can also be working who knows")
            print("If this annoys you fix it if you wanna")
            print("================================================\n")
        if ren == True:
            print("\n\n================================================")
            print(timestamp, "SSH Restarted")
            print("================================================\n")
        elif Verb == True and ren == False:
            print("\n\n================================================")
            print(timestamp, "SSH Banner updated")
            print("================================================\n")
            # Error handling
    except FileNotFoundError as err:
        print("\n\n================================================")
        print(err)
        print("================================================\n")
    except PermissionError as err:
        print("\n\n================================================")
        print(err)
        print("================================================\n")
        break
    except KeyboardInterrupt:
        print("\n\n================================================")
        print("Interrupted by User")
        print("Bye bye")
        print("================================================\n")
        if 'fp' in locals() and fp:
            fp.close()
        if 'fp1' in locals() and fp1:
            fp1.close()
        break
    except Exception as err:
        print("\n\n================================================")
        print('···Error···')
        print(err)
        print("================================================\n")
        break
