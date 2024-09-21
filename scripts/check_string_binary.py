str_list = ["GeekforGeeks!", "1111111", "001021010001010", "000000000"]

def check_if_string_is_binary(str):
    binary = "01"
    count = 0
    for i in str:
        if i not in binary:
            count += 1
    if count > 0:
        return False
    else:
        return True

if __name__ == "__main__":
    str_list = ["GeekforGeeks!", "1111111", "001021010001010", "000000000"]
    for str in str_list:
        if check_if_string_is_binary(str):
            print(f"{str} is Binary")
        else:
            print(f"{str} is Not Binary")