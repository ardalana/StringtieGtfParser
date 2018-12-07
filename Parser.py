#!/usr/bin/env python3
import sys

# Program to parse gtf output from Stringtie (containing transcripts assembled from RNA-Seq alignments)
referenceGtf=sys.argv[1]
stringtieGtf=sys.argv[2]

protCodGenes=[]
with open(referenceGtf) as annotfile:
    for line in annotfile:
        if not line.startswith('#') and 'protein_coding' in line:
            protCodDict={}
            for i in range(len(line.split('\t')[8].rstrip('\n').split(';'))):
                protCodDict[line.split('\t')[8].rstrip('\n').split(';')[i].split('=')[0]]=line.split('\t')[8].rstrip('\n').split(';')[i].split('=')[1]
            protCodGenes.append(protCodDict['Name'])

with open(stringtieGtf) as infile, open(stringtieGtf+'.parsed','w') as outfile:
    print('#gene', 'proteinCoding', 'transcript', 'coverage', 'TPM', sep='\t', file=outfile)
    for line in infile:
        if not line.startswith('#') and line.split('\t')[2]=='transcript' and 'ref_gene_name' in line:
           attribs={}
           for i in range(len(line.split('\t')[8].rstrip(';\n').split('; '))):
               attribs[line.split('\t')[8].rstrip(';\n').split('; ')[i].split(' ')[0]]=line.split('\t')[8].rstrip(';\n').split('; ')[i].split(' ')[1].strip('"')
           if attribs['ref_gene_name'] in protCodGenes: gentyp='yes'
           else: gentyp='no'
           print(attribs['ref_gene_name'], gentyp, attribs['transcript_id'], attribs['cov'], attribs['TPM'], sep='\t', file=outfile)
