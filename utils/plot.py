import matplotlib.pyplot as plt


def plot_classes_dict(dict_classes):
    fig = plt.figure(figsize=(10, 5))
    # creating the bar plot\n",
    plt.bar(dict_classes.keys(), dict_classes.values(), color='maroon', width=0.4)
    plt.xlabel("Classes")
    plt.xticks(rotation=90, size=4)
    plt.ylabel("ORF")
    plt.title("Orf's relacionats amb cada classe")
    plt.show()


def plot_classes_pattern(val1, val2):
    fig = plt.figure(figsize=(10, 5))
    x_values = ["Protein", "Hydro, Len=13"]
    y_values = [val1, val2]
    # creating the bar plot\n",
    plt.bar(x_values, y_values, color='maroon', width=0.4)
    plt.xlabel("Patterns")
    plt.ylabel("Classes")
    plt.title("Classes que contenen orf's amb els patrons especificats")
    plt.show()


def plot_means_pattern(val1, val2):
    fig = plt.figure(figsize=(10, 5))
    x_values = ["Protein", "Hydro, Len=13"]
    y_values = [val1, val2]
    # creating the bar plot\n",
    plt.bar(x_values, y_values, color='maroon', width=0.4)
    plt.xlabel("Patterns")
    plt.ylabel("Mean")
    plt.title("Nombre mitjà d'ORFs amb els quals es relacionen els ORFs amb el patró indicat")
    plt.show()


def plot_dim_dict(dict_m):
    fig = plt.figure(figsize=(10, 5))
    # creating the bar plot\n",
    plt.bar(dict_m.keys(), dict_m.values(), color='maroon', width=0.4)
    plt.xlabel("M")
    plt.ylabel("Count")
    plt.title("Classes amb dimensions != 0 i multiples de M")
    plt.show()