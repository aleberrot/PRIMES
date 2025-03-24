#include <stdio.h>
#include <stdlib.h>

int *primo(int num){
	int index = 0; 
	int half = num / 2;
	int *divisors = (int*) malloc (half * sizeof(int)); 
	if (divisors == NULL){
		exit(1);
	}
	for (int i = 1; i <= half; i++){
		if(num % i == 0){
			divisors[index] = i;
			index++;
		}
	}
	return divisors;
	
}

int main (void){
	
	int *result = primo(99);
	int x = 99 / 2;
	for(int i = 0; i <= x; i++){
		printf("%i \n", result[i]);
	}
	return 0;	

}
