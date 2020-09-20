graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 14
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 10
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 2
    memory 12
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 2
    memory 16
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 1
    memory 11
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 3
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 193
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 166
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 194
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 111
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 74
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 139
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 66
  ]
]
