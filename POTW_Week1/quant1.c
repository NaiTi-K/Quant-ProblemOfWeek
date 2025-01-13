#include <stdio.h>

int main()
{

    float gukesh[5][5] = {{90, 4, 3, 2, 1}, {0, 91, 4, 3, 2}, {0, 0, 93, 4, 3}, {0, 0, 0, 95, 5}, {0, 0, 0, 0, 100}};
    float ding[5][5] = {{100, 0, 0, 0, 0}, {8, 92, 0, 0, 0}, {3, 7, 90, 0, 0}, {2, 3, 7, 88, 0}, {1, 3, 4, 6, 86}};

    float move[5] = {0, 0, 1, 0, 0};
    float temp[5] = {0, 0, 0, 0, 0};

    for (int i = 1; i <= 20; i++)
    {

        for (int j = 0; j < 5; j++)
        {
            temp[j] = 0;
        }

        if (i % 2 != 0)
        {
            for (int j = 0; j < 5; j++)
            {
                for (int k = 0; k < 5; k++)
                {
                    temp[j] += (move[k] * gukesh[k][j]) / 100;
                }
            }
        }

        else
        {
            for (int j = 0; j < 5; j++)
            {
                for (int k = 0; k < 5; k++)
                {
                    temp[j] += (move[k] * ding[k][j]) / 100;
                }
            }
        }

        for (int x = 0; x < 5; x++)
        {
            move[x] = temp[x];
        }
    }

    for (int z = 0; z < 5; z++)
    {
        printf("%ld ", move[z]);
    }

    return 0;
}
