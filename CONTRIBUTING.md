# Contributing

Bug reports, evals on new hardware or data, docs fixes and new features are welcome.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
ruff check . && pytest
python eval/run_eval.py
```

- Keep changes small and focused. Add a test for new behaviour.
- Do not commit model weights, API keys or private data.
- A change that moves a published number must update the Results table and say why.

By contributing you agree your work is released under the MIT license.
