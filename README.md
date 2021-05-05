
SA2SU
==========

SALMON (https://github.com/COMBINE-lab/salmon) to SUPPA2 (https://github.com/comprna/SUPPA) table converter.

## How to use the script

This script runs on terminal with the following parameters:
```
python3 SA2SU.py -i <input-file.sf> <input-file.sf> <input-file.sf> -o <output-file.tsv>
```

- **-i**  | **--input-file**: **.sf**(tabular) files from SALMON output separated by a space
- **-o**  | **--output-file**: a .tsv format file from the input tables merged by 'Name' and the 'TPM' column (each column labeled as sample_N)



## Output (SUPPA2 input)

A transcript expression file with multiple samples:

```
sample1 sample2 sample3 sample4
transcript1 <expression>  <expression>  <expression>  <expression>
transcript2 <expression>  <expression>  <expression>  <expression>
transcript3 <expression>  <expression>  <expression>  <expression>
```


### AUTHOR/SUPPORT

Lucas Servi, lucasservi@gmail.com </br>
