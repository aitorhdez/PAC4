import os


def parse_orf_path(data_path):
    """
    Given a ORF's files path, parse all files and return the ORF's relationship
    collection
    :param data_path: Data path. Should contain 1 or more files
    :return: Orf relationship collection
    """
    # Processem cada arxiu del path de dades orf
    orf_rel = []
    for f in os.listdir(data_path):
        process_orf_file(data_path + "/" + f, orf_rel)
    return orf_rel


def process_orf_file(file_path, orf_rel):
    """
    Process single ORF file and extract its information
    :param file_path: Input file path
    :param orf_rel: List where to append parsed info
    :return:
    """
    with open(file_path, 'r') as inp:
        content = inp.read().splitlines()
        relatedorfs = []
        orfrelationship = []
        for line in content:
            if line.startswith("begin"):
                # Format: begin(model(tb4)).
                orfrelationship = []
                orfrelationship.append(get_parenth_value(get_parenth_value(line)))
            elif line.startswith("tb_to_tb_evalue"):
                # Format: tb_to_tb_evalue(tb3671,1.100000e-01).
                relatedorfs.append(line[line.find("(") + 1:line.find(",")])
            elif line.startswith("end"):
                orfrelationship.append(relatedorfs)
                orf_rel.append(orfrelationship)


def get_parenth_value(s):
    """
    Get string value between parenthesis
    :param s: Input string
    :return: Value between parenthesis
    """
    return s[s.find("(") + 1:s.rfind(")")]
