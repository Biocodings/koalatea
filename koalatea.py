#!/srv/gs1/software/python/3.4/bin/python3

import subprocess
import argparse
import string
import json
import os

koalatea_dir = os.path.dirname(os.path.realpath(__file__))
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-c', '--conf', help="Input configuration JSON", default=os.path.join(koalatea_dir, "koalatea.json"))
parser.add_argument('medgapdir')
parser.add_argument('bamfile')
parser.add_argument('vcffile')
args = parser.parse_args()
args_dict = vars(args)

# Get version from json
with open(args.conf) as jsonfile:
    json_dict = json.load(jsonfile)
    args_dict['version'] = json_dict['version']

template_string = 'jsonWorkflow.py -c ${conf} -s ${medgapdir}/koalatea-${version}/koalatea.sjm bam=${medgapdir}/${bamfile} vcf=${medgapdir}/${vcffile} --outdir ${medgapdir}/koalatea-${version} --run'
cmd_template = string.Template(template_string)
cmd_string = cmd_template.substitute(args_dict)
subprocess.call(cmd_string, shell=True)
