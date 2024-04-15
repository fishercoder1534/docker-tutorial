import time

def main():
    print("Hello world!")
    i = 0
    while i < 60:
       print("Sleeping for one second");
       time.sleep(1)
       i = i + 1

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Caught exception: {}.".format(e))
    print("Program finished.")
