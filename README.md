bmmt_baseline
=============

a baseline system for bmmt

#Instructions
Suppose moses is already properly installed on your machine, alll of the systems can be run using:
```bash
nice nohup experiment.perl -config config -multicore  --no-graph --exec &> log &
```

1. baseline: a basline system without tuning.
2. baseline-tune: baseline systems with tuning methods such as batch-mira or pro.
3. prob2: solving the terminology issue by simply concatenating terminology to the parallel corpus.
4. prob2-xmlmarkup: solving the terminology issue by using xml-input feature of moses

#Other files
1. src/split_term.py split the provided terminology file into two separate files
2. src/markup.py:
```bash
>>> python markup.py --help
usage: markup.py [-h] [--term TERM] path

wrap up the terminologies occurred in input file with xml markup

positional arguments:
  path         path to the input file

  optional arguments:
    -h, --help   show this help message and exit
      --term TERM  path to the terminology file

```
3. data: parallel corpus
4. results: results of different systems, they are copied from evaluation directory
5. report: report.pdf is a short report of all the experiments including the evaluation results.
