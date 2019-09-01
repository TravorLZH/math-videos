Demonstration of **[manim][1]**
==========================

The source `scenes.py` consists of the code for project **Calculus Notes**,
which is illustrating the seem-to-be-abstract knowledge in Calculus.

The terminal will help you build the this video by typing these:
```shell
$ pip3 install manimlib # This automatically installs its dependencies
$ make [SceneName]    # To build and watch one scene, see also `scenes.py'
$ make                  # Type `make' to build everything
```
## Subprojects

In `misc/`, I put one-scene videos, you can view them via this command:
```shell
$ manim source.py [SceneName] -p
```
`-p` means to view the video after build, you can see a complete list via:
```shell
$ manim --help
```

[1]: https://github.com/3b1b/manim
