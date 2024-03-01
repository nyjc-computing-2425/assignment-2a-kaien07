num = input('Enter a number (decimal or integer): ')

# type your code here
new_num = num.lstrip("0.").replace(".", "")
sf = len(new_num)

# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
