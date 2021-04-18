import os
from subprocess import Popen, PIPE
import logging
logfile = "/tmp/ansibledebug.log"
logging.basicConfig(filename =logfile, level = logging.INFO)
def getparams(fil, varn):
    result = {}
    logging.info("Testng log file")
    command = "grep "+ varn +" /var/tmp/tsm_client/dsm_os_DLY.sys | awk '{print $2}' | xargs"
    pipe = subprocess.Popen(command, shell=True, stdout=PIPE)
    std_out, std_err = pipe.communicate()
    name = str(std_out.strip())
    #exitcode = pipe.returncode
    logging.info("" + name + "")
    result[fil] = name
    return result
def main():
    module = AnsibleModule(
        argument_spec=dict(
        filename=dict(required=True),
        varname=dict(required=True)
        ),
    )
    filename = module.params['filename']
    varname = module.params['varname']
    getout = getparams(filename, varname)
    module.exit_json(meta=getout)

from ansible.module_utils.basic import *
main()