#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "fibonacci_heap.h"
#include "../memory_management_dumb.h"
//#include "quake_heap.h"

int main() {
    printf("Getting Fibonacci Timing");
    clock_t before  = clock();

    //fibonacci code
    uint32_t sizes[] = {100};
    mem_map* map = mm_create(1, sizes); //number of different types, sizes of each type 
    fibonacci_heap* fib = pq_create(map);
    pq_insert(fib, 1, 5);

    clock_t difference = clock() - before;
    int msec = difference * 1000 / CLOCKS_PER_SEC;
    printf("Time taken %d seconds %d milliseconds \n", msec/1000, msec%1000);

    //printf("Getting Quake Timing");
    //before = clock();
    //quake code
    //difference = clock() - before;
    //msec = difference * 1000 / CLOCKS_PER_SEC;
    //printf("Time taken %d seconds %d milliseconds \n", msec/1000, msec%1000);
}
