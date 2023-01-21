import sys

# a list that contains the command-line arguments passed to the script
# The first element is the name of the script itself
print(f"script name: {sys.argv[0]}")

if len(sys.argv) > 2:
    print(sys.argv[1:])
elif len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("No command-line arguments passed")
