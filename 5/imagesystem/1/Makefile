IMAGE := ans1.bmp ans2.bmp ans3.bmp ans4.bmp ans5.bmp

all : $(IMAGE)

test:
	./test.sh

ans%.bmp : ans%.out #../kadai/no%/in%.bmp
	./$< ../kadai/no$*/in$*.bmp $@

ans%.out : ans%.c bmpfile.o
	$(CC) -o $@ $^

clean:
	rm -f $(IMAGE)
	rm -f *.out
