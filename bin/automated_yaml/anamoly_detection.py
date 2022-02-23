from make_yaml import yaml_maker
import yaml

with open("D:\\Code\\nist\\github\\nist\\catalogue_info\\oracle_ai_services\\oracle_anomaly.yaml", "w") as f:
    yaml.dump(yaml_maker(name="Oracle Anomaly Detection", title="Oracle Cloud Infrastructure", author="Oracle",
description="Oracle Cloud Infrastructure (OCI) Anomaly Detection is an AI service that enables developers to more easily build business-specific anomaly detection models that flag critical incidents, resulting in faster time to detection and resolution. Specialized APIs and automated model selection simplify training and deploying anomaly detection models to applications and operations, all without data science expertise.",public="true", documentation="https://docs.oracle.com/en-us/iaas/Content/anomaly/using/home.htm", tags=["AI", "Anomaly Detection", "ML"], categories=["AI", "Anomaly Detection"], filename="D:\\Code\\nist\\github\\nist\\catalogue_info\\oracle_ai_services\\oracle_anomaly.yaml"),f, sort_keys=False)
    