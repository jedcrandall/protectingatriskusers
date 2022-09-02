#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

// gcc compare.c -o compare -lm

double cosine_similarity(long int *A, long int *B, unsigned int Vector_Length)
{
    double dot = 0.0, denom_a = 0.0, denom_b = 0.0 ;
     for(unsigned int i = 0u; i < Vector_Length; ++i) {
        dot += (double) A[i] * B[i];
        denom_a += (double) A[i] * A[i];
        denom_b += (double) B[i] * B[i];
    }
    return dot / (sqrt(denom_a) * sqrt(denom_b)) ;
}

int main(int argc, char **argv)
{
	long int *fhash = malloc(256 * 256 * 256 * sizeof(long int));
	long int *ghash = malloc(256 * 256 * 256 * sizeof(long int));
	memset(fhash, 0, 256 * 256 * 256 * sizeof(long int));
	memset(ghash, 0, 256 * 256 * 256 * sizeof(long int));
	FILE *f = fopen(argv[1], "r");
	FILE *g = fopen(argv[2], "r");
	char c;
	unsigned char *last3 = malloc(3);	
	int count;

	memset(last3, 0, 3);
	count = 0;
	while ((c = fgetc(f)) != EOF)
	{
		//printf("%s\n", last3);
		last3[0] = last3[1];
		last3[1] = last3[2];
		last3[2] = c;
		if (count >= 3)
		{
			unsigned long int i = last3[0] * 256 * 256 + last3[1] * 256 + last3[2];
			fhash[i] += 1;
		}
		count++;
	}


	memset(last3, 0, 3);
	count = 0;
	while ((c = fgetc(g)) != EOF)
	{
		//printf("%s\n", last3);
		last3[0] = last3[1];
		last3[1] = last3[2];
		last3[2] = c;
		if (count >= 3)
		{
			unsigned long int i = last3[0] * 256 * 256 + last3[1] * 256 + last3[2];
			ghash[i] += 1;
		}
		count++;
	}

	printf("%1.9f\n", cosine_similarity(fhash, ghash, 256 * 256 * 256));

}

