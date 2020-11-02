addTwoNum: main.o sl_list.o
	g++ -o addTwoNum main.o sl_list.o

main.o: add_two_number.cpp sl_list.h
	g++ -c add_two_number.cpp -o main.o

sl_list.o: sl_list.cpp sl_list.h
	g++ -c sl_list.cpp -o sl_list.o

run:
	./addTwoNum

clean:
	rm *.o
