'''A toy store usually do mail order sales and the logistics company charges them by weight
of each package so they must calculate the weight of the clowns and dolls that will come out
in each package on demand. Each clown weighs 112g and each doll 75g. Create a
program that reads the number of clowns and dolls sold in the last order and
calculate the total weight of the package to be shipped.'''


number_c = int(input('Number of clowns sold: '))
number_d = int(input('Number of dolls sold: '))

clown = 112 #grams
doll = 75 #grams
package = number_c * clown + number_d * doll

if package < 1000:
    print(f'The total weight of the package is {package} grams.')
else:
    package /= 1000
    print(f'The total weight of the package is {package} kilos.')
