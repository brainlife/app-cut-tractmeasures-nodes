<h1 align="center">Remove nodes from tract profiles</h1>

<p align="center">
  A tractmeasures table trimmed to the central nodes of every tract profile, with an equal number of nodes removed from each end.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.685"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.685-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Trims tract profiles in a tractmeasures table to a given number of central nodes, removing an equal number of nodes from each end, using pandas.**

Utility that keeps the num_nodes central nodes of every tract profile, dropping (total_nodes - num_nodes)/2 nodes at each end, and writes a new tractmeasures CSV. Use it to remove the noisy profile ends near tract terminations before group statistics.

| | |
|---|---|
| **Inputs** | `neuro/tractmeasures` |
| **Outputs** | `neuro/tractmeasures` |
| **Container** | `brainlife/freesurfer-stats:1.2` |
| **Resources** | 1 CPUs · 0.5 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.685](https://doi.org/10.25663/brainlife.app.685) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `tractmeasures` | `neuro/tractmeasures` | yes | Tract profiles table (tractmeasures.csv) with a nodeID column. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `neuro/tractmeasures` | Tractmeasures CSV containing only the retained central nodes. |

<details>
<summary><b>Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `num_nodes` | number | `180` | Number of nodes you'd like to keep in your profiles. Will remove the first and last (total_nodes - num_nodes) / 2 |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.685](https://doi.org/10.25663/brainlife.app.685), choose a `neuro/tractmeasures` dataset, set `num_nodes` and press **Execute**. The App writes a new `neuro/tractmeasures` dataset (tagged `cut_nodes`) to your project.

Profile values near the tract terminations are often noisy. This App keeps the `num_nodes` central nodes of every profile (default 180) and drops `(total_nodes - num_nodes) / 2` nodes at each end, so that group statistics are computed on the stable core of each tract.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/). The App runs in the `brainlife/freesurfer-stats:1.2` container (Python 3 with pandas and NumPy).

1. Clone this repository and check out the released version (`git checkout v1.0`).
2. Create `config.json` with the path to your tractmeasures table and the number of nodes to keep:

   ```json
   {
       "tractmeasures": "/input/tractmeasures/tractmeasures.csv",
       "num_nodes": 180
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

## Outputs

```text
output/
└── tractmeasures.csv   the input table restricted to the retained central nodes
```

The node IDs are kept as in the input table; blank cells are written as empty (NaN) values.

## Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Remove nodes from tract profiles. brainlife.io App. [doi:10.25663/brainlife.app.685](https://doi.org/10.25663/brainlife.app.685)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Brad Caron
- Franco Pestilli (project director)

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## License

MIT.
