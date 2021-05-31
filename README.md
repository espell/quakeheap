# quakeheap

This makefile and testing file live in priority-queue-testing/trunk/queues (from the codebase at https://code.google.com/archive/p/priority-queue-testing/source/default/source). The makefile was updated so that it only built the quake heap and fibonacci heap implementations. *More specifically, you should download the codebase from the link, add testing.c to it and update the makefile to match the current.*

I snuck a line within the fibonacci build (in the makefile) to build the "testing.c" file. Additionally, I changed the output location of the build to be the current folder (as opposed to within "dumb", "eager", etc).

"testing.c" has some preliminary code to time basic operations of a heap. The current code relies on the memory handlers that live in "trunk/". I arbitrarily chose the "dumb" implementation. 

## Note 

-trunk/queues/queue_common.h has ALPHA and MAXRANK defined for when we want to try simulating with different alphas.

