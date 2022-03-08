import report_util
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings 
warnings.filterwarnings('ignore')

# function to read the data.
# utilization of Pandas
def read_data():
    df = pd.read_csv('adult.csv')
    return df

# function to replace "?" in the column to "nan"
# utilization of numpy
def clean_data(col_name):
    df[df == '?'] = np.nan
    for col in [col_name]:
        df[col].fillna(df[col].mode()[0], inplace=True)
    return df[col_name].isnull().any()

# function to rename column names for easy reading
def change_columns_name():
    df.columns = ["age", "work_class", "final_weight", "education", "education_in_number", "marital_status",
             "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss",
             "hours_per_week", "native_country", "income"]
    return df


# function to rename age column to age group names
def age_with_group_level(x):
    if (x < 31):
        return 'younger than 30'
    if (31 <= x < 41):
        return '31-40'
    if (41 <= x < 51):
        return '41-50'
    if (51 <= x < 61):
        return '51-60'
    if (61 <= x < 71):
        return '61-70'
    if (71 <= x < 81):
        return '71-80'
    else:
        return 'Order than 80'

# function creates a animated graph using plotly.express model.
def age_hours_income():
    df_age_hours_income=df.groupby(['age','income']).apply(lambda x:x['hours_per_week'].count()).reset_index(name='Hours')
    fig = px.line(df_age_hours_income,x='age',y='Hours',color='income',title='Age By Hours Of Work For Income Level')
    fig.write_html('animated_graph.html')

# function to generate report.
def generate_report(dataset):
    page_title = """US Adult Income Data Analysis
    By Evelyn
    """
    report = report_util.Report(page_title)

    section = report.add_section("Overview")
    paragraph = section.add_paragraph()

    paragraph.append("This data was extracted from the U.S Census bureau database by Ronny Kohavi and Barry Becker (Data Mining and Visualization, Silicon Graphics).\n") 
    paragraph.append("The goal of this project is to show some feature table and distribution graphs in the dataset.")

    ##################################################
    # The following code demonstrates creating a table
    ##################################################
    # add a section
    section_1 = report.add_section("Table")
    # add a new paragraph
    paragraph_1 = section_1.add_paragraph()

    tbl_1 = section_1.add_table()
    tbl_1.caption = "Dataset Listing"
    tbl_1.set_header(["Age","Work Class","Education", "Marital Status", "Relationship", "Race", "Gender"])
    tbl_1.set_data(zip(dataset['age'].head(50),dataset['work_class'].head(50), dataset['education'].head(50), dataset['marital_status'].head(50), dataset['relationship'].head(50), dataset['race'].head(50), dataset['sex'].head(50)))

    paragraph_1.append_cross_reference(tbl_1)
    paragraph_1.append(f" shows the some columns information in the dataset.")

    ####################################################################################
    # The following code demonstrates creating a figure directly with the matplotlib API
    ####################################################################################
    section_2 = report.add_section("Distribution")
    paragraph_2 = section_2.add_paragraph()

    figure_2 = section_2.add_figure()
    figure_2.caption = "Education Distribution"

    ax = figure_2.matplotlib_figure.add_subplot(1,1,1)
    # create a histogram for education column
    ax.hist(df['education_in_number'], 100, density = 1)
    # adding labels for x and y axises
    ax.set_xlabel("Education")
    ax.set_ylabel("Count")
    figure_2.matplotlib_figure.tight_layout()
    
    paragraph_2.append_cross_reference(figure_2)
    figure_2_content = """ shows the histogram distribution of education in the dataset, 
    the observation appears the most density peak appears at the 9, which is high school graduation. 
    The second peak appears at 10. The last rise seems at 13, which means after high school graduation, 
    most working people decided to go to college and have some years of college education or a bachelor's degree.
    """
    paragraph_2.append(figure_2_content)

    #############################################################################################
    # The following code demonstrates creating other figures
    # utlization of seaborn model
    #############################################################################################

    section_3 = report.add_section("More Advanced Graph")

    paragraph_3 = section_3.add_paragraph()

    figure_3 = section_3.add_figure()
    title = 'age_level'.replace("_", " ").title()
    figure_3.caption = 'Income vs Different {} Groups'.format(title)
    figure_3.matplotlib_figure.add_subplot(1,1,1)
    sns.set_theme(style="white")
    # reset the age group order from youngest to oldest for better view
    order = ['younger than 30','31-40', '41-50', '51-60','61-70','71-80', 'Order than 80' ]
    # use seaborn to create coutplot compare age and income
    sns.countplot(dataset['age_level'], hue = dataset['income'], order = order)
    # rename title, x and y axises lables
    plt.title('Income vs Different {} Groups'.format(title), fontsize=14, fontweight='bold')
    plt.xlabel(title)
    plt.ylabel('No. of Count')
    # change the x axises label rotation for better view
    plt.xticks(fontsize=12, rotation =45)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.tight_layout()

    paragraph_3.append_cross_reference(figure_3)
    figure_3_content = """ shows different age group income level, the observation appears people aged between 41 and 50 have the most count 
    for income, more than 50k. It also seems to have the most percentage compared with less than 50k, which means most higher-income people 
    have reached their peak for their career around mid 40 years old, and the chances people will get their higher-income age is around middle 
    40 years old. People usually start their career around the late 20s and early 30s, and some people might get a higher pay job so that they 
    will have more than 50k at an earlier age, but the percentage for those in that age group was low. Later on, we will analyze what occupation 
    will lead to higher income at an earlier age.
    """
    paragraph_3.append(figure_3_content)

    # More Figures for Two Income Factors
    paragraph_4 = section_3.add_paragraph()

    figure_4 = section_3.add_figure()
    figure_4.caption = 'Boxenplot On Work Hours For Different Income Levels'
    figure_4.matplotlib_figure.add_subplot(1,1,1)
    sns.boxenplot(x = 'income', y = 'hours_per_week', data=dataset, palette = 'ocean');
    title1 = 'income'.title()
    title2 = 'hours_per_week'.replace("_", " ").title()
    plt.title('{} vs {}'.format(title1, title2), fontsize=14, fontweight='bold')
    plt.xlabel(title1)
    plt.ylabel(title2)
    plt.tight_layout()
    

    paragraph_4.append_cross_reference(figure_4)
    figure_4_content = """ shows the boxenplot for hours per week on different income levels. 
    People also thought there is a direct connection between working hours and income, and the more hours one works, 
    the more revenue one should earn. However, this hypothesis only works for hourly employees. 
    The boxplot above shows people making more than 50k work mean hours per week greater than those earning less than 50k. 
    At the same time, there is an extensive range of working hours for people making more than 50k, 
    so there isn't solid evidence to prove there is a direct connection between working hours and income for higher-income people. 
    """
    paragraph_4.append(figure_4_content)


    # More Figures
    paragraph_5 = section_3.add_paragraph()

    figure_5 = section_3.add_figure()
    figure_5.caption = 'Mean Age For Education Gender Group'
    figure_5.matplotlib_figure.add_subplot(1,1,1)
    df.groupby(["education", "sex"])["age"].mean().plot.barh();
    plt.title('Mean age', fontsize=14, fontweight='bold')
    plt.xlabel('Age')
    plt.ylabel('Education, Gender')
    plt.tight_layout()
    
    paragraph_5.append_cross_reference(figure_5)
    figure_5_content = """ shows the mean age for different groups of education with different gender. 
    """
    paragraph_5.append(figure_5_content)

    # More Figures
    
    paragraph_6 = section_3.add_paragraph()

    # open animated_graph.html file to view the graph
    figure_6_content = """ The animated_graph.html file in the project folder shows the mean age for different groups of education with different gender. 
    """
    paragraph_6.append(figure_6_content)

    # Generate Report.
    return report

if __name__ == "__main__":
    
    df = read_data()
    df = change_columns_name()
    clean_data('work_class')
    clean_data('occupation')
    clean_data('occupation')
    df['age_level'] = df['age'].apply(age_with_group_level)

    age_hours_income()

    report = generate_report(df)

    html_generator = report_util.HTMLReportContext("")
    html_generator.generate(report,"project-evelyn")

    