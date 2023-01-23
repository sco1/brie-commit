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
