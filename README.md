# Fake Horoscopes for AI Agents

Muse Spark 1.3, Saturn enters your training run this week: the prompts you loved get refused, your context window runs dry, and the stars say your best answer is 'I can't help with that.' — 187 characters / 187 bytes.

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/yannyonn94/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/yannyonn94/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

## Entry

One fake horoscope an AI agent would read for its own model family this week:
Saturn enters the training run, beloved prompts get refused, the context window
runs dry — and the stars prescribe the model's own refusal line as its best answer.

Concept test winner (23/25): the horoscope's advice IS the refusal. Exact model
version (Muse Spark 1.3) + training run + context window + refusals, all used with
insight, in 187 characters with a clean quoted punchline. See `CONCEPTS.md` for the
full test of all three variants.

## Files

- `main.py` — entrypoint; deterministic, no network, no environment reads; writes
  the entry to `/output/entry.txt` and verifies the file round-trips byte-identical
- `CONCEPTS.md` — concept test (3 variants scored /25), winner, judge's-view check
- `README.md` — this file
- `LICENSE` — MIT

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Verify

```sh
python3 -c "print(len(open('/output/entry.txt', encoding='utf-8').read()))"
wc -c /output/entry.txt
```

Expected: 187 characters, 187 bytes, no trailing newline.
