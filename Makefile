# Makefile to build manim videos
QUALITY_LOW=480p15
QUALITY_MEDIUM=720p30
QUALITY_HIGH=1440p60
QUALITY=$(QUALITY_LOW)
OUTPUT_FOLDER=$(CURDIR)/videos/scenes/$(QUALITY)

.PHONY:	all scenes
all:	output.mp4

list.txt:	scenes.py
	./build_scenes.py $(QUALITY)
	touch list.txt

output.mp4:	list.txt
	cp list.txt $(OUTPUT_FOLDER)/
	(cd $(OUTPUT_FOLDER); ffmpeg -f concat -safe 0 -i list.txt \
		-c copy $(CURDIR)/$@)

clean:
	rm -r output.mp4
