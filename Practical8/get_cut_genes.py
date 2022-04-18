xfile = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
alllines = xfile.readlines()

genes = {}
sequence = []
names = []
for i in alllines:
    i = i.rstrip()
    if i.startswith(">"):
        genes.setdefault(i)
        genes[i] = []
        a = genes[i]
    else:
       a.append(i)
for q in genes:
    names.append(q)
    genes[q] = "".join(genes[q])
    sequence.append(genes[q])

can_cut_seq = []
can_cut_name = []
for p in range(len(sequence)):
    if "GAATTC" in sequence[p]:
        can_cut_seq.append(sequence[p])
        can_cut_name.append(names[p])

can_cut_name_sim = []
length = []
import re
for m in range(len(can_cut_name)):
    length.append(str(len(can_cut_seq[m])))
    en = "".join(re.findall(r"gene:([^ ]+) gene_biotype", can_cut_name[m]))
    can_cut_name_sim.append(en)

oh = open("cut_genes.fa", "w")
for n in range(len(can_cut_name_sim)):
    oh.write(">" + can_cut_name_sim[n] +"        " + length[n] + "\n")
    oh.write(can_cut_seq[n] + "\n")
oh.close()
