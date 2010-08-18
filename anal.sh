
#!/bin/bash

echo Anal!

tr -s ' ' '\n' < test.txt > test.vert
tr -s ',' '\n' < test.vert > test2.vert
tr -s '.' '\n' < test2.vert > test.vert
tr -s '"' '\n' < test.vert > test2.vert
tr -s '!' '\n' < test2.vert > test.vert
tr -s '?' '\n' < test.vert > test2.vert
tr -s '“' '\n' < test2.vert > test.vert
tr -s '-' '\n' < test.vert > test2.vert
tr -s '„' '\n' < test2.vert > test.vert
tr -s '–' '\n' < test.vert > test2.vert
tr -s ':' '\n' < test2.vert > test.vert

rm test2.vert

sort test.vert | uniq -c -i > dict.txt
sort test.vert | uniq -c -i | sort -rn > freq.txt
