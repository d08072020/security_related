
def main():
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
                item=item+"["+tItem+"]("+tItem+".html),"
            item=item+"\n"
        else:
            item=item+line
    f.close()

    for key,val in item_list_by_tag.items():
        f2 = open(key+".md","w")
        for item in val:
            f2.write(item)
        f2.close()

if __name__ == '__main__':
    main()

