import os
import sys
in_fn = "SVB008_combi_1_aln.fas.output"
in_fn = "SVB041_combi_1_aln.fasta.output"

hsm = []
s = []
hbk = []
hsnn = []

n = 1001

for file_number in range(0, n):
    print(file_number)

    in_fn = "_".join(in_fn.split("_")[:2]) + "_{}_".format(file_number) + "_".join(in_fn.split("_")[3:])
    print(in_fn)
    # sys.exit()

    if os.path.isfile(in_fn):
        print("yeah, it exists")

        data = []
        with open(in_fn, "r") as fh:
            for line in fh:
                data.append(line.strip())
        if data[0] == "Error:":
            continue

        for i, line in enumerate(data):
            f_st_i = 0
            if "F_ST" in line:
                break

        results = [float(x.split(":")[-1]) for x in data[i+2:i+6]]
        hsm.append(results[0])
        s.append(results[1])
        hbk.append(results[2])
        hsnn.append(results[3])

with open("hudson_slatkin_maddison.csv", "w") as fw:
    fw.write("Hudson Slatkin and Maddison\n")
    for x in hsm:
        fw.write(str(x) + "\n")

with open("slatkin.csv", "w") as fw:
    fw.write("Slatkin\n")
    for x in s:
        fw.write(str(x) + "\n")

with open("hudson_boos_kaplan.csv", "w") as fw:
    fw.write("Hudson Boos and Kaplan\n")
    for x in hbk:
        fw.write(str(x) + "\n")

with open("hudson_snn.csv", "w") as fw:
    fw.write("Hudson (S_nn)\n")
    for x in hsnn:
        fw.write(str(x) + "\n")


hsm = []
s = []
hbk = []
hsnn = []

for file_number in range(0, n):

    in_fn = "_".join(in_fn.split("_")[:2]) + "_{}_".format(file_number) + "_".join(in_fn.split("_")[3:])
    print(in_fn)

    if os.path.isfile(in_fn):
        print("yeah, it exists")

        data = []
        with open(in_fn, "r") as fh:
            for line in fh:
                data.append(line.strip())
        if data[0] == "Error:":
            continue

        for i, line in enumerate(data):
            f_st_i = 0
            if "F_ST" in line:
                break

        print(data)
        while '' in data:
            data.remove('')
        print(data[-4:])
        results = [float(x.split(":")[-1]) for x in data[-4:]]

        hsm.append(results[0])
        s.append(results[1])
        hbk.append(results[2])
        hsnn.append(results[3])


with open("2_hudson_slatkin_maddison.csv", "w") as fw:
    fw.write("Hudson Slatkin and Maddison\n")
    for x in hsm:
        fw.write(str(x) + "\n")

with open("2_slatkin.csv", "w") as fw:
    fw.write("Slatkin\n")
    for x in s:
        fw.write(str(x) + "\n")

with open("2_hudson_boos_kaplan.csv", "w") as fw:
    fw.write("Hudson Boos and Kaplan\n")
    for x in hbk:
        fw.write(str(x) + "\n")

with open("2_hudson_snn.csv", "w") as fw:
    fw.write("Hudson (S_nn)\n")
    for x in hsnn:
        fw.write(str(x) + "\n")


