import sys
from geocode import latlon

def main():
    if len(sys.argv) > 1:
        for x in sys.argv[1:]:
            result = latlon(x, center=False, round_digits=3)
            if result:
                print ','.join(map(str, result))
            else:
                print 'na,na,na,na'
    else:
        print 'Usage: geocode "location string 1" "location string 2" ...'

if __name__ == '__main__':
    main()