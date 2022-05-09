# Install


```bash
git clone git@github.com:laszewsk/nist.git
pip install cloudmesh-installer -U
cloudmesh-installer get catalog
cms help
```

## Work

do a git pull first

```bash
cd cm
cd nist; git pull ; cd ..
cd cloudmesh-catalog; git pull ; cd ..
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

## Collaborators


* @5ham5h33r
* @AarnoStormborn
* @Amaaan09
* @ishandandekar
* @mysoladi
* @yash-chauhan-1234
