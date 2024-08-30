.PHONY: setup works fails

setup:
	uv venv --python 3.10 silly && \
	. ./silly/bin/activate && \
	uv pip install -e ./silly_package

works:
	. ./silly/bin/activate && \
	uv run silly_script

fails:
	-mkdir sub_directory && \
	. ./silly/bin/activate && \
	cd sub_directory && \
	uv run silly_script

clean:
	rm -rf silly
	rm -rf sub_directory