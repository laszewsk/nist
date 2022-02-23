from make_yaml import yaml_maker
import yaml

# print(yaml.dump(yaml_maker(class_name="oracle_speech", name="Oracle Speech", title="Oracle Cloud Infrastructure", author="Oracle",
# description="This is oracle speech", documentation="https://www.oracle.com/in/artificial-intelligence/speech/", tags=["AI", "Speech"], categories=["AI"])))

with open("D:\\Code\\nist\\github\\nist\\oracle_ai_services\\oracle_speech.yaml", "w") as f:
    yaml.dump(yaml_maker(name="Oracle Speech", title="Oracle Cloud Infrastructure", author="Oracle",
description="Oracle Cloud Infrastructure Speech is a new AI service that uses Automatic Speech Recognition (ASR) to convert speech to text. Built on the same AI models used for Oracle Digital Assistant, developers can use Oracle's time-tested acoustic and language models to provide highly accurate transcription for audio or video files across many languages.",public="true", documentation="https://www.oracle.com/in/artificial-intelligence/speech/", tags=["AI", "Speech"], categories=["AI"], filename="D:\\Code\\nist\\github\\nist\\oracle_ai_services\\oracle_speech.yaml" ),f, sort_keys=False)
    