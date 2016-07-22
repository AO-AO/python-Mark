datastores = [
[
     ["datastore",
            [
                ["value", "datastore-29"],
                ["_type", "Datastore"]
            ]
     ],
     ["name", "nfs2"],
     ["url", "ds:///vmfs/volumes/28269d51-3501294d/"],
     ["capacity", 1098974756864],
     ["freeSpace", 1095886397440],
     ["uncommitted", 27917234176],
     ["accessible", True],
     ["multipleHostAccess", True],
     ["type", "NFS"],
     ["maintenanceMode", "normal"]
],
[
     ["datastore",
            [
                ["value", "datastore-23"],
                ["_type", "Datastore"]
            ]
     ],
     ["name", "datastore1"],
     ["url", "ds:///vmfs/volumes/578ca7dd-f77450ac-9660-00221968ed8a/"],
     ["capacity", 284273147904],
     ["freeSpace", 266685382656],
     ["uncommitted", 134947537998],
     ["accessible", True],
     ["multipleHostAccess", False],
     ["type", "VMFS"],
     ["maintenanceMode", "normal"]
    ],
    [
     ["datastore",
            [
                ["value", "datastore-28"],
                ["_type", "Datastore"]
            ]
     ],
     ["name", "nfs1"],
     ["url", "ds:///vmfs/volumes/ad2e7712-821deb31/"],
     ["capacity", 1098973708288],
     ["freeSpace", 1088151646208],
     ["accessible", True],
     ["multipleHostAccess", True],
     ["type", "NFS"],
     ["maintenanceMode", "normal"]
    ],
    [
     ["datastore",
            [
                ["value", "datastore-27"],
                ["_type", "Datastore"]
            ]
     ],
     ["name", "datastore1 (1)"],
     ["url", "ds:///vmfs/volumes/578caae2-06488163-d39e-00221968eea1/"],
     ["capacity", 138781130752],
     ["freeSpace", 137761914880],
     ["accessible", True],
     ["multipleHostAccess", False],
     ["type", "VMFS"],
     ["maintenanceMode", "normal"]
    ]
]
result = []
for item in datastores:
    key_val_dic = {}
    for datastore in item:
        if type(datastore[1]) == type(result):
            key_val_dic_below = {}
            for elem in datastore[1]:
                key_val_dic_below[elem[0]] = elem[1]
            key_val_dic[datastore[0]] = key_val_dic_below
        else:
            key_val_dic[datastore[0]] = datastore[1]
    result.append(key_val_dic)
print result





