#!/bin/bash

if [ $# -ne 3 ]
then
	echo "Usage: $0 <in> <out> <name>"
	exit 1
fi

IN_DIR=${1}
OUT_DIR=${2}
OUT_NAME=${3}

for i in `ls ${IN_DIR}`
do
	MSG_NAME=`echo $i | awk -F\. '{print $1}'`
	echo $MSG_NAME
	utils/romsg2json.bash ${IN_DIR}/${i} > ${OUT_DIR}/${MSG_NAME}.json
done

python utils/generate.py ${OUT_NAME} ${IN_DIR} ${OUT_DIR} > ${OUT_DIR}/${OUT_NAME}.cs
