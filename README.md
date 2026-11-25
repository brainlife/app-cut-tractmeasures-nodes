<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Trims tract profiles in a tractmeasures table to a given number of central nodes, removing an equal number of nodes from each end, using pandas.**

Utility that keeps the num_nodes central nodes of every tract profile, dropping (total_nodes - num_nodes)/2 nodes at each end, and writes a new tractmeasures CSV. Use it to remove the noisy profile ends near tract terminations before group statistics.

Run it on brainlife.io: [https://doi.org/10.25663/brainlife.app.685](https://doi.org/10.25663/brainlife.app.685)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `tractmeasures` | `neuro/tractmeasures` | yes | Tract profiles table (tractmeasures.csv) with a nodeID column. |

| Output | Datatype | Description |
|---|---|---|
| `output` | `neuro/tractmeasures` | Tractmeasures CSV containing only the retained central nodes. |

| Parameter | Type | Default | Description |
|---|---|---|---|
| `num_nodes` | number | `180` | Number of nodes you'd like to keep in your profiles. Will remove the first and last (total_nodes - num_nodes) / 2 |

Runtime: container `brainlife/freesurfer-stats:1.2`; 1 CPUs; 0.5 h walltime.

<!-- brainlife-app:end -->

# app-cut-tractmeasures-nodes