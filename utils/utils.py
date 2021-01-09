import re

def orf_per_class_display(classes, functions, filter_str=""):
    """
    Determines the count of ORF's that pertains to each class.
    :param classes: List of parsed classes
    :param functions: List of parsed Functions
    :param filter_str: Optional. Filter the class name
    :return: Dictionary containing the count of ORF for each class
    """

    dict_cls = {}
    for cls in classes:
        cls_name = cls[1]
        # Apliquem el filtre si s'ha especificat
        if filter_str == "" or filter_str == cls_name:
            counter = len(get_orf_list_in_class(functions, cls))
            dict_cls[cls[0]] = counter
    return dict_cls


def orf_match_pattern(orf_desc, contain_word, desc_length):
    """
    Given a description, determines if the string matches the pattern
    :param orf_desc: Input string wiht the description
    :param contain_word: Description should contain this word. If don't want
    to use, use ""
    :param desc_length: Matching words should have this length. If don't want
    to use, use -1
    :return: True, if matches, False if not
    """
    # Mirem si apliquem filtre de substring a la llista
    if contain_word == "" or contain_word in orf_desc:

        # Mirem si apliquem el segon filtre. Alguna paraula de més de
        # longitud 'maxLength' conté el terme 'containWord'
        if desc_length == -1:
            return True
        else:
            for w in orf_desc.split(' '):
                if len(w) == desc_length and contain_word in w:
                    return True
    return False


def get_orf_list_in_class(functions, cls, contain_word="", desc_length=-1):
    """
    Get the list of matching orf's contained in a class. Allowd to filter by contained
    word and/or by word length in description
    :param functions: List of parsed Functions
    :param cls: Selected class
    :param contain_word: Filter word in ORF description
    :param desc_length: Filtered word length in ORF description
    :return: List of matching ORF's
    """
    # Recorrem les funcions buscant les que estan assocaides a la nostra classe
    counter = 0
    code0 = cls[0]
    matching_orf = []
    for f in functions:
        code1 = f[1]
        # Mirem que els codis siguin iguals
        if code0 == code1 and orf_match_pattern(f[3], contain_word, desc_length):
            matching_orf.append(f)

    return matching_orf


def get_cls_count_contain_orf(functions, classes, contain_word, desc_length=-1):
    """
    Returns the list of contained ORF's in each class that match the pattern
    :param functions: List of parsed functions
    :param classes: List of parsed classes
    :param contain_word: Filter word in ORF description
    :param desc_length: Filtered word length in ORF description
    :return:
    """
    counter = 0
    for cl in classes:
        if len(get_orf_list_in_class(functions, cl, contain_word, desc_length)) > 0:
            counter = counter + 1
    return counter


def get_orf_list_with_filter(functions, contain_word, desc_length):
    """
    Get the ORFs list that match a description word, word-length pattern
    :param functions: List of parsed functions
    :param contain_word: Filter word in ORF description
    :param desc_length: Filtered word length in ORF description
    :return:
    """
    matching_orf_list = []
    for orf in functions:
        if orf_match_pattern(orf[3], contain_word, desc_length):
            matching_orf_list.append(orf)
    return matching_orf_list


def get_related_orf(orf, orf_list):
    """
    Get the list of the related ORF's with a single ORF
    :param orf: Selected ORF
    :param orf_list: All ORF's list
    :return: List of ORF's that are related to 'orf'
    """
    for i in orf_list:
        if i[0] == orf[0]:
            return i[1]


def get_mean_orf_relationship(functions, orfrel, contain_word, desc_length=-1):
    """
    Get the mean of the related ORFs count for each orf, by using orf description
    filter pattern
    :param functions: List of parsed functions
    :param orfrel: List of parsed orfRelationships
    :param contain_word: Filter word in ORF description
    :param desc_length: Filtered word length in ORF description
    :return:
    """
    # Busquem tots els ORF's que contenen el patró
    orfs_list = get_orf_list_with_filter(functions, contain_word, desc_length)
    means = []
    # Per a cada ORF de la llista, mirem la quantitat de orf's relacionats
    for orf in orfs_list:
        means.append(len(get_related_orf(orf, orfrel)))

    # Calculem la mitjana
    if len(means) > 0:
        total = 0
        for m in means:
            total = total + m
        total_mean = total / len(means)
    return total_mean


def get_matching_dimension(classes, m_value):
    """
    Returns the count of classes that contains a dimension that is multiple
    of m_value
    :param classes: List of parsed classes
    :param m_value: Int. Number > 0
    :return:
    """
    counter = 0
    for cls in classes:
        for dim in cls[0].split(','):
            if int(dim) != 0 and (int(dim) % m_value == 0):
                counter = counter + 1
                break
    return counter


