TARGETS=spectrum-fitting

ROOTFLAGS = $(shell root-config --cflags)
ROOTLIBS = $(shell root-config --libs)

CXXFLAGS  = -Wall -O2 $(ROOTFLAGS)
CXXLIBS   = $(ROOTLIBS)

all: $(TARGETS)

spectrum-fitting: spectrum-fitting.o
		   g++ -o $@ spectrum-fitting.o $(CXXLIBS)

.cc.o:
	g++ -c $(CXXFLAGS) $<

clean:
	rm -f spectrum-fitting.o spectrum-fitting
