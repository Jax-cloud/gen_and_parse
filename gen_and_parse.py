import io
import json
from random import randrange

spec = json.load(open('spec.json'))

def generate(fixedFile,rows): 
  with io.open(fixedFile, 'w', encoding=spec['FixedWidthEncoding']) as outFile:
    if spec['IncludeHeader']:
        outFile.write(''.join([e+('.'*(int(spec['Offsets'][i])-len(e))) for i,e in enumerate(spec['ColumnNames'])])+'\n')
    for _ in range(rows):
        outFile.write(''.join([chr(randrange(ord('a'),ord('z')-len(spec['ColumnNames']))+i)*int(e) for i,e in enumerate(spec['Offsets'])])+'\n')
    outFile.close()

def parse(fixedFile,delimitedFile):
  with io.open(fixedFile, 'r', encoding=spec['FixedWidthEncoding']) as inFile:
    with io.open(delimitedFile, 'w', encoding=spec['DelimitedEncoding']) as outFile:
      for line in inFile:
        outFile.write(','.join([ line[sum(int(a) for a in spec['Offsets'][:i]):sum(int(a) for a in spec['Offsets'][:i+1])] for i in range(len(spec['Offsets']))])+'\n')
      outFile.close()
    inFile.close()

def main():
  generate('fixed.txt',25)
  parse('fixed.txt','delimited.csv')

if __name__ == "__main__": main()