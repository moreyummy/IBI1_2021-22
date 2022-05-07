oh = open("Blosum62.txt", "r")
Blosum62 = oh.readlines()
azhe = Blosum62[0].split(",")
import re

def compare(file1, file2):
    m = open(file1)
    seq1 = m.readlines()
    n = open(file2)
    seq2 = n.readlines()
    seq1[1] = re.sub(r"\n", "", seq1[1])
    seq2[1] = re.sub(r"\n", "", seq2[1])
    grade = 0
    for i in range(len(seq1[1])):
        row_nul = seq1[1][i]
        row_num = azhe.index(row_nul)
        verti_nul = seq2[1][i]
        verti_num = azhe.index(verti_nul)
        row = Blosum62[row_num].split(",")
        grade = grade + int(row[verti_num])
    print(grade)


def amino_acid(file1,file2):
    m = open(file1)
    seq1 = m.readlines()[1]
    n = open(file2)
    seq2 = n.readlines()[1]
    same = 0
    seq1 = re.sub(r"\n", "", seq1)
    seq2 = re.sub(r"\n", "", seq2)
    for q in range(len(seq1)):
        if seq1[q] == seq2[q]:
            same = same+1
    same = same/len(seq1)*100
    print("%.4f%%"%(same))

compare("DLX5_mouse.fa", "DLX5_human.fa")
compare("RandomSeq.fa", "DLX5_mouse.fa")
compare("RandomSeq.fa", "DLX5_human.fa")
amino_acid("DLX5_human.fa", "DLX5_mouse.fa")
amino_acid("RandomSeq.fa", "DLX5_mouse.fa")
amino_acid("RandomSeq.fa", "DLX5_human.fa")

#Based on Blosum 62, the alignment score is 1490 between human DLX5 and mouse DLX5, the	percentage of identical amino acids is 96.5398%. However, the alignment score is -348 between mouse DCLX5 and random sequence, while their percentage of identical amino acid is 3.1142%; and the alignment score is -351 between human DCLX5 and random sequence, while the percentage of their identical amino acid is 2.7682%。
#The mouse and human DLX5 genes are extremely similar and may have evolved from a single gene.









