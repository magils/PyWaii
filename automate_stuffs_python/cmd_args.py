import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("values", type=str, nargs="+")
    parser.add_argument("--file","-f",help="Testing")

    args = parser.parse_args()

    print(args.file)
    print(args.values)