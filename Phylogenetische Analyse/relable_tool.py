#!/usr/bin/env python
import glob, re, os

for file_name in glob.glob('*.treefile') + glob.glob('*.fasta') + glob.glob('*.fas'):
    base, ext = os.path.splitext(file_name)

    with open(file_name, 'r') as filtomod, open('rewos.txt', 'r') as rewos:
        text = filtomod.read()
        reli = rewos.read().splitlines()

        for word in reli:
            wotore, rewo = word.split(":")
            text = re.sub(r"\b" + wotore + r"\b", rewo, text)

        nfn = 'relabled_' + base + ext

        with open(nfn, 'w') as mofi:
           mofi.write(text)
