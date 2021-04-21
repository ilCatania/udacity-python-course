import argparse


def build_parser():
    """Create a parser to parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Find Nobel prizes in a given year and category")
    parser.add_argument('-y', '--year', help="The year to search for.")
    parser.add_argument('-c', '--category', help="The category to search for.")
    return parser

