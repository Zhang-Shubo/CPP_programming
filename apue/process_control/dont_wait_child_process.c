#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>


int main(){

    pid_t pid;
    if ((pid = fork()) < 0){
        printf("fork error");
    }
    else if (pid == 0){  //child process
        printf("second child, parent BEFORE PARENT EXIT pid = %ld\n", (long)getpid());
        if ((pid = fork()) < 0)
            printf("fork error");
        else if (pid > 0)
            // printf("second child, parent BEFORE PARENT EXIT pid = %ld\n", (long)getppid());
            exit(0);  // first child process exit  

        /* second child process*/
        sleep(2);
        printf("second child, parent pid = %ld\n", (long)getppid());
        exit(0);
    }

    if (waitpid(pid, NULL, 0) != pid) // parent process
        printf("waitpid error");
    return 0;
}