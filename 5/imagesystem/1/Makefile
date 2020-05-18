IMAGE := ans1.bmp ans2.bmp ans3.bmp ans4.bmp

all : $(IMAGE)

test:
	./test.sh

%.bmp : %.out in0.bmp
	./$< in0.bmp $@

%.out : %.c bmpfile.o
	$(CC) -o $@ $^

clean:
	rm -f $(IMAGE)
	rm -f *.out
