#!/srv/gs1/software/python/3.4/bin/python3

import subprocess
import argparse
import string

VERSION = '2.1'

parser = argparse.ArgumentParser()
parser.add_argument('inputjson')
parser.add_argument('medgapdir')
args = parser.parse_args()
args_dict = vars(args)
args_dict['VERSION'] = VERSION

template_string = 'jsonWorkflow.py -c ${inputjson} -s ${medgapdir}/koalatea-${VERSION}/koalatea.sjm bam=${medgapdir}/genome.recal.bam vcf=${medgapdir}/genome.recal.vcf --outdir ${medgapdir}/koalatea-${VERSION} --run'
cmd_template = string.Template(template_string)
cmd_string = cmd_template.substitute(args_dict)
subprocess.call(cmd_string, shell=True)
