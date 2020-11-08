
def main():
    taglist={}
    f = open("keyward.dat", "r")
    item=""
    tags=""
    for line in f:
        if line.startswith("## "):
            if item!="":
                taglist[tags]=item
            item=line
            tags=line.replace("\n","")[3:]
        else:
            item=item+line
    f.close()

    item_list_by_tag={"all":[]}
    f = open("all.dat", "r")
    item=""
    tags=""
    for line in f:
        if line.startswith("### "):
            if item!="":
                item_list_by_tag["all"].append(item)
                for tItem in tags:
                    if tItem not in item_list_by_tag:
                        item_list_by_tag[tItem]=[]
                    item_list_by_tag[tItem].append(item)
            item=line
        elif line.startswith("tag:"):
            tags=line.replace("\n","").split(":")[1].split(",")
            for tItem in tags:
                item=item+"["+tItem+"]("+tItem.replace(" ","_")+".html),"
            item=item+"\n"
        elif line.startswith("----------"):
            continue
        else:
            item=item+line
    f.close()

    tagListSort=[]
    for key,val in item_list_by_tag.items():
        if key!="all":
            tagListSort.append([len(val),key])

        f2 = open(key.replace(" ","_")+".md","w")
        if key in taglist:
            f2.write(taglist[key])
        else:
            f2.write("## "+key+"\n\n\n")
        for item in val:
            f2.write(item)
        f2.close()

    tagListSort.sort(reverse=True)
    f = open("index_seed.dat", "r")
    f2 = open("index.md", "w")
    for line in f:
        f2.write(line)
    f.close()
    for item in tagListSort:
        f2.write("["+item[1]+"("+str(item[0])+")](./"+item[1].replace(" ","_")+".html)\n")
    f2.close()

if __name__ == '__main__':
    main()

