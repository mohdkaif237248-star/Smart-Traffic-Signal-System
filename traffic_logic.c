#include <stdio.h>
#include <stdlib.h>

int main() {
    int roadA, roadB, greenTime;

    printf("Smart Traffic Signal - 2 Road Version\n");
    printf("Enter number of vehicles on Road A: ");
    if (scanf("%d", &roadA) != 1) { printf("Invalid input\n"); return 1; }

    printf("Enter number of vehicles on Road B: ");
    if (scanf("%d", &roadB) != 1) { printf("Invalid input\n"); return 1; }

    if (roadA > roadB) {
        greenTime = roadA; // 1 second per vehicle (example)
        printf("\\nRoad A has more traffic (%d vs %d).\\n", roadA, roadB);
        printf("Green signal ON for Road A for %d seconds.\\n", greenTime);
    } else if (roadB > roadA) {
        greenTime = roadB;
        printf("\\nRoad B has more traffic (%d vs %d).\\n", roadB, roadA);
        printf("Green signal ON for Road B for %d seconds.\\n", greenTime);
    } else {
        greenTime = 10;
        printf("\\nEqual traffic on both roads (%d).\\n", roadA);
        printf("Green signal alternates every %d seconds.\\n", greenTime);
    }

    printf("\\n--- Simulation Complete ---\\n");
    return 0;
}