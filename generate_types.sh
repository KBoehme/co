#!/usr/bin/env bash
set -x
set -e

quicktype ./objects/food.ts -o ./languages/py/co/food.py
quicktype ./objects/food.ts -o ./languages/go/food.go
quicktype ./objects/food.ts -o ./languages/cs/food.cs
quicktype ./objects/food.ts -o ./languages/java/food.java

quicktype ./objects/bioinformatics.ts -o ./languages/py/co/bioinformatics.py
quicktype ./objects/bioinformatics.ts -o ./languages/go/bioinformatics.go
quicktype ./objects/bioinformatics.ts -o ./languages/cs/bioinformatics.cs
quicktype ./objects/bioinformatics.ts -o ./languages/java/bioinformatics.java
