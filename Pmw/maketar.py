import string
import os
import shutil
import glob
import tarfile
import subprocess

#Version to be released
VERSION='1.3.3'

#DIR is the directory name extension and is automatically generated
DIR=VERSION.replace('.', '_')

# Date to put in documentation for the release date of this release
VERSION_DATE="25 April 2013"

#Base directory (on local PC):
BASEDIR='../builds/PMW_' + DIR

#Output directory where you want to find the .tar.gz files
#assumed to exist
OUTFILEDIR='../builds/PMW_' + DIR

# Location of Pmw source files (on local PC):
SRC_DIR='Pmw_0_0_0'

# Temporary directory
TEMP='C:\Temp\\'

#Test variables
#print(VERSION)
#print(DIR)
#print(VERSION_DATE)
#print(BASEDIR)
#print(OUTFILEDIR)
#print(SRC_DIR)

print("Using Pmw/%(SRC_DIR)s to create Pmw.%(VERSION)s" % {'SRC_DIR':SRC_DIR,\
                                                           'VERSION':VERSION})

STARTDIR = os.getcwd()
print(STARTDIR)

path = TEMP + 'Pmw'
if (os.path.isdir(path)):
    print('Old folder deleted')
    shutil.rmtree(path)

results = []
os.chdir(TEMP)
for file in glob.glob('Pmw*.tar.gz'):
    os.remove(file)

os.chdir(STARTDIR)
shutil.copytree('../Pmw', TEMP + 'Pmw')

os.chdir(TEMP + 'Pmw')
os.rename(SRC_DIR, 'Pmw_' + DIR)

for tup in os.walk('.'):
    for file in tup[1]:
        filepath = tup[0] + '\\' + file
        if (file == 'CVS') and os.path.isdir(filepath):
            shutil.rmtree(filepath)
        if (file == '__pycache__') and os.path.isdir(filepath):
            shutil.rmtree(filepath)
        if (file.endswith('.pyc')):
            shutil.rmtree(filepath)
        if (file.endswith('.py.bak')):
            shutil.rmtree(filepath)

from glob import glob
for f in glob('*~'):
    os.remove(f)
os.remove('ReleaseProcedure')
os.remove('TODO')
os.remove('maketar.sh')
os.remove('maketar.py')
os.remove('set_env.sh')

#create documentation source
os.chdir('Pmw_' + DIR)
tf = tarfile.open('Pmw_' + DIR + '.docsrc.tar.gz', 'w:gz')
tf.add('docsrc')
tf.close()
shutil.move('Pmw_' + DIR + '.docsrc.tar.gz', '../..')

#create manuals
os.chdir('docsrc')
#p = subprocess.Popen("python createmanuals.py", shell=False)
subprocess.call("python createmanuals.py")
os.chdir('..')
shutil.rmtree('docsrc')
os.chdir('..')

for tup in os.walk('.'):
    for file in tup[1]:
        filepath = tup[0] + '\\' + file
        if (file == '__pycache__') and os.path.isdir(filepath):
            shutil.rmtree(filepath)
        if (file.endswith('.pyc')):
            shutil.rmtree(filepath)
        if (file.endswith('.py.bak')):
            shutil.rmtree(filepath)


#generate package file
print('generating package file')
os.chdir('..')

if os.path.exists('src'):
    shutil.rmtree('src')
os.mkdir('src')

shutil.move('Pmw/setup.py', 'src/')
shutil.rmtree('Pmw/Alpha_99_9_example')
shutil.copytree('Pmw', 'src/Pmw')

if os.path.exists('Pmw'):
    shutil.rmtree('Pmw')
os.rename('src', 'Pmw')

tf = tarfile.open('Pmw_' + DIR + '.tar.gz', 'w:gz')
tf.add('Pmw')
tf.close()
