checks: code_style sort_imports lint static_typing

code_style:
	black .

sort_imports:
	isort .

lint:
	flake8 .

static_typing:
	mypy *.py ad_targeter/*.py
