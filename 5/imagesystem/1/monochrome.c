void monochrome(imgdata &idata){
	int x, y;
	for (y = 0; y < idata->height; y++){
		for (x = 0; x < idata->width; x++){

			double ganma = idata.source[RED][y][x]*0.299 + idata.source[GREEN][y][x]*0.587 + idata.source[BLUE][y][x]*0.114;

			idata.results[RED][y][x] = ganma;
			idata.results[GREEN][y][x] = ganma;
			idata.results[BLUE][y][x] = ganma;
		}
	}
}
