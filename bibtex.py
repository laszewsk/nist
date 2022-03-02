from cloudmesh.common.util import readfile
import yaml

from pprint import pprint

content = readfile("data/catalog/azure/bot_services.yaml")

print (content)

data = yaml.safe_load(content)
pprint (data)

bibtex_entry = """
@misc{{{label}}},
  title={{{title}}},
  name={{{name}}},
  author={{{author}}},
  howpubllished={{Web Page}},
  month = {month},
  year = {{{year}}},
  url = {{{url}}}
]
"""
# careful of international spec for dates
day, month, year = data["modified"].split("-")
import calendar

data["label"] = "wrong"
data["title"] = data["name"]
data["year"] = year
data["month"] = calendar.month_abbr[int(month)].lower()

data["url"] = data["documentation"]
if "http" not in data["url"]:
    raise ValueError("url not found")


print (bibtex_entry.format(**data))


markdown_entry = """
---
author: {author}
title:  {title}
---

## Description

{description}
"""

print (markdown_entry.format(**data))
