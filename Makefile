make:
	cms catalog check --source=catalog
	cms catalog export bibtex --source=catalog
	cms catalog export md --source=catalog
	cms catalog export hugo --source=catalog
