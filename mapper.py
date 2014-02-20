#!/usr/bin/python

import sys,os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Wrapper for the HTSeq-count utility')
parser.add_argument('-s','--sam', help='SAM file, for Hadoop it should be a STDIN, i.e. a "-"',default="-", required=True)
parser.add_argument('-g','--gff', help='GFF file', required=True)
parser.add_argument('-m','--mode',help='''mode to handle reads overlapping more than one
                        feature(choices: union, intersection-strict,
                        intersection-nonempty; default: union)''', default='union')

parser.add_argument('-t', '--type',help='''
                        feature type (3rd column in GFF file) to be used, all
                        features of other type are ignored (default, suitable
                        for Ensembl GTF files: exon)''', default='exon')

parser.add_argument('-i', '--idattr', help='''
                        GFF attribute to be used as feature ID (default,
                        suitable for Ensembl GTF files: gene_id)''',default='gene_id')


args = vars(parser.parse_args())

import glob
gffFile = glob.glob(args['gff']+"/*.gff")[0]


#print args
from subprocess import call
cmd = ["htseq-count", "--type="+args['type'], "--idattr="+args['idattr'], args['sam'], gffFile] 
print cmd
call(cmd)

#call(["readlink","-f", args['gff']])

#if args['gff'] == 'gff':
#	print args['bar']
    # code here


