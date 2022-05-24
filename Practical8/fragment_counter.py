seq = "ATGCAATCGACTACGATCAATCGAGGGCC"
fragments = []
import re
while re.search("GAATTC", seq):
    co = seq.find("GAATTC")
    fragments.append(seq[:co+1])
    seq = seq[co+1:]
fragments.append(seq)
print("%d fragments will formed if EcoRI enzyme is used"%(len(fragments)))
    

    
