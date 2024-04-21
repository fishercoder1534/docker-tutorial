import time

def main():
    print("Hello world!")
    i = 0
    while i < 300:
       time.sleep(1)
       i = i + 1
    print("Slept a total of {} seconds.".format(i))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Caught exception: {}.".format(e))
    print("Program finished.")
