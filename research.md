---
layout: page
title: "Research"
---
I wrote a short text about one of my recent works aimed at a large mathematical audience. This can be found <a href="https://www.maths.ox.ac.uk/node/74266" target="_blank">here</a>. 

<h2>  <span style="font-weight:normal"> Preprints </span> </h2>

<ol  reversed class="preprint-list">
  {% for paper in site.data.preprints %}
  {% include publication.html paper=paper %}
  {% endfor %}
</ol> 

<h2>  <span style="font-weight:normal"> Publications </span> </h2>


<ol reversed class="research-list">
{% for paper in site.data.publications %}
  {% include publication.html paper=paper %}
{% endfor %}
</ol>

<b>On AI:</b> I do believe that tools, such as AI, can be beneficial for science and other fundamental aspects of life. Nevertheless, I find it worrying that most AI tools, as of today, are not easily accessible in the same way to everyone, and are rather controlled by companies whose sole interest is to maximise their profits, while engaging in questionable working and ethical practices.
