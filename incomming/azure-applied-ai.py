form = \
"""
---
id: {id}
name: {name}
title: {title}
author: {author}
slug: unkown
public: true
description: {description}
version: unkown
license: unkown
microservice: false
protocol: TBD
owner: Amazon
modified: {date}
created: {date}
documentation: {url}
source: {source}
specification: unkown
tags:
  - AI
  - Machine Learning
categories:
  - AI
additional_metadata: unkown
endpoint: unkown
sla: unkown
authors: {author}
data: unkown
"""

constants = {
    "source":  "https://docs.microsoft.com/en-us/azure/applied-ai-services/what-are-applied-ai-services",
    "author": "Microsoft",
    "date": "today"
}


content = \
"""
---
title: 
    Azure Applied AI Services

description: 
    Azure Applied AI Services are high-level services focused on
    empowering developers to quickly unlock the value of data by applying
    AI into their key business scenarios.  Built on top of the AI APIs of
    Azure Cognitive Services, Azure Applied AI Services are optimized for
    critical tasks ranging from monitoring and diagnosing metric
    anomalies, mining knowledge from documents, enhancing the customer
    experience through transcription analysis, boosting literacy in the
    classroom, document understanding and more. Previously, companies
    would have to orchestrate multiple AI skills, add business logic, and
    create a UI to go from development to deployment for their scenario –
    all of which would consume time, expertise, and resources – these
    "scenario specific” services provide developers these benefits "out of
    the box”.



---
title: 
    Azure Form Recognizer


description: 
    Enabling organizations in all industries to consume information hidden
    within documents to increase productivity, automate business processes
    and generate knowledge and insights. Azure Form Recognizer is a service
    that lets you build automated data processing software using machine
    learning technology. Identify and extract text, key/value pairs,
    selection marks, tables, and structure from your documents. The service
    outputs structured data that includes the relationships in the original
    file, bounding boxes, confidence and more. You quickly get accurate
    results that are tailored to your specific content without heavy manual
    intervention or extensive data science expertise. Use Form Recognizer to
    automate data entry in your applications and enrich your documents'
    search capabilities. Azure Form Recognizer is built using OCR, Text
    Analytics and Custom Text from Azure Cognitive Services.
    Form Recognizer is composed of custom document processing models,
    prebuilt models for invoices, receipts, IDs and business cards, and the
    layout model.

url: 
    https://docs.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/

---
title: 
    Azure Metrics Advisor

description:
    Protecting organization's growth by enabling them to make the right
    decision based on intelligence from metrics of businesses, services and
    physical assets. Azure Metrics Advisor uses AI to perform data
    monitoring and anomaly detection in time series data. The service
    automates the process of applying models to your data, and provides a
    set of APIs and a web-based workspace for data ingestion, anomaly
    detection, and diagnostics - without needing to know machine learning.
    Developers can build AIOps, predictive maintenance, and business
    monitoring applications on top of the service. Azure Metrics Advisor is
    built using Anomaly Detector from Azure Cognitive Services.


url: https://docs.microsoft.com/en-us/azure/applied-ai-services/metrics-advisor/

---
title: 
    Azure Cognitive Search

description: 
    Unlock valuable information lying latent in all your content in order to
    perform an action or make decisions. Azure Cognitive Search is the only
    cloud search service with built-in AI capabilities that enrich all types
    of information to help you identify and explore relevant content at
    scale. Use cognitive skills for vision, language, and speech, or use
    custom machine learning models to uncover insights from all types of
    content. Azure Cognitive Search also offers semantic search capability,
    which uses advanced machine learning techniques to understand user
    intent and contextually rank the most relevant search results. Spend
    more time innovating and less time maintaining a complex cloud search
    solution. Azure Cognitive Search is built using Computer Vision and Text
    Analytics from Azure Cognitive Services.


url: 
    https://docs.microsoft.com/en-us/azure/search/


---
title: 
    Azure Immersive Reader

description: 
    Enhance reading comprehension and achievement with AI. Azure Immersive
    Reader is an inclusively designed tool that implements proven techniques
    to improve reading comprehension for new readers, language learners, and
    people with learning differences such as dyslexia. With the Immersive
    Reader client library, you can leverage the same technology used in
    Microsoft Word and Microsoft OneNote to improve your web applications.
    Azure Immersive Reader is built using Translation and Text to Speech
    from Azure Cognitive Services.

url: 
    https://docs.microsoft.com/en-us/azure/applied-ai-services/immersive-reader/


---
title: 
    Azure Bot Service

description: 
    Enable rapid creation of customizable, sophisticated, conversational
    experiences with pre-built conversational components enabling business
    value right out of the box. Azure Bot Service Composer is an open-source
    visual authoring canvas for developers and multidisciplinary teams to
    build bots. Composer integrates language understanding services such as
    LUIS and QnA Maker and allows sophisticated composition of bot replies
    using language generation. Azure Bot Service is built using
    Speech/Telephony, LUIS, and QnA Maker from Azure Cognitive Services.


url: 
    https://docs.microsoft.com/en-us/composer/


---
title: 
    Azure Video Analyzer


description: 
    Enabling businesses to build automated apps powered by video
    intelligence without being a video or AI expert. Azure Video Analyzer is
    a service for building AI-based video solutions and applications. You
    can generate real-time business insights from video streams, processing
    data near the source and applying the AI of your choice. Record videos
    of interest on the edge or in the cloud and combine them with other data
    to power your business decisions. Azure Video Analyzer is built using
    Spatial Analysis from Azure Cognitive Services. Azure Video Analyzer for
    Media is built using Face, Speech, Translation, Text analytics, Custom
    vision, and textual content moderation from Azure Cognitive Services.

url: 
    https://docs.microsoft.com/en-us/azure/azure-video-analyzer/
"""

import yaml
import textwrap

data = []
# remove empty lines
content = content.replace("”", '"')
content = content.replace("–", '-')

entries = content.split("---")
for entry in entries:
    entry = yaml.safe_load(entry)
    data.append(entry)

# generate id
for i in range(len(data)):
    try:
        data[i]["id"] = data[i]["title"].replace(" ", "-").lower()
        data[i]["name"] = data[i]["title"]
        data[i].update(constants)
        d = data[i]["description"]
    except:
        pass
print(yaml.dump(data, indent=2))

for entry in data:
    try:
        print (form.format(**entry))
    except Exception as e:
        print (e)
