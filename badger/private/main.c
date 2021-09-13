#include <stdlib.h>
//#include <unistd.h>
#include <stdio.h>
//#include <string.h>

void peek()
{
    FILE * fd;
    char flag[0x50];
    char *flag_ptr;
    
    fd = fopen("flag.txt", "r");
    fgets(flag, 0x50, fd);
    flag_ptr = &flag;
    fclose(fd);

}

int vuln()
{
    int i, j, index;
    char name[0x50], job[0x50];
    char *catchphrases[3] = {
        "Hack the planet!\n",
        "Make Bsides weird again!\n",
        "Social distancing since birth.\n"
    };
    
    // Get input from user
    printf("Welcome to Virtual BSides.\nLet's create your badge.\nEnter your name: ");
    fflush(stdout);
    fgets(name, 0x50, stdin);
    printf("Enter your job title: ");
    fflush(stdout);
    fgets(job, 0x50, stdin);
    printf("You can choose a tagline for your badge:\n");
    for (i = 0 ; i < 3; i++) { 
        printf("%d. %s", i+1, catchphrases[i]);
    }
    printf("Select your tagline: ");
    fflush(stdout);
    scanf("%lld", &index);

    // Print out the badge
    printf("Printing badge, please wait...\n\n");
    fflush(stdout);
    sleep(2);
    // Can't hurt to check the flag is there
    peek();
    printf("  ---------- BNCL BADGE ----------\n Name    : %s Job     : %s Tagline : ", name, job);
    printf(catchphrases[index -1]);
    printf("  --------------------------------\n");
    fflush(stdout);

    return 0;
}


int main(short argc, char **argv)
{
    vuln();
    return 0;
}
