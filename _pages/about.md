---
layout: about
title: About
permalink: /
subtitle: LLM Researcher @ <a href='https://github.com/LUMIA-Group'>LUMIA Group</a> · Shanghai Jiao Tong University
# <a href='mailto:maximus.cao@outlook.com'>maximus.cao@outlook.com</a>

profile:
  align: right
  image: profile/blue-profile.png
  image_circular: True # crops the image to make it circular
  more_info: >
    <style>
    .contact-container {
        font-family: sans-serif; /* Or your preferred font */
    }

    .contact-item {
        display: flex;
        align-items: center;
        margin-bottom: 12px;
        color: #333; /* Base text color */
    }

    .contact-item i {
        width: 28px; /* Keeps icons aligned */
        font-size: 1.1em;
        opacity: 1;
    }

    .contact-link {
        /* KEY FIX: This removes the browser's default purple underline */
        text-decoration: none !important; 
        
        color: inherit;
        padding-bottom: 2px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1); 
        transition: all 0.2s ease-in-out;
    }

    .contact-link:hover {
        border-bottom: 1px solid #6e5494; /* A nice subtle purple or your choice */
        color: #6e5494;
        opacity: 1;
    }
    </style>

    <div class="contact-container">
        <p class="contact-item">
            <i class="fa-brands fa-weixin"></i>
            <a href="weixin://dl/chat?maxmcao" class="contact-link">maxmcao</a>
        </p>
        
        <p class="contact-item">
            <i class="fa-solid fa-envelope"></i>
            <a href="mailto:maximus.cao@outlook.com" class="contact-link">maximus.cao@outlook.com</a>
        </p>
    </div>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

My research focuses on **parametric memory architectures** and **continual learning** for large language models (LLMs). I have published 2 papers as a (co-)first author at **NeurIPS 2025** and **ICLR 2026**.

My representative works, [Memory Decoder](https://github.com/LUMIA-Group/MemoryDecoder) and [MLP Memory](https://github.com/Rubin-Wei/MLPMemory), introduce a novel parametric memory paradigm and provide a preliminary exploration of decoupling reasoning capabilities from long-tail knowledge.

I am well-versed in LLM pretraining, embedding models, and various RAG architectures, and am dedicated to mitigating LLM hallucinations and enabling continual learning.

Previously, I interned at [Shanghai AI Lab](https://www.shlab.org.cn/) and [Microsoft Cloud + AI](https://azure.microsoft.com/).