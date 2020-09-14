def main():
    for i in range(1, 101):
        print(fizzbuzz(i))


def fizzbuzz(num):
    if num == 42:
        return "HGTTG quote here"
    # using an empty string to allow for easy expansion
    output = ""
    if num % 3 == 0:
        output += "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    if output == "":
        return num
    return output


if __name__ == "__main__":
    main()
