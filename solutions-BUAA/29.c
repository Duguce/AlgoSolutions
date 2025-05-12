#include <stdio.h>

int main()
{
    double a, b, c, d;
    char op;

    while (scanf("%lf %lf %lf %lf %c", &a, &b, &c, &d, &op) != EOF)
    {
        double real = 0.0, imag = 0.0;

        switch (op)
        {
        case '+':
            real = a + c;
            imag = b + d;
            break;
        case '-':
            real = a - c;
            imag = b - d;
            break;
        case '*':
            real = a * c - b * d;
            imag = a * d + b * c;
            break;
        case '/':
            if (c == 0 && d == 0)
            {
                printf("Inf\n");
                continue;
            }
            double denom = c * c + d * d;
            real = (a * c + b * d) / denom;
            imag = (b * c - a * d) / denom;
            break;
        }
        printf("%.2lf %.2lf\n", real, imag);
    }
    return 0;
}