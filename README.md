# CLARENCE FUN
### 1. SPRINT PLANNER
<p></p>

<hr>

### 2. BUTTONS COUNTER
<p>Python script that take exactly 2 CLI arguments 
(first for input file and second for output file).<p>

<p>Script take website links from input file, 
make connection and read content of each (requests).</p>

<p>Next program search for all buttons (BeautifulSoup):

- tag button
- tag input with types: submit, reset or button
- classes that contains (case insensitive): btn, button (regex)
</p>

<p>Afterwards script sum all of found buttons 
(buttons with button tag and class btn or 
buttons that have multiple btn or button classes are counted only once)
and list them in a pairs link-number_of_buttons</p>

<p>Covert list to sorted by number of buttons descending and finally
write pairs: link, number_of_buttons to the output csv file</p>

<hr>

### REQUIREMENTS:
- Python 3 <br/>

pip install:
- requests
- bs4
- lxml