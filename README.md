# h1b_statistics
1. [Problem](README.md#problem)
2. [Approuch](README.md#approuch)
3. [Run instructions](README.md#run-instructions)
# Problem

The immigration data trends have gained much attention recently because of the stringent provisions to the H-1B labour application process. When a newspaper editor was researching this issue, she found statistics unavailable from the US Department of Labor and its Office of Foreign Labor Certification Performance Data for past years.

This mechanism is aimed to solve this problem. By this mechanism, the editor can get Top 10 Occupations and Top 10 States for certified visa applications easily.

# Approuch

1.Load data: Use the Python Standard Library `csv` to read data.

2.Clean and prepare data: Remove the items which miss some information by checking the number of columns. Delete unnecessary quotes in data.

3.Sort: Use the Python Standard Library `conlections` to pick the top ten states and top ten occupations.

4.Output: Use the Python Standard Library `csv` to generate output files.

# Run instructions

Directly run the run.sh file to execute `h1b_analyzer.py` and the output files `top_10_occupations.txt` and `top_10_states.txt` will automatically generate under the `output` folder.
