#!/usr/bin/python

import sys,os
import argparse
import subprocess

parser = argparse.ArgumentParser(description="""Wrapper for the HTSeq-count utility. \
alexey.siretskiy@it.uu.se, 2014""")
parser.add_argument('sam', help='SAM file, for Hadoop it should be a STDIN, i.e. a "-"',default="-")
parser.add_argument('gff', help='the folder containing the GFF file')
parser.add_argument('-m','--mode',help='''mode to handle reads overlapping more than one
                        feature (default is  'union')''', default='union', choices=['union', 'intersection-strict', 'intersection-nonempty'])

parser.add_argument('-t', '--type',help='''
                        feature type (3rd column in GFF file) to be used, all
                        features of other type are ignored (default, suitable
                        for Ensembl GTF files: exon)''', default='exon')

parser.add_argument('-i', '--idattr', help='''
                        GFF attribute to be used as feature ID (default,
                        suitable for Ensembl GTF files: gene_id)''',default='gene_id')

parser.add_argument('-q','--quiet', action='store_true', help="suppress progress report and warnings")

args = vars(parser.parse_args())
#print args


import glob
try:
	gffFile = glob.glob(args['gff']+"/*.gff")[0]
except:
	print "you should point to the DIRECTORY containing the GFF file"
	raise
	
from subprocess import call
cmd = ["htseq-count", "--type="+args['type'], "--idattr="+args['idattr'], "--mode="+args['mode']]
if args['quiet']: cmd.append("--quiet")
cmd+=[args['sam'], gffFile] 

#print cmd
call(cmd)
