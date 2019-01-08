# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys

urls = [
'/news/nsf-workshop-behavioral-ontology-learning',
'/news/tool-addressing-construct-identity-literature-reviews-and-meta-analyses-mis-quarterly',
'/news/behavior-change-interventions-potential-ontologies-advancing-science-and-practice',
'/news/human-behavior-project-research-team-assists-nih-report-gem-website',
'/news/hovorka-and-co-authors-paper-nominated-best-paper-hicss',
'/news/symposium-cook-sousa-meek-and-larsen-accepted-podium-presentation-wins-46th-annual',
'/news/hovorka-and-co-authors-paper-accepted-hawaii-international-conference-system-sciences',
'/news/kai-larsen-and-co-authors-publish-article-journal-nursing-research',
'/news/kai-larsen-presents-bond-university-and-university-queensland',
'/news/chih-how-bong-presents-ieee-symposium-computer-and-informatics',
'/news/kai-larsen-and-co-author-dirk-hovorka-present-hawaii-international-conference-system-science',
'/news/jingjing-li-and-kai-larsen-present-international-conference-information-systems',
'/news/bized-magazine-septemberoctober-2010',
'/news/boulder-daily-camera-june-14-2010',
]

for url in urls:
    r = requests.get('http://theorizeit.org{}'.format(url))
    soup = BeautifulSoup(r.content, "html.parser")
    
    title = soup.find(id='page-title').string.strip()
    post_meta = soup.find(class_='meta submitted')
    post_date = post_meta.find(property="dc:date dc:created")['content'].split('T')[0]
    post_author = post_meta.find(typeof="sioc:UserAccount").string
    
    post_content_ps = soup.find(id='content')('p')
    post_content = "\n".join([str(p) for p in post_content_ps])
    
    post_tags = ' '.join([tag.string for tag in soup.find_all(rel='dc:subject')])
    
    post_file = '''---
title: {title}
posted_by: {author}
date: {post_date}
tags: {post_tags}
---

{post_content}
    '''.format(title=title, 
        author=post_author, 
        post_date=post_date, 
        post_tags=post_tags, 
        post_content=post_content)
    
    print(post_file, file=open(url.split('/')[2], 'w'))
    
    