#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#define	FILE_MODE	(S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH)
#define	DIR_MODE	(FILE_MODE | S_IXUSR | S_IXGRP | S_IXOTH)

char buf1[] = "abcdefghij";
char buf2[] = "ABCDEFGHIJ";

int main(){
    int fd;
    if ((fd = creat("file.hole", FILE_MODE)) < 0)
        printf("create err");
    if (write(fd, buf1, 10) != 10)
        printf("buffer write error");
    if (lseek(fd, 16384, SEEK_SET) == -1)
        printf("lseek error");
    if (write(fd, buf2, 10) != 10)
        printf("buffer write error");

    exit(0);
    
}