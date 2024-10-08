def import_flowers_txt(name="champ"):
    flowers = []
    with open("python_files/" + name + ".txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    x, y = map(float, line.split(","))
                    flowers.append((x, y))
                except:
                    pass

    return flowers