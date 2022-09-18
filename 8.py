def dec_to_binary(n):
    bin_num = bin(n)[2:].rjust(8, "0")
    return bin_num


# Main function
if __name__ == "__main__":

    # take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the n value
    for case in range(1, test_cases + 1):
        # take the n input values
        n = int(input())
        # Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
        bin_num = dec_to_binary(n)
        print(bin_num)
