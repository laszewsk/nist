import yaml

from make_yaml import yaml_maker

# print(yaml.dump(yaml_maker(class_name="oracle_speech", name="Oracle Speech", title="Oracle Cloud Infrastructure", author="Oracle",
# description="This is oracle speech", documentation="https://www.oracle.com/in/artificial-intelligence/speech/", tags=["AI", "Speech"], categories=["AI"])))

# Path

with open("./nist/oracle_ai_services/oracle_vision.yaml", "w") as f:
    yaml.dump(yaml_maker(name="Oracle Vision", title="Oracle Cloud Infrastructure", author="Oracle",
                         description="Oracle Cloud Infrastructure (OCI) Vision is an AI service that applies computer vision technology to analyze image-based content. Developers can make API calls to easily integrate pretrained models into their applications, or custom train models to meet their specific use cases. These models can be used to detect visual anomalies in manufacturing, extract text from documents to automate business workflows, and tag items in images to count products or shipments.",
                         public="true", documentation="https://docs.oracle.com/en-us/iaas/vision/vision/using/home.htm",
                         tags=["AI", "Vision", "Deep Learning", "Image Recognition", "Text Recognition"],
                         categories=["AI", "Deep Learning"],
                         filename="D:\\Code\\nist\\github\\nist\\oracle_ai_services\\oracle_vision.yaml"), f,
              sort_keys=False)
