# QBS 181 Data Wrangling Final Project

**Dataset and Analysis**


The Child and Adult Healthcare Quality Measures Quality data set is a collection of measures used to appraise healthcare per state. Every state is displayed with the measures they have used to appraise the quality of care in different domains of healthcare

We want to compare how healthcare quality is measured across different states, as well compare not only how healthcare has improved over a year, using the 2019 and 2020 versions of this dataset, but also, how reporting how the quality of healthcare has changed.

We want to see how insurance coverage affects the measures chosen and reported on per state, as well as what methodology is chosen for the measure, and how coverage affects this.
<br />

**final_project_hw**
Plots comparing average state rates between 2019 and 2020 and the average state rates of a random sample of states. Additionally a plot showing the mean number of states reporing measures in each domain.
<br />

**Python Script**

hyunjoe_qbq181.py is a Python program (on google colab) that displays the states with top 10% State Rate value and ranks the states based on State Rate of the data.
Top 10% States with top 10% value from the set is calculated for each dataset if the high value is a better measurement for 2020 adult data, 2020 children data, 2019 adult data, and 2019 children data.
<br />


**Installation**

APIs to be updated.
<br />


**Insurance Coverage Analysis**
As per a few chosen measures in each domain, how does insurance coverage affect the measures 
reported on per state? What methodology is chosen for the measure, and how does coverage 
affect this?

First, we look into what domains are presented in this dataset. These Domains are the fields 
of healthcare that are represented in the measures for analysis throughout this data set.

Once we understand what domains are available, we select one to two measures per domain to use
as our sample set for analysis. These measures were selected with the goal of representing the
widest set of medicaid and medicare recipients.

In order to select the measures, this column had to converted from character values to factors

Once the measures are selected, a subsetted data set is created for analysis which contains 
only the selected measures

population coloumn gives the coverage types so it is important to see what is represented here

In order to get the count of states reporting each measure in our sample of measures, we 
filter by measure, get the distinct value of states, get the length of the distinct states, 
put these values in a vector, and presenting the findings in a barplot, using ggplot

Looking at the specific coverage populations, we can calculate how many measures in our sample
are represented in each coverage population using the same mechanism as above, then 
representing our findings with a barplot.

There is another column, state specific comments, which is filled with natural language. we 
can delve deep here and see in depth how delivery system, which is what is talked about in 
this column, affects how many measures in our subset is reported.

firstly, we make a copy of the subsetted data, then seperate the state specific comments 
sections word by word. Then, we remove common english words that do not contribute to the 
context of the sentence. Next you calculate the frequency of the remaining words and plot 
these frequency

However, it is important to note that these delivery system words are not mentioned as often 
as other words, but these delivery systems have drastically different word counts according 
to the frequency chart. Perhaps each delivery system reports a different amount of measures

Finally, we filter through the main subsetted data set using the delivery systems (looking 
through the state specific comments section) and get the counts of the measures in our sample 
set. We plot these findings in a bar plot 





