try:
    x=int(input("Enter a  num"))
    print(x)
except ValueError:
    print("plz enter a integer")
except Exception:
    print("some other type of error")
