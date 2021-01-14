if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("breastCancerNKI")

library(breastCancerNKI)
library(Biobase)
library(RSQLite)

data("nki")

erStatus <- pData(nki) %>%
  select(sample = samplename, er)

probes <- fData(nki) %>%
  select(probe, gene = HUGO.gene.symbol)

expressionData <- exprs(nki) %>%
  as.data.frame %>%
  rownames_to_column("probe") %>%
  gather(sample, expression, -probe) %>%
  filter(!is.na(expression))

db <- src_sqlite("breastCancerNKI.sqlite", create = TRUE)

# create tables for each of the erStatus, probes and expressionData data frames
# with indexes for efficient searches/filtering
copy_to(db, erStatus, indexes = list("sample", "er"), temporary = FALSE, overwrite = TRUE)
copy_to(db, probes, indexes = list("probe", "gene"), temporary = FALSE, overwrite = TRUE)
copy_to(db, expressionData, indexes = list("probe", "sample"), temporary = FALSE, overwrite = TRUE)