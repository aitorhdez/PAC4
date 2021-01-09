import re
import parser.parseClasses as clsParser
import parser.parseOrfs as orfParser
import utils.utils as utils
import utils.plot as plot

# Parsegem l'arxiu de funcions
res = clsParser.parse_functions_file("/home/datasci/PycharmProjects/pac4/data/tb_functions.pl")
classes = res[0]
functions = res[1]

# Parsegem l'arxiu de ORF
orfrel = orfParser.parse_orf_path("/home/datasci/PycharmProjects/pac4/data/orfs")

# Exercici 1.1. Mostrem la llista del comptador de orf per cada classe
cls_dict = utils.orf_per_class_display(classes, functions)
plot.plot_classes_dict(cls_dict)

# Exercici 1.2. Mostrem la llista del comptador de orf per la classe
# Respiration utilitzant el filtre de la funció
cls_dict = utils.orf_per_class_display(classes, functions, "Respiration")
for c in cls_dict.keys():
    print("Respiration class contains {} ORF's" .format(cls_dict[c]))

# Exercici 2.1
# Busquem la quantitat de classes que contenen ORF amb la paraula 'protein'
# a la descripció
pattern1_count = utils.get_cls_count_contain_orf(functions, classes, "protein")
# Busquem la quantitat de classes que contenen ORF amb la paraula 'hydro' a la
# descripció i descripció de 13 paraules justes
pattern2_count = utils.get_cls_count_contain_orf(functions, classes, "hydro", 13)
plot.plot_classes_pattern(pattern1_count, pattern2_count)

# Exercici 2.2
# 2.2 El nombre mitjà d'ORFs amb els quals es relacionen els ORFs amb el patró indicat a la seva descripció.
mean1 = utils.get_mean_orf_relationship(functions, orfrel, "protein")
mean2 = utils.get_mean_orf_relationship(functions, orfrel, "hydro", 13)
plot.plot_means_pattern(mean1, mean2)

# Exercici 3
# Per a cada enter M entre 2 i 9 (ambdós inclosos), calcula el nombre de classes que tenen com a mínim una
# dimensió major estricte (>) que 0 i alhora múltiple de M. Amb el terme dimensió ens referim a cadascun dels
# 4 números que formen l'identificador de la classe (explicat a la secció anterior).
m_values = [2, 3, 4, 5, 6, 7, 8, 9]
cls_dict = {}
for i in m_values:
    cls_dict[str(i)] = utils.get_matching_dimension(classes, i)
plot.plot_dim_dict(cls_dict)

