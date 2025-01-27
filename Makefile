TARGET = PFR

CC = gcc
CFLAGS = -std=c11 -Wall

SRCS = TraitementImages/main.c TraitementImages/file_operations.c TraitementImages/image_process.c TraitementImages/cluster.c
OBJS = $(SRCS:.c=.o)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)

distclean: clean

.PHONY: clean distclean