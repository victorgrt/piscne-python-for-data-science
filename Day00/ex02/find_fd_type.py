def all_thing_is_obj(object: any) -> int:
    if (isinstance(object, list)):
        print("List:\033[95m", type(object), "\033[0m")
    elif (isinstance(object, dict)):
        print("Dict:\033[95m", type(object), "\033[0m")
    elif (isinstance(object, tuple)):
        print("Tuple:\033[95m", type(object), "\033[0m")
    elif (isinstance(object, set)):
        print("Set:\033[95m", type(object), "\033[0m")
    elif (isinstance(object, str)):
        tmp = object
        print("\033[95m" + tmp,
              "\033[0mis in the kitchen :\033[95m", type(object), "\033[0m")
    else:
        print("\033[91mType Not Found\033[0m")
    return 42
