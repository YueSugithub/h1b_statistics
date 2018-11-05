# h1b_statistics
1. [Problem](README.md#problem)
2. [Approuch](README.md#approuch)
3. [Run instructions](README.md#run-instructions)
# Problem

The immigration data trends has gained much attention recently because of the stringent provisions to the H-1B labour application process.
When a newspaper editor was researching this issue, she found statistics unavailable from the US Department of Labor and its Office of Foreign Labor Certification Performance Data for past years.

This mechanism is aimed to help to solve this problem. By this mechanism, the editor can get Top 10 Occupations and Top 10 States for certified visa applications easily.

# Approuch
##Load data
Use the Python Standard Library `csv` to read data.
##Clean data
Remove the item which misses some information by checking the number of columns.
##Sort
Use the Python Standard Library `conlections` to pick the top ten states and top ten occupations.
##Output
Use the Python Standard Library `csv` to generate output files.

# Run instructions
Directly run the run.sh file to execute `h1b_analyzer.py` and the output files `top_10_occupations.txt` and `top_10_states.txt` will automatically generated under the `outpt` folder
