import argparse
import pandas as pd

def parse_arguments():
    """parses all necessary arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="Input_files", action='append', nargs='+',
                        help="Space separated SALMON tables (.sf)")
    parser.add_argument("-o", dest="output_file", nargs='+',
                        help="Output directory, name preffix can be added")
    return parser.parse_args()

#args.Input_files[0][0]
def table_join(files):
    """Loads tables as pd.df and appends them to a big df"""
    if files == []:
        return "No Input specified"
    elif len(files) >= 1:
        df1 = pd.read_csv(files[0], sep='\t')[['Name','TPM']]
        i = 2
        for file in files[1:]:
            df = pd.read_csv(file, sep='\t')
            df = df[['Name','TPM']]
            df1 = df1.merge(df, how='outer', on='Name', validate='one_to_one')
            i+=1
        colname = ['']+['sample_'+str(x+1) for x in range(len(files))]
        df1.columns = colname
        df1 = df1.set_index('')
        return df1

def main():
    print("Creating joined table...")
    args = parse_arguments()
    out = table_join(args.Input_files[0])
    print(args.output_file[0])
    outdir = args.output_file[0] + "_SA2SU.tsv"
    print("Writing table " + outdir)
    out.to_csv(outdir, sep = "\t")
    
if __name__ == "__main__":
    main()
