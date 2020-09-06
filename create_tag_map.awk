BEGIN {
  FS = "\t";
  OFS = "\t";
  print "# coding: utf8"
  print "from __future__ import unicode_literals"
  print "from spacy.symbols import POS, " poses "\n"
  print "TAG_MAP = {"
}
{
  if (substr($1,1,1) == "#" || substr($1,1,1)== "" ) {
    # skip lines
  } else {
    #split UD tags
    split($6, splits,"|")
    joined = "";
    # UD tags are comma separated
    for (i=1; i <= length(splits); i++) {
      split(splits[i], minisplits, "=")
      # skip empty (_) as in CCONJ or SCONJ
      if (minisplits[1] != "_"){
        joined = joined ", " "\""minisplits[1]"\":" "\""minisplits[2]"\"";
        } else {
          joined = joined
        }

      }

      # ignore UD tags (other than POS) for the time being
      # because spacy v2 can't deal with arbitrary values
      # and some of our values are not "acceptable"
      # https://github.com/explosion/spaCy/issues/6019

      # if (NR != lines) {
      #   print "    \"" $5 "\":{POS:" $4 joined"},"
      # } else {
      #   print "    \"" $5 "\":{POS:" $4 joined"}"
      # }
      #
      if (NR != lines) {
        print "    \"" $5 "\":{POS:" $4"},"
      } else {
        print "    \"" $5 "\":{POS:" $4"}"
      }


      }
    }
END {
  print "}"
}

    # from ..symbols import POS, NOUN, VERB, DET
    #
    # TAG_MAP = {
    #     "NNS":  {POS: NOUN, "Number": "plur"},
    #     "VBG":  {POS: VERB, "VerbForm": "part", "Tense": "pres", "Aspect": "prog"},
    #     "DT":   {POS: DET}
    # }
