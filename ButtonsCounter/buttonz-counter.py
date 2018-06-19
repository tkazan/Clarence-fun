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
        cli_args = [input_file_path, output_file_path]
        return cli_args


def links_and_content_list_creator(arguments):
    """Take a file path from a command line arguments
    and return list of each link with its content out of the file."""
    links_and_contents_list = []
    with open(arguments[0]) as f:
        for line in f:
            link = line.strip()
            try:
                r = requests.get(link)
                html = r.content
            except requests.exceptions.RequestException:
                html = None
            links_and_contents_list.append([link, html])
        return links_and_contents_list


def buttons_counter(list_with_links_and_contents):
    """Loop through the list_of_links_and_contents
    and return a list of links and buttons amount in each"""
    list_of_links_and_btn_amt = []
    for element in list_with_links_and_contents:
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
    args = inputs_checker()
    list_of_links_and_contents = links_and_content_list_creator(args)
    links_and_btn_amt_sorted_list = buttons_counter(list_of_links_and_contents)
    output_file_generator(args, links_and_btn_amt_sorted_list)
    print("Success! The csv file: {} with links and "
          "counted buttons in each has been created.".format(args[1]))

