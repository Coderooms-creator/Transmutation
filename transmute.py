import argparse
def transmute_common_leet(word):
    capMap = {
        "i" : ["i", "!","1"],
        "l" : ["l", "1"],
        "e" : ["e", "3"],
        "t" : ["t", "7"],
        "a" : ["a", "4", "@"],
        "s" : ["s", "5", "$"],
        "o" : ["o", "0"],
        "b" : ["b", "8"],
    }
    out = []
    for c in word:
        if c in capMap:
            out.append(capMap[c][1])  
        else:
            out.append(c)
    return ''.join(out)
def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate transmutations of words in a file.")
    parser.add_argument('-L', action='store_true', help="Apply common leet transmutations")
    parser.add_argument('input_file', help="Input text file with words")
    parser.add_argument('output_file', help="Output file for transformed words")
    return parser.parse_args()
def process_file(input_file, output_file, options):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            word = line.strip()  
            if options.L:
                word = transmute_common_leet(word)
            
            outfile.write(word + "\n")  
def main():
    args = parse_arguments()
    process_file(args.input_file, args.output_file, args)

if __name__ == "__main__":
    main()

# made by  coderooms❤
