#!/usr/bin/env python

"""
    Author: John Vardanian
    Last Modified: 2016-06-18
    Python3.5 using PyCharm / Atom / Sublime Text 3

    r0.0.9-2016-06-18(a)

    Generate a dictionary list as a text file using permutations of terms
    delimited by a comma. Terms are intended to be accumulated during
    information gathering phase of a penetration test. The more relevant the
    terms, the higher chance of success.

    Usage:
    Currently no type checking. Enter each categorized set of terms separated
    by commas- no spaces at this time.
"""

import itertools
import shlex


def numeric_alternatives(term):
    """
        Replace numeric chars within a string with common substitutions of
        letters, spelling, and symbols.

        :param term: string
        :return new_term: term with all numbers replaced by common alternatives
        :rtype: string
    """
    new_term = ""
    number_alt_dict = {'0': ['O', 'zero'], '1': ['l', 'i', '|', 'one'],
                       '2': ['z', 'two'], '3': ['E', 'three'],
                       '4': ['A', 'four'], '5': ['S', 'five'],
                       '6': ['G', 'six'], '7': ['T', 'seven'],
                       '8': ['B', 'eight'], '9': ['G', 'nine']}
    for letter in term:
        if letter in number_alt_dict:
            new_term += number_alt_dict[letter][0]
        else:
            new_term += letter
    return new_term


def simple_letter_alternatives_full(term):
    """
        Replace alpha chars within a string with common substitutions of
        numbers and symbols.

        :param term: string
        :return new_term: term with all letters replaced by common alternatives
        :rtype: string
    """
    new_term = ""
    letter_alt_dict = {'a': ['@'], 'b': ['8'], 'e': ['3'], 'i': ['!'],
                       'l': ['1'], 'o': ['0'], 's': ['$'], 't': ['7'],
                       'Z': ['2']}
    for letter in term:
        if letter in letter_alt_dict:
            new_term += letter_alt_dict[letter][0]
        else:
            new_term += letter
    return new_term


def letter_alternatives_permute(term):
    """
        Replace alpha chars within a string with common substitutions of
        numbers and symbols.

        :param term: string
        :return new_terms: list of strings derived from term with replacements
        :rtype: list
    """
    letter_alt_dict = {'a': ['@', '4'], 'b': ['8'], 'c': ['(', '['],
                       'e': ['3'], 'g': ['6', '9'], 'h': ['#'],
                       'i': ['!', '|', 'eye'], 'l': ['1', 'el'],
                       'o': ['0', 'oh'], 's': ['5', '$'], 't': ['+', '7'],
                       'Z': ['2', 'zee']}
    new_terms = []
    index = 0
    while index < len(term):
        letter_list = list(term)
        if letter_list[index] in letter_alt_dict:
            letter_list[index] = letter_alt_dict[letter_list[index]][0]
            new_terms.append(''.join(letter_list))
        index += 1

    return new_terms


def alternate_case(term, first):
    """
        Change case to alternate_case between lower and upper; if first is true
        begin with the fist char in caps.

        :param term: string
        :param first: boolean
        :return ret: permutation of term with alternating casing on letters
        :rtype: string
    """
    ret = ""
    for char in term:
        if first:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            first = not first
    return ret


def permute_phone(phone):
    """
        Return list of various phone permutations (area code, reversed etc).

        :param phone:
        :return: list of 6 phone number permutations of arg phone
        :rtype: list
    """
    return [phone, phone[3:], phone[0:3], phone[6:], phone[::-1],
            reverse_term(phone[0:3])]


def permute_case(term):
    """
        Return list of term with title case, all lower, and all upper.

        :param term: base string to case upper, title, & lower
        :return: list
        :rtype: list
    """
    return [term.upper(), term.lower(), term.capitalize()]


def permute_year(year):
    """
        Return list of common year perms. (last 2 digits, backwards, etc).

        :param year: string
        :return: list of 4 permuted strings derived from argument year
        :rtype: list
    """
    return [year[2:], year, year[::-1], '_' + str(year)]


def reverse_term(term):
    """
        Return string in reverse.

        :param term: string
        :return: argument term in reverse as string
        :rtype: string
    """
    return term[::-1]


def full_string_permutation(term):
    """
        Return all permutations of a string in a list.

        :param term: string
        :return: list of all permutations of argument 'term'
        :rtype: list
    """
    words = []
    res = itertools.permutations(term, len(term))
    for i in res:
        words.append(''.join(i))
    return words


def split_by_comma(prompt):
    """
        Return list of items exploded by char ',' and trimmed of whitespace.

        :param prompt: string
        :return: list exploded by commas
        :rtype: list
    """
    temp = input(prompt + ": ")
    temp = ','.join(shlex.split(temp))
    return [x.strip() for x in temp.split(',')]


def permute_zip_code(zip_code):
    """
        Return list of string zip_code with 3 variations.

        :param zip_code: string
        :return: list of strings of permuted zip code argument
        :rtype: list
    """
    return [reverse_term(zip_code), numeric_alternatives(zip_code), zip_code]


def permute_music(music):
    """
        Return common permutations of music related terms.

        :param music: string
        :return: list of permuted variations of string 'music'
        :rtype: list
    """
    return permute_case(music) + [reverse_term(music)] + [
        alternate_case(music, True)] + [alternate_case(music, False)] + [
               simple_letter_alternatives_full(music)]


def permute_street_number(street_number):
    """
        Return common permutations of street numbers.

        :param street_number: string
        :return: list of permutations of a street number
        :rtype: list
    """
    return [street_number, reverse_term(street_number),
            numeric_alternatives(street_number), "_" + str(street_number),
            str(street_number) + "_"]


def generic_permuted_list(temp_list):
    """
        Return a list containing most frequently used permutation functions

        :param temp_list:
        :return new_list: most common variations of terms to be used in dict
        :rtype: list
    """
    new_list = []
    for temp in temp_list:
        new_list += letter_alternatives_permute(temp)
        new_list += letter_alternatives_permute(alternate_case(temp, True))
        new_list += letter_alternatives_permute(alternate_case(temp, False))
        new_list += letter_alternatives_permute(permute_case(temp))
        new_list += permute_case(temp)
        new_list.append(alternate_case(temp, True))
        new_list.append(alternate_case(temp, False))
        new_list.append(reverse_term(temp))
    return new_list


def permute_lists(first, second):
    """
        Return list of all combinations of words from lists sent as args

        :param first: list
        :param second: list
        :return temp_list: list of combined words from arguments
        :rtype: list
    """
    temp_list = []
    for first_item in first:
        for second_item in second:
            temp_list.append(first_item + second_item)
            temp_list.append(second_item + first_item)
    return temp_list


def main():
    """
        All code below currently for testing and proof of concept. Generate
        text file of potential passwords (dictionary list), tailored towards
        information gathered during initial phase of pen test.
    """
    final_collection = []

    years = split_by_comma("Years")
    pet_names = split_by_comma("Pets")
    sports = split_by_comma("Sports")
    music = split_by_comma("Music")
    family_members = split_by_comma("Family")
    phone_numbers = split_by_comma("Phones")
    states = split_by_comma("States")
    cities = split_by_comma("Cities")
    zip_codes = split_by_comma("Zip codes")
    streets = split_by_comma("Street names")
    street_numbers = split_by_comma("Street numbers")
    schools = split_by_comma("Schools")
    colors = split_by_comma("Colors")
    other_terms = split_by_comma("Other terms")

    print("\nPlease wait while your dictionary is generated. " +
          "This may take several minutes.\n")

    year_list = []
    for year in years:
        year_list += permute_year(year)
    pet_list = generic_permuted_list(pet_names)
    sports_list = generic_permuted_list(sports)
    family_list = generic_permuted_list(family_members)
    music_list = generic_permuted_list(music)
    states_list = generic_permuted_list(states)
    city_list = generic_permuted_list(cities)
    phone_list = []
    for phone in phone_numbers:
        phone_list += permute_phone(phone)
    zip_list = []
    for zip_code in zip_codes:
        zip_list += permute_zip_code(zip_code)
    school_list = generic_permuted_list(schools)
    color_list = generic_permuted_list(colors)
    street_list = generic_permuted_list(streets)
    street_num_list = []
    for street_number in street_numbers:
        street_num_list += permute_street_number(street_number)
    other_list = generic_permuted_list(other_terms)

    combinations = []

    combinations += permute_lists(pet_list, family_list)
    combinations += permute_lists(pet_list, sports_list)
    combinations += permute_lists(pet_list, school_list)
    combinations += permute_lists(pet_list, states_list)
    combinations += permute_lists(pet_list, city_list)
    combinations += permute_lists(pet_list, other_list)
    combinations += permute_lists(pet_list, street_list)
    combinations += permute_lists(pet_list, music_list)
    combinations += permute_lists(pet_list, color_list)
    for pet in pet_list:
        combinations.append(pet)

    combinations += permute_lists(family_list, sports_list)
    combinations += permute_lists(family_list, school_list)
    combinations += permute_lists(family_list, states_list)
    combinations += permute_lists(family_list, city_list)
    combinations += permute_lists(family_list, other_list)
    combinations += permute_lists(family_list, street_list)
    combinations += permute_lists(family_list, music_list)
    combinations += permute_lists(family_list, color_list)
    for family in family_list:
        combinations.append(family)

    combinations += permute_lists(sports_list, school_list)
    combinations += permute_lists(sports_list, states_list)
    combinations += permute_lists(sports_list, city_list)
    combinations += permute_lists(sports_list, other_list)
    combinations += permute_lists(sports_list, street_list)
    combinations += permute_lists(sports_list, music_list)
    combinations += permute_lists(sports_list, color_list)
    for sport in sports_list:
        combinations.append(sport)

    combinations += permute_lists(school_list, states_list)
    combinations += permute_lists(school_list, city_list)
    combinations += permute_lists(school_list, other_list)
    combinations += permute_lists(school_list, street_list)
    combinations += permute_lists(school_list, music_list)
    combinations += permute_lists(school_list, color_list)
    for school in school_list:
        combinations.append(school)

    combinations += permute_lists(states_list, city_list)
    combinations += permute_lists(states_list, other_list)
    combinations += permute_lists(states_list, street_list)
    combinations += permute_lists(states_list, music_list)
    combinations += permute_lists(states_list, color_list)
    for state in states_list:
        combinations.append(state)

    combinations += permute_lists(city_list, other_list)
    combinations += permute_lists(city_list, street_list)
    combinations += permute_lists(city_list, music_list)
    combinations += permute_lists(city_list, color_list)
    for city in city_list:
        combinations.append(city)

    combinations += permute_lists(other_list, street_list)
    combinations += permute_lists(other_list, music_list)
    combinations += permute_lists(other_list, color_list)
    for other in other_list:
        combinations.append(other)

    combinations += permute_lists(street_list, music_list)
    combinations += permute_lists(street_list, color_list)
    for street in street_list:
        combinations.append(street)

    combinations += permute_lists(music_list, color_list)
    for music in music_list:
        combinations.append(music)
    for color in color_list:
        combinations.append(color)
    for number in phone_list:
        combinations.append(number)

    length = len(other_list)
    index = 0
    while index < length:
        for item in other_list[index:]:
            combinations.append(other_list[index] + item)
            combinations.append(item + other_list[index])
        index += 1

    temp_list = []
    for word in combinations:
        temp_list.append(word + "!")
        temp_list.append(word + "1")
        temp_list.append(word + "123")
        for year in year_list:
            temp_list.append(word + year)
        for zip_code in zip_codes:
            temp_list.append(word + zip_code)
        for street_number in street_num_list:
            temp_list.append(word + street_number)
        for number in phone_list:
            temp_list.append(word + number)

    final_collection += temp_list
    collection = list(set(final_collection))
    collection = [word for word in collection if 15 >= len(word) > 5]

    with open('dictionary.txt', 'a') as my_file:
        for word in collection:
            my_file.write(word + '\n')


if __name__ == "__main__":
    main()
