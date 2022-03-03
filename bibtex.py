from cloudmesh.common.util import readfile
import yaml
import calendar
from pprint import pprint

class converter:
  def __init__(self, loc):
    content = readfile(loc)
    # print (content)

    self.data = yaml.safe_load(content)
    # pprint (data)
    # careful of international spec for dates
    self.day, self.month, self.year = self.data["modified"].split("-")

    self.data["title"] = self.data["name"]
    self.data["year"] = self.year
    self.data["month"] = calendar.month_abbr[int(self.month)].lower()
    self.data["id"]=self.data["title"].replace(" ", "-").lower()
    self.data["url"] = self.data["documentation"]
    if "http" not in self.data["url"]:
        raise ValueError("url not found")


  def to_bibtex(self):

    self.bibtex_entry = """
    @misc{{{id}}},
      title={{{title}}},
      author={{{author}}},
      howpublished={{Web Page}},
      
      ---

      description={{{description}}}

      ---
      
      month = {month},
      year = {{{year}}},
      url = {{{url}}},
      tags={{{tags}}},
      categories={{{categories}}}
    ]
    """

    return self.bibtex_entry.format(**self.data)

  def to_md(self):

    self.markdown_entry = """
    ---
    id: {id}
    author: {author}
    title:  {title}
    ---

    ## Description

    {description}

    ---
    howpublished: {{Web Page}},
    month: {month}
    year: {year},
    url: {url},
    tags: {tags},
    categories: {categories}
    """

    return self.markdown_entry.format(**self.data)

if __name__=="__main__":
  c=converter("D:\\Code\\nist\\github\\nist\\data\\catalog\\oracle_ai_services\\oracle_anomaly.yaml")
  print(c.to_bibtex())
  print("\n")
  print(c.to_md())
