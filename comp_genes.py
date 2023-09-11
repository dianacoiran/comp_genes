
# variables
sequence_file = "ecoli.fasta"

ecoli_gene_set = set()
ecoli_gene_list = []
kleb_gene_set = set()
kleb_gene_list = []

## Bacteria 1. E coli:

with open(sequence_file) as f1:
    for line in f1:
        if line.startswith(">"):
            # print(line)

            # crear variable temporal y separar por fragmentos el titulo
            temporal = line.split()
            gene_name_ecoli = temporal[-3][-4:]
            # print(temporal)
            print(gene_name_ecoli)

            # cargar datos a lista y a set
            ecoli_gene_list.append(gene_name_ecoli)
            ecoli_gene_set.add(gene_name_ecoli)

    ## bacteria 2 Klebsiella pneumoniae

sequence_file = "klebsiella.gb"

with open(sequence_file) as f2:
    for line in f2:
        if "/gene=" in line:
            line = line.strip()
            gene_name_kleb = line[-5:-1]
            #print(line)
            print(gene_name_kleb)

            # cargar datos a lista y a set
            kleb_gene_list.append(gene_name_kleb)
            kleb_gene_set.add(gene_name_kleb)

print("El número de genes en Klebsiella pneumoniae es:",len(kleb_gene_set))
print("El número de genes en Escherichia coli es:",len(ecoli_gene_set))

ecoli_dif_kleb = ecoli_gene_set.difference(kleb_gene_set)
kleb_dif_ecoli = kleb_gene_set.difference(ecoli_gene_set)

interseccion = ecoli_gene_set.intersection(kleb_gene_set)
genes_comun = list(interseccion)

print("Los genes presentes en E.coli que no estan en Klebsiella.p son:", len(ecoli_dif_kleb))
print("Los genes presentes en Klebsiella.p que no estan en E.coli son:", len(kleb_dif_ecoli))
print("Los genes que comparten ambas bacterias son:", len(genes_comun))

##Buscar genes especificos de cada bacteria

#produccion de pigmento

pigmento = 'gyrB'
if pigmento in kleb_gene_set:
    print(f"El gen de pigmentación '{pigmento}' fue encontrado en klebsiella p,  "
          f"responsable del color rosado en estas colonias.")
else:
    print(f"El gen '{pigmento}' no fue encontrado en klebsiella p, "
          f"resultado no esperado.")


if pigmento in ecoli_gene_set:
    print(f"El gen de pigmentación '{pigmento}' se encuentra en E coli, "
          f"resultado no esperado.")
else:
    print(f"El gen '{pigmento}' no fue encontrado en E coli, "
          f"resultado esperado de este microorganismo.")



#Producción de indol

indol = 'tnaB'
if indol in ecoli_gene_set:
    print(f"El gen de produccion de indol '{indol}' fue encontrado en E coli,  "
          f"responsable de la formación de anillo rojo al reaccionar con "
          f"reactivo de Kovac.")
else:
    print(f"El gen '{indol}' no fue encontrado en ecoli, "
          f"resultado no coherente biológicamente.")


if indol in kleb_gene_set:
    print(f"El gen de produccion de indol '{indol}' se encuentra en Klebsiella.p "
          f"resultado no coherente biologicamente.")
else:
    print(f"El gen de produccion de indol '{indol}' no fue encontrado en klebsiella p, "
          f"resultado esperado de este microorganismo.")
