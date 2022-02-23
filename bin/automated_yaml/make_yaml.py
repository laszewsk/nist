import yaml
import datetime
import os

class yaml_maker(yaml.YAMLObject):

    def __init__(self, name,title, author, description, filename, documentation, tags, categories, id="unknown", slug="unknown", public="true",  version="unknown", license="unknown",
    microservices="no", protocol="TBD", source="unknown", endpoint="unknown", specification="unknown", owner="Oracle", additional_metadata="unkown", sla="https://www.oracle.com/cloud/sla/", authors= "The Oracle team can be contacted through a user's individual My Oracle Support portal.",
    data="Oracle's policy on data usage and management can be read about on the Online Data Agreement document https://www.oracle.com/us/corporate/contracts/data-cloud-online-agreement-3087248.pd"):
        self.id=id
        self.name=name
        self.title=title
        self.author=author
        self.slug=slug
        self.public=public
        self.description=description
        self.version=version
        self.license=license        
        self.microservice=microservices
        self.protocol=protocol
        self.owner=owner
        self.modified= str(datetime.datetime.fromtimestamp(os.path.getmtime(filename))).split(" ")[0]
        self.created= str(datetime.datetime.fromtimestamp(os.path.getctime(filename))).split(" ")[0]
        self.documentation=documentation
        self.source=source
        self.specification=specification
        self.tags=tags
        self.categories=categories                            
        self.additional_metadata=additional_metadata
        self.endpoint=endpoint
        self.sla=sla
        self.authors=authors
        self.data=data
    



    