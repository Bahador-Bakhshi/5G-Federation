graph [
  node [
    id 0
    label 1
    disk 3
    cpu 4
    memory 14
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 2
    memory 8
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 5
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 6
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 1
    memory 8
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 1
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 193
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 68
  ]
  edge [
    source 1
    target 2
    delay 31
    bw 176
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 112
  ]
  edge [
    source 1
    target 4
    delay 32
    bw 192
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 122
  ]
]
