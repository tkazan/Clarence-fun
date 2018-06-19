import sys
import csv
from pprint import pprint

csv_file_path = sys.argv[1]
velocity = int(sys.argv[2])

with open(csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    csv_content_list = []
    for row in csv_reader:
        task_id = int(row['task_id'])
        story_points = int(row['story_points'])
        ksp = int(row['KSP'])
        profit_index = ksp / story_points
        if story_points <= velocity:
            csv_content_list.append([task_id, story_points, ksp, profit_index])
    csv_content_list.sort(key=lambda x: x[1], reverse=True)
    csv_content_list.sort(key=lambda x: x[3], reverse=True)

    total_story_points = 0
    chosen_tasks_list = []
    for task in csv_content_list:
        if total_story_points == velocity:
            break
        elif total_story_points + task[1] <= velocity:
            total_story_points += task[1]
            chosen_tasks_list.append(task[0])
chosen_tasks_list.sort()
chosen_tasks_list = [str(task) for task in chosen_tasks_list]
sys.stdout.write(', '.join(chosen_tasks_list) + '\n')
