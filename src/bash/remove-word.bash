#!/bin/bash

LEXFILE=lexemes.tsv
ATTRIBUTES=attributes/*.tsv

if test $# -lt 2 ; then
    echo "Usage: $0 LEMMA HOMONYM"
    exit 1
fi

echo "Following lexemes are affected:"
if ! egrep "^(${1})	\['(${2})'\]" $LEXFILE ; then
    echo "None found, folding"
    exit 1
fi

for f in ${ATTRIBUTES} ; do
    cp -v ${f} ${f}~
    sed -r -e "/^(${1})	\['(${2})'\]/d" ${f} > ${f}~~
    diff -u ${f}~ ${f}~~
    cp ${f}~~ ${f}
done

echo Abovementioned removals have been made, if all is fine,
echo do commit the result immediately
