#!/usr/bin/python

from osmapi import OsmApi
import sys

username = sys.argv[1]
searchfortag = sys.argv[2]
searchforvalue = sys.argv[3]
action = sys.argv[4]

print("Searching for tag=%s, value=%s, action=%s, user=%s" %(searchfortag, searchforvalue, action, username))

counter = 0

MyApi = OsmApi()

csets = MyApi.ChangesetsGet(username=username)

for i_cs in csets:
    changeset_info = MyApi.ChangesetGet(i_cs)
    changeset = MyApi.ChangesetDownload(i_cs)

    for i_ed in changeset:
        if i_ed['action'] == action:
            node_id = i_ed['data']['id']
            node = MyApi.NodeGet(node_id)

            try:
                if node['tag'][searchfortag] == searchforvalue:
                    counter = counter + 1
                    print("Counter: %i %s, node id: %s" % (counter, searchforvalue, node_id))
            except:
                a=1

print("Number of items: %i" % counter)
