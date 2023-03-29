MKFILE_PATH := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SOURCES := workload.py

.PHONY: all clean

all: out

out/package: requirements.txt
	mkdir -p out/package
	cat $(MKFILE_PATH)install_face_recognition.sh | docker run -i --rm -v $(MKFILE_PATH):/app -w /app alpine:3.16
	#echo "apk add python3 python3-dev py3-pip; pip3 install --upgrade --target out/package -r requirements.txt" | docker run -i --rm -v $(MKFILE_PATH):/app -w /app alpine:3.16

out/lib: out/lib
	mkdir -p out/lib
	cat $(MKFILE_PATH)install_libs.sh | docker run -i --rm -v $(MKFILE_PATH):/app -w /app alpine:3.16


out: ${SROUCES} out/package out/lib
	cp ${SOURCES} out

clean:
	sudo rm -r out
    :q
