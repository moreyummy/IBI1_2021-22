from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt


tree = xml.dom.minidom.parse("go_obo.xml")
root = tree.documentElement
ohoh = root.getElementsByTagName("term")


is_a_list=[]
father_is = []
is_a_dict={}
children={}
for term in ohoh:
    id=term.getElementsByTagName('id')[0]
    id=id.childNodes[0].data
    is_a=term.getElementsByTagName('is_a')
    for every_is_a in is_a:
        every_is_a_data=every_is_a.childNodes[0].data
        is_a_list.append(every_is_a_data)
    is_a_dict[id]=is_a_list             #is_a_dict={id:[is_a]}
    children[id]=[]
    is_a_list=[]


for every_id in is_a_dict:
    for every_is_a in is_a_dict[every_id]:
        children[every_is_a].append(every_id)


number=[]
def suma(first):
    global number
    first=children[first]
    number.extend(first)
    for next in first:
        suma(next)
    number=list(set(number))
    n=len(number)


all = [];n=0
term_count=len(children)
for id in children:
    n+=1
    number = []
    suma(id)
    nodes=len(number)
    all.append(nodes)
all_mean = np.means(all)
print("the mean of child nodes across all terms is %d"%(all_mean))

translation_all = []
index = []
node = []
for g in range(len(ohoh)):
    translation = ohoh[g].getElementsByTagName("defstr")[0].childNodes[0].data
    if translation.find("translation") != -1:
        translation_all.append(translation)
        index.append(g)
for h in range(len(index)):
    node.append(all[index[h]])
node_mean = np.mean(node)
print("the mean of child nodes across terms associated wit 'translation' is %d"%(node_mean))
print("the mean of nodes across all terms is bigger than the mean of child nodes across terms associated wit 'translation' ")


plt.boxplot(all, vert=True, patch_artist=True, boxprops={"color": "gray"}, showmeans=True)
plt.title("The distribution	of child nodes across all terms", color="blue")
plt.xlabel("All terms")
plt.ylabel("the number of child nodes")
plt.show()

plt.boxplot(node, vert=True, patch_artist=True, boxprops={"color": "gray"}, showmeans=True)
plt.title("The distribution	of child nodes across terms	associated with ‘translation’", color="blue")
plt.xlabel("terms associated with 'translation")
plt.ylabel("the number of child nodes")
plt.show()






































