#include <stdio.h>
#include <stdlib.h>

// int main(void);
// int main(int argc, char* argv[]);

long EOA = 5;
long MAX = 107341413800;

void processOneDay(int* fish) {

    long i;
    int count=0;
    for(i=0; i<EOA; i++) {
        int val = fish[i];
        if(val==0) {
            fish[i] = 6;
            count++;
        }
        else {
            fish[i] = --val;
        }
    }
    if(count>0) {
        for(i=EOA; i< EOA+count; i++) {
            fish[i] = 8;
        }
        EOA = EOA+count;
    }
}


int main(int argc, char* argv[]) {
    int c;
    FILE * fp;

    fp = fopen ("test_input.txt", "r");

    while(1) {
        c = fgetc(fp);
        if( feof(fp) ) { 
            break ;
        }
        printf("%c", c);
    }

    fclose(fp);

    int *fish;
    fish = (int *) malloc(MAX * sizeof(c));
    long i = 0;

    fish[0] = 3;
    fish[1] = 4;
    fish[2] = 3;
    fish[3] = 1;
    fish[4] = 2;

    int day = 1;
    do {
        processOneDay(fish);
//        for(i=0; i<EOA; i++) {
//            printf("%d ", fish[i]);
//        }
//        printf("\t");
        printf("day: %d; lenght: %ld\n", day, EOA);
        day++;
    } while (day < 257);

    free(fish);

    return 0;
}
