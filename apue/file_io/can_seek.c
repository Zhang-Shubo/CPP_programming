#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main(){
    if (lseek(STDIN_FILENO, 0, SEEK_CUR) == -1)
        printf("can not seek\n");
    else
        printf("seek OK\n");
    _exit(0);
    
}