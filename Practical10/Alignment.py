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
    for q in range(len(seq1)):
        if seq1[q] == seq2[q]:
            same = same+1
    same = same/len(seq1)*100
    print("%.4f%%"%(same))

amino_acid("DLX5_mouse.fa", "DLX5_human.fa")
compare("DLX5_human.fa", "DLX5_mouse.fa")











