# In this script import a module and enable to recibe parameters to execute the script parameters

# to execute this file write en console
# pyton modeula_as_script.py 50 "HI SCRIPT"

if __name__ == "__main__":
    import sys
    import fibo
    fibo.fib(int(sys.argv[1]))
    print(sys.argv[2])