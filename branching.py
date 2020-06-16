import sys

suma = int(sys.argv[1]) + int(sys.argv[2])

if suma <= 0:
    print("You have chosen the path of destitution.")

elif 1 <= suma <= 100:
    print("You have chosen the path of plenty.")

elif suma > 100:
    print("You have chosen the path of excess.")
