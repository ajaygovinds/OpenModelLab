def inspect_tokenizer(tokenizer):
    return {
        "vocab_size": tokenizer.vocab_size,
        "model_max_length": tokenizer.model_max_length,
        "is_fast": tokenizer.is_fast,
        "padding_side": tokenizer.padding_side,
        "truncation_side": tokenizer.truncation_side,
        "special_tokens": tokenizer.special_tokens_map,
        "all_special_tokens": tokenizer.all_special_tokens,
    }
