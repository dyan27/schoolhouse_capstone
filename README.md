
## Student Instruction

In this assignment, you need to submit the Python code needed to run your program. You also need to submit a report generated from the program (the HTML files and figure/plot files). For report generation projects, see files below for example and module to support report generation.

(4 points) Program reads in external dataset effectively. If the program requires something like a password, please do not include it if it is private.

(2 points) Program runs on my system with the actual dataset or a notional example dataset if the actual dataset is private or requires special access. (If actual dataset is private, screenshots or report can be of the notional example dataset)

(4 points) Code readability

Variables are named well
Code uses the same naming convention (Links to an external site.) throughout (does not need to match any modules that you use)
Comments are used to document code that is not clear by itself
No dead or unused parts in the code, such as unused variables
(8 points) Incorporate any eight of the following components into your code:

function that utilizes one or more parameters (1 point for each function)
utilization of the Pandas Python module (1 point for usage, 2 points for heavy usage)
utilization of the numpy Python module (1 point of usage)
utilization of any other data oriented Python module (1 point for each module)
class and instance(s)  (1 point for each class, 1 point for each method)
extra plots (1 point for each plot)
web service requests (2 points for proper usage)
SQL database or another type of database (4 points for proper usage)
Data formats other than CSV formatted data such as XML, JSON, or Excel speadsheets (1 point)
Animated plots (4 points)

(6 points) have at least 3 sections with different content

(18 points) have at least two plots/charts with the following appropriate details:

Title
X-Axis label
Y-Axis label
Represents data from dataset effectively
X-Axis marker labels appropriate
Y-Axis marker labels appropriate
(4 points) have a data table with clear data and headers

(4 points) incorporate dataset computations to change the content of the generated report
Here are some files that you should use to generate your report [report_generator_project_files.zip](https://github.com/dyan27/AFIT-DASC511-Project/blob/main/report_generator_project_files.zip). Download and unzip the file.  


## Instructor Instruction for running flask v2:
1. python3 -m venv venv
2. source venv/bin/activate
3. pip3 install -r requirements.txt
4. flask run
5. http://localhost:5000/project

Notes: 
1. You might need to upgrade your pip:
(python3 -m pip install --upgrade pip)
2. If there is anaconda installed in the system, you need to deactive and activate again venv.
(deactivate)
(source venv/bin/activate)

## About the code for this project
In this project, I have completed the following:
1. Using more than one functions with one or more parameters.
2. Utilization of the Pandas Python module
3. Utilization of the numpy Python module
4. Utilization of the seaborn Python module
5. Some extra plots
6. Creating an animated plot
7. Have at least 3 sections with different content
8. Including more than two plots.charts with appropriate title and labeling.
9. Including a data table with clear data and headers
10. Incorporate some data cleaning to change the content of generated report.


<!-- ## Building in flask:
To serve the project in flask, use the following commands:
```
virtualenv -v venv
source venv/Scripts/activate
pip install -r requirements.txt

export FLASK_APP=mysite.py
export FLASK_ENV=development

flask db init
flask db migrate -m "initial migration"
flask db upgrade

flask run
```
Note that `export` is the command for Unix/Mac and `set` is the Windows equivalent
Similarly, sourcing the activate script has numerous options, all contained within ./venv/Scripts
If there are any issues in running the above commands to start the application, please contact SSgt Tatro from 336TRS, whose email can be found in the `git log` command of the 336TRS branch of development -->


