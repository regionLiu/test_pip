 
import os


class Cmd(object):
    def contribute_cmd(self):
        cmd = "pip install xlrd"
        return cmd
    
    def run_cmd(self,cmd):
        print(cmd)
        a = os.system(cmd)
        print(a)
        
if __name__ == '__main__':
    code = Cmd()
    cmd = code.contribute_cmd()
    code.run_cmd(cmd)