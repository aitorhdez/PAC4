import re


def parse_functions_file(file_path):
    """
    Given a file_path, parse the functions file and store its info in
    classes / functions collections
    :param file_path: Input file_path string
    :return: List of classes, List of functions
    """
    # Parsegem l'arxiu de functions en dues coleccions:
    # classes i functions
    classes = []
    functions = []
    # Llegim l'arxiu linia a linia
    with open(file_path, 'r') as inp:
        content = inp.read().splitlines()
        for line in content:
            if line.startswith('class'):
                classes.append(parse_class(line))
            elif line.startswith('function'):
                functions.append(parse_function(line))
    return classes, functions


def parse_class(line):
    """
    Parse class information from single line
    :param line: Input line string
    :return: Parsed Class
    """
    # Parsegem la linia de classe
    # Format: class([1,0,0,0],"Small-molecule metabolism ")

    # Parsegem text entre []
    code = re.search(r"\[(.*?)\]", line).group().strip('[').strip(']')
    # Parsegem text entre ""
    description = re.search(r'"([^"]*)"', line).group().strip('"').strip()

    return (code, description)


def parse_function(line):
    """
    Parse function information from single line
    :param line: Input line string
    :return: Parsed Function
    """
    # Parsegem la linia de function
    # function(tb186,[1,1,1,0],'bglS',"beta-glucosidase").

    # Parsegem orf
    orf = line[line.find("(") + 1:line.find(",")]
    # Parsegem text entre []
    code = re.search(r"\[(.*?)\]", line).group().strip('[').strip(']')
    # Parsegem text entre ''
    description = re.search("\'(.*?)\'", line).group().strip("'")
    # Parsegem text entre ""
    description2 = re.search(r'"([^"]*)"', line).group().strip('"').strip()
    return orf, code, description, description2
