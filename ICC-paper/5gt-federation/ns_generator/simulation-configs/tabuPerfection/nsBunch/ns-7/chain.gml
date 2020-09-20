graph [
  node [
    id 0
    label 1
    disk 4
    cpu 2
    memory 14
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 2
    memory 8
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 4
    memory 11
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 3
    memory 9
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 2
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 115
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 106
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 56
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 152
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 107
  ]
  edge [
    source 2
    target 4
    delay 29
    bw 92
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 151
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 73
  ]
]
