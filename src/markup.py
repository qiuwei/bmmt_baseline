
#/usr/bin/env python

import argparse, re

def readin_term(path):
    """
    read in the terminology
    """
    term_dict = {}
    with open(path, 'r') as term_file:
        for line in term_file:
            determ, enterm = line.strip().split('\t')
            term_dict[determ] = enterm
    return term_dict

def process_de_str(destr, term_dict, depattern):
    """
    preprocess the input German string to add the xml markup
    """
    return depattern.sub(lambda m: r'<np translation="{0}">{1}<\np>'.format(term_dict.get(m.group()), m.group()), destr)


def build_de_pattern(term_dict):
    """
    build a regualr expression pattern which matches all de phrases in the term_dict
    """
    re_str_list =  [r'\b{}\b'.format(k) for k in term_dict.keys()]
    re_str = '|'.join(re_str_list)
    return re.compile(re_str, re.IGNORECASE)

def process_de_file(path, term):
    """
    preprocess the input German file to add the xml markup
    """
    term_dict = readin_term(term)
    depattern = build_de_pattern(term_dict)
    with open(path, 'r') as infile:
        for line in infile:
            print process_de_str(line.strip(), term_dict, depattern)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='wrap up the terminologies occurred in input file with xml markup')
    parser.add_argument('--term', help='path to the terminology file')
    parser.add_argument('path', help='path to the input file')

    args = parser.parse_args()
    process_de_file(args.path, args.term)
