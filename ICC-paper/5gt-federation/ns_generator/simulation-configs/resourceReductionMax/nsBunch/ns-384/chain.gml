graph [
  node [
    id 0
    label 1
    disk 4
    cpu 2
    memory 1
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 2
    memory 11
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 13
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 4
    memory 12
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 3
    memory 12
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 4
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 150
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 83
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 76
  ]
  edge [
    source 1
    target 3
    delay 30
    bw 189
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 74
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 77
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 138
  ]
]
