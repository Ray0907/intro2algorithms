#include <stdio.h>

#define MAX(a,b) ((a) >= (b) ? (a) : (b))
#define MIN(a,b) ((a) <= (b) ? (a) : (b))

void minMax(int *arr, int n, int *max, int *min) {
	int i =0;
	if(n %2 == 1) {
		*max = arr[0];
		*min = arr[0];
		i = 1;
	}
	else {
		if(arr[1] > arr[0]) {
			*max = arr[1];
			*min = arr[0];
		} else {
			*max = arr[0];
			*min = arr[1];
		}
		i = 2;
	}
	while(i < n) {
		if(arr[i] >= arr[i+1]) {
			*max = MAX(*max, arr[i]);
			*min = MIN(*min, arr[i+1]);
		} else {
			*max = MAX(*max, arr[i+1]);
			*min = MIN(*min, arr[i]);
		}
		i +=2;
	}
}

int main() {
	int arr[7] = {3,5,-1,0,2, 1000, -2};
	int max = 0, min = 0;
	minMax(arr, 7, &max, &min);
	printf("Max=%d Min=%d\n", max, min);
	return 0;
}