IMAGE := ans1.bmp ans2.bmp ans3.bmp ans4.bmp ans5.bmp ans6.bmp ans7.bmp ans8.bmp ans9.bmp ans10.bmp ans11.bmp ans12.bmp ans13.bmp ans14.bmp ans15.bmp ans16.bmp ans17.bmp ans19.bmp

all : $(IMAGE)

clean:
	rm -f $(IMAGE)
	rm -f *.out

test:
	./test.sh

ans%.bmp : ans%.out #../kadai/no%/in%.bmp
	./$< ../kadai/no$*/in$*.bmp $@

ans%.out : ans%.c bmpfile.o
	$(CC) -fno-plt -fstack-protector-strong -Wall -lm -std=c99 -g -o $@ $^

