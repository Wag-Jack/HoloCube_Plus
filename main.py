import encode as e
import transmit_color as t
import decode as d

def main():
    transmission = e.convert_to_binary(input('Please give a string to transmit: '))
    print(f"Message converted to binary: {transmission}")
    constellation = e.map_constellation(transmission)
    t.display_transmission(constellation)


if __name__ == '__main__':
    main()