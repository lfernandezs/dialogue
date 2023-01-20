from time import sleep

def dialogue(string, time=0.05):
    for char in string:
        print(char, end='', flush=True)
        sleep(time)
    print('\n')