#!/bin/bash

LEXFILE=lexemes.tsv
ATTRIBUTES=attributes/*.tsv

if test $# -lt 3 ; then
    echo "Usage: $0 LEMMA HOMONYM NEW_HOMONYM"
    exit 1
fi

echo "Following lexemes are affected:"
if ! egrep "^(${1})	\['(${2})'\]" $LEXFILE ; then
    echo "None found, folding"
    exit 1
fi

for f in ${ATTRIBUTES} ; do
    cp -v ${f} ${f}~
    sed -r -e "s/^(${1})	\['(${2})'\]/\1	['${3}']/" ${f} > ${f}~~
    diff -u ${f}~ ${f}~~
    cp ${f}~~ ${f}
done

echo Abovementioned changes have been made, if all is fine,
echo do commit the result immediately
