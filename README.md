# Git cloner

This script allows us to clone a set of repositories specified inside a txt file into a concrete folder.

Execution example: 

```
python3 cloner.py --file repositories.txt --dest ~/Desktop/correccions
```

## Generate task report

The idea is to transform the rubrik values into a readable report for each alumn.

### Parameters

- The rubricks file (in json format with the fields: [name, id, value]): --rubrickFile
- The values file (in json format witht eh fields: [alumn, rubrickId1, rubrickId2 ... ]): --valuesFile

### Output

A report that assigns the value to the rubrick in markdown.

### Execution example

```
python3 generateTaskReport.py --rubrickFile /path/to/rubricks --valuesFile /path/to/values
```
