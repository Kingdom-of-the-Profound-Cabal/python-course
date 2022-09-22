import sys

if len(sys.argv) > 2:
    print(sys.argv[1:])
elif len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("No command-line arguments passed")
