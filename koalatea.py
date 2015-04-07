#!/srv/gs1/software/python/3.4/bin/python3

import subprocess
import argparse
import string
import json

parser = argparse.ArgumentParser()
parser.add_argument('inputjson')
parser.add_argument('medgapdir')
args = parser.parse_args()
args_dict = vars(args)

# Get version from json
with open(args.inputjson) as jsonfile:
    json_dict = json.load(jsonfile)
    args_dict['version'] = json_dict['version']

template_string = 'jsonWorkflow.py -c ${inputjson} -s ${medgapdir}/koalatea-${version}/koalatea.sjm bam=${medgapdir}/genome.recal.bam vcf=${medgapdir}/genome.recal.vcf --outdir ${medgapdir}/koalatea-${version} --run'
cmd_template = string.Template(template_string)
cmd_string = cmd_template.substitute(args_dict)
subprocess.call(cmd_string, shell=True)
