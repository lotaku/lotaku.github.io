#!/usr/bin/env bash

echo "publish to lotaku.github.io"
rm -f -rf /Users/l/learnspace/lotaku.github.io/*
pelican -o /Users/l/learnspace/lotaku.github.io
cd /Users/l/learnspace/lotaku.github.io
git add .
git commit -m "update"
git push
echo "Done"
