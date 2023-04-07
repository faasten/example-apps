FUNCTIONS=thumbnail face_recognition
OUTPUTS=$(patsubst %, output/%.img, $(FUNCTIONS))

.PHONY: all
all: $(OUTPUTS)

output/%.img: functions/%/*
	@truncate -s 500M $@
	@mkfs.ext2 -F $@
	@ \
		if [ -f functions/$*/Makefile ]; then \
			make -C functions/$*; \
			cptofs -t ext2 -i $@ functions/$*/out/* /; \
		else \
			cptofs -t ext2 -i $@ functions/$*/* /; \
		fi
	@e2fsck -f $@
	@resize2fs -M $@
