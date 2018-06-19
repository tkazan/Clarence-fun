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


def links_and_content_list_creator(cli_args):
    """Take a file path from a command line arguments
    and return list of each link with its content out of the file."""
    links_contents_list = []
    with open(cli_args[0]) as f:
        for line in f:
            link = line.strip()
            try:
                r = requests.get(link)
                html = r.content
            except requests.exceptions.RequestException:
                html = None
            links_contents_list.append([link, html])
        return links_contents_list


def buttons_counter(links_contents_list):
    """Loop through the list_of_links_and_contents
    and return a list of links and buttons amount in each"""
    links_btn_amt = []
    for element in links_contents_list:
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
            links_btn_amt.append([link, len(total_buttons)])
        except TypeError:
            links_btn_amt.append(
                [link, 0])
    sorted_links_btn_amt = sorted(links_btn_amt, key=lambda x: x[1], reverse=True)
    return sorted_links_btn_amt


def output_file_generator(arguments, sorted_links_btn_amt):
    """Create a file with links to websites
    and number of buttons inside each."""
    with open(arguments[1], 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['address', 'number_of_buttons'])
        for elem in sorted_links_btn_amt:
            csv_writer.writerow([elem[0], elem[1]])


if __name__ == '__main__':
    args = inputs_checker()
    links_contents = links_and_content_list_creator(args)
    links_btn_amt = buttons_counter(links_contents)
    output_file_generator(args, links_btn_amt)
    print("Success! The csv file: {} with links and "
          "counted buttons in each has been created.".format(args[1]))

