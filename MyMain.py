#MyMain.py:
from Kvaser_01 import runWriteCanPythonic, runWriteCan  # Import the runWriteCan function

def InitFunc():
    print("This is Init.")

def main():
    InitFunc()
    runWriteCan()
    #runWriteCanPythonic(0x18FF1100)

if __name__ == "__main__":
    main()
