#!/usr/bin/python3

from subprocess import run
from random import randint
import time
from datetime import datetime
bax = 0
ren = False

while True:
    try:
        sel = randint(1, 16)                     #Change to amount of numbered Bannerfiles you have Filenum (min, max)
        tim = randint(6, 20)                    #Randomenised time for delay in seconds (min, max)
        time.sleep(tim)

        fp = open('/home/pi/Desktop/Cats/' + str(sel), 'rt')    #'/usr/share/banner/'
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
        if bax == 0 & ren == True:
            try:
                subprocess.run ('/etc/init.d/ssh restart')
            except:
                bax = 1
        if bax == 1 & ren == True:
            try:
                subprocess.run ('/etc/rc.d/ssh restart')
            except:
                bax = 2
        if bax == 2 & ren == True:
            try:
                subprocess.run ('systemctl restart ssh')
            except:
                bax = 3
        if bax == 3 & ren == True:
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
        print('...Error...')
        print("================================================\n")
        break
    finally:
                                                #Closing files again just to be sure
        if 'fp' in locals() and fp:
            fp.close()
        if 'fp1' in locals() and fp1:
            fp1.close()
