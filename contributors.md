---
layout: page
title: Contributors
regenerate: true
---

## Director
<p><a href="http://www.colorado.edu/business/kai-r-larsen">Kai Larsen</a>, Leeds School of Business, University of Colorado at Boulder</p>

## Faculty Affiliates & Collaborators (in order joined)

* <a href="http://openlibrary.org/a/OL236569A/Alexander-G.-Voronovich">Alexander G. Voronovich</a>, National Oceanic and Atmospheric Administration
* <a href="http://www.colorado.edu/business/jintae-lee">Jintae Lee</a>, Leeds School of Business, University of Colorado, Boulder
* <a href="http://www.albany.edu/~er945/">Eliot Rich</a>, University at Albany, State University of New York
* <a href="http://www.ucdenver.edu/academics/colleges/nursing/faculty-staff/faculty/Pages/p_cook.aspx">Paul F. Cook</a>, College of Nursing, University of Colorado, Denver
* <a href="http://nursing.fau.edu/directory/sakraida/index.php">Teresa Sakraida</a>, College of Nursing, Florida Atlantic University
* Karen Peifer, College of Nursing, University of Colorado, Denver
* <a href="http://www.colorado.edu/neuroscienceprogram/allen.html">David L. Allen</a>, Integrative Physiology, University of Colorado, Boulder
* <a href="https://lallyschool.rpi.edu/faculty/dorit-nevo">Dorit Nevo</a>, Lally School of Management &amp; Technology, Rensselaer Polytechnic Institute
* <a href="http://www.colorado.edu/ibs/HB/mollborn/">Stefanie Mollborn</a>, Sociology, University of Colorado, Boulder
* <a href="https://mcdb.colorado.edu/directory/Mike_Klymkowsky">Mike Klymkowsky</a>, Molecular, Cellular &amp; Developmental Biology, University of Colorado, Boulder
* <a href="http://www.ucdenver.edu/academics/colleges/nursing/faculty-staff/faculty/Pages/l_pedro.aspx">Leli Pedro</a>, College of Nursing, University of Colorado, Denver
* <a href="http://www.colorado.edu/education/derek-briggs">Derek C. Briggs</a>, Education, University of Colorado, Boulder
* <a href="http://www.cs.cmu.edu/~cprose/">Carolyn Rose</a>, Computer Science, Language Technologies Institute, Carnegie Mellon
* <a href="http://sydney.edu.au/business/staff/dirkho">Dirk S. Hovorka</a> Business Information Systems, University of Sydney
* <a href="http://apps.bond.edu.au/staff/profile.asp?s_id=1534">James Birt</a> Humanities and Social Sciences, Bond University
* <a href="https://www.ucl.ac.uk/health-psychology/people/Susan_Michie">Susan Michie</a> Psychology and Language Sciences, University College of London
* <a href="http://www.uofmhealth.org/profile/2165/lawrence-chin-i-md">Lawrence An</a> University of Michigan Medical School
* <a href="http://www.lebow.drexel.edu/davidgefen">David Gefen</a> College of Business, Drexel University
* <a href="http://www.rjwest.co.uk/">Robert West</a> Health Psychology, University College of London
* <a href="http://www.abdn.ac.uk/hsru/people/m.johnston/">Marie Johnston</a> Health Services, University of Aberdeen

## Ph.D Students (in order joined)

* Jingjing Li, Business
* Jeffrey R. Sweeney, Business
* Xin (Emily) Pan, Information Systems
* Sid Saleh, <a href="http://atlas.colorado.edu/">ATLAS</a>
* Ehab Ababneh (Developer), Computer Science (Ph.D)
* James Endicott (Developer), Computer Science (Ph.D)

## Ph.D Graduates

* <a href="https://www.commerce.virginia.edu/faculty/li">Jingjing Li</a>, Information Systems
* <a href="http://www.linkedin.com/pub/chih-how-bong/10/a9a/307">Chih How Bong</a>, Computer Science
* <a href="http://works.bepress.com/dirk_hovorka/">Dirk Hovorka</a>, Information Systems

## Friends of the Project (major volunteer contributors)

* Zoya A. Voronovich
* Melanie Roberts
* Josh Price
* Nithesh Dasari (MS)
* Trevor Chambers
* Zebula Sampedro
* Nick Zager

## Current Research Assistants

{% assign ras = site.research_assistants_current | sort: "name" %}
{% for ra in ras %}
* [{{ra.name}}]({{ra.url}}){% if ra.extra_name %} ({{ra.extra_name}}){% endif %}, {{ra.majors}}
{%- endfor %}

## Former Research Assistants

{% for ra in site.research_assistants_former %}
* [{{ra.name}}]({{ra.url}}){% if ra.extra_name %} ({{ra.extra_name}}){% endif %}, {{ra.majors}}
{%- endfor %}
