[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/brie-commit/1.1.0?logo=python&logoColor=FFD43B)](https://pypi.org/project/brie-commit/)
[![PyPI](https://img.shields.io/pypi/v/brie-commit?logo=Python&logoColor=FFD43B)](https://pypi.org/project/brie-commit/)
[![PyPI - License](https://img.shields.io/pypi/l/brie-commit?color=magenta)](https://github.com/sco1/brie-commit/blob/main/LICENSE)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sco1/brie-commit/main.svg)](https://results.pre-commit.ci/latest/github/sco1/brie-commit/main)
# brie-commit
A collection of cheesy [pre-commit](https://pre-commit.com/) hooks

## Using brie-commit with pre-commit
Add this to your `.pre-commit-config.yaml`

```yaml
repos:
-   repo: https://github.com/sco1/brie-commit
    rev: v1.1.0
    hooks:
    -   id: brie-commit
```

## Hooks
### `brie-commit`
This hook doesn't do anything except add cheese to your pre-commit invocation.

```bash
$ pre-commit run
🧀🧀🧀...................................................................Passed
```

### `up-to-no-gouda`
This hook replaces all instances of `good` with `gouda` in your text files.

```bash
$ echo "This is looking pretty good." > ./gouda_vibes.txt
$ pre-commit run -a
🧀🧀🧀...................................................................Passed
good2gouda...............................................................Failed
- hook id: up-to-no-gouda
- files were modified by this hook
$ cat ./gouda_vibes.txt
This is looking pretty gouda.
```
