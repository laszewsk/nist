make:
	cms catalog export bibtex --source=catalog
	cms catalog export md --source=catalog
	cms catalog export hugo --source=catalog
