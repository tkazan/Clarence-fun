import sys
import requests
from bs4 import BeautifulSoup
import re
import csv


def inputs_checker():
    """Check command line arguments and if all are correct return them"""
    try:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        if not output_file_path.endswith('.csv'):
            print("WARNING! Output (second argument) needs to be a .csv file.")
            sys.exit()
        f = open(input_file_path)
        f.close()
    except IndexError:
        print("WARNING! There have to be exactly 2 command line arguments.")
        sys.exit()
    except FileNotFoundError:
        print("WARNING! There is no such file or directory '{}'.".format(input_file_path))
        sys.exit()
    else:
        arguments = [input_file_path, output_file_path]
        return arguments


def list_of_websites_links_and_content_creator(arguments):
    """Take a file path from a command line arguments
    and return list of each link with its content out of the file."""
    list_of_links_and_contents = []
    with open(arguments[0]) as f:
        for line in f:
            link = line.strip()
            try:
                r = requests.get(link)
                html = r.content
            except requests.exceptions.RequestException:
                html = None
            list_of_links_and_contents.append([link, html])
        return list_of_links_and_contents


def buttons_counter(list_of_links_and_contents):
    """Loop through the list_of_links_and_contents
    and return a list of links and buttons amount in each"""
    list_of_links_and_btn_amt = []
    for element in list_of_links_and_contents:
        link = element[0]
        html = element[1]
        try:
            soup = BeautifulSoup(html, 'lxml')

            buttons = soup.find_all('button')
            inputs = soup.find_all('input', {'type': ['submit', 'reset', 'button']})
            pattern = re.compile('.*(btn|button).*', re.IGNORECASE)
            btn_button_classes = soup.find_all(class_=pattern)

            total_buttons = buttons + inputs

            sorted_btn_button_classes = []
            for elem in btn_button_classes:
                if elem not in total_buttons:
                    sorted_btn_button_classes.append(elem)
            total_buttons += sorted_btn_button_classes
            list_of_links_and_btn_amt.append([link, len(total_buttons)])
        except TypeError:
            list_of_links_and_btn_amt.append(
                [link, 0])
    sorted_list_of_links_and_btn_amt = sorted(list_of_links_and_btn_amt,
                                              key=lambda x: x[1], reverse=True)
    return sorted_list_of_links_and_btn_amt


def output_file_generator(arguments, sorted_list_of_links_and_btn_amt):
    """Create a file with links to websites
    and number of buttons inside each."""
    with open(arguments[1], 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['address', 'number_of_buttons'])
        for elem in sorted_list_of_links_and_btn_amt:
            csv_writer.writerow([elem[0], elem[1]])


if __name__ == '__main__':
    arguments = inputs_checker()
    list_of_links_and_contents = list_of_websites_links_and_content_creator(arguments)
    sorted_list_of_links_and_btn_amt = buttons_counter(list_of_links_and_contents)
    output_file_generator(arguments, sorted_list_of_links_and_btn_amt)
    print("Success! The csv file: {} with links and "
          "counted buttons in each has been created.".format(arguments[1]))

