MKFILE_PATH := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SOURCES=workload.py

.PHONY: all clean
all: out

out/package: requirements.txt
	mkdir -p out/package
	echo "apk add musl-dev gcc zlib-dev jpeg-dev python3 python3-dev py3-pip; pip3 install --upgrade --target /app/out/package -r requirements.txt" | docker run -i --rm -v $(MKFILE_PATH):/app -w /app alpine:3.16

out/lib:
	mkdir -p out/lib
	echo "apk add jpeg zlib; cp -r /usr/lib/* /app/out/lib" | docker run -i --rm -v $(MKFILE_PATH):/app -w /app alpine:3.16

#__pycache__: workload.py package lib
#	echo "apk add python3; LD_LIBRARY_PATH=/app/lib PYTHONPATH=/app:/app/package python3 -m workload" | docker run -i --rm -v $(MKFILE_PATH):/app -w /app alpine:3.10

out: ${SOURCES} out/package out/lib
	cp ${SOURCES} out

clean:
	rm -r out
