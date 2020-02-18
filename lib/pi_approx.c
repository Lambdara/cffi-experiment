#include <stdlib.h>
#include <stdio.h>
#include "pi_approx.h"

float pi(int n){
    int hits = 0;

    for (int i = 0; i < n; i++){
        float x = rand() / (float) RAND_MAX;
        float y = rand() / (float) RAND_MAX;

        if (x*x+y*y < 1) {
            hits++;
        }
    }

    return (float) hits / (float) n * 4.0;
}

int main(void){
    printf("Result %f", pi(1000));
}
