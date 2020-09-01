#!/usr/local/bin/fish

# concat all UD files

set COMBOUDFILES ".comboUDfiles"

cat UD_Serbian_Cyrl-SET/*.conllu > "$COMBOUDFILES"

# remove empty lines and comments; alphabetize by tags; get unique tags
sed 's/#.*$//;/^$/d' "$COMBOUDFILES" | sort -k5 | awk '!seen[$5]++' > .temp

# get unique poses
set poses (cat .temp | cut -f 4 | sort | uniq | sed  's/$/,/' | sed -e  '$ s/,$//' )

#calculate number of lines (easier than treating last line in awk differently)
set lines (cat .temp | wc -l)

/usr/local/bin/awk -v poses="$poses" -v lines="$lines" -f create_tag_map.awk .temp > sr/tag_map.py

rm .temp
rm "$COMBOUDFILES"
