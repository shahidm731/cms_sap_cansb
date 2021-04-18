import os
from subprocess import Popen, PIPE
import logging
logfile = "/tmp/ansibledebug.log"
logging.basicConfig(filename =logfile, level = logging.INFO)
def getstat(val):
    result = []
    logging.info("Testng log file")
    command = "/usr/sap/hostctrl/exe/lssap -s | awk -F'|' '{print $1}' | egrep -v '===' | egrep -v 'lssap|SID|DAA' | sort -u"
    pipe = subprocess.Popen(command, shell=True, stdout=PIPE)
    #logging.info("" + str(pipe.stdout) + "")
    for line in pipe.stdout:
        print(line)
        result.append(line.strip())
        logging.info("The line is " + line + "")
    return result
def main():
    module = AnsibleModule(
        argument_spec=dict(
        value=dict(required=True)
        ),
    )
    val = module.params['value']
    getout = getstat(val)
    module.exit_json(msg=getout)

from ansible.module_utils.basic import *
main()