def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def is_anagram(first_string, second_string):
    if not first_string:
        first_string = ""
    if not second_string:
        second_string = ""

    char_list_first_string = list(first_string.lower())
    char_list_second_string = list(second_string.lower())

    char_list_first_string = merge_sort(char_list_first_string)
    char_list_second_string = merge_sort(char_list_second_string)

    result = "".join(char_list_first_string) == "".join(
        char_list_second_string
    )

    if first_string == "" or second_string == "":
        result = False

    return (
        "".join(char_list_first_string),
        "".join(char_list_second_string),
        result,
    )
