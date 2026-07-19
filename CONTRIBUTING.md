# Contributing

All changes require a focused branch and pull request to `main`.

## Bounded bootstrap rules

1. Keep changes within the authorized repository contract.
2. Do not add product implementation, live credentials, protected data, or environments.
3. Use only the Python standard library in the bootstrap harness.
4. Run the complete verification sequence twice from a clean state.
5. Record architecture choices through ADR or RFC review before implementation.
6. Treat Gate 1 as `Recovery required` until separately approved.
