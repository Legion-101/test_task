
def isEnum(value: int):
    bValue = bin(value)
    if int(bValue[-1:]) == 0:
        return True
    return False

def main():
    values = [22, 21, 1, 5, 6, 4, 0, 128, 111, -121]
    for value in values:
        print(isEnum(value))

if __name__ == "__main__":
    main()