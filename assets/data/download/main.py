"""
Options for downloading and preprocess data
"""

import yaml
import argparse
import sys, os
sys.path.append(".")
import utils

ops = yaml.load(open("data.yml"), Loader=yaml.FullLoader)

parser = argparse.ArgumentParser("DOWNLOAD DATA")
parser.add_argument("-data", help="Choose dataset to download. Options: {}".format(list(ops.keys())),
                    required=True, type=str)
args = parser.parse_args()


if __name__ == "__main__":
    data_conf = ops[args.data]
    data = getattr(utils, data_conf["func"])(data_conf["url"])

    data.to_csv(os.path.join("..", data_conf["out"]), sep="\t", index=False)
