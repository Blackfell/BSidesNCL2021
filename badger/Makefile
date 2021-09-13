# Makefile for badger

CFLAGS ?= -Wl,-N --static 

all:	badger

badger: main.c
	$(CC) $(CFLAGS) -o badger main.c
	cp badger badger_stripped
	strip badger_stripped

clean:
	rm -f badger
	rm -f badger_stripped
