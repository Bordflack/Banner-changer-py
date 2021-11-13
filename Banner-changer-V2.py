#!/usr/bin/python3
#Made by Bordflack

from os import path
from subprocess import run
from random import randint
import time
from datetime import datetime
import json
bax = 0
ren = False
strtupopt = True

try:
    with open('settings.file', 'r') as load:
        loadedset = json.load(load)
        sel = loadedset['0']
        selopt = loadedset[str(sel)]
        Fhig = selopt['Fhig']
        Flow = selopt['Flow']
        Lowtim = selopt['Lowtim']
        Htim = selopt['Htim']
        ren = selopt['Rneed']
        Verb = selopt['Verb']
        ASCII = selopt['ASCII']
        strtup = selopt['Auto']     #Auto    start script without humaninteraction
    
except FileNotFoundError as err:
    try:
        print("================================================")
        print('Settings not found\nMaking new File')
        print("================================================")
        loadedset = {'0': 1, '1': {'Fhig': 1, 'Flow': 0, 'Lowtim': 30, 'Htim': 60, 'Rneed': False, 'Verb': True, 'ASCII': '/home/pi/Desktop/Cats/', 'Auto': False}, '2': {'Fhig': 1, 'Flow': 0, 'Lowtim': 30, 'Htim': 60, 'Rneed': False, 'Verb': True, 'ASCII': '/home/pi/Desktop/Cats/', 'Auto': False}, '3': {'Fhig': 1, 'Flow': 0, 'Lowtim': 30, 'Htim': 60, 'Rneed': False, 'Verb': True, 'ASCII': '/home/pi/Desktop/Cats/', 'Auto': False}}
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
    except Exception as err:
        print("ERROR")
        print(err)
        exit()
    #save = open('settings.file', 'wt')
    #loadedset = str({0: {'Selected': 1}, 1: {'Fhig': 1, 'Flow': 0, 'Lowtim': 30, 'Htim': 60, 'Rneed': False, 'Verb': True, 'ASCII': '/home/pi/Desktop/Cats/', 'Auto': False}, 2: {'Fhig': 1, 'Flow': 0, 'Lowtim': 30, 'Htim': 60, 'Rneed': False, 'Verb': True, 'ASCII': '/home/pi/Desktop/Cats/', 'Auto': False}, 3: {'Fhig': 1, 'Flow': 0, 'Lowtim': 30, 'Htim': 60, 'Rneed': False, 'Verb': True, 'ASCII': '/home/pi/Desktop/Cats/', 'Auto': False}})
    #save.write(loadedset)
    #save.close()
#except Exception as err:
#    print("================================================\n")
#    print('Error in start up\n')
#    print(err)
    #print(loadedset)
#    print("\n================================================\n")
#    exit()

if strtup == True:
    strtupopt = False
#print("Strtup")
while strtupopt == True:
    print("================================================")
    print('1.Help \n2.Options  \n3.Run  \n4.Quit')
    print("================================================")
    try:
        select = int(input('\n: '))
    except:
        print('Use numbers only please.')


    if select == 1:
        print('This script is used for changing the SSH Banner (Make sure to enable the Banner in the SSH-config file and that the file location is pointed at the correct file.)in a randomised Time in seconds.')
        print('It selects from the correctly named files and uses the content to overwrite the Banner File')
        print('\nUse this Script at your own Risk.\nIf Securety problems are found please notivy me.')
        select = input(':')
        continue
    elif select == 2:                #Reading saved options and if wanted saves them
        inset = True
        while inset == True:
            print("================================================")
            print('1.Load \n2.Edit \n3.Back')
            print("================================================")
            try:
                selset = int(input('Selection: '))
                if selset == 1:
                    try:
                        while True:
                            selset = int(input('Which to load 1-3, back with 4:'))
                            if selset >= 1 and selset <= 3:
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
                                
                                #opt = open('settings.file', 'wt')                              #change me whoop whoop
                                #opt[0] = {'Selected': selset}
                                #opt.close()
                                inset = False
                                break
                            elif selset == 4:
                                break
                            else:
                                print('Enter a number 1-4/n')
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
                            print("================================================")
                            print('Edit which Setting 1-3?\n4 for back')
                            print("================================================")
                            selset = int(input('Selection: '))
                        except:
                            print("\n================================================")
                            print('Numbers from 1-4 please')
                            print("================================================")
                        if selset >= 4:
                            break
                        elif selset >= 1 and selset <= 3:
                            
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
                                
                                
                                print('================================================')
                                print('Selected Option:',selset)
                                print('================================================')
                                                                                                                                                        #Changing temporary settings
                                while True:
                                    print('\n1.Highest file number:', tFhig, '\n2.Lowest file number:', tFlow, '\n3.Highest delay in s:', tHtim, '\n4.Lowest delay in s:', tLowtim, '\n5.Restart of ssh enabled:', tren, '\n6.Verbale mode:', tVerb, '\n7.Path to Files:', tASCII, '\n8.No intraction mode:', tstrtup)
                                    num = int(input('\n0 for selection of back or save\nSelect 1-9:'))
                                    if num == 0:
                                        num = int(input('\n0.back\n1.save\n2.exit \noptions:'))
                                        if num == 0:
                                            continue
                                                                                                                                                        #Saveing temporary settings
                                        elif num == 1:
                                            with open('settings.file', 'w') as f:
                                                loadedset[str(selset)] = {'Fhig': tFhig, 'Flow': tFlow, 'Lowtim': tLowtim, 'Htim': tHtim, 'Rneed': tren, 'Verb': tVerb, 'ASCII': tASCII, 'Auto': tstrtup}
                                                json.dump(loadedset, f, indent=2)
                                            break
                                            #opt = open('settings.file', 'wt')
                                            #opt[0] = {'Selected': selset}
                                            #opt[selset] = {'Fhig': tFhig, 'Flow': tFlow, 'Lowtim': tLowtim, 'Htim': tHtim, 'Rneed': tren, 'Verb': tVerb, 'ASCII': tASCII, 'Auto': tstrtup}
                                            #opt.close()
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
                                        print('\nuse "./" if the files are located in the same folder or in a sub folder\n')
                                        ttASCII = input('Path:')
                                        print(ttASCII)
                                        if path.isdir(ttASCII) == False:
                                            print("\n\nPlease enter a valid path to which you have access.\n\n")
                                            time.sleep(5)
                                        elif path.isdir(ttASCII) == True:
                                            tASCII = ttASCII
                                        continue
                                    elif num == 8:
                                        num = int(input('\n1 to enable 0 to disable:'))
                                        if num == 1:
                                            tstrtup = True
                                        elif num == 0:
                                            tstrtup = False
                                        continue
                                    elif num == 0:
                                        break
                                    
                            #continue
                            except Exception as err:
                                print("···ERROR···")
                                print(err)
                        else:
                            print("Enter a Number 1-3\n4 for back")
                elif selset == 3:
                    inset = False
                    continue
                else:
                    print('Enter a nuber from 1 to 3\n')
#            except:
#                print('Numbers please.')
#            try:
#                opt = open('setings.file', 'wrt')
#                with open('/home/pi/Desktop/Cats/Setings.json', 'wrt') as opt:                           #Wat tis for
#                    optionf = json.load(opt)
            except FileNotFoundError as err:
                print(err)
            except:
                print('···ERROR···')
            continue
    elif select == 3:
        strtupopt = False
        continue
    elif select == 4:
        exit()
        


#
#
#
#
#
#
#
#
#
#This worked before if no change happened it still works


while True:
    try:
        sell= randint(Flow, Fhig)                     #Change to amount of numbered Bannerfiles you have Filenum (min, max)
        tim = randint(Lowtim, Htim)                    #Randomenised time for delay in seconds (min, max)
        time.sleep(tim)

        fp = open(ASCII + str(sell), 'rt')    #'/usr/share/banner/'
        fp1 = open('/etc/ssh/Banner', 'wt')
        re = fp.read()
        fp1.write(re)
        timestamp = datetime.now()
        
        
                                                #Closing files so the changes are Readable by sshd
        if 'fp' in locals() and fp:
            fp.close()
        if 'fp1' in locals() and fp1:
            fp1.close()
                                                #Restarting the sshd server to apply the changes
        if bax == 0 and ren == True:
            try:
                subprocess.run ('/etc/init.d/ssh restart')
            except:
                bax = 1
        if bax == 1 and ren == True:
            try:
                subprocess.run ('/etc/rc.d/ssh restart')
            except:
                bax = 2
        if bax == 2 and ren == True:
            try:
                subprocess.run ('systemctl restart ssh')
            except:
                bax = 3
        if bax == 3 and ren == True:
            try:
                #subprocess.run ('systemctl restart ssh')
                print("kek")
            except:
                print("\n\n================================================")
                print("subprocess.run Error")
                print("Can also be working who knows")
                print("If this annoys you fix it yourself")
                #print(err)
                print("================================================\n")
        if ren == True:
            print("\n\n================================================")
            print(timestamp, "SSH Restarted")
            print("================================================\n")
        else:
            print("\n\n================================================")
            print(timestamp, "SSH Banner updated")
            print("================================================\n")
                                                #Error handling
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
        print("================================================\n")
        break
    except:
        print("\n\n================================================")
        print('···Error···')
        print("================================================\n")
        break
    finally:
                                                #Closing files again just to be sure
        if 'fp' in locals() and fp:
            fp.close()
        if 'fp1' in locals() and fp1:
            fp1.close()
 