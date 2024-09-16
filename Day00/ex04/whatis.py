# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgoret <vgoret@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/11 16:26:14 by vgoret            #+#    #+#              #
#    Updated: 2024/09/12 15:36:01 by vgoret           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def checkArgs() -> bool:
	try:
		assert len(sys.argv) == 2, "AssertionError: wrong number of arguments"
	except AssertionError as msg:
		print(msg)
		return (False)
	try:
		num = int(sys.argv[1])
		assert isinstance(num, int), "AssertionError: argument is not an int"
	except ValueError:
		return (print("ValueError: argument is not a valid integer"), False)
	except AssertionError as msg:
		return (print(msg), False)
	return (True)



def isOddOrEven() -> None:
	if checkArgs() == True :
		num = int(sys.argv[1])
		if num % 2 == 0:
			print("Im \033[32mEven\033[0m!")
		else:
			print("Im \033[31mOdd\033[0m!")

isOddOrEven()