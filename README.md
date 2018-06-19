# CLARENCE FUN
### 1. SPRINT PLANNER

<p>Program help to choose tasks for for next sprint.
Each task has id, story_points and KSP(Knowledge and Skill Points).
The goal is to choose task with maximum KSP but sum of story_points
can't exceed team velocity. <br/>
It's an approximation algorithm but it's efficiency and performance 
should be enough for a large set.</p>

<p>Python script take exaclty 2 CLI arguments
(first for input csv file, second for team velocity) and check them.</p>

<p>Script read rows from csv file, reject tasks with story_points over team 
velocity, count profit indexes (KSP / story_points)for each task and add to list of tasks.
Next list of tasks is sorted, firstly by story_points and secondly by profit indexes 
both descending.</p>

<p>Afterwards program is taking task with the biggest profit indexes as long
as sum of their story_points is less than team velocity. Finally program give 
output with indexes of chosen tasks.</p>

<p>Module name: sprint-planning-helper.py<br/>
Example of use from CLI: sprint-planning-helper.py test-file.csv 5</p>

<hr>

### 2. BUTTONS COUNTER

<p>Python script take exactly 2 CLI arguments 
(first for input file and second for output file).<p>

<p>Script take website links from input file, 
make connection and read content of each (requests).</p>

<p>Next program search for all buttons (BeautifulSoup):

- tag button
- tag input with types: submit, reset or button
- classes that contains (case insensitive): btn, button (regex)
</p>

<p>Afterwards script count all of found buttons 
(buttons with button tag and class btn or 
buttons that have multiple btn or button classes are counted only once)
and list them in a pairs link-number_of_buttons</p>

<p>Convert list to sorted by number of buttons descending and finally
write pairs: link, number_of_buttons to the output csv file</p>

<p>Module name: buttonz-counter.py<br/>
Example of use from CLI: buttonz-counter.py website_to_scrape.txt text.csv</p>

<hr>

### REQUIREMENTS:
- Python 3 <br/>

pip install:
- requests
- bs4
- lxml

<strong>OR</strong> pip install -r requirements.txt