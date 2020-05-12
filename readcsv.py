#!/usr/bin/env python3

```
USEAGE:
code.py <brokenpair.csv> <output.csv> <adjustment - number>
```

import csv
import sys


brokenpairscsv = sys.argv[1]
newcsv = sys.argv[2]
ADJUSTMENT = sys.argv[3]

input_file = str(brokenpairscsv)
ADJUSTMENT = int(ADJUSTMENT)

def brokenpairsCLC (brokenpairscsv):

    adjustment_value = "The adjustment value is: %d" %(ADJUSTMENT)
    input_file_name = "The input file is: %s" %(input_file)

    with open(newcsv, 'a') as fh:
        writer = csv.writer(fh)
        writer.writerow([input_file_name])
        writer.writerow([adjustment_value])

    with open(brokenpairscsv, 'r') as fh:
        fhcsv = csv.reader(fh, delimiter=',')

        field_names_list = next(fhcsv)
        with open(newcsv, 'a') as fh:
            writer = csv.writer(fh)
            writer.writerow(field_names_list)

        #next(fhcsv)

        for row in fhcsv:
            entry = row
            Ref_start = int(entry[1])

            Ref_end = int(entry[2])
            Ref_annotation = entry[4]
            Mate_start = int(entry[6])
            Mate_end = int(entry[7])
            Mate_annotation = entry[9]

            # if Mate_annotation != Ref_annotation:
            #    print(entry)

            if Mate_start not in range((Ref_start - ADJUSTMENT), (Ref_start + ADJUSTMENT)) and Mate_end not in range((Ref_end - ADJUSTMENT), (Ref_end + ADJUSTMENT)):
                with open(newcsv, 'a') as fh:
                    writer = csv.writer(fh)
                    writer.writerow(row)


brokenpairsCLC(brokenpairscsv)
