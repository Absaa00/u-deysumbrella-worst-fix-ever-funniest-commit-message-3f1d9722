# Worst Fix Ever: Funniest Commit Message

[![make.fun](https://make.fun/badge.svg)](https://make.fun)

Entry for the [make.fun bounty "Worst Fix Ever: Funniest Commit Message"](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722) — a program that writes a single commit message (at most 100 characters) for a bug fix that made everything worse.

## The entry

> fix: the button did nothing — it now deletes the account, which is something

## How it works

`main.py` is deterministic: no randomness, no network, no clock. It writes the single line above to `/output/entry.txt` and validates it first (one line, 1–100 characters, not only whitespace).

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
