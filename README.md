# Install


```bash
git clone git@github.com:laszewsk/nist.git
pip install cloudmesh-installer -U
cloudmesh-installer get catalog
cms help
```


## Modfy entries

example catalog/aws/aws-deeplens.yaml

``bash
cd nist
# ... edit the entry in catalog ...
emacs catalog/aws/aws-deeplens.yaml
# save
git commit -m "describe what you changed" catalog/aws/aws-deeplens.yaml
git push
``

