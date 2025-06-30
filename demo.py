import os,time,subprocess
def kill_program():

    subprocess.run(['taskkill','/F','/IM','cmd.exe'])
    time.sleep(1)

kill_program()