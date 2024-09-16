
def slice_me(family: list, start: int, end: int) -> list:
	try:
		# Vérifier que 'family' est une liste
		if not isinstance(family, list):
			raise AssertionError("Arg1 must be a list")
    	# Vérifier que chaque élément de 'family' est également une liste et de la même longueur
		#TODO
		
		if isinstance(start, int) is False or isinstance(end, int) is False:
			raise AssertionError("Start and End need to be int!")

    	# Vérifier que toutes les sous-listes ont la même longueur
		#TODO
		lenght = len(family[0])

		initial_shape = (len(family), lenght)
		print("initial shape :", initial_shape)
	except AssertionError as error:
		print(error)

def main():
	family = [[1.80, 78.4],
	[2.15, 102.7],
	[2.10, 98.5],
	[1.88, 75.2]]
	family2 = [None]
	# slice_me(family, 0, "test")
	# slice_me(family, 0, 2)
	slice_me(family, 0, 2)
	# print(slice_me(family, 0, 2))
	# print(slice_me(family, 1, -2))

if __name__ == "__main__":
    main()
