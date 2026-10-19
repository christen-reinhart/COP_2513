# Practice 8 - practice with positional and keyword arguments

### Do not modify the functions below. ###

def order_soup(flavor, temperature):
    # returns the results
    return f"You ordered {temperature} {flavor} soup." 

def order_tea(flavor="matcha", temperature="iced", milk=False):
    # prints the results
    print(f"You ordered {temperature} {flavor} tea", end=" ")
    if milk:
        print("with milk.")
    else:
        print("without milk.")
    
# main code #

#TODO # Add the function calls with the correct arguments to print the expected output.

### Add your code in the spaces between the comments

print("----- SOUP -----")

# 1.
# Call order_soup() using only positional arguments.
# Expected output: You ordered hot tomato soup.

print(order_soup("tomato", "hot"))

# 2.
# Call order_soup() using only keyword arguments
# Expected output: You ordered warm butternut squash soup.

print(order_soup(flavor="butternut squash", temperature="warm"))

# 3.
# Call order_soup() using one positional argument and one keyword argument
# Expected output: You ordered cold cucumber soup.

print(order_soup("cucumber", temperature="cold"))

print("----- TEA -----")

# 4.
# Call order_tea() to print the expected output.
# If any argument is the same as the default value, do not pass that argument.
# Output: You ordered iced matcha tea without milk.

order_tea()

# 5.
# Call order_tea() to print the expected output.
# If any argument is the same as the default value, do not pass that argument.
# Output: You ordered iced matcha tea with milk.

order_tea(milk=True)

# 6.
# Call order_tea() to print the expected output.
# If any argument is the same as the default value, do not pass that argument.
# Output: You ordered iced mint tea with milk.

order_tea(flavor="mint", milk=True)
