import argparse, json

parser = argparse.ArgumentParser(
            prog = 'Generate task report',
            description = 'Generates a report given rubricks and values files',
        )

parser.add_argument('--rubricksFile', help='The file containing the rubricks')
parser.add_argument('--valuesFile', help='The file containing the values')

args = parser.parse_args()

with open(args.rubricksFile, 'r') as rubricksReader:
    rubricks = json.load(rubricksReader)

with open(args.valuesFile, 'r') as valuesReader: 
    values = json.load(valuesReader)

def appendToResult(result, newLine):
    return "{}{}\n".format(result, newLine)

final = ""
for alumn in values:
    final = appendToResult(final, "### {}\n".format(alumn['alumn']))
    for rubrick in rubricks:
        final = appendToResult(final, "- {}: {}".format(rubrick['name'], alumn["{}".format(rubrick['id'])]))

    final = appendToResult(final, "\nNOTA FINAL: {}\n".format(alumn['TOTAL']))

print(final)