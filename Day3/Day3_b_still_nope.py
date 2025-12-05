
import os
import itertools
import progressbar

current_script_dir = os.path.dirname(os.path.realpath(__file__))
inputfile=current_script_dir + '\in_test2.txt'

answer = 0
numlen = 12
delim = ''

# Define a custom set of widgets
widgets = [
    'Progress: ',                                # Description text
    progressbar.Percentage(),         # Show percentage completed
    ' ',                              
    progressbar.Bar(marker=':'),      # Custom bar with specified marker
    ' ',
    progressbar.ETA(),                    # Estimated time remaining
    ' | ',
    progressbar.Timer(),                  # Time elapsed
]

with open(inputfile, 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
    print('Input has',line_count,'lines')


# Initialize the progress bar with widgets
bar = progressbar.ProgressBar(widgets=widgets, maxval=line_count)
bar.start()
x = 0
with open(inputfile, 'r') as file:
    for line in file:
        print(line)
        numbers = list(line)
        all_jolts = []
        for j in itertools.combinations(line, numlen):
            all_jolts.append(int(delim.join(j)))
        print(all_jolts)
        print(max(all_jolts))
        answer = answer + max(all_jolts)
        print('.', end="")
        x =+ 1
        bar.update(x)


print(answer)