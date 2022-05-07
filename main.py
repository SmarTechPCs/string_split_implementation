def whitespaces_split(input_string):
    prev_space_end_index = -1
    split_string_list = []
    string_length = len(input_string)

    for current_index in range(string_length):
        if input_string[current_index].isspace():
            # If a word ending in the previous index was found
            # then, save it - substring
            if current_index - prev_space_end_index > 1:
                split_string_list.append(input_string[prev_space_end_index+1 : current_index])
                # print("added word:", input_string[prev_space_end_index + 1:current_index])
            prev_space_end_index = current_index

    # Adding trailing word if any
    if input_string and not input_string[string_length - 1].isspace():
        split_string_list.append(input_string[prev_space_end_index+1 : string_length])

    return split_string_list


if __name__ == "__main__":
    print("list:", whitespaces_split("To be or not to be, that is the question"))
    print("list:", whitespaces_split("To be or not to be,that is the question"))
    print("list:", whitespaces_split("   "))
    print("list:", whitespaces_split(" abc "))
    print("list:", whitespaces_split(""))
    print("list:", whitespaces_split("  hello \n"))
    print("list:", whitespaces_split("  hello \n world"))
    print("list:", whitespaces_split("""one two
    three """))
    print("list:", whitespaces_split("nothing"))