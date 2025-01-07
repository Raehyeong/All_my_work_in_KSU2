def string_list_converter(input_data, input_type):
    if input_type == 'string':
        return list(input_data)
    elif input_type == 'list':
        return ''.join(input_data)
    else:
        raise ValueError("Invalid input_type. Use 'string' or 'list'.")

def list_ascii_converter(input_data, input_type):
    if input_type == 'list':
        return [ord(char) for char in input_data]
    elif input_type == 'ascii':
        return [chr(ascii_val) for ascii_val in input_data]
    else:
        raise ValueError("Invalid input_type. Use 'list' or 'ascii'.")

def ascii_binary_converter(input_data, input_type):
    if input_type == 'ascii':
        return [bin(ascii_val)[2:] for ascii_val in input_data]
    elif input_type == 'binary':
        return [int(binary_str, 2) for binary_str in input_data]
    else:
        raise ValueError("Invalid input_type. Use 'ascii' or 'binary'.")

def test_text_converter():
    inputString = input("Original String: ")
    
    # 1.String -> Characters
    char_list = string_list_converter(inputString, 'string')
    print(f"List of characters: {char_list}\n")
    
    # 2. Characters -> ASCII Codes
    ascii_list = list_ascii_converter(char_list, 'list')
    print(f"ASCII list: {ascii_list}\n")
    
    # 3. ASCII Lists -> Binary List
    binary_list = ascii_binary_converter(ascii_list, 'ascii')
    print(f"Binary list: {binary_list}\n")
    
    # 4. Binary List -> ASCII Lists
    ascii_list_back = ascii_binary_converter(binary_list, 'binary')
    print(f"ASCII list (back): {ascii_list_back}\n")
    
    # 5. ASCII Lists -> Characters
    char_list_back = list_ascii_converter(ascii_list_back, 'ascii')
    print(f"List of characters (back): {char_list_back}\n")
    
    # 6. Characters -> String
    name_back = string_list_converter(char_list_back, 'list')
    print(f"Original string (back): {name_back}\n")

test_text_converter()
