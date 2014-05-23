#/usr/bin/env python

import argparse, os

def split_term(path):
    """
    split the terminology file into two files .de and .en
    """
    with open(path, 'r') as term_file:
        base_dir = os.path.dirname(path)
        depath= os.path.join(base_dir, 'terminology.de')
        enpath= os.path.join(base_dir, 'terminology.en')
        with open(depath, 'w') as defile:
            with open(enpath, 'w') as enfile:
                for line in term_file:
                    deline, enline = line.strip().split('\t')
                    defile.write(deline)
                    defile.write(os.linesep)
                    enfile.write(enline)
                    enfile.write(os.linesep)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to the terminology file')

    args = parser.parse_args()
    split_term(args.path)
