# Timestamps

[OpenTimestamps](https://opentimestamps.org) proofs for the assets of release `v1`.
Each proof commits to the SHA-256 of the file below.

| file | SHA-256 |
|---|---|
| `goldbach-exceptional-set-11over20-v1.pdf` | `56098137d4707e2245ef8e0aef29297dfbf57af8cbe986ed2b1a076c0633b193` |
| `goldbach-exceptional-set-11over20-v1.tar.gz` | `df35634a8d5daac54506dad1aab6ea0cc154477b9ed29b07c48c2e3d8e32fe5d` |

To verify, download the release asset into this directory and run

    pip install opentimestamps-client
    ots verify timestamps/<file>.ots
