def main():
    print("Even or Odd Checker")
    print("Type 'exit' to stop the program.")

    while True:
        user_input = input("Enter a number: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if user_input.isdigit():
            number = int(user_input)
            if number % 2 == 0:
                print(f"{number} is Even ✅")
            else:
                print(f"{number} is Odd 🔢")
        else:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()