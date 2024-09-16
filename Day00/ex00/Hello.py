# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgoret <vgoret@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/11 16:07:38 by vgoret            #+#    #+#              #
#    Updated: 2024/09/11 16:07:39 by vgoret           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#list
ft_list[1] = "World!"

#tuple
ft_tuple = ("Hello", "France!")

#set
ft_set.remove('Hello')
ft_set.remove('tutu!')
ft_set.add('Paris!')
ft_set.add('Hello')

#dict
ft_dict["Hello"] = '42Paris!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)