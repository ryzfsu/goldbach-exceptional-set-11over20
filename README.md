# The Goldbach exceptional set: an exponent 11/20

Ruiyi Zhang

DOI: [10.5281/zenodo.23396431](https://doi.org/10.5281/zenodo.23396431)

Let `E(X)` count the positive even integers at most `X` that are not sums of two primes. The
manuscript proves `E(X) << X^(11/20 + eps)` for every `eps > 0`.

Theorem 2 proves the bound under the hypothesis that every Dirichlet `L`-function, including
`zeta(s)`, has no zeros in `Re s > 7/8`. Theorem 1 combines it with the zero-free half-plane
`Re s > 7/8` of OpenAI, *The Quasi-Riemann Hypothesis* (Theorem 1.1), cited with a pinned commit
and SHA-256 in the bibliography. That input is external and is not reproved here.

A four-level Harman decomposition gives a signed prime minorant. Exact rational bounds for four
discarded families give a positive lower bound for its logarithmically weighted mass. The
distribution estimate is a Bombieri-Vinogradov bound at level `X^(9/20 - eta)` with both maxima
and a divisor weight; the minor arcs use an exponential-sum bound for the same weight, and the
major arcs use classical zero-density estimates.

## Files

- `main.tex`, `main.pdf`: the manuscript (35 pages).
- `anc/cert1120.py`: exact rational recomputation of the mass certificate of Appendix A.
- `anc/cert1120.out`: its output; `anc/environment.txt`: the environment used.

Run from `anc/` with Python 3 (standard library only):

```sh
python3 cert1120.py
```

The output should equal `cert1120.out`. The script checks only the finite sums; the analytic
reduction to them is proved in the manuscript.

## Citation

Ruiyi Zhang, *The Goldbach exceptional set: an exponent 11/20*, preprint, Zenodo, 2026. https://doi.org/10.5281/zenodo.23396431

```bibtex
@misc{zhang2026goldbach1120,
  author    = {Zhang, Ruiyi},
  title     = {The Goldbach exceptional set: an exponent 11/20},
  year      = {2026},
  publisher = {Zenodo},
  note      = {Preprint},
  doi       = {10.5281/zenodo.23396431},
  url       = {https://doi.org/10.5281/zenodo.23396431}
}
```
