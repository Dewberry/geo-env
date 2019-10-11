import subprocess

if __name__ == '__main__':
	result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
	stringout = result.stdout.decode('utf-8')
	modules = [x.split('==')[0] for x in stringout.split('\r\n')]

	with open('import_errors.txt' , 'w') as errors:
		for module in modules:
		    try:
		        exec('import {}'.format(module.lower()))
		    except ModuleNotFoundError as e:
		        print(e)
		        errors.write(str(e) + '\n')
		    except SyntaxError as e:
		        pass