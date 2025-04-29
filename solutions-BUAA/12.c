#include <stdio.h>
# define MOD 1000007


int main(){
    int n, x;
    int coeff[1000000];
    while (scanf("%d %d", &n, &x) != EOF) {
        for (int i = 0; i <= n; i++) {
            scanf("%d", &coeff[i]);
        }
        int result = 0;
        for (int i = n; i >= 0; i--) {
            result = (result * x + coeff[i]) % MOD;
        }
        printf("%d\n", result);
    }
}