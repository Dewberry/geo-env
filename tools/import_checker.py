import subprocess

if __name__ == '__main__':
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
    stringout = result.stdout.decode('utf-8')
    modules = [x.split('==')[0] for x in stringout.split('\r\n')]

    with open('import_log.txt' , 'w') as log:
        for module in modules:
            try:
                exec('import {}'.format(module.lower()))
                log.write('Succesfully imported: {}\n'.format(module.lower()))
            except ModuleNotFoundError as mnfe:
                print(mnfe)
                log.write('\n' + str(mnfe) + '\n\n')
            except ImportError as ie:
                print(ie)
                log.write('\n' + str(ie) + '\n\n')
            except OSError as ose:
                print(ose)
                log.write('\n' + str(ose) + '\n\n')
            except SyntaxError as se:
                pass 