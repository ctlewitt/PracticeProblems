"""
bunnies:
write a functino that takes a starting number of bunnies and a litter size andn prints out the number of bunnies in the
first 20 generations.  Remember that bunnies reproduce asexually and are immortal

"""

def bunnies(init_pop, litter_size):
    num_babies = init_pop
    num_adolescents = 0
    num_adults = 0
    for _ in range(20):
        print(num_babies + num_adolescents + num_adults)
        num_adults += num_adolescents
        num_adolescents = num_babies
        num_babies = num_adults * litter_size
print("bunnies init pop 5, litter size 3")
bunnies(5, 3)
print("bunnies init pop 0, litter size 3")
bunnies(0, 3)
print("bunnies init pop 5, litter size 0")
bunnies(5, 0)
print("bunnies init pop 2000, litter size -10")
bunnies(2000, -10)
print("bunnies init pop many, litter size lots")
bunnies(10000000, 100000000000000000000000000)
