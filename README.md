# Introduction to R for Data Science and Statistical Analysis in Ecology

Open teaching materials for the R and statistics course of the **Erasmus Mundus Joint Master in Global Change Ecology and Biodiversity Management ([GLOBE](https://globe-master.eu/))**, taught at **Universidad Rey Juan Carlos** (URJC, Madrid, Spain).

**Instructor:** Julia Chacón Labella (Universidad Rey Juan Carlos)

The course introduces R as a tool for ecological data analysis, from the first steps in the R environment to linear and generalized linear models, using ecological examples throughout.

## Course structure

| Section | Topic | Contents |
|:--|:--|:--|
| [Section I](section-I_R-environment/) | Introduction to the R environment as a tool for data analyses | R and RStudio, objects, operators, scripts and packages; reading and writing files; basic statistics, `if`/`else`, `for` loops and functions |
| [Section II](section-II_graphics/) | Graphical tools for data exploration | Base R graphics and `ggplot2`; types of graphs and aesthetics; exploratory data analysis |
| [Section III](section-III_linear-models/) | Linear models | Simple and multiple regression, model assumptions, multicollinearity, ANOVA, post-hoc tests and ANCOVA |
| [Section IV](section-IV_glm/) | Generalized linear models (GLM) | Error distributions and link functions; Poisson, negative binomial and binomial GLMs; overdispersion |

## Section I materials

| Session | Tutorial |
|:--|:--|
| General Introduction I: Installing R and first overview | [`S1_session1_GLOBE_RStudio_EN.Rmd`](section-I_R-environment/S1_session1_GLOBE_RStudio_EN.Rmd) |
| General Introduction II: Object Types in R | [`S1_session2_GLOBE_ObjectTypes_EN.Rmd`](section-I_R-environment/S1_session2_GLOBE_ObjectTypes_EN.Rmd) |

## How to use these materials

1. Install [R](https://cran.r-project.org/) and [RStudio Desktop](https://posit.co/downloads).
2. Download this repository (green **Code** button > **Download ZIP**) or clone it with Git.
3. Open `globe-r-stats.Rproj` in RStudio.
4. Open any tutorial (`.Rmd`) and click **Knit** to render it as HTML or PDF. Rendering to PDF requires a LaTeX distribution: install it once from the R console with `install.packages("tinytex"); tinytex::install_tinytex()`.

## Repository structure

```
globe-r-stats/
├── README.md
├── LICENSE.md
├── globe-r-stats.Rproj
├── assets/                    # shared resources: logos and LaTeX preamble for PDFs
├── data/                      # datasets used in the course
├── section-I_R-environment/   # Section I tutorials (.Rmd) and their figures (images/)
├── section-II_graphics/
├── section-III_linear-models/
└── section-IV_glm/
```

## Citation

If you use or adapt these materials, please cite them as:

> Chacón Labella, J. (2026). *Introduction to R for Data Science and Statistical Data Analysis*. Teaching materials, Erasmus Mundus Joint Master GLOBE, Universidad Rey Juan Carlos. https://github.com/juliachacon/globe-r-stats
## License

Text, figures and code are released under a [CC BY 4.0](LICENSE.md) licence. The GLOBE and URJC logos belong to their respective institutions and are not covered by this licence.
