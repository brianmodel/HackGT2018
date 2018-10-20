#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 01:41:25 2018

@author: RahulBhethanabotla
"""

#!/usr/bin/env python
# encoding: utf-8

import pytextrank
import sys
import networkx as nx
import pylab as plt
import random

## Stage 2:
##  * collect and normalize the key phrases from a parsed document
##
## INPUTS: <stage1>
## OUTPUT: JSON format `RankedLexeme(text, rank, ids, pos)`

def createSummary(s):
    filename = "summ.json"
    with open(filename, 'w') as k:
        seed = random.randint(0, 100000000)
        print(s)
        k.write("{\"id\":"+ "\""+ str(seed) + "\""+ ", \"text\":" + "\"" + s + "\""+ "}")
    k.close()

    path_stage0 = filename
    path_stage1 = "o1.json"

    with open(path_stage1, 'w') as f:
        for graf in pytextrank.parse_doc(pytextrank.json_iter(path_stage0)):
            f.write("%s\n" % pytextrank.pretty_print(graf._asdict()))
            # to view output in this notebook
            print(pytextrank.pretty_print(graf))

    path_stage2 = "o2.json"

    graph, ranks = pytextrank.text_rank(path_stage1)
    pytextrank.render_ranks(graph, ranks)

    with open(path_stage2, 'w') as f:
        for rl in pytextrank.normalize_key_phrases(path_stage1, ranks):
            f.write("%s\n" % pytextrank.pretty_print(rl._asdict()))
            # to view output in this notebook
            print(pytextrank.pretty_print(rl))




    path_stage3 = "o3.json"

    kernel = pytextrank.rank_kernel(path_stage2)

    with open(path_stage3, 'w') as f:
        for s in pytextrank.top_sentences(kernel, path_stage1):
            f.write(pytextrank.pretty_print(s._asdict()))
            f.write("\n")
            # to view output in this notebook
            print(pytextrank.pretty_print(s._asdict()))

    phrases = ", ".join(set([p for p in pytextrank.limit_keyphrases(path_stage2, phrase_limit=12)]))
    sent_iter = sorted(pytextrank.limit_sentences(path_stage3, word_limit=150), key=lambda x: x[1])
    s = []

    for sent_text, idx in sent_iter:
        s.append(pytextrank.make_sentence(sent_text))

    graf_text = " ".join(s)
    print(graf_text)


def main():
    arg = sys.argv[1]
    print(arg)
    createSummary(arg)


if __name__ == "__main__":
    main()
