 
import os


class Cmd(object):
    def contribute_cmd(self):
        cmd = "sh update_modules.sh"
        return cmd
    
    def run_cmd(self,cmd):
        print(cmd)
        os.system(cmd)
        
if __name__ == '__main__':
    code = Cmd()
    cmd = code.contribute_cmd()
    code.run_cmd(cmd)