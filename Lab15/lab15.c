#include <stdio.h>
#include <math.h>

double f(int i) {
    return sqrt(i+2) - sqrt(i) - (3/11);
}

double g(int j) {
    return ((3*pow(j,2)) - 11) / (pow((-j), 3) - 2);
}

int main() {
    int n = 10;  
    double a[n][n];  
    double total_sum = 0;  

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            a[i][j] = (f(i+1) + g(j+1));
            total_sum += a[i][j];  
        }
    }
    printf("%lf", g(10));
    printf("\n");
    printf("%lf\n", f(10));
    double total;
    printf("\n");
    double ch = 0.01;
    printf("%lf\n", ch);
    total = (ch*total_sum);
    printf("%lf\n", total_sum);
    printf("%lf\n", total);
   
    return 0;
}