# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgoret <vgoret@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/11 16:09:50 by vgoret            #+#    #+#              #
#    Updated: 2024/09/11 16:24:32 by vgoret           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def isNan(x) -> bool:
	return (x != x)

def NULL_not_found(object: any) -> int:
	object_type = type(object)
	if object is None:
		return(print("\033[0;31mNothing\033[0;0m:", object, object_type), 0)
	elif isNan(object):
		return (print("\033[0;31mCheese\033[0;0m:", object, object_type), 0)
	elif isinstance(object, int) and object == 0:
		return (print("\033[0;31mZero\033[0;0m:", object, object_type), 0) 
	elif isinstance(object, str) and object == " ":
		return (print("\033[0;31mEmpty\033[0;0m:", object_type), 0)
	elif isinstance(object, bool) and object == False:
		return (print("\033[0;31mFake\033[0;0m:", object, object_type), 0)
	else:
		print("\033[0;31mType not Found\033[0;0m")
	return (1)