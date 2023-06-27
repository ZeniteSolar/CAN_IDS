#!/bin/python

if __name__ == "__main__":

    from can_ids_generator import *

    can.export_json()
    can.export_c_library()
    can.export_csv("can_ids.csv")
    loads = can.get_can_load_by_topic()
    ids = list(loads.keys())
    ids.sort()
    for id in ids:
        print("Id: ", id, "load:", loads[id])
    print("Total load:", round(can.get_can_load(),3), "%")
    can.plot_load()