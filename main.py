#!/bin/python

if __name__ == "__main__":

    from can_ids_generator import *

    can.export_json()
    can.export_c_library()
