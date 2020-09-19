.PHONY: all build run logs stop

all: build run

run:
	docker run -it --rm -d -v `pwd`:/home/jovyan/work -p 127.0.0.1:8888:8888 --name lets_build_compiler python-lark

logs:
	docker logs lets_build_compiler

build:
	docker build . -t python-lark

stop:
	docker stop lets_build_compiler
