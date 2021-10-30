import re  # to hadle with regular expressions
import csv  # to work with csv files


class Csvfile1:  # class counts only lowercase words

    def upd_f():
        a = {}

        with open('NewsFeed.txt', 'r') as f:
            for line in f:
                for word in line.split():
                    word = word.lower()
                    word = word.replace(',', '')  # replacing ',' and ';'
                    word = word.replace(':', '')
                    if word not in a.keys():  # if word not in dictionary, insert it to dict
                        a.update({word: 1})
                    else:  # otherwise, count as one more entry in the file
                        value = a[word]
                        value = value + 1
                        a.update({word: value})

        a_copy = a.copy()  # copy dict for futher deleting not conditional trash

        for key, value in a_copy.items():
            if re.findall('^[-+]?[0-9]+$', key):
                a.pop(key)
            elif re.findall('^[-+]?[-]+$', key):
                a.pop(key)
            elif re.findall('^[-+]?[0-9][0-9].[0-9][0-9]+$', key):
                a.pop(key)
            elif re.findall('^(\d{2})[/.-](\d{2})[/.-](\d{4})$', key):
                a.pop(key)

        with open('csv_file1.csv', 'w+') as csv_file:  # saving to scv
            for key, value in a.items():
                csv_file.write(f' {key} - {value} \n')
        print('first ready')


class Csvfile2:  # letters counter

    def upd_f():

        c = []  # letterlist

        with open('NewsFeed.txt', 'r') as f:  # separating letters from symbols
            for line in f:
                for word in line.split():
                    word = word.lower()
                    b = [char for char in word]  # reading symbols in lowercase
                    n = len(b)
                    for i in range(n):
                        if re.findall('^[-+]?[a-z]+$', b[i]):  # add to list for letters
                            if b[i] not in c:  # if it not in list already
                                c.append(b[i])

        n = len(c)  # for cycle
        lower_let = []  # list that contain count of lowercase letters
        upper_let = []  # list that contain count of uppercase letters
        all_let = []  # list that contain count of letters
        k = 0  # variable, that contain count of all letters

        with open('NewsFeed.txt', 'r') as f:  # occurrence of each letter
            fil = f.read()
            for i in range(n):
                lower_let.append(fil.count(c[i]))
                upper_let.append(fil.count(c[i].upper()))
                all_let.append(lower_let[i] + upper_let[i])
                k = k + all_let[i]

        with open('csv_file2.csv', 'w+') as csv_file:  # saving to csv
            headers = ['Letter', ' Number of occurrences', ' Number of uppercase', ' Percentage, %']  # define headers
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()  # write headers
            for i in range(n):  # write all info to csv file
                writer.writerow(
                    {'Letter': c[i], ' Number of occurrences': all_let[i], ' Number of uppercase': upper_let[i],
                     ' Percentage, %': round(all_let[i] / k * 100, 2)})
        print('second ready')
