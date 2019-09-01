# Makefile to build manim videos
QUALITY_LOW=480p15
QUALITY_MEDIUM=720p30
QUALITY_HIGH=1440p60
include quality.mk
OUTPUT_FOLDER=$(CURDIR)/videos/scenes/$(QUALITY)

.PHONY:	all all-scenes merge clean
all:
	@/bin/echo "Use \`make all-scenes' to render mp4 for each scene"

all-scenes:	scenes.py
	../template/build_scenes.py $(QUALITY)

merge:
	cp list.txt $(OUTPUT_FOLDER)/
	(cd $(OUTPUT_FOLDER); ffmpeg -y -f concat -safe 0 -i list.txt \
		-c copy $(CURDIR)/output.mp4 2>/dev/null)

%:
	../template/build_scenes.py $(QUALITY) $@

clean:
	rm -r output.mp4
