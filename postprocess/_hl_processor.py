"""
Author: Jia-Huei (Dylan) Ju (dylanjootw@gmail.com)
Date: Nov. 23, 2023

The following adjustments are based on:
- Original CNC pipeline 
- Huggingface's `QA Pipeline`

References:
https://github.com/cnclabs/codes.fin.highlight/blob/main/highlighting/models.py
https://github.com/huggingface/transformers/blob/v4.35.2/src/transformers/pipelines/question_answering.py#L225
"""
class ImportanceProcessor:

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def __call__(self, logits):
