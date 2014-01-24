# This script creates a tar file of a Pmw distribution ready to be
# released.  The source for the distribution is in the directory
# Pmw/${SRC_DIR}.  The tar file is stored in
#     /tmp/Pmw.${VERSION}.tar.gz


###----------COPIED FROM ReleaseProcedure---------------


# Version to be released
VERSION=1.3.3

#DIR is the directory name extension and is automatically generated
DIR=`echo $VERSION | tr . _`

# Date to put in documentation for the release date of this release
VERSION_DATE=`date "+%d %b %Y"`

#Base directory (on local PC):
BASEDIR=`bash basedir.sh`

#Output directory where you want to find the .tar.gz files
#assumed to exist
OUTFILEDIR=$BASEDIR

# Location of Pmw source files (on local PC):
SRC_DIR=Pmw_0_0_0

###-----------------------------------------------------


STARTDIR=$PWD
echo Using Pmw/${SRC_DIR} to create Pmw.${VERSION}.
#remove older build directories
if [ -e /tmp/Pmw ] 
then
	/bin/rm -rf /tmp/Pmw
fi

#remove older .tar.gz distro files
rm /tmp/Pmw*.tar.gz

# tar cf - ./Pmw | (cd /tmp; tar xf -)
tar cf - ../Pmw | (cd /tmp; tar xf -)
mv /tmp/Pmw/${SRC_DIR} /tmp/Pmw/TEMP
/bin/rm -rf /tmp/Pmw/Pmw_*
mv /tmp/Pmw/TEMP /tmp/Pmw/Pmw_${DIR}
cd /tmp/Pmw
for dir in `find . -name CVS -type d`
do
    /bin/rm -r $dir
done
for file in `find . -name "*.pyc" -type f`
do
    /bin/rm -r $file
done

/bin/rm ReleaseProcedure maketar.sh
echo Unexpected files:
echo ===== start =====
cat << EOF | sed "s/0_0_0/${DIR}/" > /tmp/Pmw.dirs1
.
./Alpha_99_9_example
./Alpha_99_9_example/lib
./Pmw_0_0_0
./Pmw_0_0_0/bin
./Pmw_0_0_0/contrib
./Pmw_0_0_0/demos
./Pmw_0_0_0/docsrc
./Pmw_0_0_0/docsrc/images
./Pmw_0_0_0/docsrc/text
./Pmw_0_0_0/lib
./Pmw_0_0_0/tests
EOF
find . -type d | sort > /tmp/Pmw.dirs2
diff /tmp/Pmw.dirs1 /tmp/Pmw.dirs2
/bin/rm /tmp/Pmw.dirs1 /tmp/Pmw.dirs2
cat << EOF | sed "s/0_0_0/${DIR}/" > /tmp/Pmw.dirs1
./Pmw_0_0_0/docsrc/Pmw.announce
EOF
find . -type f | egrep -v "\.(py|html|gif|bmp)$" | \
    egrep -v "(README|Pmw.def)" > /tmp/Pmw.dirs2
diff /tmp/Pmw.dirs1 /tmp/Pmw.dirs2
echo ====== end ======
/bin/rm /tmp/Pmw.dirs1 /tmp/Pmw.dirs2
cd /tmp/Pmw/Pmw_${DIR}

# Create documentation source:
echo -e "\n==============\n Creating documentation source"
tar cf Pmw.${VERSION}.docsrc.tar ./docsrc
gzip Pmw.${VERSION}.docsrc.tar
mv Pmw.${VERSION}.docsrc.tar.gz /tmp

echo -e "\n Creating manuals"
/bin/rm -rf doc
cd /tmp/Pmw/Pmw_${DIR}/docsrc
./createmanuals.py
cd /tmp/Pmw/Pmw_${DIR}

/bin/rm -rf docsrc
cd /tmp/Pmw
for file in `find . -name "*.pyc" -type f`
do
    /bin/rm -r $file
done
cd /tmp
/bin/rm -f Pmw.${VERSION}.tar.gz

#create a source dir to hold setup.py and Pmw


if [ ! -d 'src' ]; then
    mkdir src    
fi


mv Pmw/setup.py src
cp -r Pmw ./src/.

tar cf Pmw.${VERSION}.tar ./src
gzip Pmw.${VERSION}.tar

# Now that the tar file has been created, unpack and run the tests.
echo 'Testing unpacking...'
/bin/rm -rf pmw.tmp
mkdir pmw.tmp
cd /tmp/pmw.tmp
gzip -dc /tmp/Pmw.${VERSION}.tar.gz | tar xf -

echo 'Copying output files'
cd $STARTDIR
cp /tmp/Pmw.${VERSION}.tar.gz $OUTFILEDIR
cp /tmp/Pmw.${VERSION}.docsrc.tar.gz $OUTFILEDIR
