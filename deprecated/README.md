# Cloudmesh Catalog

Cloudmesh catalog can be used to store information about a software
component or project. The information included in it can be
categorized so that a comparision is possible.  The catalog is
mplemented as REST service so it can be integrated in other projects
and searched programatically.

The catalog depends on the cloudmesh command shell which allows eay
integration of new commands line environment.  It projects a sample
Interface for the catalog from the commandline

We also intent to creat static web pages from the catalog but have not
yet settled on a framework. We will explore hugo docsy as it provides
an easy way to generate hirarchical web pages, but also has a tagging
mechnism for the bages. For this reason the information of a mage will
also be convertable to markdown which is used by hugo.

## Instalation for developers

1. If you do not have yet create an ssh key and upload it to the
   github repository.

   ```ssh-keygen```

   Upload the `~/.ssh/id_rsa.pub` key to github

2. Download cloudmesh with its source repositories

   Make sure you ave python 3.10.2

   On Mac or Linux do

   ```bash
   $ python3.10 -m venv ~/ENV3
   $ source ~/ENV3/bin/activate
   ```

   On Windows 

   ```bash
   $ py --version # make sure its 3.10.2
   $ py -m venv ~/ENV3
   $ source ~/ENV3/bin/activate
   ```

   After that the instalation is the same

   ```bash
   $ mkdir cm
   $ cd cm
   $ pip install cloudmesh-installer
   $ cloudmesh-installer -ssh install cms
   $ cms help
   ```
   This will download all source code for the cloudmesh shell
   and compile from source.

3. Next install the cataloge with

   ```bash
   $ git clone git@github.com:cloudmesh/cloudmesh-catalog.git
   $ cd cloudmesh-catalog
   $ pip install -e .
   ```

   If you prefer to use https and not ssh in github you can also do
   `git clone https://github.com/cloudmesh/cloudmesh-catalog.git`
   instead of the git clone in the previous section

4. Now you are all ready to do programming and enhancing
   cloudmesh-catalog If you have any issues, contact
   laszewski@gmail.com


## Managing the Service

TODO: This is not yes implemented.

A manual pasge shoudl be implemented in
`cloudmesh-catalog/catalog/command/catalog.py` This manual page shoudl
then be included here once it is completed.

you can get the manual page with 

```bash
$ cms catalog help
```

## BUG

The previous work could benefit from exploring the use of YAMLDB
written by Gregor von Laszewski.  Currently it uses pickl and does not
allow for convenient view of the data in native form, or sophisticated
queries which are enabled in YAMLDB while using jmse queies.

## Adding catalog and registry data

To add catalog and registry data for new services, one must create new
.yaml files in the appropriate folders: 'data/catalog/my_example.yaml'
and 'data/registry/my_example.yaml'. Each file must follow yaml
formatting similar to the following example.

Example file: Amazon Comprehend (Catalog), amazon_comprehend.yaml

```
amazon_comprehend:
  id: unknown
  name: Amazon Comprehend
  title: Amazon Comprehend
  author: Amazon
  slug: amazon-comprehend
  public: true
  description: |
    Comprehend is Amazon's solution for cloud-based NLP.
    It is available with an AWS account. To use,
    it requires use of either the AWS Command Line
    Interface or an AWS SDK for Python, Java, or .NET.
    Notable features include functionality for giving
    batches of documents to be processed as well as
    submission of multiple jobs in a list. The DetectEntities
    function also allows use of a custom-trained
    model, but many other functions do not.
  version: unknown
  license: unknown
  microservice: no
  protocol: AWS API
  owner: Amazon Web Services
  modified: 9/29/2021
  created: 11/29/2017
  documentation: https://docs.aws.amazon.com/comprehend/index.html
  source: unknown
  specification: unknown
  tags: ["nlp", "nlp service", "machine learning", "cloud service", "nlp api",
        "deep learning", "natural language processing", "artificial intelligence"]
  categories: ["NLP"]
  additional_metadata: unknown
  endpoint: unknown
  sla: https://aws.amazon.com/machine-learning/language/sla/
  authors: The AWS team can be contacted through support ticket at https://aws.amazon.com/contact-us/
  data: |
    User data is stored on Amazon servers under the associated AWS account and is protected under the AWS
    shared responsibility model as detailed here https://aws.amazon.com/compliance/shared-responsibility-model/
```

## Using the Catalog and Registry classes

Written in catalog.py and registry.py are classes capable of reading and storing the data written in the .yaml files. Both use the same interface.
Here is an example of the Catalog class in action:

```
# initialize the catalog using data found in the given directory
catalog = Catalog('data/catalog/')
# query the catalog for Amazon Comprehend data, save result to amazon_catalog_data
amazon_catalog_data = cat.query({'name': 'Amazon Comprehend'})
# add a new data file to the catalog
catalog.add('new_example/azure_language.yaml')
# save entire catalog to a pickle file
catalog.to_pickle('catalog.pkl')
# load from pickle file
catalog.from_pickle('catalog.pkl')
# print catalog data
print(catalog.data)
```

## Using the yaml to markdown conversion script

In 'scripts/yaml_to_md.py' is a class YamlToMd used to assist in the
conversion of .yaml catalog data to a readable markdown page.  Here is
an example which takes the catalog data entry
'data/catalog/amazon_comprehend.yaml' and produces
'output/amazon_comprehend.md':

```
converter = YamlToMd('data/catalog/amazon_comprehend.yaml')
converter.generate_md(dir='output/')
```

Note that it is advisable to go through and look over the generated
markdown files manually to spot any possible minor errors in
conversion.  One such known error comes from the MdUtils package,
which may add extra line breaks that split some urls unintentionally.

BUG: verify if the markdown is the markdown used by hugo, we may
support multiple markdown formats.
