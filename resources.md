---
title: Resources
layout: page
---

The citations below are for the INN Search Engine and the currently published INN papers. These may also be used as citations in your own papers using INN, depending on your usage type. PDFs of these papers are attached at the bottom of the page.

## INN Search Engine
* Larsen, Kai R., 2013, Inter-Nomological Network, http://inn.colorado.edu, access date


## Inter-Nomological Networks
* Kai R. Larsen and Bong C.H. (forthcoming 2016): A Tool for addressing Construct Identity in Literature Reviews and Meta-Analyses. MIS Quarterly (ISSN 2162-9730).
* Kai R. Larsen, Jintae Lee, Jingjing Li, and Chih How Bong (2010), A Transdisciplinary Approach to Construct Search and Integration, 16th Americas Conference on Information Systems, Lima, Peru, August 12-15.
* Larsen, K. R. and D. S. Hovorka (2012). Developing Interfield Nomological Nets. Hawaii International Conference on System Sciences. Maui, Hawaii, IEEE.
* Jingjing Li and Kai R. Larsen, “Establishing Nomological Networks for Behavioral Science: a Natural Language Processing Based Approach,” International Conference on Information Systems (ICIS), Shanghai, China, December 4th-7th, 2011.


## The INN Similarity Function
* Kai R. Larsen and Bong C.H. (forthcoming 2016): A Tool for addressing Construct Identity in Literature Reviews and Meta-Analyses. MIS Quarterly (ISSN 2162-9730).
* Larsen, Kai R. and David Monarchi (2003), A Mathematical Approach to Categorization and Labeling of Qualitative Data: The Latent Categorization Method, Sociological Methodology, Vol. 34, No. 1, pp. 349-392.


## Natural Language Processing
* Bong, C. H., K. R. Larsen and J. Martin (2012). A Large Scale Knowledge Integration Which Leads to Human Decision Making. IEEE Symposium on Computer and Informatics. Penang, Malaysia, IEEE.


## Qualitative Review
* Cook, Paul F., Kai R. Larsen, Teresa Sakraida, and Leli Pedro, 2012, A Novel Transdisciplinary Approach to Concept Analysis: The Inter-Nomological Network, Nursing Research, Vol. 61, No. 5, pp. 369-378.
* Hovorka, Dirk S., Kai R. Larsen, James Birt, and Gavin Finnie, "A Meta-theoretic Approach to Theory Integration in Information Systems," 46th Hawaii International Conference on System Sciences, Grand Wailea, Maui, Hawaii, January 7 - 10, 2013.


## Construct Validity
* Kai R. Larsen, Dorit Nevo, and Eliot Rich (2008), Exploring the Semantic Validity of Questionnaire Scales, Proceedings of the 41st Hawaii International Conference on System Sciences, Waikoloa, Hawaii, January 7-10, pp. 1-10.


## Attachments

{% assign papers = site.static_files | where: "paper", true %}
{% for paper in papers %}
* [paper.basename]( {{ paper.path | relative_url }} )
{% endfor %}
