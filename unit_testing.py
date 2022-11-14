import unittest
import csv


class TestStringMethods(unittest.TestCase):

    def testa_column3(self):                                                                                                                # column 3
        iterator = 0

        with open('details.csv', 'r', encoding="ISO-8859-1") as file_given, open('details_result.csv', 'r', encoding="ANSI") as file_result:
            csvreader_given = list(csv.reader(file_given, delimiter=','))
            csvreader_result = list(csv.reader(file_result, delimiter=';'))

            row_given = [row[2] for row in csvreader_given]                                                                                 # reading column 3 from details.csv
            row_result = [row[2] for row in csvreader_result]                                                                               # reading column 3 from details_result.csv

            result = float((sum(item_given == item_result for item_given, item_result in zip(row_given, row_result)))/len(row_given))*100   # calculating result in percentage
            result = str(round(result,2))+"%"
            print("""----------------------------------------------------------------------------------------------------- TEST COLUMN 3 -----------------------------------------------------------------------------------------------------""")
            for item_given, item_result in zip(row_given, row_result):                                                                      # iterating over to lists
                    try:                                                                                                                    # exception handling
                        (self.assertEqual(item_result, item_given)==1)
                    except AssertionError:
                        print("Item expected: \"{}\", my result: \"{}\"".format(item_given, item_result))                                   # printing difference
                    else:
                        iterator += 1                                                                                                       # counting same results

            if iterator == len(row_given):                                                                                                  # 100% result same
                print("Items in both are the same! {}\{} matches".format(iterator, len(row_given)))
            print("Match result {}".format(result))

        self.assertEqual(len(row_given), iterator)                                                                                          # compare results


    ################################################################ the code below works on the same principle, but the columns change ########################################################################
    def testb_column4(self):
        iterator = 0

        with open('details.csv', 'r', encoding="ISO-8859-1") as file_given, open('details_result.csv', 'r', encoding="ISO-8859-1") as file_result:
            csvreader_given = list(csv.reader(file_given, delimiter=','))
            csvreader_result = list(csv.reader(file_result, delimiter=';'))

            row_given = [row[3] for row in csvreader_given]
            row_result = [row[3] for row in csvreader_result]

            result = float((sum(item_given == item_result for item_given, item_result in zip(row_given, row_result)))/len(row_given))*100
            result = str(round(result,2))+"%"
            print("""----------------------------------------------------------------------------------------------------- TEST COLUMN 4 -----------------------------------------------------------------------------------------------------""")
            for item_given, item_result in zip(row_given, row_result):
                    try:
                        (self.assertEqual(item_result, item_given)==1)
                    except AssertionError:
                        print("Item expected: \"{}\", my result: \"{}\"".format(item_given, item_result))
                    else:
                        iterator += 1

            if iterator == len(row_given):
                print("Items in both are the same! {}\{} matches.".format(iterator, len(row_given)))
            print("Match result {}".format(result))
        self.assertEqual(len(row_given), iterator)

    def testc_column5(self):
        iterator = 0

        with open('details.csv', 'r', encoding="ISO-8859-1") as file_given, open('details_result.csv', 'r', encoding="ISO-8859-1") as file_result:
            csvreader_given = list(csv.reader(file_given, delimiter=','))
            csvreader_result = list(csv.reader(file_result, delimiter=';'))

            row_given = [row[4] for row in csvreader_given]
            row_result = [row[4] for row in csvreader_result]

            result = float((sum(item_given == item_result for item_given, item_result in zip(row_given, row_result)))/len(row_given))*100
            result = str(round(result,2))+"%"
            print("""----------------------------------------------------------------------------------------------------- TEST COLUMN 5 -----------------------------------------------------------------------------------------------------""")
            for item_given, item_result in zip(row_given, row_result):
                    try:
                        (self.assertEqual(item_result, item_given)==1)
                    except AssertionError:
                        print("Item expected: \"{}\", my result: \"{}\"".format(item_given, item_result))
                    else:
                        iterator += 1

            if iterator == len(row_given):
                print("Items in both are the same! {}\{} matches.".format(iterator, len(row_given)))
            print("Match result {}".format(result))
        self.assertEqual(len(row_given), iterator)

    def testd_column6(self):
        iterator = 0

        with open('details.csv', 'r', encoding="ISO-8859-1") as file_given, open('details_result.csv', 'r', encoding="ISO-8859-1") as file_result:
            csvreader_given = list(csv.reader(file_given, delimiter=','))
            csvreader_result = list(csv.reader(file_result, delimiter=';'))

            row_given = [row[5] for row in csvreader_given]
            row_result = [row[5] for row in csvreader_result]

            result = float((sum(item_given == item_result for item_given, item_result in zip(row_given, row_result)))/len(row_given))*100
            result = str(round(result,2))+"%"
            print("""----------------------------------------------------------------------------------------------------- TEST COLUMN 6 -----------------------------------------------------------------------------------------------------""")
            for item_given, item_result in zip(row_given, row_result):
                    try:
                        (self.assertEqual(item_result, item_given)==1)
                    except AssertionError:
                        print("Item expected: \"{}\", my result: \"{}\"".format(item_given, item_result))
                    else:
                        iterator += 1

            if iterator == len(row_given):
                print("Items in both are the same! {}\{} matches.".format(iterator, len(row_given)))
            print("Match result {}".format(result))
        self.assertEqual(len(row_given), iterator)

    def teste_column8(self):
        iterator = 0

        with open('details.csv', 'r', encoding="UTF8") as file_given, open('details_result.csv', 'r', encoding="ANSI") as file_result:
            csvreader_given = list(csv.reader(file_given, delimiter=','))
            csvreader_result = list(csv.reader(file_result, delimiter=';'))

            row_given = [row[7] for row in csvreader_given]
            row_result = [row[6] for row in csvreader_result]

            result = float((sum(item_given == item_result for item_given, item_result in zip(row_given, row_result)))/len(row_given))*100
            result = str(round(result,2))+"%"
            print("""----------------------------------------------------------------------------------------------------- TEST COLUMN 8 -----------------------------------------------------------------------------------------------------""")
            for item_given, item_result in zip(row_given, row_result):
                    try:
                        (self.assertEqual(item_result, item_given)==1)
                    except AssertionError:
                        print("Item expected: \"{}\", my result: \"{}\"".format(item_given, item_result))
                    else:
                        iterator += 1

            if iterator == len(row_given):
                print("Items in both are the same! {}\{} matches.".format(iterator, len(row_given)))
            print("Match result {}".format(result))
        self.assertEqual(len(row_given), iterator)

    def testf_column9(self):
        iterator = 0

        with open('details.csv', 'r', encoding="UTF8") as file_given, open('details_result.csv', 'r', encoding="ANSI") as file_result:
            csvreader_given = list(csv.reader(file_given, delimiter=','))
            csvreader_result = list(csv.reader(file_result, delimiter=';'))

            row_given = [row[8] for row in csvreader_given]
            row_result = [row[7] for row in csvreader_result]

            result = float((sum(item_given == item_result for item_given, item_result in zip(row_given, row_result)))/len(row_given))*100
            result = str(round(result,2))+"%"
            print("""----------------------------------------------------------------------------------------------------- TEST COLUMN 9 -----------------------------------------------------------------------------------------------------""")
            for item_given, item_result in zip(row_given, row_result):
                    try:
                        (self.assertEqual(item_result, item_given)==1)
                    except AssertionError:
                        print("Item expected: \"{}\", my result: \"{}\"".format(item_given, item_result))
                    else:
                        iterator += 1

            if iterator == len(row_given):
                print("Items in both are the same! {}\{} matches.".format(iterator, len(row_given)))
            print("Match result {}".format(result))
        self.assertEqual(len(row_given), iterator)

    def testg_column10(self):
        iterator = 0

        with open('details.csv', 'r', encoding="ISO-8859-1") as file_given, open('details_result.csv', 'r', encoding="ISO-8859-1") as file_result:
            csvreader_given = list(csv.reader(file_given, delimiter=','))
            csvreader_result = list(csv.reader(file_result, delimiter=';'))

            row_given = [row[9] for row in csvreader_given]
            row_result = [row[8] for row in csvreader_result]

            result = float((sum(item_given == item_result for item_given, item_result in zip(row_given, row_result)))/len(row_given))*100
            result = str(round(result,2))+"%"
            print("""----------------------------------------------------------------------------------------------------- TEST COLUMN 10 -----------------------------------------------------------------------------------------------------""")
            for item_given, item_result in zip(row_given, row_result):
                    try:
                        (self.assertEqual(item_result, item_given)==1)
                    except AssertionError:
                        print("Item expected: \"{}\", my result: \"{}\"".format(item_given, item_result))
                    else:
                        iterator += 1

            if iterator == len(row_given):
                print("Items in both are the same! {}\{} matches.".format(iterator, len(row_given)))
            print("Match result {}".format(result))
        self.assertEqual(len(row_given), iterator)



if __name__ == '__main__':
    unittest.main()
