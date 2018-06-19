import sys
import csv


def inputs_checker():
    """Check command line arguments and if all are correct return them"""
    try:
        csv_file_path = sys.argv[1]
        velocity = int(sys.argv[2])
        if not csv_file_path.endswith('.csv'):
            print("WARNING! First argument needs to be a .csv file.")
            sys.exit()
        f = open(csv_file_path)
        f.close()
    except IndexError:
        print("WARNING! There have to be exactly 2 command line arguments.")
        sys.exit()
    except ValueError:
        print("WARNING! Second argument (team velocity) has to be an integer.")
        sys.exit()
    except FileNotFoundError:
        print("WARNING! There is no such file or directory '{}'.".format(csv_file_path))
        sys.exit()
    else:
        cli_args = [csv_file_path, velocity]
        return cli_args


def sorted_tasks_list_creator(arguments):
    """Take a file path and team velocity from a command line arguments
    and return sorted list of tasks."""
    csv_file_path = arguments[0]
    velocity = arguments[1]
    with open(csv_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_content_list = []
        for row in csv_reader:
            task_id = int(row['task_id'])
            story_points = int(row['story_points'])
            ksp = int(row['KSP'])
            profit_index = ksp / story_points
            if story_points <= velocity:
                csv_content_list.append([task_id, story_points,
                                         ksp, profit_index])
        csv_content_list.sort(key=lambda x: x[1], reverse=True)
        csv_content_list.sort(key=lambda x: x[3], reverse=True)
        return csv_content_list


def task_chooser(tasks_list, arguments):
    """Take a sorted tasks list and team velocity, choose most profitable tasks
    that don't exceed velocity value and write to STDOUT their indexes"""
    velocity = arguments[1]
    total_story_points = 0
    chosen_tasks_list = []
    for task in tasks_list:
        if total_story_points == velocity:
            break
        elif total_story_points + task[1] <= velocity:
            total_story_points += task[1]
            chosen_tasks_list.append(task[0])
    chosen_tasks_list.sort()
    chosen_tasks_list = [str(task) for task in chosen_tasks_list]
    sys.stdout.write(', '.join(chosen_tasks_list) + '\n')


if __name__ == '__main__':
    args = inputs_checker()
    csv_sorted_list = sorted_tasks_list_creator(args)
    task_chooser(csv_sorted_list, args)

