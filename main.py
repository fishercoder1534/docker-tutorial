
def main():
    print("Hello world!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Caught exception: {}.".format(e))
    print("Program finished.")
