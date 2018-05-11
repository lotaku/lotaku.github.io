#!/usr/bin/env bash

echo "update blog source ..."
cd /Users/l/learnspace/blog
pelican
git add .
git commit -m "update"
git push
echo "Done"
