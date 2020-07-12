#!/bin/bash

for f in `cat $1`; do
	echo "\includepdf{$2"$f".pdf}"
done
