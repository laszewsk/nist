import yaml

from make_yaml import yaml_maker

# print(yaml.dump(yaml_maker(class_name="oracle_speech", name="Oracle Speech", title="Oracle Cloud Infrastructure", author="Oracle",
# description="This is oracle speech", documentation="https://www.oracle.com/in/artificial-intelligence/speech/", tags=["AI", "Speech"], categories=["AI"])))

with open("D:\\Code\\nist\\github\\nist\\oracle_ai_services\\oracle_labeling.yaml", "w") as f:
    yaml.dump(yaml_maker(name="Oracle Data Labeling", title="Oracle Cloud Infrastructure", author="Oracle",
                         description="Oracle Cloud Infrastructure (OCI) Data Labeling is a service for building labeled datasets to more accurately train AI and machine learning models. With OCI Data Labeling, developers and data scientists assemble data, create and browse datasets, and apply labels to data records through user interfaces and public APIs. The labeled datasets can be exported for model development across Oracle's AI and data science services for a seamless model-building experience.",
                         public="true", documentation="https://www.oracle.com/in/artificial-intelligence/speech/",
                         tags=["AI", "Iamge Classification", "Virtual Assistance", "Irregularity Detection",
                               "Forms Processing", "Information Extraction"], categories=["AI", "Virtual Assistance"],
                         filename="D:\\Code\\nist\\github\\nist\\oracle_ai_services\\oracle_labeling.yaml", ), f,
              sort_keys=False)
