import os                                                                                                   # responsible for chcecking if file exist
import csv                                                                                                  # responsible for csv file
import re                                                                                                   # responsible for regex

class File:

    def __init__(self, file):
        self.file = file

    def file_check(self, source_filename):

        if (os.path.exists(source_filename)):                                                               # checking if file is in proper dir
            all_rows_from_file = []

            source_csvfile = open(source_filename, 'r', encoding="ANSI")
            dest_filename = source_filename[:len(source_filename) - 10] + "_result.csv"                     #creating dest filename
            csvreader = csv.reader(source_csvfile, delimiter=';')                                           # creating a csv reader object
            fields = next(csvreader)

            for row in csvreader:                                                                           # extracting source file to list
                all_rows_from_file.append(row)

            source_csvfile.close()
            return all_rows_from_file, dest_filename
        else:                                                                                               # if file is not in proper dir
            print("Check source_file path!")
            exit(1)

    def re_find(self,  all_rows_from_file, regex):                                                          # method to find regex
        rows_to_file = []                                                                                   # list to iterate on and to write to file
        found_item = []

        for row in all_rows_from_file:                                                                      # extracting each data row one by one
            if any((match := regex.search(item)) for item in row):                                          # searching for regex in each row from details
                row.append(match.group(0))                                                                  # appending result to row_reader list
                found_item.append(match.group(0))
            else:                                                                                           # if no result in row is found
                row.append('')                                                                              # appending empty item to row_reader list
                found_item.append('')

            rows_to_file.append(row)                                                                        # write result to dest file

        return rows_to_file, found_item                                                                     # returning list with result added to end of each row


    def write_to_file(self, all_rows_to_file, dest_filename):                                       # writing to file
        dest_csvfile = open(dest_filename, 'w', encoding="ANSI", newline='')  # reading csv file
        csvwriter = csv.writer(dest_csvfile, delimiter=';')                                                 # creating object to work on file
        print("\nResult is in the same path as \"details.csv\", named \"{}\".".format(dest_filename))
        for row in all_rows_to_file:                                                                        # writing result to dest file
            csvwriter.writerow(row)

        dest_csvfile.close()                                                                                # closing opened file

def main():

    Details = File("details_empty.csv")                                                                     # creating object
    all_rows_from_file, dest_filename = Details.file_check(Details.file)
    rows_to_file, found_item =  Details.re_find(all_rows_from_file, re.compile(r"(?:(?<=\siss\.\s)\d*|(?<=\snr\s)\d\d*|(?<=\s\Do\.\s)\d*|(?<=\snum\.\s)\d*|(?<=\s\Dssue\s)\d*)"))      #column3
    rows_to_file, found_item =  Details.re_find(all_rows_from_file, re.compile(r"(?:(?<=vol\.\s)\d*|(?<=\st\.\s)\d*|(?<=Vol\.\s)\d*|(?<=\sT\.\s)\d\d)"))                               #column4
    rows_to_file, found_item =  Details.re_find(all_rows_from_file, re.compile(r"(?:(?<=nr art\.\s)\D+\d+)"))                                                                          #column5
    rows_to_file, found_item =  Details.re_find(all_rows_from_file, re.compile(r"(?:(?<=\ss\.\s)\d+-\d+|(?:\d+-\d+))"))                                                                #column6
    rows_to_file, found_item =  Details.re_find(all_rows_from_file, re.compile(r"(?:(?<=\s\:\s).+(?=\,\s2019)|(?<=\s\:\s).+(?=\s\\)|(?<=\s\:\s).+(?=\,\scop\.\s2019))"))               #column8
    rows_to_file, found_item =  Details.re_find(all_rows_from_file, re.compile(r"(?:^.+(?=\s:))"))                                                                                     #column9
    rows_to_file, found_item =  Details.re_find(all_rows_from_file, re.compile(r"(?:(?<=\,\s)?2\d{3})"))                                                                               #column10

    Details.write_to_file(rows_to_file, dest_filename)


main()