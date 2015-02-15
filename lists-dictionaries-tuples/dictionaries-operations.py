# -----------------------------------------------------------
# demonstrates how to work with dictionaries (basic operations)
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define a dictionary of capitals
capitals = {
	"Norway": "Oslo",
	"Germany": "Berlin",
	"France": "Paris"
}
print("original:", capitals)

# add a capital
capitals["Switzerland"] = "Bern"
print("modified:", capitals)

# remove a capital
del capitals["Norway"]
print("modified:", capitals)

# count the number of capitals
print("number of elements:", len(capitals))

# clear the dictionary
capitals = {}
print("empty disctionary:", capitals)

