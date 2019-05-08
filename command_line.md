# Command Line

## grep  (global regular expression print)
Using grep example

### Example 1

    $ ps | grep python

This finds all running processes with the word 'python'

### Example 2

    $ grep "exist" pgadmin.log

grep will search the input file `pgadmin.log` for a search string `exist`, and print the lines that match it. Beginning at the first line in the file, grep copies a line into a buffer, compares it against the search string, and if the comparison passes, prints the line to the screen. Grep will repeat this process until the file runs out of lines. 
grep does not store lines, change lines, or search only a part of a line.

### Example 3

    $ grep "COPY$" pgadmin.log 

Searches for lines in `pgadmin.log` that end with `COPY`

## AWK
A text pattern scanning and processing language. An awk program operates on each line of an input file.
For each line of the input file, it sees if there are any pattern-matching instructions, in which case it
only operates on lines that match that pattern, otherwise it operates on all lines. These
'pattern-matching' commands can contain regular expressions as for grep. The awk commands can
do some quite sophisticated maths and string manipulations, and awk also supports associative
arrays.

### Example 1
    
    $ awk '{print $1}' pgadmin.log

This prints the first column for each line in the file

Awk assigns some variables for each data field found:
$0 for the whole line.
$1 for the first field.
$2 for the second field.
$n for the nth field.
The whitespace character like space or tab is the default separator between fields in awk.

### Example 2

    $ echo "This is an assessment" | awk '{$2="REALLY IS"; print $0}'

This sets the second column "is" to "REALLY IS" and prints the entire line


## sed (Stream Editor)
sed performs basic text transformations on an input stream (a file or input from a pipeline) in a
single pass through the stream, so it is very efficient. However, it is sed's ability to filter text in a
pipeline which particularly distinguishes it from other types of editor.

## xargs
A filter for feeding arguments to a command, and also a tool for assembling the commands themselves. It breaks a data stream into small enough chunks for filters and commands to process. Consider it as a powerful replacement for backquotes.