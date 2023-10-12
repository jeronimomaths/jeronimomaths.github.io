---
layoput: page
title: Miscellaneous
---

This is the Sage code used to compute the Betti numbers of the Lie algebra cohomology with trivial coefficients of the non-Carnot graded central products of low-dimension in [our paper](https://jeronimomaths.github.io/publications/)  with [G. Pallier](https://pallier.org/gabriel/) and C. [Llosa Isenrich](https://www.math.kit.edu/user/llosa/index.html).

Here is the table with the results

\begin{table}[t]
    \centering
    \begin{tabular}{c|c|c|l|l}
         $G$ (non-Carnot) & $\delta_G$ & $\delta_{\text{gr}(G)}$ & Betti numbers of $G$ & Betti numbers of $\operatorname{gr}(G)$  \\
         \hline
%         \vspace{2pt}
         $G = L_{5,5} \times_Z L_{3,2}$ & $n^3$ & $n^3$ & 1,5,10,11,11,10,5,1 &  1,5,{\bf 11},15,15,11,5,1 \\
 %        \vspace{2pt}
         $G = L_{5,5} \times_Z L_{4,3}$ & $n^3$ & $n^3$ & 1,5,11,14,14,14,11,5,1 &  1,5,11,{\bf 15},16,15,11,5,1 \\
  %       \vspace{2pt}
         $G = L_{5,5} \times_Z L_{5,5} $ & $n^3$ & $n^3$ & 1,6,16,25,26,26,25,16,6,1 & same as for $G$ \\
   %      \vspace{2pt}
         $G = L_{5,5} \times_Z L_{5,4} $ & $n^3$ & $n^4$ & 
         1,7,21,34,33,33,34,21,7,1 & 1,7,21,34,{\bf 37},{37},34,21,7,1 \\
    %     \vspace{2pt}
         $G = L_{5,7} \times_Z L_{3,2}$ & $n^4$ & $n^5$ & 1,4,6,9,9,6,4,1 & 1,4,{\bf 8},11,11,8,4,1 \\
     %    \vspace{2pt}
         $G = L_{5,6} \times_Z L_{3,2}$ & $n^4$ & $n^5$ & 1,4,6,8,8,6,4,1 & 1,4,{\bf 8},11,11,8,4,1 \\
      %   \vspace{2pt}
         $G = L_{5,7} \times_Z L_{4,3}$ & $n^4$ & $n^5$ & 1,4,7,9,10,9,7,4,1 & 1,4,{\bf 9},14,16,14,9,4,1 \\
       %  \vspace{2pt}
         $G = L_{5,6} \times_Z L_{4,3}$ & $n^4$ & $n^5$ & 1,4,7,10,12,10,7,4,1 & 1,4,{\bf 9},14,16,14,9,4,1 \\
        % \vspace{2pt}
         $G = L_{5,6} \times_Z L_{5,5}$ & $n^4$ & $n^5$ & 1,5,11,16,21,21,16,11,5,1 &  1,5,11,{\bf 17},22,22,17,11,5,1 \\
         %\vspace{2pt}
         $G = L_{5,7} \times_Z L_{5,5}$  & $n^4$ & $n^5$ & 1,5,11,16,19,19,16,11,5,1 & 1,5,11,{\bf 17},22,22,17,11,5,1\\
\end{tabular}
