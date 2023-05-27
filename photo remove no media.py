try:
    file = open("fileNames.txt", "r")
    new_file = open("New_file.txt", "w").write("")
    Done_file = open("New_file.txt", "a")
    
    for line in file.readlines():
        sp = line.split()
        def check(a):
            if a == "_":
                return ""
            else:
                return "g"
        Done_file.write("ren " + sp[0] + " " + sp[0][0:23] + check(sp[0][23]) + "\n" + "ren " + sp[1] + " " + sp[1][0:23] + check(sp[1][23]) + "\n" + "ren " + sp[2] + " " + sp[2][0:23] + check(sp[2][23]) + "\n")
finally:
    file.close()
    Done_file.close()
