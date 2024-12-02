from package_sorter import sort 

def main():
    # Test Cases
    test_cases = [
        (50, 60, 70, 15),  # Expected "STANDARD" (Volume: 210000, Mass: 15)
        (150, 150, 150, 25),  # Expected "REJECTED" (Bulky and Heavy)
        (200, 200, 200, 10),  # Expected "SPECIAL" (Bulky, but not Heavy)
        (50, 50, 50, 25),  # Expected "SPECIAL" (Heavy, but not Bulky)
        (30, 40, 50, 5),  # Expected "STANDARD" (Neither Bulky nor Heavy)
        (100, 100, 100, 15),  # Expected "STANDARD" (Volume: 1000000, Mass: 15)
        (150, 80, 70, 30),  # Expected "SPECIAL" (Bulky and Heavy)
        (150, 80, 70, 10),  # Expected "SPECIAL" (Bulky but not Heavy)
        (100, 100, 100, 20),  # Expected "SPECIAL" (Just on the mass threshold)
        (200, 200, 200, 25),  # Expected "REJECTED" (Both Bulky and Heavy)
    ]

    # Loop through test cases and print results
    for i, (width, height, length, mass) in enumerate(test_cases, 1):
        result = sort(width, height, length, mass)
        print(f"Test case {i}: sort({width}, {height}, {length}, {mass}) => {result}")

if __name__ == "__main__":
    main()
