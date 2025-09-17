# Data-Science-Programming

This is my repo for the course Data Science Programming

## Getting started with R

### Prerequisites
- Install R (4.x recommended) from `https://cran.r-project.org`
- Optional: Install RStudio Desktop from `https://posit.co/download/rstudio-desktop/`

### Project layout
- `hello_world.R`: quick sanity check script
- `install_packages.R`: installs required packages
- `analysis.R`: reads `data/sample.csv`, prints summary, saves a plot to `outputs/value_by_group.png`
- `data/sample.csv`: small example dataset

### One-time setup
Run this to install required R packages:

```bash
Rscript /home/dang.cpm/__MY_SPACE__/VinUni/Data-Science-Programming/install_packages.R
```

### Run scripts (terminal)
- Hello world:

```bash
Rscript /home/dang.cpm/__MY_SPACE__/VinUni/Data-Science-Programming/hello_world.R
```

- Analysis (generates `outputs/value_by_group.png`):

```bash
Rscript /home/dang.cpm/__MY_SPACE__/VinUni/Data-Science-Programming/analysis.R
```

If you prefer, `cd` into the project first and then run with relative paths:

```bash
cd /home/dang.cpm/__MY_SPACE__/VinUni/Data-Science-Programming
Rscript install_packages.R
Rscript hello_world.R
Rscript analysis.R
```

### Run in R or RStudio
From R console (with the working directory set to the project root):

```r
source("install_packages.R")
source("hello_world.R")
source("analysis.R")
```

Notes:
- The analysis script writes outputs to the `outputs/` directory and assumes `data/sample.csv` exists.
- If you run from another working directory, use absolute paths or set `setwd("/home/dang.cpm/__MY_SPACE__/VinUni/Data-Science-Programming")` first.