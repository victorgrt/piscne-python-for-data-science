from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_blue
from pimp_image import ft_green


array = ft_load("landscape.jpg")

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
# ft_grey(array)
print(ft_invert.__doc__)
print(ft_green.__doc__)
print(ft_blue.__doc__)
print(ft_red.__doc__)
