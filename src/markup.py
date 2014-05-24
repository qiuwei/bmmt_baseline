
#/usr/bin/env python

import argparse, os

def readin_term(path):
    """
    read in the terminology
    """
    term_dict = {}
    with open(path, 'r') as term_file:
        for line in term_file
            determ, enterm = line.strip().split('\t')
            term_dict[determ] = enterm
    return term_dict

def process_de_str():
    """
    preprocess the input German string to add the xml markup
    """


def process_de():
    """
    preprocess the input German file to add the xml markup
    """


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--term', help='path to the terminology file')
    parser.add_argument('path', help='path to the input file')

    args = parser.parse_args()
    term_dict = readin_term(args.path)
