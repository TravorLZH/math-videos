# Makefile to build manim videos
QUALITY=1440p60
OUTPUT_FOLDER=$(CURDIR)/media/videos/scenes/$(QUALITY)

.PHONY:	all scenes
all:	output.mp4

list.txt:	scenes.py
	./build_scenes.py
	touch list.txt

output.mp4:	list.txt
	cp list.txt $(OUTPUT_FOLDER)/
	(cd $(OUTPUT_FOLDER); ffmpeg -f concat -safe 0 -i list.txt \
		-c copy $(CURDIR)/$@)

clean:
	rm -r output.mp4
