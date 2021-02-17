---
title: MWE for SJM
fontsize: 9pt
classoption: t
---

# Section 1

## Overview

This is plain text

+ Bullet item
  - sub-item
  - sub-item
+ Next item

## LaTex table environment

\begin{tabular}{lrrrr}
\toprule
Person &  Woman &  Man &  Camera &   TV \\
\midrule
0.45 &   0.02 & 0.39 &    0.70 & 0.12 \\
0.33 &   0.09 & 0.25 &    0.68 & 0.48 \\
0.83 &   0.53 & 0.99 &    0.79 & 0.54 \\
\bottomrule
\end{tabular}

## md table environment

:::::::::::::: {.columns}
::: {.column width="33%"}
\resizebox{\textwidth}{!}{
\begin{tabular}{lrrrr}
\toprule
Person &  Woman &  Man &  Camera &   TV \\
\midrule
0.45 &   0.02 & 0.39 &    0.70 & 0.12 \\
0.33 &   0.09 & 0.25 &    0.68 & 0.48 \\
0.83 &   0.53 & 0.99 &    0.79 & 0.54 \\
\bottomrule
\end{tabular}
}
:::
::: {.column width="33%" align=bottom}
\resizebox{\textwidth}{!}{
\begin{tabular}{lrrrr}
\toprule
Person &  Woman &  Man &  Camera &   TV \\
\midrule
0.45 &   0.02 & 0.39 &    0.70 & 0.12 \\
0.33 &   0.09 & 0.25 &    0.68 & 0.48 \\
0.83 &   0.53 & 0.99 &    0.79 & 0.54 \\
\bottomrule
\end{tabular}
}
:::
::: {.column width="33%"}
\resizebox{\textwidth}{!}{
\begin{tabular}{lrrrr}
\toprule
Person &  Woman &  Man &  Camera &   TV \\
\midrule
0.45 &   0.02 & 0.39 &    0.70 & 0.12 \\
0.33 &   0.09 & 0.25 &    0.68 & 0.48 \\
0.83 &   0.53 & 0.99 &    0.79 & 0.54 \\
\bottomrule
\end{tabular}
}
:::
::::::::::::::

## Premium by Region
\resizebox{.5\textwidth}{!}{
\begin{tabular}{lrrrr}
\toprule
{} &  Policies &    Amount Subject &       Premium &  Avg Rate \\
Region          &           &                   &               &           \\
\midrule
Fl - Other      &    450.00 &  5,928,103,242.00 & 25,795,666.00 &      0.44 \\
Fl - Tri-County &    562.00 &  8,012,769,836.40 & 49,436,192.00 &      0.62 \\
Gulf            &    259.00 &  3,808,792,672.50 & 16,741,093.00 &      0.44 \\
Mid-Atlantic    &     71.00 &  1,040,159,076.00 &  4,762,750.00 &      0.46 \\
Northeast       &     31.00 &    430,323,020.00 &  1,416,509.00 &      0.33 \\
Total           &  1,373.00 & 19,220,147,846.90 & 98,152,210.00 &      0.51 \\
\bottomrule
\end{tabular}
}
