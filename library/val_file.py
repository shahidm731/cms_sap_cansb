import os

def getstat(fname, ftype, bucket):
    result = []
    if ftype == 's3cmd':
        print("Type s3cmd")
        command = ""
        getmem = subprocess.Popen('bootinfo -r',
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=True)
        std_out, stderr = getmem.communicate()
    elif ftype == 'local':
        if os.path.isfile("/var/tmp/tsm_client/" + fname + ""):
            print("true")
            result.append('File Found')
        else:
            result.append('File NOT Found')
    return result
def main():
    module = AnsibleModule(
        argument_spec=dict(
        filename=dict(required=True),
        type=dict(required=True),
        bucket=dict(required=True)
        ),
    )
    filen = module.params['filename']
    ftype = module.params['type']
    bucket = module.params['bucket']
    getout = getstat(filen, ftype, bucket)
    module.exit_json(msg=getout)

from ansible.module_utils.basic import *
main()