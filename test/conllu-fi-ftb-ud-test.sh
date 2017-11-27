#!/bin/bash
if test -z $srcdir ; then
    echo Use make check or define srcdir
    exit 1
fi
fsadir="../src/generated/"
conllus="fi_ftb-ud.conllu"
cs="get-covered.bash"
if test ! -d "$fsadir" ; then
    echo Missing $fsadir
    exit 77
fi
if ! test -x /usr/bin/python3 ; then
    echo Missing python
    exit 77
fi
if test ! -r $conllus ; then
    echo missing $conllus, use $cs and re-try
    exit 77
fi
if ! /usr/bin/python3 ../src/python/omorfi-conllu.py -f $fsadir -i $conllus -o omorfi_ftb-ud.conllu -O --hacks=ftb ; then
    echo analysis failed
    exit 2
fi
if ! /usr/bin/python3 $srcdir/conllu-compare.py -H omorfi_ftb-ud.conllu -r fi_ftb-ud.conllu -l omorfi_ftb-ud.log -t 75 ; then
    echo We missed the target of 75 % conllu matches
    exit 1
fi
exit 0
