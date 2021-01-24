```
(env) ⋊> ~/D/B/spacy-serbian-pipeline on binder-fish ⨯ python3 -m spacy train config.cfg --output models/srp
ℹ Using CPU

=========================== Initializing pipeline ===========================
Set up nlp object from config
Pipeline: ['lemmatizer', 'tok2vec', 'tagger', 'parser']
Created vocabulary
Finished initializing nlp object
Initialized pipeline components: ['lemmatizer', 'tok2vec', 'tagger', 'parser']
✔ Initialized pipeline

============================= Training pipeline =============================
ℹ Pipeline: ['lemmatizer', 'tok2vec', 'tagger', 'parser']
ℹ Initial learn rate: 0.001
E    #       LOSS TOK2VEC  LOSS TAGGER  LOSS PARSER  LEMMA_ACC  TAG_ACC  DEP_UAS  DEP_LAS  SENTS_F  SCORE
---  ------  ------------  -----------  -----------  ---------  -------  -------  -------  -------  ------
⚠ Aborting and saving the final best model. Encountered exception:
KeyError("[E900] Could not run the full pipeline for evaluation. If you
specified frozen components, make sure they were already initialized and
trained. Full pipeline: ['lemmatizer', 'tok2vec', 'tagger', 'parser']")
Traceback (most recent call last):
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/spacy/training/loop.py", line 261, in evaluate
    scores = nlp.evaluate(dev_corpus(nlp))
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/spacy/language.py", line 1319, in evaluate
    for doc, eg in zip(
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/spacy/util.py", line 1433, in _pipe
    doc = proc(doc, **kwargs)
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/srp/__init__.py", line 37, in __call__
    lemma = lookup.get(t.text, None)
  File "spacy/tokens/token.pyx", line 263, in spacy.tokens.token.Token.text.__get__
  File "spacy/tokens/token.pyx", line 806, in spacy.tokens.token.Token.orth_.__get__
  File "spacy/strings.pyx", line 132, in spacy.strings.StringStore.__getitem__
KeyError: "[E018] Can't retrieve string for hash '8737485628806624168'. This usually refers to an issue with the `Vocab` or `StringStore`."

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/Cellar/python@3.8/3.8.7/Frameworks/Python.framework/Versions/3.8/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/local/Cellar/python@3.8/3.8.7/Frameworks/Python.framework/Versions/3.8/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/spacy/__main__.py", line 4, in <module>
    setup_cli()
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/spacy/cli/_util.py", line 65, in setup_cli
    command(prog_name=COMMAND)
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/click/core.py", line 829, in __call__
    return self.main(*args, **kwargs)
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/click/core.py", line 782, in main
    rv = self.invoke(ctx)
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/click/core.py", line 1259, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/click/core.py", line 1066, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/click/core.py", line 610, in invoke
    return callback(*args, **kwargs)
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/typer/main.py", line 497, in wrapper
    return callback(**use_params)  # type: ignore
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/spacy/cli/train.py", line 59, in train_cli
    train(nlp, output_path, use_gpu=use_gpu, stdout=sys.stdout, stderr=sys.stderr)
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/spacy/training/loop.py", line 113, in train
    raise e
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/spacy/training/loop.py", line 98, in train
    for batch, info, is_best_checkpoint in training_step_iterator:
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/spacy/training/loop.py", line 210, in train_while_improving
    score, other_scores = evaluate()
  File "/Users/ttasovac/Development/BCDH/spacy-serbian-pipeline/env/lib/python3.8/site-packages/spacy/training/loop.py", line 263, in evaluate
    raise KeyError(Errors.E900.format(pipeline=nlp.pipe_names)) from e
KeyError: "[E900] Could not run the full pipeline for evaluation. If you specified frozen components, make sure they were already initialized and trained. Full pipeline: ['lemmatizer', 'tok2vec', 'tagger', 'parser']"
```
