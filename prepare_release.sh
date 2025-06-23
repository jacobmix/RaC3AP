#!/bin/bash

SCRIPT_DIR=$(cd `dirname $0` && pwd)
cd $SCRIPT_DIR
./build_apworld.sh

OUTPUT=rac3jp_ap
rm -rf $OUTPUT $OUTPUT.zip
mkdir -p $OUTPUT
cp -f ./rac3.apworld ${OUTPUT}
cp -r ./Client/bin/Release/net8.0/ ${OUTPUT}/rac3_jp_client
zip -r $OUTPUT{.zip,}

