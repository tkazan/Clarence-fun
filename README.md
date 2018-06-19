Tobiasz Kazanowski<br/>
<a href="mailto:tobiaszkazanowski@gmail.com">tobiaszkazanowski@gmail.com</a>
# CLARENCE FUN
### 1. SPRINT PLANNER

<p>Program helps to choose tasks for next sprint.
Each task has id, story_points and KSP (Knowledge and Skill Points).
The goal is to choose tasks with maximum KSP however sum of their story_points
cannot exceed team velocity. <br/>
The program uses approximation algorithm therefore it is not entirely acurate, 
but it is good enough for a large set of data.</p>

<p>Python script takes exactly 2 CLI arguments
(first for input csv file, second for team velocity) and checks them.</p>

<p>Script reads rows from csv file, rejects tasks with story_points over team 
velocity, counts profit indexes (KSP / story_points) for each task 
and adds them to the list of tasks.
In the next step the list is sorted, firstly by profit indexes and secondly 
by story_points both descending.</p>

<p>Afterwards program is taking tasks with the biggest profit indexes as long
as sum of their story_points is less than team velocity. Finally program gives 
output with indexes of chosen tasks.</p>

<p>Module name: sprint-planning-helper.py<br/>
Example of use from CLI: sprint-planning-helper.py test-file.csv 5</p>

<hr>

### 2. BUTTONS COUNTER

<p>Python script takes exactly 2 CLI arguments 
(first for input file and second for output file).<p>

<p>Script takes website links from input file, 
makes connection and reads content of each (using requests).</p>

<p>In next step program searches for all buttons (using BeautifulSoup):

- tag button
- tag input with types: submit, reset or button
- classes that contain (case insensitive): btn, button (using regex)
</p>

<p>Afterwards script counts all of found buttons 
(buttons with button tag and class btn or 
buttons that have multiple btn or button classes are counted only once)
and lists them in a pairs link-number_of_buttons</p>

<p>Then converts list to sorted by number of buttons descending and finally
writes pairs: link, number_of_buttons to the output csv file</p>

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