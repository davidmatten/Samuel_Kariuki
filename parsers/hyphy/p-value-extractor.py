import argparse
import os
import sys
from glob import glob
import json


def format_output(p_val_dct, migrations_count, from_blood, from_semen, filename):
    return "{},{},{},{},{},{}".format(p_val_dct["panmictic"], p_val_dct["structured"], migrations_count,
                                      from_blood, from_semen, filename)


def main(indir, outFile):
    print("Collecting results files from {}".format(indir))
    print("Going to write results to {}".format(outFile))
    if (indir[-1] == "/") or (indir[-1] == "/"):
        indir = indir[:-1]

    output_lines = []
    for fn in glob(indir + os.path.sep + "*"):
        from_blood = 0
        from_semen = 0
        #print(fn)
        filename = os.path.split(fn)[1]
        with open(fn, "r") as fh:
            dct = json.load(fh)
            #print(dct.keys())
            #print(dct["p-value"])
            #print(dct["migrations"])
            #print(dct["events"])
            for node_id, node_dct in dct["events"].items():
                if node_dct["from"] == "BLOOD":
                    from_blood += 1
                else:
                    from_semen += 1
            output_lines.append(format_output(dct["p-value"], dct["migrations"], from_blood, from_semen, filename))
    with open(outFile, "w") as fw:
        fw.write("panmictic,structured,migration_count,Blood_to_semen,Semen_to_blood,filename\n")
        for outline in output_lines:
            fw.write(outline+"\n")
    print("Completed.")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='extracts p-values from results files produced from HyPhy.')
    parser.add_argument('-indir', '--indir', type=str,
                        help='The directory where all the json format files exist, which are used as input to this '
                             'scraper.', required=True)
    parser.add_argument('-out', '--outFile', type=str,
                        help='The full filepath (including filename) to the output .csv file, ', required=True)

    args = parser.parse_args()
    indir = args.indir
    outFile = args.outFile

    main(indir=indir, outFile=outFile)

# /windows_c/Users/User/GoogleDrive/uct/dev/source/skariuki/select_p_values
